# Tribonacci row: create and add first 3 numbers
first_tribonacci_number = int(input())
second_tribonacci_number = int(input())
third_tribonacci_number = int(input())
tribonacci_row = [first_tribonacci_number, second_tribonacci_number, third_tribonacci_number]

# numerical_spiral: create and add first_number, and step
current_spiral_number = int(input())
spiral_step = int(input())

current_tribonacci_number = third_tribonacci_number

while current_tribonacci_number <= 1000000:
    current_tribonacci_number = first_tribonacci_number + \
                                second_tribonacci_number + \
                                third_tribonacci_number
    tribonacci_row.append(current_tribonacci_number)
    first_tribonacci_number = second_tribonacci_number
    second_tribonacci_number = third_tribonacci_number
    third_tribonacci_number = current_tribonacci_number

spiral_numbers = [current_spiral_number]
spiral_count = 0
spiral_step_mul = 1

while current_spiral_number <= 1000000:
    current_spiral_number += spiral_step * spiral_step_mul
    spiral_numbers.append(current_spiral_number)
    spiral_count += 1

    if spiral_count % 2 == 0:
        spiral_step_mul += 1

found_number = False
for i in range(len(tribonacci_row)):
    for j in range(len(spiral_numbers)):
        if tribonacci_row[i] == spiral_numbers[j] and tribonacci_row[i] <= 1000000:
            print(tribonacci_row[i])
            found_number = True
            break
    if found_number:
        break

if not found_number:
    print("No")

