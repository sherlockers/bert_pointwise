import csv
import tensorflow as tf
import pandas as pd

filename = "/home/yangguodong/digix/bert/digix_data/top100forbert_en.csv"
filename1 = "/home/yangguodong/digix/bert/digix_data/train_en.csv"
filename2 = "/home/yangguodong/digix/bert/digix_data/dev_en.csv"

# data = pd.read_csv(filename)
# data.loc[0:int(len(data) * 0.8)].to_csv(filename1, encoding='utf-8', index=False)
# data.loc[int(len(data) * 0.8):len(data)].to_csv(filename2, encoding='utf-8', index=False)
data = pd.read_csv(filename)
iter_large = filter(lambda index: len(data.page[index]) > 400, data.index)
large = []
for i in iter_large:
    large.append(i)

