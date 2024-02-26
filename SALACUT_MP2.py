from icecream import ic
import re as regex

def Language_Checker(Expression):
    Expression = Expression.replace(" ","").replace("+","|")
    if Expression == 'e':
        Expression = ""
    if "e" in Expression: 
        ic()
        Expression = Expression.replace("e","")
    ic(Expression)
    for x in range(0, int(input())):
        #ic()
        test_case = input()

        if test_case == "e":
            test_case = ""

        if regex.fullmatch(Expression, test_case):
            print("yes")
        else:
            print("no")

def main():
    for x in range(0, int(input())):
        Language_Checker(input())

main()