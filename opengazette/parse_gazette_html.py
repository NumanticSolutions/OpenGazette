# [2408] NMoroney
#

import bs4 as bs
import textwrap as tw


class ParseGazetteHTML:
    """parse patent gazette html"""

    na = '_na_'
    empty = '_empty_'

    def to_identifier(self, html_name) -> str:
        ts = html_name.split('/')
        t1 = ts[-1].replace(".html", "")
        if t1.startswith("US") and "-" in t1:
            return t1.split('-')[0]
        else:
            return t1

    def find_title(self, tables) -> str:
        title = self.na
        if len(tables) > 0:
            rows = tables[0].find_all('tr')
            cols = rows[1].find_all('td')
            if len(cols[0].text) > 0:
                title = cols[0].text
            else:
                title = self.empty
        return title

    def find_inventors(self, tables) -> str:
        inventors = self.na
        if len(tables) > 0:
            rows = tables[0].find_all('tr')
            cols = rows[2].find_all('td')
            if len(cols[0].text) > 0:
                inventors = cols[0].text
                if inventors.startswith("Latin Name"):
                    inventors = self.empty
            else:
                inventors = self.empty
        return inventors

    def find_assigned(self, tds) -> str:
        assigned = self.na
        for td in tds:
            str_td = str(td)
            str_no_tags = str(td.string)
            if "Assigned to " in str_td:
                a1 = str_no_tags.replace("Assigned to ", "")
                assigned = a1
        return assigned

    def find_filed_by(self, tds) -> str:
        filed_by = self.na
        for td in tds:
            str_td = str(td)
            str_no_tags = str(td.string)
            if "Filed by " in str_td:
                a1 = str_no_tags.replace("Filed by ", "")
                filed_by = a1
        return filed_by

    def basic_information(self, html, html_name):
        """ returns : identifier, title, inventors & filed_by"""

        identifier = self.to_identifier(html_name)

        soup = bs.BeautifulSoup(html, features="lxml")

        tables = soup.find_all(name="table")
        title = self.find_title(tables)
        inventors = self.find_inventors(tables)

        tds = soup.find_all(name="td", class_="table_data")
        filed_by = self.find_filed_by(tds)

        return identifier, title, inventors, filed_by

    def exemplary_claim(self, html, html_name, is_wrapped=True):
        """returns : identifier and exemplary claim, option to wrap or not"""

        soup = bs.BeautifulSoup(html, features="lxml")
        claim_root = soup.find_all(name="div", class_=["claim_text_root"], recursive=True)
        identifier = self.to_identifier(html_name)
        claim = self.na
        if len(claim_root) == 1:
            claim, claim_str = '', ''
            for child in claim_root[0].recursiveChildGenerator():
                name = getattr(child, "name", None)
                if (name is None) and (not child.isspace()):
                    claim_str += child.text + " "
            single_line = claim_str.replace("\n", " ")
            if is_wrapped:
                wrapped = tw.wrap(single_line, 80)
                for line in wrapped:
                    claim += line + "\n"
            else:
                claim = single_line
        return identifier, claim

    def more_information(self, html, html_name):
        """ returns : identifier, long_id & assigned_to"""

        soup = bs.BeautifulSoup(html, features="lxml")
        tds = soup.find_all(name="td", class_="table_data")
        identifier = self.to_identifier(html_name)
        long_id, assigned_to = self.na, self.na
        for td in tds:
            str_td = str(td)
            str_no_tags = str(td.string)
            if "<td class=\"table_data\"><b>" in str_td:
                long_id = str_no_tags
            if "Assigned to " in str_td:
                assigned_to = str_no_tags.replace("Assigned to ", "")

        return identifier, long_id, assigned_to
