#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 4: functions

"""

# Project 4

import math
EPSILON = 1.0e-7

# this function accepts as the user inputs a (string) as a numerical value and returns the sim of the s


def sum_natural_squares(N):
   ''' Summing the Natural Squares '''
   if  N.isdigit() == True and N != '0':
       #converting the string entered into a integar so we can perfrom math on it
       N_int = int(N)
       Sum = (N_int*(N_int+1))/2
       return Sum  
   else:
       return None

       
def approximate_pi():
    ''' Approximating Pi '''
    
    pi = 0.0
    for i in range(1,10000000,4):
        pi += 4/i
        pi -= 4/(i+2)
        return pi

    
def approximate_sin(x):
    #https://stackoverflow.com/questions/59954286/python-define-a-function-to-calculate-sinx

    ''' Approximating sine '''
    if isinstance(x,float) == True:
        
        term = x
        two_n = 0
        total = 0
    
        while abs(term) >= EPSILON:
            total += term
            two_n += 2
            term *= -x * x / (two_n * (two_n + 1))
        return total
    
    else:
        return None
    

def approximate_cos(x):
    ''' Approximating cosine '''
    
    if isinstance(x,float) == True:
        
        term = 1
        two_n = 0
        total = 0
    
        while abs(term) >= EPSILON:
            total += term
            two_n += 2
            term *= -x * x/(two_n * two_n)
     
        return total
    
    else:
        return None
    




def main():
    
    running = True
    
    while running == True:
    
        response = input('''Please Choose one of the options below:
                         
              A. Display the sum of squares of the first N natural 
              B.  Display the approximate value of Pi.
              C.  Display the approximate value of the sine of X.
              D.  Display the approximate value of the cosine of X.
              M.  Display the menu of options.
              X. Exit from the program. 
              '''
              ).lower()
        

        if response == 'a':
            
            N= str(input("Please Enter a Number to calculate: "))
            #call funciton 
            Sum = sum_natural_squares(N) 
            # printing return values 
            if Sum != None:
                print("The Sum of Natural Sqaures is: ", Sum)
            else:
                print("Error: N was not a valid natural number", "[", N, "]" )
        
        # Pi calculation    
            
        elif response =='b':
            print("\n Calculating Pi: ")
            
            #call function
            pi = approximate_pi()
            
            print("Approximation: ", round(pi,15))
            
            #calculate pi from math module
            
            pi_math = math.pi
            
            print("Math Module: ", round(pi_math,10))
            
            #pi difference
            difference = pi_math - pi
            print("Difference: ", round(difference,10))
            

        elif response =='c':
            
            
            x_in = input("What value of Sine would you like to figure out?: ")
            
            answer = approximate_sin(x_in)
    
            #call function
            print("The Approximate Value of Sine is equal to: ", answer)
            
            
        elif response == 'd':
            
            x_cos = int(input("what value of Cosine would you like to figure out?: "))
            
            answer_cos = approximate_cos(x_cos)
            #Call function
            print("The approximate value of cosine of")
            print(answer_cos)
            
        
        elif response == 'm':
            continue
        elif response == 'x':
            print("See you later!!!!!")
            running = False
            break
        

        else:
            print("Error, please try again: ")
            continue
            
            
        question = input("Would you like to solve another problem? (yes or no):").lower()
    
        if question == 'yes':
            
            running = True
        else:
            print("Hope to see you again! ")
            break



main()


