# Название файла: dataVisualization.py

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
data = pd.read_csv('data.csv')

# Группировка данных по категориям и подсчет количества записей в каждой категории
grouped_data = data.groupby('category').size()

# Создание графика
plt.figure(figsize=(8, 6))
plt.bar(grouped_data.index, grouped_data.values)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Data Visualization')
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение графика в файл
plt.savefig('chart.png')

# Вывод информации о сохранении графика
print('Chart saved as chart.png')
