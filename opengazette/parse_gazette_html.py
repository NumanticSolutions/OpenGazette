# [2408] NMoroney
#

import bs4 as bs
import textwrap as tw

class ParseGazetteHTML:
    """parse patent gazette html"""

    def basic_information(self, html):
        """ returns : number, title, inventors & assigned"""

        soup = bs.BeautifulSoup(html, features="lxml")
        tds = soup.find_all(name="td", class_="table_data")
        number, title, assigned, inventors = 'na', 'na', 'na', 'na'
        for td in tds:
            str_td = str(td)
            str_no_tags = str(td.string)
            if "<td class=\"table_data\"><b>" in str_td:
                n1 = str_no_tags
                n2 = n1.replace(",", "")
                number = n2.replace(" ", "")
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

    def exemplary_claim(self, html, is_wrapped=True):
        """returns : 80 char wrapped exemplary claim text"""

        soup = bs.BeautifulSoup(html, features="lxml")
        claim_root = soup.find_all(name="div", class_=["claim_text_root"])
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
        return claim