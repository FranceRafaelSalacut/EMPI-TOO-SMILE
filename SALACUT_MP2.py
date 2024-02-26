import re as regex

def Language_Checker(Expression):
    Expression = Expression.replace(" ","")
    Expression = Expression.replace("+","|")
    if Expression == "e":
        Expression == ""
    #ic()
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