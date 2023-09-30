import random


def get_digit(num):
    return [int(x) for x in str(num)]


def no_duplicate(num):
    num_li = get_digit(num)

    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def generate_number():
    while True:
        num = random.randint(1000, 9999)

        if no_duplicate(num):
            return num


def number_of_bulls_cows(num, guess):
    bull_cow = [0, 0]
    num_li = get_digit(num)
    guess_li = get_digit(guess)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1

    return bull_cow


num = generate_number()
tries = int(input('Enter number of tries: '))

while tries > 0:
    guess = int(input('Enter your guess: '))

    if not no_duplicate(guess):
        print('Number should not have repeated digits. Try again.')
        continue
    if guess < 1000 or guess > 9999:
        print('Enter 4 digit nuber only. try again.')
        continue

    bull_cow = number_of_bulls_cows(num, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1

    if bull_cow[0] == 4:
        print('You guessed right!')
        break
else:
    print(f"You ran out of tries. Number was {num}")
