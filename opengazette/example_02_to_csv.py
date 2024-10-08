# © 2024 Numantic Solutions LLC
# MIT License
# NMoroney
#

import csv
from io import StringIO
import zipfile

from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('example 2 : to tsv\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/', 'e-OG20240730_1524-5-subset-101_110.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

field = ["identifier", "title", "inventors", "filed_by"]

for html in htmls:
    print(html)

print("len htmls :" + str(len(htmls)))

# to uncompressed csv file
#
parser = ParseGazetteHTML()
name_csv = name_zip[:-4] + "-ntif.csv"
with open(name_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(field)
    for i in range(len(htmls)):
        print(i, end=" ")
        html = zpg.read_html(archive, htmls[i])
        identifier, title, inventors, filed_by = parser.basic_information(html, htmls[i])
        writer.writerow([identifier, title, inventors, filed_by])
    print()

# to zipped csv file
#
sio = StringIO()
csv_write = csv.writer(sio)
csv_write.writerow(field)
for i in range(len(htmls)):
    html = zpg.read_html(archive, htmls[i])
    identifier, title, inventors, filed_by = parser.basic_information(html, htmls[i])
    csv_write.writerow([identifier, title, inventors, filed_by])

with zipfile.ZipFile(name_csv + ".zip", "w", zipfile.ZIP_DEFLATED, False) as zip_file:
    zip_file.writestr(name_csv, sio.getvalue().encode())

zpg.close_archive(archive)
