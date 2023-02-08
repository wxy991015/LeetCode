def myAtoi(s: str) -> int:
    num_result = 0
    word_phrase = s.split(" ")
    for i in range(len(word_phrase)):
        word = word_phrase[i]
        word_copy = word.strip("+-")
        if word_copy.isdigit():
            num_result = int(word_copy)
            if word[0] == "-":
                num_result = -num_result
    return num_result