# [2408] NMoroney
#

import csv

from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('example 2 : to tsv\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/',  'e-OG20240730_1524-5-subset-101_111.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

parser = ParseGazetteHTML()
name_csv = name[:-4] + ".csv"
with open(name_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["number", "title", "inventors", "assigned"]
    writer.writerow(field)
    for i in range(len(htmls)):
        print(i, end=" ")
        html = zpg.extract_html(archive, htmls[i])
        number, title, inventors, assigned = parser.basic_information(html, htmls[i])
        writer.writerow([number, title, inventors, assigned])
    print()

zpg.close_archive(archive)