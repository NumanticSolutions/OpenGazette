# [2408] NMoroney
#

from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('example 1 : get information\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/',  'e-OG20240730_1524-5-subset-101_111.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

idx = 0
html_name = htmls[idx]
html = zpg.extract_html(archive, htmls[idx])

parser = ParseGazetteHTML()
number, title, inventors, assigned  = parser.basic_information(html, html_name)
print("number    : " + number)
print("title     : " + title)
print("inventors : " + inventors)
print("assigned  : " + assigned)
print("zip path  : " + htmls[idx] + "\n")

number, full_number, filed = parser.more_information(html, html_name)
print("full number : " + full_number)
print("filed       : " + filed + "\n")

number, claim = parser.exemplary_claim(html, html_name)
print ("exemplary claim :\n" + claim)

zpg.close_archive(archive)