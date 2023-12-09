import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
file_path = 'california_housing_train.csv'
df = pd.read_csv(file_path)

# Фильтрация данных: выбираем строки, где количество людей от 0 до 500
filtered_data = df[(df['population'] >= 0) & (df['population'] <= 500)]

# Расчет средней стоимости дома для отфильтрованных строк
avg = filtered_data['median_house_value'].mean()

# Вывод результата
print(avg)