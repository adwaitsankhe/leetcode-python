class ReverseInteger:
    def reverse(self, x: int) -> int:
        result = 0
        is_negative = False

        if x < 0:
            is_negative = True
            x = abs(x)

        while x:
            result = result * 10 + x % 10
            x = x // 10

        if result > pow(2, 31):
            return 0
        else:
            return -1 * result if is_negative else result


if __name__ == "__main__":
    assert(ReverseInteger().reverse(123) == 321)
    assert(ReverseInteger().reverse(-123) == -321)
    assert(ReverseInteger().reverse(12300) == 321)
