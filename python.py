#УРОК 1

# this is komment
print("Hello world")
# Математические ОПЕРАТОРЫ.
#**-возведение в степень
#%-деление по модулю
#//-целочисленное деление с отбрасыванием дробной части
#/ деление, * умножение, - вычетание, + сложение.
print(23 %7)
print(23 //7)
# 3 типа данных:
# функция int() - конвертирование целочисленных типов данных (целые числа)
# функция ""- str() тип данных строки (строки)
# функция float - числа с плавающей точкой (вещественные числа)

my_name = "Alex" #my_name - переменная, Alex - значение переменной. Инициализировать - присвоить значение переменной.
my_friend = "Maha"
my_number = 13
print(my_name + " " + my_friend)

#когда складываем одинаковые типы данных(сложение/склеивание строк) - это конкатенация.
#когда сладываем и умножаем разные типы данных (строка на число) - репликация(брауткаст).

print(my_name + " 13") #(my_name + " 13") - называется выражением. Выражения и их компоненты это операторы переменных и вызовы их функций.
print(my_name + " " + str(my_number))
print(f"{my_name} любимое число {my_number}") # f"{переменная}строка" - функция f-string - которая делает интрополяцию.

print(my_name * 5) #репликация (умножение строки на число)
# Переменная - это область памяти компьютера, в которой может храниться одиночное значение. знак = является оператором присваивания и сохраняет значение
color = "blye" #называется инициализация - процедура сосздания (создаем переменную и придаем значение) Мы создали переменную color и присвоили ей значение.
print(color)
#  имя переменной должно представлять собой одно слово без пробела. в имени используются только буквы цифры символы подчеркивания
# но не может начинаться с цифры.
_1 = "my little var"
print(_1)
# дефисом переменная не обозначается и спец символы нельзя.
print(len(my_name))#len считает количесвто символов в массиве
#my_name = input("ввод: ") #Все что введется в инпут - на выходе будет строка str.
#print("Привет:" + my_name)
#my_name = int(input("ввод: ")) # Строгий тип данных - когда хочу чтобы вводились только числа, делаем int
#print(my_name)

my_name = float(input("ввод: "))
print(5 + my_name)

#домашка - len() -  относится к категории встроенных функций. Есть список встроенных функций. Обр. внимание на функцию round().

a = "hololo"
print(len(a))

#УРОК 2

chek = True
print(chek)