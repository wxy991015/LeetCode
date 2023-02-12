from typing import List

def reverseWords(s: List[str]) -> None:
    sentence = "".join(s)[::-1]
    word = ""
    words = []
    for i in range(len(sentence)):
        if sentence[i] == " ":
            words.extend(list(word[::-1]))
            words.append(sentence[i])
            word = ""
        else:
            word += sentence[i]
    words.extend(word[::-1])
    s.clear()
    s.extend(words)

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
reverseWords(s)
print(s)