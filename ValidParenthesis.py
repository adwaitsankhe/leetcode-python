class ValidParenthesis:
    def isValid(self, s) -> bool:
        bracket_map = {"[": "]", "{": "}", "(": ")"}
        stack = []
        for bracket in s:
            if bracket in bracket_map:
                stack.append(bracket_map[bracket])
            elif not stack or stack.pop() != bracket:
                return False

        return not stack


if __name__ == "__main__":
    assert (ValidParenthesis().isValid("()") == True)
    assert (ValidParenthesis().isValid("([)") == False)
    assert (ValidParenthesis().isValid("[(])") == False)
    assert (ValidParenthesis().isValid("()[]{}") == True)
