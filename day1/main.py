import re

regex = r"(?:one|two|three|four|five|six|seven|eight|nine|\d)?"

stringToNum = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}



with open("day1/input_copy.txt") as f:
    total = 0
    for line in f:
        numbers = re.findall(regex, line.lower())

        numbers = list(filter(None, numbers))

        if (len(numbers) < 2 ):
            numbers.append(numbers[0])

        numbers = [stringToNum[num] if num in stringToNum else int(num) for num in numbers]
        
        
        numbers[0]
        numToAdd = int(str(numbers[0])+str(numbers[-1])) 
        total += numToAdd
        print(numbers,numToAdd,total)
