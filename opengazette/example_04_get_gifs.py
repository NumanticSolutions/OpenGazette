# © 2024 Numantic Solutions LLC
# MIT License
# NMoroney
#

from zipped_patent_gazette import ZippedPatentGazette

print('example 4 : get gifs\n')

zpg = ZippedPatentGazette()
path_zip, name_zip = '../data/', 'e-OG20240730_1524-5-subset-101_111.zip'
archive = zpg.open_archive(path_zip, name_zip)
htmls, gifs = zpg.quick_list(archive)

rand_gif = zpg.random_gif(archive, gifs)

with open('temp-rand.gif', 'wb') as f:
    f.write(rand_gif)

for gif in gifs:
    gif_name = gif.split('/')[-1]
    image = zpg.read_gif(archive, gif)
    with open(gif_name, 'wb') as f:
        f.write(image)

zpg.close_archive(archive)
