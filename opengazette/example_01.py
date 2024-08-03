# [2408] NMoroney
#

import zipped_patent_gazette

zpg = zipped_patent_gazette.ZippedPatentGazette()

print('example 1 : zipped patent gazette')

path, name = '../data/',  'e-OG20240730_1524-5-subset-101_111.zip'

archive = zpg.open_archive(path, name)
htmls, gifs = zpg.quick_list(archive)

for n in range(len(htmls)):
  print(str(n) + " : " + htmls[n] + " - " + gifs[n])

