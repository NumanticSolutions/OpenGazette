# © 2024 Numantic Solutions LLC
# MIT License
# NMoroney
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
    archive.close()
    return pd.read_csv(csv)


def query_column(df_column, query, is_case_sensitive=False):
    return df[df_column.str.contains(query, case=is_case_sensitive)]


path_zip, name_zip = '../data/', 'e-OG20240730_1524-5-subset-101_111-ntif.csv.zip'
df = zipped_csv_to_df(path_zip, name_zip)

query = 'bag'
matches = query_column(df['title'], query)
print("query : " + query + "\n" + str(matches.title))

query = ' CA '
# query='\(US\)'
matches = query_column(df['inventors'], query, True)
print("\nquery : " + query + "\n" + str(matches.inventors))
