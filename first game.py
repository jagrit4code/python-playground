import random 
secret = random.randint(1,100)
count=0
while True:
    guess = int(input("guess a number between 1 and 100"))
    count=count+1
    if guess > secret:
        print("try smaller")
    elif guess< secret:
        print("try bigger")
    else:
        print("you guesed it!")
        print(f"you guessed it in {count} tries!")
        break
    
        