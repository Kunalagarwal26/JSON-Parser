from lexer import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        self.pos += 1

    def expect(self, token_type):
        token = self.peek()

        if token is None:
            raise Exception(f"Expected {token_type}, but reached end")

        if token.type != token_type:
            raise Exception(f"Expected {token_type}, got {token.type} at position {token.pos}")

        self.advance()
        return token

    def parse(self):
        result = self.parse_value()

        if self.peek() is not None:
            raise Exception(f"Extra data after JSON at position {self.peek().pos}")

        return result

    def parse_value(self):
        token = self.peek()

        if token is None:
            raise Exception("Unexpected end of input")

        if token.type == TokenType.LBRACE:
            return self.parse_object()

        elif token.type == TokenType.LBRACKET:
            return self.parse_array()

        elif token.type == TokenType.STRING:
            self.advance()
            return token.value

        elif token.type == TokenType.NUMBER:
            self.advance()
            return token.value

        elif token.type == TokenType.TRUE:
            self.advance()
            return True

        elif token.type == TokenType.FALSE:
            self.advance()
            return False

        elif token.type == TokenType.NULL:
            self.advance()
            return None

        else:
            raise Exception(f"Unexpected token {token.type} at position {token.pos}")

    def parse_object(self):
        obj = {}
        self.expect(TokenType.LBRACE)

        if self.peek() and self.peek().type == TokenType.RBRACE:
            self.advance()
            return obj

        while True:
            key = self.expect(TokenType.STRING).value
            self.expect(TokenType.COLON)

            obj[key] = self.parse_value()

            if self.peek() and self.peek().type == TokenType.COMMA:
                self.advance()
            else:
                break

        self.expect(TokenType.RBRACE)
        return obj

    def parse_array(self):
        arr = []
        self.expect(TokenType.LBRACKET)

        if self.peek() and self.peek().type == TokenType.RBRACKET:
            self.advance()
            return arr

        while True:
            arr.append(self.parse_value())

            if self.peek() and self.peek().type == TokenType.COMMA:
                self.advance()
            else:
                break

        self.expect(TokenType.RBRACKET)
        return arr