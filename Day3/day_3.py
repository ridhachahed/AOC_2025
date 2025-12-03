
from collections import deque

banks = []

with open("input.txt") as file: 
    for line in file:
        banks.append(list(line.strip()))



def part_1(banks):
    counter = 0
    
    for bank in banks:
        maximum_battery = deque([])
        for battery in bank:
            #print(f"Queue is {maximum_battery}")
            if len(maximum_battery) < 2:
                maximum_battery.append(battery)
                continue
        
            exisiting_battery = "".join(maximum_battery)
            
            # Possibility 1: Remove first element and move to the left
            candidate_1 = maximum_battery[-1] + battery
            # Possibility 2: Keep first element and swap second element
            candidate_2 =  maximum_battery[0] + battery
            
            if candidate_1 > candidate_2:
                if int(candidate_1) > int(exisiting_battery):
                    maximum_battery.append(battery)
                    maximum_battery.popleft()
            else:             
                if int(candidate_2) > int(exisiting_battery):
                    maximum_battery.pop()
                    maximum_battery.append(battery)
                
            #print("\n")
        max_joltage = "".join(list(maximum_battery))
        #print(f"Max voltage is {max_joltage}")
        counter += int(max_joltage)
       
    return counter


solution_1 = part_1(banks)

print(f"The solution to part 1 is {solution_1}")


def part_2(banks):
    counter = 0
    
    sequence_size = 12 
    for bank in banks:
        maximum_battery = []
        for battery in bank:
            #print(f"Queue is {maximum_battery}")
            if len(maximum_battery) < sequence_size:
                maximum_battery.append(battery)
                continue
            
            # There is N possible swaps
            current_maximum = int("".join(maximum_battery))
            maximum_battery.append(battery)
            saved_battery = maximum_battery.copy()
            
            for i in range(sequence_size+1): 
                # i is the index we remove
                maximum_battery.pop(i)
                current_candiate = int("".join(maximum_battery))
                if current_candiate > current_maximum: 
                    current_maximum = current_candiate
                # revert changes for next trial 
                maximum_battery = saved_battery.copy()
            
            # save the maximum we found
            maximum_battery = list(str(current_maximum))

        max_joltage = "".join(list(maximum_battery))
        
        counter += int(max_joltage)
       
    return counter


solution_2 = part_2(banks)

print(f"The solution to part 2 is {solution_2}")
