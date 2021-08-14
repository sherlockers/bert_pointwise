import csv
import tensorflow as tf
import pandas as pd

filename = "/home/yangguodong/digix/bert/digix_data/train_tr_wash.csv"
filename1 = "/home/yangguodong/digix/bert/digix_data/train_tr.csv"
filename2 = "/home/yangguodong/digix/bert/digix_data/dev_tr.csv"

data = pd.read_csv(filename)
data.loc[0:int(len(data) * 0.8)].to_csv(filename1, encoding='utf-8', index=False)
data.loc[int(len(data) * 0.8):len(data)].to_csv(filename2, encoding='utf-8', index=False)
