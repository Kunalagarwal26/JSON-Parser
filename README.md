# JSON Parser from Scratch (Python)

A simple and complete **JSON parser built from scratch in Python**, without using the built-in `json` module.

---

## Features

* Custom Lexer (Tokenization)
* Recursive Descent Parser
* Supports:

  * Objects `{}`
  * Arrays `[]`
  * Strings (with escape characters)
  * Numbers (int & float)
  * Booleans (`true`, `false`)
  * Null (`null`)
* Error handling with position tracking
* CLI support for parsing JSON files
* Built-in test cases

---

## Tech Stack

* **Language:** Python 3
* **Concepts Used:**

  * Lexical Analysis (Lexer)
  * Parsing (Recursive Descent)
  * Data Structures (dict, list)

---

## Project Structure

```
json-parser-from-scratch/
│── lexer.py
│── parser.py
│── main.py
│── utils.py
│── tests/
│   └── test_cases.json
│── sample.json
│── README.md
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kunalagarwal26/JSON-Parser.git
cd json-parser-from-scratch
```

---

## Usage

### Run Test Cases

```bash
python main.py
```

### Parse a JSON File

```bash
python main.py sample.json
```

### Example Input (`sample.json`)

```json
{
  "name": "Kunal",
  "age": 21,
  "skills": ["Python", "AI"]
}
```

### Output

```python
{'name': 'Kunal', 'age': 21, 'skills': ['Python', 'AI']}
```

---

## Testing

* Test cases are stored in:

```
tests/test_cases.json
```

* Includes:

  * ✅ Valid JSON examples
  * ❌ Invalid JSON cases

Run all tests:

```bash
python main.py
```

---

## Concepts Covered

* How JSON parsing works internally
* Tokenization (breaking input into tokens)
* Recursive parsing of nested structures
* Error handling in parsers

---

## Author

**Kunal Agarwal**

---
