import random

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# generate random int
num=random.randint(1,100)

# create list to store guesses
guesses = [0]

while True:

    # get input from user
    guess = int(input("I'm thinking of a number between 1 and 100.\n What is your guess?"))
    
    # check wether it is valid or not
    if guess < 1 or guess > 100:
        print("Out of bounds, please try again!: ")
        continue

    # compare guess with our random number and if correct print message and stop program
    if guess == num:
        print(f"Congratulations, you guessed it in only {len(guesses)} guesses!")
        break
    
    # incorrect guess, append it to the list of guesses
    guesses.append(guess)
    
    # compare with previous guesses, if first guess then guesses[-2] is always false so it proceeds to else
    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print("WARMER")
        else:
            print("COLDER")
    else:
        if abs(num-guess) <= 10:
            print("WARM")
        else:
            print("COLD")