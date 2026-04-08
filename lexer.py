from enum import Enum


class TokenType(Enum):
    LBRACE = "{"
    RBRACE = "}"
    LBRACKET = "["
    RBRACKET = "]"
    COLON = ":"
    COMMA = ","
    STRING = "STRING"
    NUMBER = "NUMBER"
    TRUE = "true"
    FALSE = "false"
    NULL = "null"


class Token:
    def __init__(self, type_, value=None, pos=None):
        self.type = type_
        self.value = value
        self.pos = pos

    def __repr__(self):
        return f"{self.type.name}:{self.value}"


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def peek(self):
        if self.pos < len(self.text):
            return self.text[self.pos]
        return None

    def advance(self):
        self.pos += 1

    def tokenize(self):
        tokens = []

        while self.pos < len(self.text):
            char = self.peek()

            if char.isspace():
                self.advance()

            elif char == "{":
                tokens.append(Token(TokenType.LBRACE, pos=self.pos))
                self.advance()

            elif char == "}":
                tokens.append(Token(TokenType.RBRACE, pos=self.pos))
                self.advance()

            elif char == "[":
                tokens.append(Token(TokenType.LBRACKET, pos=self.pos))
                self.advance()

            elif char == "]":
                tokens.append(Token(TokenType.RBRACKET, pos=self.pos))
                self.advance()

            elif char == ":":
                tokens.append(Token(TokenType.COLON, pos=self.pos))
                self.advance()

            elif char == ",":
                tokens.append(Token(TokenType.COMMA, pos=self.pos))
                self.advance()

            elif char == '"':
                tokens.append(self.read_string())

            elif char.isdigit() or char == "-":
                tokens.append(self.read_number())

            elif self.text.startswith("true", self.pos):
                tokens.append(Token(TokenType.TRUE, True, self.pos))
                self.pos += 4

            elif self.text.startswith("false", self.pos):
                tokens.append(Token(TokenType.FALSE, False, self.pos))
                self.pos += 5

            elif self.text.startswith("null", self.pos):
                tokens.append(Token(TokenType.NULL, None, self.pos))
                self.pos += 4

            else:
                raise Exception(f"Unexpected character at position {self.pos}: {char}")

        return tokens

    def read_string(self):
        start_pos = self.pos
        self.advance()
        result = ""

        while self.peek() is not None:
            char = self.peek()

            if char == '"':
                self.advance()
                return Token(TokenType.STRING, result, start_pos)

            if char == "\\":  # escape handling
                self.advance()
                esc = self.peek()

                escape_map = {
                    '"': '"',
                    "\\": "\\",
                    "n": "\n",
                    "t": "\t"
                }

                if esc in escape_map:
                    result += escape_map[esc]
                else:
                    raise Exception(f"Invalid escape character at {self.pos}")

                self.advance()
            else:
                result += char
                self.advance()

        raise Exception(f"Unterminated string starting at {start_pos}")

    def read_number(self):
        start_pos = self.pos
        result = ""

        if self.peek() == "-":
            result += "-"
            self.advance()

        while self.peek() is not None and (self.peek().isdigit() or self.peek() == "."):
            result += self.peek()
            self.advance()

        try:
            if "." in result:
                return Token(TokenType.NUMBER, float(result), start_pos)
            else:
                return Token(TokenType.NUMBER, int(result), start_pos)
        except:
            raise Exception(f"Invalid number at position {start_pos}: {result}")