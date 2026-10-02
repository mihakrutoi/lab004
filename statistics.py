n = int(input("Введите количество чисел n: "))

first_num = int(input("Введите число: "))

total_sum = first_num
maximum = first_num
positives_count = 1 if first_num > 0 else 0

for _ in range(n - 1):
    num = int(input("Введите число: "))
    total_sum += num
    
    if num > maximum:
        maximum = num        
    if num > 0:
        positives_count += 1

print(f"Сумма: {total_sum}")
print(f"Количество положительных: {positives_count}")
print(f"Максимум: {maximum}")