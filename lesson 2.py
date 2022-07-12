#оператор   операция
#==         равно
#!=         не равно
#<          меньше
#>          больше
#<=         меньше равно
#>=         больше равно

# Булевы операторы
# and - и называют бинарным, потому что применяется к 2ум булевым значениям
# or - или называют бинарным, потому что применяется к 2ум булевым значениям
# not - нет называют унарным, потому что применяется к 1му булевому значению
# and и or работают с двумя булевыми значениями

#таблица истинности для and
#Выражение           результат
#True and True       True
#True and False      False
#False and True      False
#False and False     False

#Оператор or или (вернет True когда один из операторов True)

print(1==1)
print(1!=1)
print(1<=1)
print(1==1.0)
print(int(1=="1.0"))

#таблица истинности оператора or
#Выражение           результат
#True or True       True
#True or False      True
#False or True      True
#False or False     False


#оператор not рименятеся к одному из значений либо к true либо к false
#Выражение           результат
#not true             false
#not false            true

print((4<5) and (9<6))
print((4<5) or (9==6))


alex = True
if not True:
    print("Hello Alex")
elif not alex:
    print("Daa")
else:
    print("non")

# elif - иначе если, и содаржит блок условий.

name = 'alex'
number = 13

if name == "alex" and number == 13:
    print('вы угадали')
else:
    print("вы не угадали")

