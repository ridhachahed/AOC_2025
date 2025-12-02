

start = []
end = []

with open("input.txt") as file:
    for line in file:
        combo = line.split(",")
        for c in combo:
            split_c = c.split("-")
            start.append(split_c[0])
            end.append(split_c[1])

def detect_invalid_pattern(number: str):
    " Returns true if invalid pattern detected"
    list_of_char = list(number)
    length = len(list_of_char)
    if length % 2 == 0:
        mid = int(length / 2)
        first_half = "".join(list_of_char[:mid])
        second_half = "".join(list_of_char[mid:])
        return first_half == second_half
    else:
        return False
    

def part_1(start, end):
    counter = 0
    for a, b in zip(start, end):
        for i in range(int(a), int(b)+1):
            if detect_invalid_pattern(str(i)):
                counter += i
    return counter

counter = part_1(start, end)
print(f"The answer to part 1 is {counter}")



def detect_invalid_pattern_combi(number: str):
    " Returns true if invlaid pattern detected"
    list_of_char = list(number)
    length = len(list_of_char)
    detected = False
    
    for end in range(1, length):
        # Check if possible by length
        if length % end:
            continue
        # possible to have a combi
        else:
            pattern = "".join(list_of_char[:end])
            #print(f"pattern: {pattern}")                
            canary = True
            for i in range(0, length, len(pattern)):
                test = "".join(list_of_char[i:i+len(pattern)])
                #print(f"test: {test}")
                if test != pattern:
                    #print("different!")
                    canary = False
                    break
            detected = canary
            if detected:
                break
    return detected


def part_2(start, end):
    counter = 0
    for a, b in zip(start, end):
        for i in range(int(a), int(b)+1):
            if detect_invalid_pattern_combi(str(i)):
                #print(f"detected the follwoing pattern in [{a},{b}] : {i}")
                counter += i
    return counter

counter = part_2(start, end)
print(f"The answer to part 2 is {counter}")