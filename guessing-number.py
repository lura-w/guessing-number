import random as rn

i = 0
number = rn.randint(1,10)

name = input("Hello, What's your name?")
print(f'Okay {name}, try to guess a number between 1 and 10:')

while i < 5:
    try:
        guess = int(input())
    except ValueError:
        print('Not a number')
        i += 1
        continue
    if guess < number and guess >= 1:
        print('Your guess is too low')
    elif guess > number and guess <= 10:
        print('Your guess is too high')
    elif guess == number:
        if i == 0:
            print(f'Congratulations, you guessed in {i+1} time!!')
            break
        else:
            print(f'Congratulations, you guessed in {i+1} times!!')
            break
    else:
        print('Number not in the range')
    i += 1
    
if i == 5:
    print(f'Another time, the number was {number}')