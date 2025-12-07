
from copy import deepcopy

def read_input(filename):
    # replace @ by True and . by False
    results = []
    with open(filename) as file:
        for line in file:
            result_line = []
            for c in line.strip():
                result_line.append(c == "@")
            results.append(result_line)
    return results
def neighberhood(x, y, x_max, y_max):
    candidates = []
    # left 
    if x > 0:
        candidates.append((x-1, y))
    # right 
    if x < x_max - 1: 
        candidates.append((x+1, y))
    # top 
    if y > 0:
        candidates.append((x, y-1))
    # bottom 
    if y < y_max - 1:
        candidates.append((x, y+1))

    # top-left 
    if y > 0 and x > 0:
        candidates.append((x-1, y-1))
    # top-right
    if y > 0 and x < x_max - 1:
        candidates.append((x+1, y-1))
    # bottom-left
    if y < y_max -1 and x > 0:
        candidates.append((x-1, y+1))
    # bottom-right 
    if y < y_max - 1 and x < x_max -1: 
        candidates.append((x+1, y+1))
    
    return candidates


def solution_1(filename):

    counter_total = 0
    plan = read_input(filename)
    x_max, y_max = len(plan[0]), len(plan)

    for x in range(x_max):
        for y in range(y_max):
            element = plan[y][x]
            if element:
                counter_element = 0
                neighbours = neighberhood(x, y, x_max, y_max)
                for (x_neigh, y_neigh) in neighbours:
                    neighbour_element = plan[y_neigh][x_neigh]
                    if neighbour_element:
                        counter_element += 1
                # fewer than four rolls of papter to access the 
                if counter_element <4:
                    counter_total +=1
    return counter_total

filename = "input.txt"
count_1 = solution_1(filename)

print(f"There are {count_1} accessible rolls of paper")


def transform_plan(plan):

    counter_total = 0
    new_plan = deepcopy(plan)
    x_max, y_max = len(plan[0]), len(plan)

    for x in range(x_max):
        for y in range(y_max):
            element = plan[y][x]
            if element:
                counter_element = 0
                neighbours = neighberhood(x, y, x_max, y_max)
                for (x_neigh, y_neigh) in neighbours:
                    neighbour_element = plan[y_neigh][x_neigh]
                    if neighbour_element:
                        counter_element += 1
                # fewer than four rolls of papter to access the 
                if counter_element <4:
                    counter_total +=1
                    new_plan[y][x] = False
    return counter_total, new_plan

def solution_2(filename):
    counter_total = 0
    plan = read_input(filename)
    new_plan = []
    while (True):
        new_count, new_plan = transform_plan(plan)
        counter_total += new_count
        if new_plan == plan:
            break
        else:
            plan = new_plan
    return counter_total

count_2 = solution_2(filename)
print(f"There are {count_2} accessible rolls of paper")