# © 2024 Numantic Solutions LLC
# MIT License
# NMoroney
#

from zipped_patent_gazette import ZippedPatentGazette

print('example 2 : to tsv\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/', 'e-OG20240813_1525-2-521-530-not_issued_527.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

not_issued = zpg.not_issued_indices(archive, htmls)

length = len(not_issued)
print("len not issued: " + str(length))
if length > 0:
    print("not issued[0] : " + str(not_issued[0]))
    print("html          : " + htmls[not_issued[0]])
    print(zpg.read_html(archive, htmls[not_issued[0]]))




