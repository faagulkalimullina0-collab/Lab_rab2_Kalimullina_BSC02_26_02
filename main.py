
print("Выберите материал:")
print("1 — сталь, p = 7850 кг/м3")
print("2 — алюминий, p = 2700 кг/м3")
print("3 — медь, p = 8900 кг/м3")

f = True
while f:
    rech = input("Введите номер материала (1, 2 или 3): ")
    if rech == "1":
        mode = "сталь"
        p = 7850
        f = False
    elif rech == "2":
        mode = "алюминий"
        p = 2700
        f = False
    elif rech == "3":
        mode = "медь"
        p = 8900
        f = False
    else:
        print("Ошибка! Введите 1, 2 или 3.")

f = True
while f:
    try:
        L = float(input("Введите длину листа L (от 0.1 до 5 м): "))
        if 0.1 <= L <= 5:
            f = False
        else:
            print("Ошибка! Длина должна быть от 0.1 до 5 м.")
    except ValueError:
        print("Ошибка! Введите число.")

f = True
while f:
    try:
        W = float(input("Введите ширину листа W (от 0.1 до 3 м): "))
        if 0.1 <= W <= 3:
            f = False
        else:
            print("Ошибка! Ширина должна быть от 0.1 до 3 м.")
    except ValueError:
        print("Ошибка! Введите число.")

f = True
while f:
    try:
        t = float(input("Введите толщину листа t (от 0.1 до 20 мм): "))
        if 0.1 <= t <= 20:
            f = False
        else:
            print("Ошибка! Толщина должна быть от 0.1 до 20 мм.")
    except ValueError:
        print("Ошибка! Введите число.")

f = True
while f:
    try:
        q = int(input("Введите количество листов q (от 1 до 1000): "))
        if 1 <= q <= 1000:
            f = False
        else:
            print("Ошибка! Количество должно быть от 1 до 1000.")
    except ValueError:
        print("Ошибка! Введите целое число.")

m = L * W * (t / 1000) * p * q

if t < 0.5:
    clas = "тонкий лист"
elif 0.5 <= t <= 5:
    clas = "нормальная толщина"
else:
    clas = "толстый лист"

print("\nРезультаты расчёта:")
print(f"Материал: {mode}")
print(f"Масса партии: {m:.2f} кг")
print(f"Класс толщины: {clas} (t = {t} мм)")
