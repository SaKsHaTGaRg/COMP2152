elements = ["hydrogen" , "helium" , "lithium" , "beryllium" , "boron" , "carbon"]
# print("Elements :" , elements)
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
            return int(input(print))
        except ValueError:
            print(" Error :Please enter an integer")
            continue