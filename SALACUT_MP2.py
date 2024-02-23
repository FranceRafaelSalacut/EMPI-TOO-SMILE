import re as regex

def Language_Checker(Expression):
    Expression = Expression.replace(" ","")
    Expression = Expression.replace("+","|")
    subjects = []
    #ic()
    for x in range(0, int(input())):
        #ic()
        if regex.fullmatch(Expression, input()):
            print("yes")
        else:
            print("no")

def main():
    for x in range(0, int(input())):
        Language_Checker(input())

main()