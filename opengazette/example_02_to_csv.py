# [2408] NMoroney
#

import csv
from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('example 1 : get information\n')

zpg = ZippedPatentGazette()
path, name = '../data/',  'e-OG20240730_1524-5-subset-101_111.zip'
archive = zpg.open_archive(path, name)
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
        number, title, inventors, assigned = parser.basic_information(html)
        writer.writerow([number, title, inventors, assigned])
    print()
