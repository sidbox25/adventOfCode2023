import re

# Define the regex pattern
regex = r"(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)?"

stringToNum = {
    "zero": 0,
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

with open("day1/input.txt") as f:
    total = 0
    for line in f:
        numbers = re.findall(regex, line.lower())  # Use lower() to match case-insensitively

        numbers = list(filter(None, numbers))


        if len(numbers) < 2:
            numbers.append(numbers[0])

        # Convert words to numbers
        numbers = [stringToNum[num] if num in stringToNum else int(num) for num in numbers]

        num_to_add = int(str(numbers[0]) + str(numbers[-1]))
        total += num_to_add
        print(numbers, num_to_add, total)
