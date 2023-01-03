# version 1 - Faster
def similarPairs(words: list[str]) -> int:
    similar_pairs = 0
    for i in range(len(words)):
        word1 = words[i]
        for j in range(i+1, len(words)):
            word2 = words[j]
            if set(word1) == set(word2): similar_pairs += 1
    return similar_pairs

# version 2
def similarPairs1(words: list[str]) -> int:
    cnt = 0
    # enumerate => (0, words[0]), (1, words[1])...
    for i,w1 in enumerate(words):
        for w2 in words[i+1:]:
            cnt += set(w1) == set(w2)
    return cnt

words = ["aabb","ab","ba"]
print(f"Output: {similarPairs(words)}")