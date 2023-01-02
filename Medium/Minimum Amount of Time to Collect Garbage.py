def garbageCollection(garbage: list[str], travel: list[int]) -> int:
    minimum_time = 0
    metal_garbage_time = 0
    paper_garbage_time = 0
    glass_garbage_time = 0
    for i in range(len(garbage)):
        # if not ==> still need to travel[i-1] add if garbage in other later index
        # Metal garbage time: 0
        if "M" in garbage[i]:
            metal_garbage_unit = garbage[i].count("M")
            if metal_garbage_time == 0:
                metal_garbage_time += sum(travel[0:i])
            metal_garbage_time += metal_garbage_unit * 1 + travel[i-1]
        # Paper garbage time: 8
        if "P" in garbage[i]:
            paper_garbage_unit = garbage[i].count("P")
            if paper_garbage_time == 0:
                paper_garbage_time += sum(travel[0:i]) + paper_garbage_unit * 1
            else:
                paper_garbage_time += paper_garbage_unit * 1 + travel[i-1]
        # Glass garbage time: 13
        if "G" in garbage[i]:
            glass_garbage_unit = garbage[i].count("G")
            if glass_garbage_time == 0:
                glass_garbage_time += sum(travel[0:i]) + glass_garbage_unit * 1
            else:
                # if not ==> still need to travel[i-1] add if garbage in other later index
                glass_garbage_time += glass_garbage_unit * 1 + travel[i-1]
                print(glass_garbage_unit)
    print(f"Metal garbage time: {metal_garbage_time}")
    print(f"Paper garbage time: {paper_garbage_time}")
    print(f"Glass garbage time: {glass_garbage_time}")
    minimum_time = paper_garbage_time + glass_garbage_time + metal_garbage_time
    return minimum_time

garbage = ["G","P","GP","GG"]
travel = [2,4,3]
print(f"Output: {garbageCollection(garbage, travel)}")