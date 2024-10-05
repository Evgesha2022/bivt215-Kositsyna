import math
import random

def nok(a, b):
    return abs(a * b) // math.gcd(a, b)

def get_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = random.randint(1, 100)
    
    question = f"{num1} {num2} {num3}"
    
    # Вычисляем НОК для трех чисел
    lcm_two = nok(num1, num2)
    correct_answer = str(nok(lcm_two, num3))
    
    return question, correct_answer

