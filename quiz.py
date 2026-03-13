score = 0
answer = input("what is the capital of australia")
if answer.lower() == "canberra":
    print("correct")
    score = score + 1
else:
    print("wrong!")
answer2 = input("what is the national animal of russia")
if answer2.lower() == "brown bear":
    print("correct")
    score = score + 1 
else:
    print("wrong")
answer3 = input("what is the national food of ingland")
if answer3.lower() == "chicken tikka masala":
    print("correct")
    score = score + 1
else:
    print("wrong")
print(f"you got {score} out of 3!")
