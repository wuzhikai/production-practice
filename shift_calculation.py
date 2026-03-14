# Программа для расчёта выполнения сменного задания
import datetime

# Запрашиваем данные у пользователя
product = input("Введите название продукта: ")
plan = float(input("Введите плановое задание (тонн): "))
fact = float(input("Введите фактически произведённое количество (тонн): "))

# Вычисляем процент выполнения
percent = (fact / plan) * 100
print(f"\nПроцент выполнения: {percent:.2f}%")

# Определяем результат
if percent >= 100:
    result = "ПЛАН ВЫПОЛНЕН"
else:
    result = "ПЛАН НЕ ВЫПОЛНЕН"
print(f"Результат: {result}")

# Записываем данные в файл
with open("shift_report.txt", "a", encoding="utf-8") as f:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    f.write(f"{now} | {product} | План: {plan} т | Факт: {fact} т | Выполнено: {percent:.2f}% | {result}\n")

print("\nРезультат записан в файл shift_report.txt")