from source.codes import CODES
import string
import re
from typing import List
#def check_format(data):

d='2023-10-24  11:27AM'


def check_string_group(s: str):
    for name, group in [("digits", string.digits), ("letters", string.ascii_lowercase), ("punctuation", string.punctuation),
                        ("whitespace", string.whitespace)]:
        if s in group:
            return name


def split_format_components(s: str):
    s = s.lower()
    index = []
    for idx, elem in enumerate(s[1:], 1):
        if check_string_group(elem) != check_string_group(s[idx-1]):
            index.append(idx)
    index.insert(0, 0)
    index.append(len(s))

    return [s[index[i-1]: index[i]] for i, _ in enumerate(index[1:], 1)]


def check_codes(splited_str: List[str]):
    codes = []
    for idx, elem in enumerate(splited_str):
        elem_codes = []
        if not re.search(r"\w", elem):
            codes.append(elem)
            continue
        prev = splited_str[idx-1] if idx != 0 else ""
        nxt = splited_str[idx+1] if idx < len(splited_str)-1 else ""
        exp = prev+elem+nxt
        for k, v in CODES.items():
            match = re.search(v["regex"], exp)
            if match:
                elem_codes.append((k, match))
        codes.append(elem_codes)
    return codes

a=split_format_components(d)
print(len(a))
print(a)
print(check_codes(a))
#
# d2=[]
# temp=""
# for elem in d:
#     if elem not in string.digits:
#         d2.append(temp)
#         temp = elem
#         continue
#     temp += elem

