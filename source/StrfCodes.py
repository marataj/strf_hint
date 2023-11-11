"""
This module contains datetime codes.

"""
from typing import Literal, Optional
import re
import functools


class StrfCodes:
    """
    This class is a container for strf datetime codes related data.

    """
    BASIC_CODES = {
        "%a": {
            "description": "Weekday as locale’s abbreviated name.",
            "example": "Sun",
            "type": "day",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": r"|".join(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
        },
        "%A": {
            "description": "Weekday as locale’s full name.",
            "example": "Sunday",
            "type": "day",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": r"|".join(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
        },
        "%b": {
            "description": "Month as locale’s abbreviated name.",
            "example": "Sep",
            "type": "month",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": "|".join(
                ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        },
        "%B": {
            "description": "Month as locale’s full name.",
            "example": "September",
            "type": "month",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": "|".join(
                ['january', 'february', 'march', 'april', 'may', 'jun', 'july', 'august', 'september', 'october',
                 'november', 'december'])
        },
        "%m": {
            "description": "Month as a zero-padded decimal number.",
            "example": "09",
            "type": "month number",
            "prefix": r"[-/.]?\b",
            "suffix": r"\b[-/.]?",
            "regex": r"0[1-9]|1[0-2]"
        },
        "%-m": {
            "description": "Month as a decimal number. (Platform specific)",
            "example": "9",
            "type": "month number",
            "prefix": r"[-/.]?\b",
            "suffix": r"\b[-/.]?",
            "regex": "[0-9]|1[0-2]"
        },
        # TODO: Add expressions for common constructions, like 2023-11-03, 2023/11/03, 11:40, 22:40, 1:20 PM

        "%Y": {
            "description": "Year with century as a decimal number.",
            "example": "2013",
            "type": "year",
            "prefix": r"[-/.]?\b",
            "suffix": r"\b[-/.]?",
            "regex": r"\d{3,4}"
        },
        "%d": {
            "description": "Day of the month as a zero-padded decimal number.",
            "example": "08",
            "type": "day number",
            "prefix": r"[-/.]?\b",
            "suffix": r"\b[-/.]?",
            "regex": "0[1-9]|[1-2][0-9]|3[0-1]"
        },
        "%-d": {
            "description": "Day of the month as a decimal number. (Platform specific)",
            "example": "8",
            "type": "day number",
            "prefix": r"[-/.]?\b",
            "suffix": r"\b[-/.]?",
            "regex": "[1-9]|[1-2][0-9]|[0-1]"
        },
        "%H": {
            "description": "Hour (24-hour clock) as a zero-padded decimal number.",
            "example": "07",
            "type": "hour",
            "prefix": r":?\b",
            "suffix": r"\b:?",
            "regex": "0[0-9]|1[0-9]|2[0-4]"
        },
        "%-H": {
            "description": "Hour (24-hour clock) as a decimal number. (Platform specific)",
            "example": "7",
            "type": "hour",
            "prefix": r":?\b",
            "suffix": r"\b:?",
            "regex": r"[0-9]|1[0-9]|2[0-4]"
        },
        "%I": {
            "description": "Hour (12-hour clock) as a zero-padded decimal number.",
            "example": "07",
            "type": "hour",
            "prefix": r":?\b",
            "suffix": r"(am|pm)?\b:?",
            "regex": r"0[0-9]|1[0-2]"
        },
        "%-I": {
            "description": "Hour (12-hour clock) as a decimal number. (Platform specific)",
            "example": "7",
            "type": "hour",
            "prefix": r":?\b",
            "suffix": r"(am|pm)?\b:?",
            "regex": r"[0-9]|1[0-2]"
        },
        "%p": {
            "description": "Locale’s equivalent of either AM or PM.",
            "example": "AM",
            "type": "am/pm",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": r"am|pm"
        },
        "%M": {
            "description": "Minute as a zero-padded decimal number.",
            "example": "06",
            "type": "minute",
            "prefix": r":?\b",
            "suffix": r"(am|pm)?\b:?",
            "regex": r"0[0-9]|[1-5][0-9]"
        },
        "%-M": {
            "description": "Minute as a decimal number. (Platform specific)",
            "example": "6",
            "type": "minute",
            "prefix": r":?\b",
            "suffix": r"(am|pm)?\b:?",
            "regex": r"[0-9]|[1-5][0-9]"
        },
        "%S": {
            "description": "Second as a zero-padded decimal number.",
            "example": "05",
            "type": "second",
            "prefix": r":?\b",
            "suffix": r"(am|pm)?\b:?",
            "regex": r"0[0-9]|[1-5][0-9]"
        },
        "%-S": {
            "description": "Second as a decimal number. (Platform specific)",
            "example": "5",
            "type": "second",
            "prefix": r":?\b",
            "suffix": r"(am|pm)?\b:?",
            "regex": r"[0-9]|[1-5][0-9]"
        },
        "%f": {
            "description": "Microsecond as a decimal number, zero-padded to 6 digits.",
            "example": 0,
            "type": "microsecond",
            "prefix": r":?\b",
            "suffix": r"\b:?",
            "regex": r"\d{6}"
        },
        "%Z": {
            "description": "Time zone name (empty string if the object is naive).",
            "example": "UTC",
            "type": "timezone",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": "|".join(
                ['acdt', 'acst', 'act', 'act', 'acwst', 'adt', 'aedt', 'aest', 'aet (aest/aedt)', 'aft', 'akdt', 'akst',
                 'almt', 'amst', 'amt', 'amt', 'anat', 'aqtt', 'art', 'ast', 'ast', 'awst', 'azost', 'azot', 'azt',
                 'bnt', 'biot', 'bit', 'bot', 'brst', 'brt', 'bst', 'bst', 'bst', 'btt', 'cat', 'cct', 'cdt', 'cdt',
                 'cest', 'cet', 'chadt', 'chast', 'chot', 'chost', 'chst', 'chut', 'cist', 'ckt', 'clst', 'clt', 'cost',
                 'cot', 'cst', 'cst', 'cst', 'ct (cst/cdt)', 'cvt', 'cwst', 'cxt', 'davt', 'ddut', 'dft', 'easst',
                 'east', 'eat', 'ect', 'ect', 'edt', 'eest', 'eet', 'egst', 'egt', 'est', 'et (est/edt)', 'fet', 'fjt',
                 'fkst', 'fkt', 'fnt', 'galt', 'gamt', 'get', 'gft', 'gilt', 'git', 'gmt', 'gst', 'gst', 'gyt', 'hdt',
                 'haec', 'hst', 'hkt', 'hmt', 'hovst', 'hovt', 'ict', 'idlw', 'idt', 'iot', 'irdt', 'irkt', 'irst',
                 'ist', 'ist', 'ist', 'jst', 'kalt', 'kgt', 'kost', 'krat', 'kst', 'lhst', 'lhst', 'lint', 'magt',
                 'mart', 'mawt', 'mdt', 'met', 'mest', 'mht', 'mist', 'mit', 'mmt', 'msk', 'mst', 'mst', 'mut', 'mvt',
                 'myt', 'nct', 'ndt', 'nft', 'novt', 'npt', 'nst', 'nt', 'nut', 'nzdt', 'nzst', 'omst', 'orat', 'pdt',
                 'pet', 'pett', 'pgt', 'phot', 'pht', 'phst', 'pkt', 'pmdt', 'pmst', 'pont', 'pst', 'pwt', 'pyst',
                 'pyt', 'ret', 'rott', 'sakt', 'samt', 'sast', 'sbt', 'sct', 'sdt', 'sgt', 'slst', 'sret', 'srt', 'sst',
                 'sst', 'syot', 'taht', 'tha', 'tft', 'tjt', 'tkt', 'tlt', 'tmt', 'trt', 'tot', 'tst', 'tvt', 'ulast',
                 'ulat', 'utc', 'uyst', 'uyt', 'uzt', 'vet', 'vlat', 'volt', 'vost', 'vut', 'wakt', 'wast', 'wat',
                 'west', 'wet', 'wib', 'wit', 'wita', 'wgst', 'wgt', 'wst', 'yakt', 'yekt'])
        },
        "%j": {
            "description": "Day of the year as a zero-padded decimal number.",
            "example": "251",
            "type": "yearday",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": r"00\d|0\d\d|[1-2]\d\d|3[0-6][0-6]"
        },
        "%-j": {
            "description": "Day of the year as a decimal number. (Platform specific)",
            "example": "251",
            "type": "yearday",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": r"\d|\d\d|[1-2]\d{2}|3[0-6]{2}"
        },
        "%U": {
            "description": "Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.",
            "example": "36",
            "type": "week number",
            "prefix": r"\b(cw|wk)?",
            "suffix": r"(cw|wk)?\b",
            "regex": r"0\d|[1-4]\d|5[0-4]"
        },
        "%-U": {
            "description": "Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)",
            "example": "36",
            "type": "week number",
            "prefix": r"\b(cw|wk)?",
            "suffix": r"(cw|wk)?\b",
            "regex": r"\d|[1-4]\d|5[0-4]"
        },
        "%W": {
            "description": "Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.",
            "example": "35",
            "type": "week number",
            "prefix": r"\b(cw|wk)?",
            "suffix": r"(cw|wk)?\b",
            "regex": r"0\d|[1-4]|5[0-4]"
        },
        "%-W": {
            "description": "Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)",
            "example": "35",
            "type": "week number",
            "prefix": r"\b(cw|wk)?",
            "suffix": r"(cw|wk)?\b",
            "regex": r"\d|[1-4]\d|5[0-4]"
        },
        "%w": {
            "description": "Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.",
            "example": '0',
            "type": "weekday number",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": r"[0-6]"
        },
        "%y": {
            "description": "Year without century as a zero-padded decimal number.",
            "example": "13",
            "type": "year",
            "prefix": r"[-/.]?\b",
            "suffix": r"\b[-/.]?",
            "regex": r"0\d|\d\d"
        },
        # "%c": {
        #     "description": "Locale’s appropriate date and time representation.",
        #     "example": "Sun Sep 8 07:06:05 2013",
        #     "prefix": [],
        #     "suffix": [],
        #     "regex": r""
        # },
        # "%x": {
        #     "description": "Locale’s appropriate date representation.",
        #     "example": '09/08/13',
        #     "prefix": [],
        #     "suffix": [],
        #     "regex": r""
        # },
        # "%X": {
        #     "description": "Locale’s appropriate time representation.",
        #     "example": '07:06:05',
        #     "prefix": [],
        #     "suffix": [],
        #     "regex": r""
        # },
        "%%": {
            "description": "A literal '%' character.",
            "example": "%",
            "type": "literal",
            "prefix": r"\b",
            "suffix": r"\b",
            "regex": "%"
        },
    }
    DATE_COMMON_FORMATS = [
        "%Y-%m-%d", "%Y\.%m\.%d", "%Y/%m/%d", "%Y,%m,%d",
        "%d-%m-%Y", "%d\.%m\.%Y", "%d/%m/%Y", "%d,%m,%Y",
        "%m-%d-%Y", "%m\.%d\.%Y", "%m/%d/%Y", "%m,%d,%Y",

        "%Y-%m-%-d", "%Y\.%m\.%-d", "%Y/%m/%-d",  "%Y,%m,%-d",
        "%-d-%m-%Y", "%-d\.%m\.%Y", "%-d/%m/%Y",  "%-d,%m,%Y",
        "%m-%-d-%Y", "%m\.%-d\.%Y", "%m/%-d/%Y",  "%m,%-d,%Y",

        "%y-%m-%d", "%y\.%m\.%d", "%y/%m/%d", "%y,%m,%d",
        "%d-%m-%y", "%d\.%m\.%y", "%d/%m/%y", "%d,%m,%y",
        "%m-%d-%y", "%m\.%d\.%y", "%m/%d/%y", "%m,%d,%y",

        "%y-%m-%-d", "%y\.%m\.%-d", "%y/%m/%-d",  "%y,%m,%-d",
        "%-d-%m-%y", "%-d\.%m\.%y", "%-d/%m/%y",  "%-d,%m,%y",
        "%m-%-d-%y", "%m\.%-d\.%y", "%m/%-d/%y",  "%m,%-d,%y",

        "%B %d, %Y", "%B %-d, %Y", "%B %d %Y", "%B %-d %Y",

        "%B-%d-%Y", "%B\.%d\.%Y", "%B/%d/%Y", "%B,%d,%Y",
        "%d-%B-%Y", "%d\.%B\.%Y", "%d/%B/%Y", "%d,%B,%Y",
        "%Y-%B-%d", "%Y\.%B\.%d", "%Y/%B/%d", "%Y,%B,%d",
        "%B-%-d-%Y", "%B\.%-d\.%Y", "%B/%-d/%Y",  "%B,%-d,%Y",
        "%-d-%B-%Y", "%-d\.%B\.%Y", "%-d/%B/%Y",  "%-d,%B,%Y",
        "%Y-%B-%-d", "%Y\.%B\.%-d", "%Y/%B/%-d",  "%Y,%B,%-d",
        "%B-%d-%y", "%B\.%d\.%y", "%B/%d/%y", "%B,%d,%y",
        "%d-%B-%y", "%d\.%B\.%y", "%d/%B/%y", "%d,%B,%y",
        "%y-%B-%d", "%y\.%B\.%d", "%y/%B/%d", "%y,%B,%d",
        "%B-%-d-%y", "%B\.%-d\.%y", "%B/%-d/%y",  "%B,%-d,%y",
        "%-d-%B-%y", "%-d\.%B\.%y", "%-d/%B/%y",  "%-d,%B,%y",
        "%y-%B-%-d", "%y\.%B\.%-d", "%y/%B/%-d",  "%y,%B,%-d",

        "%b %d, %Y", "%b %-d, %Y", "%b %d %Y", "%b %-d %Y",

        "%b-%d-%Y", "%b\.%d\.%Y", "%b/%d/%Y", "%b,%d,%Y",
        "%d-%b-%Y", "%d\.%b\.%Y", "%d/%b/%Y", "%d,%b,%Y",
        "%Y-%b-%d", "%Y\.%b\.%d", "%Y/%b/%d", "%Y,%b,%d",
        "%b-%-d-%Y", "%b\.%-d\.%Y", "%b/%-d/%Y",  "%b,%-d,%Y",
        "%-d-%b-%Y", "%-d\.%b\.%Y", "%-d/%b/%Y",  "%-d,%b,%Y",
        "%Y-%b-%-d", "%Y\.%b\.%-d", "%Y/%b/%-d",  "%Y,%b,%-d",
        "%b-%d-%y", "%b\.%d\.%y", "%b/%d/%y", "%b,%d,%y",
        "%d-%b-%y", "%d\.%b\.%y", "%d/%b/%y", "%d,%b,%y",
        "%y-%b-%d", "%y\.%b\.%d", "%y/%b/%d", "%y,%b,%d",
        "%b-%-d-%y", "%b\.%-d\.%y", "%b/%-d/%y",  "%b,%-d,%y",
        "%-d-%b-%y", "%-d\.%b\.%y", "%-d/%b/%y",  "%-d,%b,%y",
        "%y-%b-%-d", "%y\.%b\.%-d", "%y/%b/%-d",  "%y,%b,%-d",
    ]
    TIME_COMMON_FORMATS = [
        "%-I:%M %p", "%-I\.%M %p",
        "%I:%M %p", "%I\.%M %p",
        "%-I:%-M %p", "%-I\.%-M %p",
        "%I:%-M %p", "%I\.%-M %p",
        "%H:%M", "%H\.%M",
        "%-H:%M", "%-H\.%M",
        "%H:%-M", "%H\.%-M",
        "%-H:%-M", "%-H\.%-M",

        "%-I%p", "%I%p","%-I %p", "%I %p",

        "%I:%M:%S %p", "%I\.%M\.%S %p",
        "%-I:%M:%S %p", "%-I\.%M\.%S %p",
        "%I:%-M:%S %p", "%I\.%-M\.%S %p",
        "%-I:%-M:%S %p", "%-I\.%-M\.%S %p",
        "%I:%M:%S%p", "%I\.%M\.%S%p",
        "%-I:%M:%S%p", "%-I\.%M\.%S%p",
        "%I:%-M:%S%p", "%I\.%-M\.%S%p",
        "%-I:%-M:%S%p", "%-I\.%-M\.%S%p",

        "%H:%M:%S", "%H\.%M\.%S",
        "%-H:%M:%S", "%-H\.%M\.%S",
        "%H:%-M:%S", "%H\.%-M\.%S",
        "%-H:%-M:%S", "%-H\.%-M\.%S",
    ]
    PREFIX = ["cw", "wk", "day", "week", "time"]

    @functools.lru_cache()
    def get_regex(self, code: str, affix: Optional[Literal["False", "Word-border", "True"]] = "False"):
        try:
            if affix == "False":
                return self.BASIC_CODES[code]["regex"]
            if affix == "Word-border":
                return rf"\b({self.BASIC_CODES[code]['regex']})\b"
            if affix == "True":
                return rf"{self.BASIC_CODES[code]['prefix']}({self.BASIC_CODES[code]['regex']}){self.BASIC_CODES[code]['suffix']}"
        except KeyError:
            return None

    def get_type(self, code: str):
        return self.BASIC_CODES[code]["type"]

    @functools.lru_cache()
    def generate_format_regex(self, code_group: str):
        for match in re.finditer("%-?[aAwdbBmyYHIpMSfzZjUWcxX%]", code_group):
            code = match.group()
            regex = f"({self.get_regex(code)})"
            if regex:
                code_group = code_group.replace(code, regex)

        return fr"{code_group}"
