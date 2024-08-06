# [2406] n8m
#

from zipfile import ZipFile

from random import randrange


class ZippedPatentGazette :
  """Process zipped patent gazettes"""

  def open_archive(self, path, zip_name) :
    archive = ZipFile(path + zip_name)
    return archive

  def quick_list(self, archive) :
    names = archive.namelist()
    htmls, gifs = ( [], [] )
    for name in names :
      if self.og_html in name :
        if name.endswith(self.dot_html) :
          htmls.append(name)
        if name.endswith(self.dot_gif) :
          gifs.append(name)
    return htmls, gifs

  def generate_uuids(self, archive, htmls) :
    uuids, not_issued = ( [], [] )
    for html in htmls :
      ts = html.split('/')
      uuid = ts[-1].replace(self.dot_html, "")
      uuids.append(uuid)

      item = archive.read(html)
      s = item.decode()

      if 'Not Issued' in s :
        not_issued.append(uuid)

    return uuids, not_issued

  def random_html(self, archive, htmls) :
    rn = randrange(len(htmls))
    item = archive.read(htmls[rn])
    return item.decode()

  def extract_html(self, archive, html) -> str:
    item = archive.read(html)
    s = item.decode()
    return s

  def quick_data(self, archive, htmls) :
    n = 0 

    def splitter(s) :
      s2 = s.split('<b>')
      s3 = s2[1].split('</b>')
      return s3[0].strip()

    numbers, titles, inventors, assignees = ( [], [], [], [] )
    for html in htmls :
      item = archive.read(html)
      s = item.decode()

      if 'Not Issued' in s :
        numbers.append("na")
        titles.append("na")
        inventors.append("na")
        assignees.append("na")
      else :
        m = 0
        lines = s.split('\n')
        for line in lines :
          if '"table_data"' in line :
            if m == 0 :
              numbers.append(splitter(line))
            if m == 1 :
              titles.append(splitter(line))
            if m == 2 :
              inventors.append(splitter(line))
            if m == 3 :
              assignees.append(splitter(line))
            m += 1
      n += 1

    return numbers, titles, inventors, assignees

  def match_gifs_with_htmls(self, htmls, gifs) :
    fs = htmls.copy()
    fs.extend(gifs)
    fs.sort()

    def to_id(s) :
      ts = s.split('/')
      us = ts[-1].split('-')
      s2 = us[0] + '-' + us[1]
      return s2.replace(self.dot_html, "")

    matched = [] 
    for i in range(len(fs)) :
      j = i - 1
      if fs[i].endswith(self.dot_html) :
        if j > 0 :
          ki, kj = ( to_id(fs[i]), to_id(fs[j]) )
          ids_match = (ki == kj)
          if fs[j].endswith(self.dot_gif) and ids_match:
            matched.append(fs[j])
          else :
            matched.append('na')
        else :
          matched.append('na')
    return matched

  def extract_claims(self, archive, htmls) :
    claims = []
    for html in htmls :
      item = archive.read(html)
      s = item.decode()

      if 'Not Issued' in s :
        claims.append("na")
      else :
        lines = s.split('\n')
        claim = ''
        for line in lines :
          if "claim_text" in line :
            s2 = line.replace('<div class="claim_text">', '')
            s3 = s2.replace('<div class="claim_text_root">', '')
            s4 = s3.replace('</div>', '').strip().replace('\n', '')
            claim += s4
        if len(claim) > 0 :
          claims.append(claim)
        else :
          claims.append("na")

    return claims

  def close_archive(self, archive) :
    archive.close()

  og_html = '/OG/html/'
  dot_html, dot_gif = ( '.html', '.gif' )
