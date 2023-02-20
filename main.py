#-----------------------------------------DZ1-----------------------------------------------------
"""
#1. Найдите сумму цифр трехзначного числа.

n = int(input("Ввведите трехзначное число: "))    # n = 156
a = n % 10                                        # а = 156 % 10 = 6
n = n // 10                                       # n = 156 //10 = 15
b = n % 10                                        # b = 15 % 10 = 5
n = n // 10                                       # n = 15 // 10 = 1
print("Сумма цифр трехзначного числа:", a+b+n)    #  6 + 5 + 1 = 12


#2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#   Сколько журавликов сделал каждый ребенок, если известно, 
#   что Петя и Сережа сделали одинаковое количество журавликов,
#   а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

n = int(input("Введите общее кол-во сделанных журавликов: "))
a = n//3
print("Петя сделал журавликов в количестве :", a//2, "шт.")
print("Катя сделала журавликов в количестве :", a*2, "шт.")
print("Сережа сделал журавликов в количестве :", a//2, "шт.")



#3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

n = input("Введите шестизначным номер билета: ")
a = int(n[0]) + int(n[1]) + int(n[2])
b = int(n[3]) + int(n[4]) + int(n[5])
if a == b:
    print('Счастливый')
else:
    print('Обычный')

"""

#4 Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#  если разрешается сделать один разлом по прямой между дольками 
#  (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))
if k < m*n and (k%m==0 or k%n==0):
    print('YES')
else:
    print('NO')