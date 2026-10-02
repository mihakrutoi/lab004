n = int(input("Введите количество чисел n: "))

count = 0
total_sum = 0

for _ in range(n):
    num = int(input("Введите число: "))
    count += 1
    total_sum += num

print(f"Количество: {count}")
print(f"Сумма: {total_sum}")