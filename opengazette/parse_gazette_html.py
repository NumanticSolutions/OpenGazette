# [2408] NMoroney
#

import bs4 as bs
import textwrap as tw

class ParseGazetteHTML:
    """parse patent gazette html"""

    def to_number(self, html_name) -> str:
        ts = html_name.split('/')
        t1 = ts[-1].replace(".html", "")
        if t1.startswith("US") and "-" in t1:
            return t1.split('-')[0]
        else:
            return t1

    def basic_information(self, html, html_name):
        """ returns : number, title, inventors & assigned"""

        soup = bs.BeautifulSoup(html, features="lxml")
        tds = soup.find_all(name="td", class_="table_data")
        number = self.to_number(html_name)
        title, assigned, inventors = 'na', 'na', 'na'
        for td in tds:
            str_td = str(td)
            str_no_tags = str(td.string)
            if "text-transform: uppercase" in str_td:
                title = str_no_tags
            if "Assigned to " in str_td:
                a1 = str_no_tags.replace("Assigned to ", "")
                assigned = a1
            if ("colspan=\"3\"" in str_td and
                    "Assigned to " not in str_td and
                    "Appl. No. " not in str_td and
                    "Filed by " not in str_td and
                    "PCT Filed " not in str_td and
                    "Claims priority" not in str_td and
                    "Prior Publication " not in str_td and
                    "align=" not in str_td and
                    "Int. Cl. " not in str_td and
                    "subject to a terminal disclaimer" not in str_td):
                inventors = str_no_tags
        return number, title, inventors, assigned

    def exemplary_claim(self, html, html_name, is_wrapped=True):
        """returns : number and exemplary claim, option to wrap or not"""

        soup = bs.BeautifulSoup(html, features="lxml")
        claim_root = soup.find_all(name="div", class_=["claim_text_root"])
        number = self.to_number(html_name)
        claim = 'na'
        if len(claim_root) == 1:
            claim, claim_str = '', ''
            for child in claim_root[0].children:
                if child.string != None:
                    claim_str += child.string
            single_line = claim_str.replace("\n", " ")
            if is_wrapped:
                wrapped = tw.wrap(single_line, 80)
                for line in wrapped:
                    claim += line + "\n"
            else:
                claim = single_line
        return number, claim

    def more_information(self, html, html_name):
        """ returns : number, full_number & filed"""

        soup = bs.BeautifulSoup(html, features="lxml")
        tds = soup.find_all(name="td", class_="table_data")
        number = self.to_number(html_name)
        full_number, filed = 'na', 'na'
        for td in tds:
            str_td = str(td)
            str_no_tags = str(td.string)
            if "<td class=\"table_data\"><b>" in str_td:
                full_number = str_no_tags
            if "Filed by " in str_td:
                filed = str_no_tags.replace("Filed by ", "")

        return number, full_number, filed