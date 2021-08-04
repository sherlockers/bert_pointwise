import csv
import tensorflow as tf

filename = "/home/yangguodong/digix/bert/digix_data/train_tr_orign.csv"
filename1 = "/home/yangguodong/digix/bert/digix_data/train_tr.csv"
filename2 = "/home/yangguodong/digix/bert/digix_data/dev_tr.csv"
i = 0
with tf.gfile.Open(filename, "r") as fin:
    reader = csv.DictReader(fin, delimiter=",")
    with tf.gfile.Open(filename1, "w") as fout1:
        writer1 = csv.DictWriter(fout1, delimiter=",", fieldnames=reader.fieldnames)
        writer1.writeheader()
        with tf.gfile.Open(filename2, "w") as fout2:
            writer2 = csv.DictWriter(fout2, delimiter=",", fieldnames=reader.fieldnames)
            writer2.writeheader()
            for row in reader:
                i += 1
                if i <= 140000:
                    writer1.writerow(row)
                else:
                    writer2.writerow(row)