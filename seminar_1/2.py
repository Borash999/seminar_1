# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

a = int(input("Введите количество журавликов: "))
if (a%6==0):
    b = a//3
    c = b*2
    b = b//2
    print ("Каждый ребенок сделал= ", b, c, b) 
else:
    print ("Число не кратно 6")  

