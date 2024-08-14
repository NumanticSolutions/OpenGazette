# © 2024 Numantic Solutions LLC
# MIT License
# NMoroney
#

from zipped_patent_gazette import ZippedPatentGazette
from parse_gazette_html import ParseGazetteHTML

print('example 1 : get information\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/', 'e-OG20240730_1524-5-subset-101_111.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

idx = 3
html_name = htmls[idx]
html = zpg.read_html(archive, htmls[idx])

if True:
    print(html + "\n")

parser = ParseGazetteHTML()
identifier, title, inventors, filed_by = parser.basic_information(html, html_name)
print("identifier : " + identifier)
print("title      : " + title)
print("inventors  : " + inventors)
print("filed_by   : " + filed_by)
print("zip path   : " + htmls[idx] + "\n")

identifier, long_id, assigned_to = parser.more_information(html, html_name)
print("identifier  : " + identifier)
print("long id     : " + long_id)
print("assigned_to : " + assigned_to + "\n")

identifier, claim = parser.exemplary_claim(html, html_name)
print("identifier      : " + identifier)
print("exemplary claim :\n" + claim)

zpg.close_archive(archive)
