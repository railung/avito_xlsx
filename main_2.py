import pandas as pd
import random
from datetime import datetime, timedelta

# Функция для генерации случайной цены
def generate_random_price(min_price=1000, max_price=5000):
    return random.randint(min_price, max_price)

# Функция для перемешивания фотографий
def shuffle_photos(photos_list):
    random.shuffle(photos_list)
    return photos_list

# Функция для генерации случайных временных слотов
def generate_time_slots(start_time, end_time, num_slots):
    time_slots = []
    time_delta = (end_time - start_time) / num_slots
    for i in range(num_slots):
        slot_time = start_time + i * time_delta
        # Изменение формата времени на DD.MM.YYYY HH:MM:SS
        time_slots.append(slot_time.strftime("%d.%m.%Y %H:%M:%S"))
    return time_slots

# Пример списка заголовков, фотографий и городов
titles = ["Рабочий стол на заказ", "Шкаф-купе на заказ", "Кухонный гарнитур", "Мебель для офиса"]
photos = [
    ["photo1.jpg", "photo2.jpg", "photo3.jpg"],
    ["photo4.jpg", "photo5.jpg", "photo6.jpg"],
    ["photo7.jpg", "photo8.jpg", "photo9.jpg"]
]
cities = ["Москва", "Подольск", "Коломна", "Химки", "Мытищи"]

# Количество объявлений
num_ads = 10

# Определяем временной диапазон публикаций
start_time = datetime.now()  # Текущее время
end_time = start_time + timedelta(days=1)  # Завершение публикаций через 1 день

# Генерация временных слотов для каждого объявления
time_slots = generate_time_slots(start_time, end_time, num_ads)

# Создаем список объявлений
generated_ads = []
for i in range(num_ads):
    ad_data = {
        "Id": f"ad-{i+1:03d}",
        "Title": random.choice(titles),
        "Price": generate_random_price(),
        "Photos": ", ".join(shuffle_photos(random.choice(photos))),
        "City": random.choice(cities),
        "DateBegin": time_slots[i],  # Время начала публикации в формате DD.MM.YYYY HH:MM:SS
        # Дата окончания публикации — через 12 часов после начала
        "AvitoDateEnd": (datetime.strptime(time_slots[i], "%d.%m.%Y %H:%M:%S") + timedelta(hours=12)).strftime("%d.%m.%Y %H:%M:%S"),
    }
    generated_ads.append(ad_data)

# Конвертируем данные в DataFrame для экспорта в Excel
generated_ads_df = pd.DataFrame(generated_ads)

# Сохраняем в файл Excel
generated_ads_df.to_excel("generated_avito_ads.xlsx", index=False)

print("Объявления успешно сгенерированы и сохранены в 'generated_avito_ads.xlsx'")
