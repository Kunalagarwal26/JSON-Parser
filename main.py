import sys
import json
from lexer import Lexer
from parser import Parser


# 🔥 Pretty Print Function
def pretty_print(data, indent=0):
    space = "  " * indent

    if isinstance(data, dict):
        print("{")
        items = list(data.items())
        for i, (k, v) in enumerate(items):
            print(f'{space}  "{k}": ', end="")
            pretty_print(v, indent + 1)
            if i < len(items) - 1:
                print(",")
            else:
                print()
        print(f"{space}}}", end="")

    elif isinstance(data, list):
        print("[")
        for i, item in enumerate(data):
            print(space + "  ", end="")
            pretty_print(item, indent + 1)
            if i < len(data) - 1:
                print(",")
            else:
                print()
        print(f"{space}]", end="")

    elif isinstance(data, str):
        print(f'"{data}"', end="")

    elif data is True:
        print("true", end="")

    elif data is False:
        print("false", end="")

    elif data is None:
        print("null", end="")

    else:
        print(data, end="")


# 🔥 Validate Mode
def validate_json(text):
    try:
        Parser(Lexer(text).tokenize()).parse()
        print("Valid JSON ✅")
    except Exception as e:
        print(f"Invalid JSON ❌ → {e}")


# 🔥 Parse + Pretty Print
def parse_file(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return

    try:
        result = Parser(Lexer(text).tokenize()).parse()
        print("\nPretty Printed JSON:\n")
        pretty_print(result)
        print("\n")
    except Exception as e:
        print(f"Error: {e}")


# 🔥 Test Runner (same as before)
def run_tests():
    with open("tests/test_cases.json") as f:
        data = json.load(f)

    print("\n✅ VALID TESTS")
    for case in data["valid_cases"]:
        try:
            Parser(Lexer(case).tokenize()).parse()
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


# 🚀 MAIN ENTRY
if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        run_tests()

    elif len(args) == 2:
        parse_file(args[1])

    elif len(args) == 3 and args[1] == "--validate":
        try:
            with open(args[2], "r") as f:
                text = f.read()
            validate_json(text)
        except FileNotFoundError:
            print(f"File '{args[2]}' not found")

    else:
        print("Usage:")
        print("  python main.py                # Run tests")
        print("  python main.py file.json      # Pretty print JSON")
        print("  python main.py --validate file.json  # Validate JSON")