def is_valid_json(input_str):
    input_str = input_str.strip()
    return input_str == "{}"

if __name__ == "__main__":
    test_json = input("{}: ")
    
    if is_valid_json(test_json):
        print("Valid JSON")
    else:
        print("Invalid JSON")
