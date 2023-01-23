from typing import List

# version 1 - time limit exceeded
def numTeams(rating: List[int]) -> int:
    number_of_teams = 0
    for i in range(len(rating)):
        for j in range(i+1, len(rating)):
            for k in range(j+1, len(rating)+1):
                if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                    number_of_teams += 1
    return number_of_teams

# version 2 - 
def numTeams1(rating: List[int]) -> int:
    ascending = descending = 0
    for i in range(len(rating)):
        soldiers_as_collection, soldiers_des_collection = [rating[i]], [rating[i]]
        for j in range(i+1, len(rating)):
            if rating[j] > soldiers_as_collection[-1]:
                soldiers_as_collection.append(rating[j])
        for j in range(i+1, len(rating)):
            if rating[j] < soldiers_des_collection[-1]:
                soldiers_des_collection.append(rating[j])
    return ascending + descending

rating = [1,2,3,4]
print(f"Output: {numTeams1(rating)}")