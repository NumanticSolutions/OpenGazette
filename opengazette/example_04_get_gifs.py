# © 2024 Numantic Solutions LLC
# MIT License
# NMoroney
#

from zipped_patent_gazette import ZippedPatentGazette

print('example 4 : get gifs\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/', 'e-OG20240730_1524-5-subset-101_110.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

rand_gif = zpg.random_gif(archive, gifs)

with open('temp-rand.gif', 'wb') as f:
    f.write(rand_gif)

names = []
for gif in gifs:
    gif_name = gif.split('/')[-1]
    names.append(gif_name)
    image = zpg.read_gif(archive, gif)
    with open(gif_name, 'wb') as f:
        f.write(image)

wide = 5
with open('temp_gifs.html', 'w') as f:
    f.write('<html><table>')
    i = 0
    length = len(names)
    while i < length:
        j = 0
        f.write('<tr>')
        while j < wide and i < length:
            f.write('<td><img src=\"' + names[i] + '\" width=\"100px\"></td>')
            j += 1
            i += 1
        f.write('</tr>')
    f.write('</table></html>')


zpg.close_archive(archive)
