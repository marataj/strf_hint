from source.codes import CODES
import string
import re
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


print(split_format_components(d))
print(d)
#
# d2=[]
# temp=""
# for elem in d:
#     if elem not in string.digits:
#         d2.append(temp)
#         temp = elem
#         continue
#     temp += elem

