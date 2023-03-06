def isCircularSentence(sentence: str) -> bool:
    words = sentence.split()
    for i in range(len(words)):
        word = words[i]
        if i == len(words) - 1:
            if word[-1] != words[0][0]:
                return False
        else:
            if word[-1] != words[i+1][0]:
                return False
    return True

sentence = "Leetcode is cool"
print(f"Output: {isCircularSentence(sentence)}")