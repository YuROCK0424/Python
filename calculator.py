# Простой калькулятор

from colorama import init
from colorama import Fore
init()

print(Fore.WHITE)

question = input("Что делаем? (+, -, *, /): ")

first_number = float(input("Введи первое число: "))
second_number = float(input("Введи второе число: "))

print(Fore.GREEN)

if question == "+":
	meaning = first_number + second_number
	print("Результат: "+ str(meaning))

elif question == "-":
	meaning = first_number - second_number
	print("Результат: "+ str(meaning))

elif question == "*":
	meaning = first_number * second_number
	print("Результат: "+ str(meaning))

elif question == "/":
	meaning = first_number / second_number
	print("Результат: "+ str(meaning))

else:
	print(Fore.RED)
	print("Выбрана неверная операция!")