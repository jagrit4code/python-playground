def ask_question(question,correct_answer):
    answer = input( question )
    if answer.lower() == correct_answer:
        print("correct!")
        return 1
    else:
        print("wrong!")
        return 0

score = 0 
score = score + ask_question("what is the capital of australia?","canberra")
score = score + ask_question("what is the national animal of russia?","brown bear")
score = score + ask_question("what is the national food of england","chicken tikka masala")
print(f"you got {score} out of 3! ")
