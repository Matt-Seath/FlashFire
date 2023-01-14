import pandas as pd
from tqdm import tqdm
from core.models import User


file = "assets/test.csv"


def main():

    data = {
        "name": ["abyy", "barb", "chris"],
        "email": ["gsdf@gmail.com", "hdfsd@gmail.com", "id@gmail.com"],
        "cash": [20.0, 23.3, 4.0]
    }

    # load data into a DataFrame object:
    df = pd.DataFrame(data)
    # df.to_csv(file, index_label="index")

    # columns = df.columns.values()
    # print(columns)

    it = df.iterrows()
    for i in tqdm(range(len(df.index)), desc="cool"):
        _, row = next(it)
        row_d = row.to_dict()
        print(row_d)

        entry = User(**row_d)
        entry.save()
        print("yup")


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
