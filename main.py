import sys
import json
from lexer import Lexer
from parser import Parser


def run_tests():
    with open("tests/test_cases.json") as f:
        data = json.load(f)

    print("\n✅ VALID TESTS")
    for case in data["valid_cases"]:
        try:
            result = Parser(Lexer(case).tokenize()).parse()
            print(f"PASS: {case}")
        except Exception as e:
            print(f"FAIL: {case} → {e}")

    print("\n❌ INVALID TESTS")
    for case in data["invalid_cases"]:
        try:
            Parser(Lexer(case).tokenize()).parse()
            print(f"FAIL: {case}")
        except:
            print(f"PASS: {case}")


def parse_file(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return

    result = Parser(Lexer(text).tokenize()).parse()
    print("\nParsed Output:")
    print(result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        parse_file(sys.argv[1])
    else:
        run_tests()