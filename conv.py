def convertor1():
    kgs = float(input("enter the weight in KGs"))
    pounds = kgs*2.205 
    print(f"the weight in pounds is {pounds:.2f} ")
def convertor2():
    pounds = float(input("enter the weight in pounds"))
    kgs = pounds/2.205
    print(f"the weight in kgs is {kgs:.2f}")
while True:
    print("1.convert kgs to pounds")
    print("2.convert pounds to kgs")
    print("3.exit the convertor")
    choice = int(input("enter your choice"))
    if choice == 1:
        convertor1()
    elif choice == 2:
        convertor2()
    elif choice ==3:
        print("thanks for using the convertor")
        break