# version 1 - loop through sentence
def reverseWords(s: str) -> str:
    s = s.strip()
    words = []
    word = ""
    for i in range(len(s)):
        if s[i] == " ":
            if len(word) != 0:
                words.append(word)
                word = ""
            continue
        word += s[i]
    words.append(word)
    reversed_res = ""
    i = len(words) - 1
    while i >= 0:
        reversed_res += words[i] + " "
        i -= 1
    reversed_res = reversed_res.strip()
    return reversed_res

# version 2 - use split method
def reverseWords1(s: str) -> str:
    s = s.strip()
    words = s.split()
    reversed_res = " ".join(words[::-1])
    return reversed_res

s = "a good   example"
print(f"Output: {reverseWords1(s)}")