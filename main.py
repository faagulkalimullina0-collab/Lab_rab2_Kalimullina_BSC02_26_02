# import math

# print("Выберите режим обработки:")
# print("1 — черновая, k = 1.0")
# print("2 — получистовая, k = 0.85")
# print("3 — чистовая, k = 0.7")


# while True:
#     rech = input("Введите номер режима (1, 2 или 3): ")
#     if rech == "1":
#         mode = "черновая"
#         k = 1.0
#         break
#     elif rech == "2":
#         mode = "получистовая"
#         k = 0.85
#         break
#     elif rech == "3":
#         mode = "чистовая"
#         k = 0.7
#         break
#     else:
#         print("Введите 1, 2 или 3.")

# while True:
#     try:
#         D = float(input("Введите диаметр D (от 1 до 500 мм): "))
#         if 1 <= D <= 500:
#             break
#         else:
#             print("Число должно быть от 1 до 500.")
#     except :
#         print("Ошибка! Введи число, пожалуйста.")

# while True:
#     try:
#         n = float(input("Введите частоту n (от 50 до 3000 об/мин): "))
#         if 50 <= n <= 3000:
#             break
#         else:
#             print("Ошибка! Число должно быть от 50 до 3000.")
#     except:
#         print("Ошибка! Введи число, пожалуйста.")

# V = math.pi * D * n / 1000
# V_adj = V * k

# if D < 10:
#     diam = "малый диаметр"
# elif 10 <= D <= 100:
#     diam = "нормальный диаметр"
# else:
#     diam = "крупный диаметр"


# print(f"Режим: {mode}")
# print(f"Скорость резания V: {V:.2f} м/мин")
# print(f"Скорректированная V_adj: {V_adj:.2f} м/мин")
# print(f"Класс диаметра: {diam} (D = {D} мм)")




import math

print("Выберите режим обработки:")
print("1 — черновая, k = 1.0")
print("2 — получистовая, k = 0.85")
print("3 — чистовая, k = 0.7")

f = True
while f:
    rech = input("Введите номер режима (1, 2 или 3): ")
    if rech == "1":
        mode = "черновая"
        k = 1.0
        f = False  
    elif rech == "2":
        mode = "получистовая"
        k = 0.85
        f = False  
    elif rech == "3":
        mode = "чистовая"
        k = 0.7
        f = False  
    else:
        print("Ошибка! Введите 1, 2 или 3.")

f = True
while f:
    try:
        D = float(input("Введите диаметр D (от 1 до 500 мм): "))
        if 1 <= D <= 500:
            f = False  
        else:
            print("Число должно быть от 1 до 500.")
    except ValueError: 
        print("Ошибка! Введи число, пожалуйста.")

f = True
while f:
    try:
        n = float(input("Введите частоту n (от 50 до 3000 об/мин): "))
        if 50 <= n <= 3000:
            f = False  
        else:
            print("Ошибка! Число должно быть от 50 до 3000.")
    except ValueError:
        print("Ошибка! Введи число, пожалуйста.")

V = math.pi * D * n / 1000
V_adj = V * k

if D < 10:
    diam = "малый диаметр"
elif 10 <= D <= 100:
    diam = "нормальный диаметр"
else:
    diam = "крупный диаметр"

print(f"Режим: {mode}")
print(f"Скорость резания V: {V:.2f} м/мин")
print(f"Скорректированная V_adj: {V_adj:.2f} м/мин")
print(f"Класс диаметра: {diam} (D = {D} мм)")