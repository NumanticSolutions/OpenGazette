# [2408] NMoroney
#

import os
import bs4 as bs

import zipped_patent_gazette

zpg = zipped_patent_gazette.ZippedPatentGazette()

print('example 1 : zipped patent gazette')

path, name = '../data/',  'e-OG20240730_1524-5-subset-101_111.zip'

archive = zpg.open_archive(path, name)
htmls, gifs = zpg.quick_list(archive)

if False:
  for n in range(len(htmls)):
    print(str(n) + " : " + htmls[n] + " - " + gifs[n])

html = zpg.extract_html(archive, htmls[0])

if False:
  print(html)

soup = bs.BeautifulSoup(html, features="lxml")

# print(html)

results = soup.find_all("td", class_="table_data")
for result in results :
  print(result)

print()

results = soup.find_all(name="div", class_=["claim_text_root", "claim_text"])
for result in results :
  print(result)


