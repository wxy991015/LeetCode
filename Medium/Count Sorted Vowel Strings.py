def countVowelStrings(n: int) -> int:
    def solver(n: int, vowels: int):
        if n == 0:
            return 1
        result = 0
        for i in range(vowels, 6):
            result += solver(n-1, i)
        return result
    return solver(n, 1)

n = 2
print(f"Output: {countVowelStrings(n)}")