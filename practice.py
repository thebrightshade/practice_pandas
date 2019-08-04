
import pdb
from os.path import isfile, join
from os import listdir
import pandas as pd


list_of_files = [
    file for file in listdir('./data') if isfile(join('./data', file))]

for item in list_of_files:
    item_name = item.split('.')[0].lower()
    exec(
        "{} = {} ".format(
            item_name, "pd.read_csv('data/{}'.format(item), index_col=0, header=None, names=['Value','Age'])"))
    exec("{}_dict = {}.T.to_dict()".format(item_name, item_name))


def get_adults(df):
    adults = 0
    minors = 0
    for item in df.index:
        if df.loc[item]['Age'] >= 18:
            adults = adults + 1
        elif df.loc[item]['Age'] < 18:
            minors = minors + 1
    return adults, minors

pdb.set_trace()
