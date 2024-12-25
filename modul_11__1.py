# 1. Библиотека Requests:
import requests

# Отправление GET-запроса на API:
r = requests.get('https://api.imgbb.com/1/upload')

# Получение ответов в виде словаря
rj = r.json()
print(rj)

# Получение значения по ключу:
print(f'Значение: {rj['status_code']}')

# Получение заголовков запросов:
print(r.request.headers)

# Скачивание и сохранение файла
img1 = 'https://avatars.mds.yandex.net/i?id=234869a17a12d98905ce6de048fc1060_l-4507718-images-thumbs&n=13'
r = requests.get(img1)
with open('winter.jpg', 'wb') as file:
    file.write(r.content)

# 2. Библиотека Pillow:
from PIL import Image

# Открытие ранее скаченного файла
im = Image.open('winter.jpg')

# Изменение размера изображения:
ir = im.resize((520, 420))

# Конвертирование изображения в другой формат и сохранение
ir.save('winter2.bmp', format='bmp')

# Показ изменненых данных:
print(ir.format, ir.size, ir.mode)

# 3. Библиотека Numpy:
import numpy

# Создание векторов x и y
x = numpy.linspace(-5, 5, 70)
y = x ** 2

# 4. Библиотека Matplotlib
import matplotlib.pyplot as plt

# Создание точечной диаграммы
plt.figure(figsize=(12, 6))
plt.title('Диаграмма', size=22, color='green')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.grid(True, color='red')
plt.plot(x, y)

# Показ диаграммы
plt.show()
