class SubtractProductAndSumOfDigitsOfInteger:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        add = 0
        while n > 0:
            prod *= n % 10
            add += n % 10
            n = int(n / 10)

        return prod - add


if __name__ == "__main__":
    assert (SubtractProductAndSumOfDigitsOfInteger().subtractProductAndSum(23) == 1)
    assert (SubtractProductAndSumOfDigitsOfInteger().subtractProductAndSum(654) == 105)
    assert (SubtractProductAndSumOfDigitsOfInteger().subtractProductAndSum(236) == 25)
