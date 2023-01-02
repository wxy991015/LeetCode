def processQueries(queries: list[int], m: int) -> list[int]:
    result = [0] * len(queries)
    # permutation list
    p = [i for i in range(1, m+1)]
    for i in range(len(queries)):
        index = p.index(queries[i])
        result[i] = index
        value = p.pop(index)
        p.insert(0, value)
    return result

queries = [3,1,2,1]
m = 5
print(f"Output: {processQueries(queries, m)}")