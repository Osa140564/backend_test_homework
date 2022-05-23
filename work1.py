from math import *
import itertools


message = 'Добро пожаловать в самую лучшую программу для вычисления 
           квадратного корня из заданного числа'

def  CalculateSquareRoot (Number):
    """ Вычисляет квадратный корень."""
    return  sqrt(Number )

def calc(your_number):
    if your_number <= 0:
        return    
     
    root = 0
    print(f'Мы вычислили корень квадратный из введенного вами 
          числа. Это будет: {CalculateSquareRoot(your_number)}')


print (message)
calc (25.5)