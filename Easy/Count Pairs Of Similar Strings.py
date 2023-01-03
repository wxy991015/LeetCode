def similarPairs(words: list[str]) -> int:
    similar_pairs = 0
    for i in range(len(words)):
        word1 = words[i]
        for j in range(i+1, len(words)):
            word2 = words[j]
            if set(word1) == set(word2): similar_pairs += 1
    return similar_pairs

words = ["aabb","ab","ba"]
print(f"Output: {similarPairs(words)}")