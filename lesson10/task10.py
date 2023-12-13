import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_labels = list(set(lst))
one_hot_encoding = pd.DataFrame(0, columns=unique_labels, index=range(len(lst)))

for i, label in enumerate(lst):
    one_hot_encoding.loc[i, label] = 1

data_one_hot = pd.concat([data, one_hot_encoding], axis=1)

data_one_hot.drop('whoAmI', axis=1, inplace=True)

print(data_one_hot.head())
