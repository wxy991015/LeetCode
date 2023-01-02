def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    groups = dict()
    for i in range(len(groupSizes)):
        if groupSizes[i] in groups:
            groups[groupSizes[i]].append(i)
        else:
            groups[groupSizes[i]] = [i]

    result_group = []
    for key in groups:
        if key == len(groups[key]):
            result_group.append(groups[key])
        else:
            group_num = len(groups[key]) // key
            start, end = 0, key
            for i in range(group_num):
                group = groups[key][start:end]
                result_group.append(group)
                start, end = start + key, end + key
    return result_group

groupSizes = [2,1,3,3,3,2]
print(f"Output: {groupThePeople(groupSizes)}")