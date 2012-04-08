from math import *

def main():
    x = int(raw_input("Enter a number to get the square root"))
    guess = 1
    guess = improve_answer(guess,x)
    square_root(guess,x)

def square_root(guess,x):
    while(not good_enough(guess,x)):
        guess = improve_answer(guess,x)
    print guess

def average(a,b):
    return (a+b)/2.0

def improve_answer(guess,x):
    return average(guess,x/guess)

def good_enough(guess,x):
    good = abs(guess*guess-x)
    return(good<0.001)
    

if __name__ == '__main__':
    main()




