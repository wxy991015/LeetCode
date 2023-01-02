def calculateTime(keyboard: str, word: str) -> int:
    time = 0
    start = 0
    keyboard_list = list(keyboard)
    # faster than "for i in range(len(word))"
    for i in word:
        letter_index = keyboard_list.index(i)
        time += abs(letter_index - start)
        start = letter_index
    return time

"""
idx=0
sum=0
for i in word:
id=keyboard.index(i)
sum=sum+abs(id-idx)
idx=id
return sum
"""

keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(f"Output: {calculateTime(keyboard, word)}")