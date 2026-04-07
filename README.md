# JSON-Parser

This project is a step-by-step implementation of a **JSON Parser**, without using Python’s built-in `json` module.

---

## Features

* Custom Lexer (Tokenization)
* Recursive Descent Parser
* Supports:

  * Objects
  * Arrays
  * Strings
  * Numbers
  * Booleans
  * Null
* Error handling for invalid JSON

---

## Project Structure

* `lexer.py` → Converts input into tokens
* `parser.py` → Parses tokens into Python objects
* `main.py` → Entry point
* `tests/` → JSON test cases

---

## Goal

To understand how parsers work internally (like compilers & interpreters).

---

## Tech Stack

* Python 3

---

## Progress

* [ ] Step 1: Basic JSON validation
* [ ] Step 2: Parse strings
* [ ] Step 3: Parse numbers, booleans, null
* [ ] Step 4: Nested objects & arrays
* [ ] Step 5: Error handling & testing
