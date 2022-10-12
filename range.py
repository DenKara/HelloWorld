value = int(input("Введите число "))

ls = list()

for i in range(1, value + 1):
    print(i)
    ls.append(i * 2)

print("Квадраты равны", ls)
