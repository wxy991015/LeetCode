def findArray(pref: list[int]) -> list[int]:
    result = [pref[0]]
    start = pref[0]
    for i in range(1, len(pref)):
        # if start * value == pref[i] ==> value == pref[i] * start ==> start == pref[i] * value
        value = pref[i] ^ start
        result.append(value)
        start = start ^ value
    return result

pref = [5,2,0,3,1]
print(f"Output: {findArray(pref)}")