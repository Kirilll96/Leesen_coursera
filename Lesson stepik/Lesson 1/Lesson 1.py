n = int(input("Введите число последовательности: "))
summ = 0



if(1 <= n and n <= 100):
    for i in range(1, n + 1):
        inp_val = int(input(f"Введите число #{i}: "))
        summ += inp_val
else:
    print("Введеное число последовательности бльшое или слишком мало")
print("Сумма чисел = ", summ)
