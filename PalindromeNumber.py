class PalindromeNumer:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_number = x
        reversed_number = 0

        while x:
            reversed_number = reversed_number * 10 + (x % 10)
            x //= 10

        return True if original_number == reversed_number else False


if __name__ == "__main__":
    assert (PalindromeNumer().isPalindrome(123) == False)
    assert (PalindromeNumer().isPalindrome(121) == True)
