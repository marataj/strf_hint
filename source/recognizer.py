from source.StrfCodes import StrfCodes
import string
import re
from typing import List

d='2023-10-24  11:27AM'


class Recognizer(StrfCodes):

    IGNORABLE = ["cw", "wk", "day", "week", "time"]

    def __init__(self):
        pass

    def recognize_common_patterns(self, s: str):
        temp = s
        for group in self.DATE_COMMON_FORMATS+self.TIME_COMMON_FORMATS:
            group_regex = self.generate_format_regex(group)
            match = re.search(group_regex, temp.lower())
            if match:
                temp = temp[:match.span()[0]]+group+temp[match.span()[1]:]

        return temp.replace("\\", "")

    def _check_string_group(self, s: str):
        for name, group in [("digits", string.digits), ("letters", string.ascii_lowercase+string.ascii_uppercase), ("punctuation", string.punctuation),
                            ("whitespace", string.whitespace)]:
            if s in group:
                return name

    def _split_format_components(self, s: str):
        index = []
        for idx, elem in enumerate(s[1:], 1):
            if self._check_string_group(elem) != self._check_string_group(s[idx-1]):
                index.append(idx)
        index.insert(0, 0)
        index.append(len(s))

        return [s[index[i-1]: index[i]] for i, _ in enumerate(index[1:], 1)]

    def check_codes(self, splited_str: List[str]):
        codes = []
        used_types = []
        for idx, elem in enumerate(splited_str):
            elem_codes = []
            if not re.search(r"\w", elem) or elem.lower() in self.IGNORABLE:
                codes.append(elem)
                continue
            elem=elem.lower()
            prev = splited_str[idx-1].lower() if idx != 0 else ""
            nxt = splited_str[idx+1].lower() if idx < len(splited_str)-1 else ""
            exp = prev+elem+nxt
            for k, v in self.CODES.items():
                if v["type"] in used_types:
                    continue
                match = re.search(v["regex"], exp)
                if not match:
                    match = re.search(v["regex"], elem)
                if match:
                    elem_codes.append((k, match.span()[1]-match.span()[0], v["type"]))
            if len(set([i[1] for i in elem_codes])) != 1:
                elem_codes = sorted(elem_codes, key=lambda el: el[1], reverse=True)
            codes.append(elem_codes[0][0])
            used_types.append(elem_codes[0][2])
        return codes

    def decode_format(self, datetime_string: str):
        return self.check_codes(self._split_format_components(datetime_string))


#
# d2=[]
# temp=""
# for elem in d:
#     if elem not in string.digits:
#         d2.append(temp)
#         temp = elem
#         continue
#     temp += elem

