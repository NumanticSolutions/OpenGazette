# [2408] NMoroney
#

#
# * command line version :
#     + input path and zip name
#     + output is zipped csv
#

import csv
from io import StringIO
import zipfile

from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('gazette to zipped csv :\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '/Users/numantic/data/bulk/',  'e-OG20240806_1525-1.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

parser = ParseGazetteHTML()
name_csv = name_zip[:-4] + ".csv"
field = ["number", "title", "inventors", "filed_by"]

sio = StringIO()
csv_write = csv.writer(sio)
csv_write.writerow(field)
for i in range(len(htmls)):
    html = zpg.extract_html(archive, htmls[i])
    number, title, inventors, filed_by = parser.basic_information(html, htmls[i])
    csv_write.writerow([number, title, inventors, filed_by])
    if i % 1000 == 0:
        print(i, end=" ", flush=True)
print(i)

with zipfile.ZipFile(name_csv+".zip", "w", zipfile.ZIP_DEFLATED, False) as zip_file:
    zip_file.writestr(name_csv, sio.getvalue().encode())

zpg.close_archive(archive)