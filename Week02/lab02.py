import random

elements = ["hydrogen" , "helium" , "lithium" , "beryllium" , "boron" , "carbon"]
print("Elements :" , elements)
# # git add . && git commit -m"" && git push
#
# # def funct_name():
# #     return True
#
# def say_greeting(name , message="HI"):
#     print(f" {message} , {name}")
#
# say_greeting("sakshat")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integere!")
            continue

try:
    elements_selected = get_valid_int_input("Enter the index of the element you would like to select: ")
    #roll the dice
    elementRoll =  random.randint(1,6)
    totalNum = elements_selected + elementRoll

    # print the result based on the totalNum
    if elementRoll <= 2:
        print("You rolled a weak element, freind")
    elif elementRoll <= 4:
        print("your elememt is moderate")
    else:
        print("You rolled a strong element")
except Exception as e:
    print("")
