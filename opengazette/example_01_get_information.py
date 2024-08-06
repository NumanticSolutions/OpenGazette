# [2408] NMoroney
#

from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('example 1 : zipped patent gazette\n')

zpg = ZippedPatentGazette()
path, name = '../data/',  'e-OG20240730_1524-5-subset-101_111.zip'
archive = zpg.open_archive(path, name)
htmls, gifs = zpg.quick_list(archive)

idx = 0
html = zpg.extract_html(archive, htmls[idx])

parser = ParseGazetteHTML()
number, title, assigned, inventors = parser.basic_information(html)
print("number    : " + number)
print("title     : " + title)
print("assigned  : " + assigned)
print("inventors : " + inventors)
print("zip path  : " + htmls[idx] + "\n")

claim = parser.exemplary_claim(html)
print ("exemplary claim :\n" + claim)
