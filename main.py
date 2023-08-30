class human:
    name = None
    age = None
    work = None
a = input("Введите Фамилия, Имя: ")
b = input("Введите возраст: ")
c = input("Введите деятельность: ")
file = open('Human/H.txt', 'a+')
file.write("\n\nЧеловек:\n")
file.write("Ф.И: " + a)
file.write(".\n")
file.write("Возраст: " +b)
file.write(".\n")
file.write("Деятельность: " + c)
file.write(".")

if a == human.name:
    input(human.name)
if b == human.age:
    int(input(human.age))
if c == human.work:
    input(human.work)

print("Ваще Ф.А: "+ a,)
print("Ваш возраст: "+ b)
print("Ваша деятельность: "+ c)
input()
