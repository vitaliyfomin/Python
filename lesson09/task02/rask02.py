import pandas as pd

# Загрузка данных из CSV-файла в DataFrame
file_path = 'california_housing_train.csv'
df = pd.read_csv(file_path)

# Находим минимальное значение переменной 'population'
min_population = df['population'].min()

# Выбираем строки с минимальным значением 'population'
min_population_rows = df[df['population'] == min_population]

# Находим максимальное значение переменной 'households' в этом подмножестве
max_households_in_min_population = min_population_rows['households'].max()

# Вывод результата
print(max_households_in_min_population)
