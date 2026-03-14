trac={}
while True:
    print("1.add an expense")
    print("2.view all expenses")  
    print("3.see total amount spent")
    print("4.exit the tracker")
    choice = int(input('enter your choice'))
    if choice == 1:
        name_input = input("enter the name of the expense")
        amount_input = float(input("enter the amount spent on the expense "))
        trac[name_input]=amount_input
    elif choice == 2:
        if len(trac) == 0:
            print("wyd , go spent some money!")
        else:
            for name_input, amount_input in trac.items():
                print(f"{name_input}: {amount_input}")
    elif choice == 3 :
        if len(trac) == 0:
            print("no expense yet")
        else:
            total=0
            for amount_input in trac.values():
                total = total + amount_input
            print(f"total spent: {total:.2f}")
    elif choice == 4:
        print("thanks for using tracker")
        break 


