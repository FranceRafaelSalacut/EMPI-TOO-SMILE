'''
HONOR CODE
I declare, upon my honor, that I did this machine problem assignment by myself using online resources from the following: 

(1) https://www.geeksforgeeks.org/re-fullmatch-function-in-python/
(2) https://docs.python.org/3/library/re.html

Further, my solution is not a copy from the aforementioned sources.

REPO LINK
NOTE: THE COMMIT MESSAGES ARE NOT FUNCTIONAL
https://github.com/FranceRafaelSalacut/EMPI-TOO-SMILE

The code is very short (if comments are removed) since the regex library in python is powerful. 
'''

import re as regex

def Language_Checker(Expression):
    # Removing all spaces for the regex to work and replacing the "+" into "|" since python regex recognizes "|" as union or "OR".
    Expression = Expression.replace(" ","").replace("+","|")
    
    # Replacing the empty string "e" with a blank since python recognizes it more as an empty string.
    if Expression == "e":
        Expression = ""
    if "e" in Expression: 
        Expression = Expression.replace("e","")
        
    #ic()
    
    # Immediately plugging in the user input to the loop.
    for x in range(0, int(input())):
        #ic()
        
        test_case = input()
        
        if test_case == "e":
            test_case = ""
        
        # I found this function call of python's regex library through geeks for geeks then looked for documentation afterwards.
        if regex.fullmatch(Expression, test_case):
            print("yes")
        else:
            print("no")

def main():
    # Immediately plug in the first input into the for loop as well as into the function call.
    for x in range(0, int(input())):
        Language_Checker(input())

main()