# [2406] n8m
#

from zipfile import ZipFile
from random import randrange


class ZippedPatentGazette:
    """Process zipped patent gazettes"""

    og_html = '/OG/html/'
    dot_html, dot_gif = ('.html', '.gif')

    def open_archive(self, path, zip_name):
        archive = ZipFile(path + zip_name)
        return archive

    def quick_list(self, archive):
        names = archive.namelist()
        htmls, gifs = ([], [])
        for name in names:
            if self.og_html in name:
                if name.endswith(self.dot_html):
                    htmls.append(name)
                if name.endswith(self.dot_gif):
                    gifs.append(name)
        return htmls, gifs

    def generate_uuids(self, archive, htmls):
        uuids, not_issued = ([], [])
        for html in htmls:
            ts = html.split('/')
            uuid = ts[-1].replace(self.dot_html, "")
            uuids.append(uuid)

            item = archive.read(html)
            s = item.decode()

            if 'Not Issued' in s:
                not_issued.append(uuid)

        return uuids, not_issued

    def random_html(self, archive, htmls):
        rn = randrange(len(htmls))
        item = archive.read(htmls[rn])
        return item.decode()

    def extract_html(self, archive, html) -> str:
        item = archive.read(html)
        s = item.decode()
        return s

    def match_gifs_with_htmls(self, htmls, gifs):
        fs = htmls.copy()
        fs.extend(gifs)
        fs.sort()

        def to_id(s):
            ts = s.split('/')
            us = ts[-1].split('-')
            s2 = us[0] + '-' + us[1]
            return s2.replace(self.dot_html, "")

        matched = []
        for i in range(len(fs)):
            j = i - 1
            if fs[i].endswith(self.dot_html):
                if j > 0:
                    ki, kj = (to_id(fs[i]), to_id(fs[j]))
                    ids_match = (ki == kj)
                    if fs[j].endswith(self.dot_gif) and ids_match:
                        matched.append(fs[j])
                    else:
                        matched.append('na')
                else:
                    matched.append('na')
        return matched

    def close_archive(self, archive):
        archive.close()
