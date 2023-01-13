import pandas as pd
import csv

file = "assets/test.csv"


def main():

    data = {
        "calories": ["a", "b", "c", "d", "e", "f"],
        "duration": ["g", "h", "i", "j", "k", "l"]
    }

    # load data into a DataFrame object:
    df = pd.DataFrame(data)
    # df.to_csv(file, index_label="index")

    # columns = df.columns.values()
    # print(columns)

    it = df.iterrows()
    for i in range(len(df.index)):
        _, row = next(it)
        row_d = row.to_dict()
        print(row_d)


#     with open(file, newline='') as csvfile:
#         spamreader = csv.reader(csvfile)
#         print(len(spamreader))
#         next(spamreader)
#         for row in spamreader:
#             print(row)

# with open('eggs.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
