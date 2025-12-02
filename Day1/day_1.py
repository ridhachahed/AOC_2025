

def check_boundary(number:int) -> int:
    while(number > 99 or number <0):
        if number > 99: 
            number = number - 100
        elif number < 0:
            number = 100 + number
    return number

def part_1(start_number: int):
    
    count_zeroes: int = 0 
    with open("input.txt") as file:
        for line in file:
            line = list(line.strip())
            # either L (negatif) or R (positif)
            rotation = line[0]
            number = int("".join(line[1:]))

            if rotation.lower() == "l":
                start_number -= number
            elif rotation.lower() == "r":
                start_number += number
            else:
                raise ValueError(f"invalid roation {rotation.lower()}")
            
            start_number = check_boundary(start_number)
            
            if start_number == 0:
                count_zeroes +=1
            
    print(f"Final number is {start_number}")
    print(f"The password is {count_zeroes}")
    
part_1(start_number = 50)


    
def check_boundary_and_dial(old_number, new_number):
    count = 0
    counter_dial = 0
    
    while(new_number > 99 or new_number <0):
        if new_number > 99: 
            new_number = new_number - 100
            counter_dial +=1
        elif new_number < 0:
            new_number = 100 + new_number
            if not(old_number == 0 and count == 0):
                counter_dial +=1
        count +=1
    
    return new_number, counter_dial
    
    
def part_2(start_number: int):
    count_zeroes = 0
    old_number = start_number
    
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            rotation = line[0]
            number = int(line[1:])
            
            # Don't count when starting form zero ! 
            if rotation.lower() == "l":
                new_number = old_number - number
                if new_number <= 0 and old_number != 0:
                    count_zeroes += (-new_number) // 100 + 1
                elif new_number < 0 and old_number == 0:
                    count_zeroes += (-new_number - 1) // 100 
                    if new_number % 100 == 0 and new_number != 0:
                        count_zeroes += 1
                new_number = new_number % 100
                    
            elif rotation.lower() == "r":
                new_number = old_number + number
                if old_number == 0:
                    count_zeroes += (new_number - 1) // 100 if new_number > 0 else 0
                else:
                    count_zeroes += new_number // 100
                new_number = new_number % 100
                    
            old_number = new_number
            
    print(f"The password is {count_zeroes}")
    


    
part_2(start_number = 50)