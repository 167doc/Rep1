import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print("Please, enter the number")
    a = int(input().strip())

    def odd_even(n):
        if n %2 !=0:
            return print("Weird")
        else:
            if n>=2 and n<=5:
                return print("Not Weird")
            
            if n>=6 and n<=20:
                return print("Weird")
            
            if n>20:
                return print("Not Weird")

odd_even(a)
                