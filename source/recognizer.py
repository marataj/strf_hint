import functools
import re
import string
from typing import List, Tuple

from source.StrfCodes import StrfCodes


class Recognizer(StrfCodes):
    """
    Class responsible for recognizing the strf-codes and decoding the patterns.

    """

    def _recognize_common_patterns(self, s: str) -> Tuple[str, str]:
        """
        Method responsible for recognizing predefined common patterns of strf-codes.

        Parameters
        ----------
        s: `str`
            Input text to be decoded with strf-codes.

        Returns
        -------
        `Tuple`[`str`, `str`]
            Tuple contains two strings: index 0 -> input text with recognized part replaced with the proper strf-codes.
            index 1 -> match_mask, which indicates which elements of returned string were matched. 0 means not matched;
            1 means matched.

        """
        temp_s = s
        match_mask = "0" * len(s)
        for group in self.DATE_COMMON_FORMATS + self.TIME_COMMON_FORMATS:
            group_regex = self._generate_format_regex(group)
            match = re.search(group_regex, temp_s.lower())
            if match:
                temp_s = temp_s[: match.span()[0]] + group + temp_s[match.span()[1] :]
                match_mask = (
                    match_mask[: match.span()[0]]
                    + "1" * len(group)
                    + match_mask[match.span()[1] :]
                )

        return temp_s.replace("\\", ""), match_mask

    def _recognize_single_codes(self, s: str, match_mask: str) -> str:
        """
        Method responsible for recognizing single strf-codes from unmatched parts of input string.

        Parameters
        ----------
        s: `str`
            Input text to be decoded.

        match_mask: `str`
            Mask, that indicates which parts of input text were previously matched, and contain the strf-codes.
            0 means not matched; 1 means matched.

        Returns
        -------
        `str`
            Input text with recognized part replaced with the proper strf-codes.

        """
        for unmatched, span in self._retrieve_unmatched(s, match_mask):
            matched = self._check_codes(self._split_format_components(unmatched))
            s = s[: span[0]] + matched + s[span[1] :]
        return s

    def _split_format_components(self, s: str) -> List[str]:
        """
        Methode responsible for splitting the string in the sign-typed groups (digits, letters, punctuation,
        whitespaces.

        Parameters
        ----------
        s: Input text to be split.

        Returns
        -------
        `List`[`str`]
            List of strings, as a result of splitting into sign-typed groups.

        """
        index = []
        for idx, elem in enumerate(s[1:], 1):
            if self._check_string_group(elem) != self._check_string_group(s[idx - 1]):
                index.append(idx)
        index.insert(0, 0)
        index.append(len(s))

        return [s[index[i - 1] : index[i]] for i, _ in enumerate(index[1:], 1)]

    def _check_codes(self, split_str: List[str]) -> str:
        """
        Method recognizes the single strf-codes in elements of the list containing split input text. Then replaces
        recognized parts with specific codes.

        Parameters
        ----------
        split_str: `List`[`str`]
            List containing input text split into sign-groups.

        Returns
        -------
        `str`
            String prepared from split_str with recognized parts replaced with specific codes.

        """
        codes = []
        used_types = []
        for idx, elem in enumerate(split_str):
            elem_codes = []
            if re.search(r"\W", elem) or elem.lower() in self.IGNORABLE:
                codes.append(elem)
                continue
            prev = split_str[idx - 1].lower() if idx != 0 else ""
            nxt = split_str[idx + 1].lower() if idx < len(split_str) - 1 else ""
            exp = prev + elem.lower() + nxt
            for code in self.BASIC_CODES.keys():
                if self._get_type(code) in used_types:
                    continue
                match = re.search(self._get_regex(code, "True"), exp)
                if not match:
                    match = re.search(self._get_regex(code, "True"), elem.lower())
                if match:
                    elem_codes.append(
                        (code, match.span()[1] - match.span()[0], self._get_type(code))
                    )
            if len(set([i[1] for i in elem_codes])) != 1:
                elem_codes = sorted(elem_codes, key=lambda el: el[1], reverse=True)
            if not any(elem_codes):
                codes.append(elem)
                continue
            codes.append(elem_codes[0][0])
            used_types.append(elem_codes[0][2])

        return "".join(codes)

    def decode_format(self, decoded_string: str):
        decoded_string, match_mask = self._recognize_common_patterns(decoded_string)
        decoded_string = self._recognize_single_codes(decoded_string, match_mask)
        return decoded_string

    @staticmethod
    def _retrieve_unmatched(s: str, match_mask: str) -> List[Tuple[str, Tuple[int, int]]]:
        """
        Method responsible for retrieving unmatched parts of the input string, and returns them as a list of tuples,
        containing unmatched part of string and its span (as a tuple of integers).

        Parameters
        ----------
        s: `str`
            Input string.

        match_mask: `str`
            Mask that indicates matched and unmatched elements of the input string. 0: means unmatched, 1 matched.

        Returns
        -------
        `List`[`Tuple`[`str`, `Tuple`[`int`, `int`]]]

            List containing tuple for each unmatched part of the string. Tuples contain string, and its span in the
            input string.

        """
        return [
            (s[r.span()[0] : r.span()[1]], r.span())
            for r in re.finditer("0+", match_mask)
        ]

    @staticmethod
    @functools.lru_cache
    def _check_string_group(s: str) -> str:
        """
        Method returns name of the group of signs, that tested element bellows to. The input sign is tested against
        its membership to 4 basic groups of signs: digits, letters, punctuation signs and whitespaces.

        Parameters
        ----------
        s: str
            Single sign to be tested.

        Returns
        -------
        `str`
            Name of the specific group, that the tested element belongs to.
        """
        if len(s) != 1:
            raise ValueError("S must be a single sign.")

        for name, group in [
            ("digits", string.digits),
            ("letters", string.ascii_lowercase + string.ascii_uppercase),
            ("punctuation", string.punctuation),
            ("whitespace", string.whitespace),
        ]:
            if s in group:
                return name
