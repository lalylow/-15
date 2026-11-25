# Лаба 15: визуализация данных — библиотека Matplotlib
import os
import numpy as np
import matplotlib
matplotlib.rcParams["font.family"] = "DejaVu Sans"  # кириллица
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)  # папка для графиков

# ---------- Задание 1. Линейный график ----------
days = ["Пн", "Вт", "Ср", "Чт", "Пт"]
work = [2, 3.5, 7, 5, 9]
plt.figure()
plt.plot(days, work, "o-", color="steelblue", label="Сложность задач")
plt.xlabel("День недели")
plt.ylabel("Сложность")
plt.title("Сложность задач по дням")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("images/plot1.png", dpi=150)
plt.show()
plt.close()

# ---------- Задание 2. Scatter: донаты vs уровень ----------
np.random.seed(42)
level = np.random.randint(1, 100, 60)
donates = level * 15 + np.random.normal(0, 200, 60)
plt.figure()
plt.scatter(level, donates, alpha=0.6, color="seagreen")
plt.xlabel("Уровень игрока")
plt.ylabel("Сумма донатов, руб.")
plt.title("Зависимость донатов от уровня")
plt.grid(True, alpha=0.3)
plt.savefig("images/scatter_donates.png", dpi=150)
plt.show()
plt.close()

# ---------- Задание 3. Bar: игроки по классам ----------
classes = ["Воин", "Маг", "Стрелок", "Паладин"]
counts  = [14, 9, 11, 6]
plt.figure()
plt.bar(classes, counts, color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
plt.xlabel("Класс персонажа")
plt.ylabel("Количество игроков")
plt.title("Распределение игроков по классам")
plt.savefig("images/bar_classes.png", dpi=150)
plt.show()
plt.close()

# ---------- Задание 4. Гистограмма ----------
np.random.seed(7)
times = np.random.normal(loc=120, scale=25, size=500)
plt.figure()
plt.hist(times, bins=30, color="steelblue", edgecolor="black")
plt.xlabel("Время выполнения, мс")
plt.ylabel("Количество задач")
plt.title("Распределение времени выполнения задач")
plt.savefig("images/hist_times.png", dpi=150)
plt.show()
plt.close()
print("Среднее:", times.mean().round(1))
print("Минимум:", times.min().round(1))
print("Максимум:", times.max().round(1))

# ---------- Задание 5. Subplots 1x2 ----------
np.random.seed(42)
x = np.arange(1, 21)
y = x * 3 + np.random.normal(0, 10, 20)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(x, y, "o-")
axes[0].set_title("Линейный график")
axes[0].set_xlabel("Время")
axes[0].set_ylabel("Значение")
axes[1].scatter(x, y, color="crimson")
axes[1].set_title("Точечная диаграмма")
axes[1].set_xlabel("Время")
axes[1].set_ylabel("Значение")
plt.tight_layout()
plt.savefig("images/subplots.png", dpi=150)
plt.show()
plt.close()

# ---------- Задание 6. Проверка PNG ----------
print("\nФайлы в images/:")
for f in sorted(os.listdir("images")):
    print(" ", f)

# ---------- Задание 7 (бонус). График из Pandas ----------
# Раскомментируй, если рядом лежит dataset.csv из лабы 14
# import pandas as pd
# df = pd.read_csv("dataset.csv", encoding="utf-8")
# counts = df["klass"].value_counts()
# plt.figure()
# plt.bar(counts.index, counts.values, color="slateblue")
# plt.title("Игроки по классам (из Pandas)")
# plt.savefig("images/pandas_bar.png", dpi=150)
# plt.show()