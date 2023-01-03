from collections import defaultdict

def highFive(items: list[list[int]]) -> list[list[int]]:
    top_five_average = []
    scores_record = defaultdict(list)
    for i in range(len(items)):
        id, score = items[i][0], items[i][1]
        if id in scores_record:
            scores_record[id].append(score)
        else:
            scores_record[id] = [score]
    for id in scores_record:
        scores_record[id].sort(reverse=True)
        top_five = scores_record[id][0:5]
        top_five_average.append([id, int(sum(top_five)/5)])
    return top_five_average

items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(f"Output: {highFive(items)}")