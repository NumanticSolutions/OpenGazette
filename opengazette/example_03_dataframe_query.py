# [2408] NMoroney
#

import pandas as pd
from io import StringIO

from zipfile import ZipFile

def zipped_csv_to_df(path_zip, name_zip):
    archive = ZipFile(path_zip + name_zip)
    name_csv = name_zip[:-4]
    item = archive.read(name_csv)
    s = item.decode()
    csv = StringIO(s)
    return pd.read_csv(csv)

def query_title(df, query):
    return df[df['title'].str.contains(query, case=False)]

path_zip, name_zip = '../data/',  'e-OG20240730_1524-5-subset-101_111-ntif.csv.zip'
df = zipped_csv_to_df(path_zip, name_zip)

query='bag'
matches = query_title(df, query)
print("query : " + query + "\n" + str(matches.title))
