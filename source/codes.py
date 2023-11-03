"""
This module contains datetime codes.

"""

BASIC_CODES = {
    "%a": {
        "description": "Weekday as locale’s abbreviated name.",
        "example": "Sun",
        "prefixes": [],
        "suffixes": [],
        "regex": r"\b"+r"|".join(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])+r"\b"
    },
    "%A": {
        "description": "Weekday as locale’s full name.",
        "example": "Sunday",
        "prefixes": [],
        "suffixes": [],
        "regex": r"|".join(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
    },
    "%w": {
        "description": "Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.",
        "example": '0',
        "prefixes": ["day", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": r"(day )?\b[0-6]\b"
    },
    "%d": {
        "description": "Day of the month as a zero-padded decimal number.",
        "example": "08",
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": r"[-/.]?\b(0[1-9]|[1-2][0-9]|3[0-1])\b[-/.]?"
    },
    "%-d": {
        "description": "Day of the month as a decimal number. (Platform specific)",
        "example": "8",
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": r"[-/.]?\b([1-9]|[1-2][0-9]|[0-1])\b[-/.]?"
    },
    "%b": {
        "description": "Month as locale’s abbreviated name.",
        "example": "Sep",
        "prefixes": [],
        "suffixes": [],
        "regex": r"\b"+"|".join(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])+r"\b"
    },
    "%B": {
        "description": "Month as locale’s full name.",
        "example": "September",
        "prefixes": [],
        "suffixes": [],
        "regex": "|".join(['january', 'february', 'march', 'april', 'may', 'jun', 'july', 'august', 'september', 'october', 'november', 'december'])
    },
    "%m": {
        "description": "Month as a zero-padded decimal number.",
        "example": "09",
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": r"[-/.]?\b(0[1-9]|1[0-2])\b[-/.]?"
    },
    "%-m": {
        "description": "Month as a decimal number. (Platform specific)",
        "example": "9",
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": r"[-/.]?\b([0-9]|1[0-2])\b[-/.]?"
    },
    # TODO: Add expressions for common constructions, like 2023-11-03, 2023/11/03, 11:40, 22:40, 1:20 PM
    "%y": {
        "description": "Year without century as a zero-padded decimal number.",
        "example": "13",
        "prefixes": [],
        "suffixes": [],
        "regex": r"[-/.]?\b(\d{4})\b[-/.]?"
    },
    "%Y": {
        "description": "Year with century as a decimal number.",
        "example": "2013",
        "prefixes": [],
        "suffixes": [],
        "regex": r"[-/.]?\b(\d{1,4})\b[-/.]?"
    },
    "%H": {
        "description": "Hour (24-hour clock) as a zero-padded decimal number.",
        "example": "07",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b(0[0-9]|1[0-9]|2[0-4])\b:?"
    },
    "%-H": {
        "description": "Hour (24-hour clock) as a decimal number. (Platform specific)",
        "example": "7",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b([0-9]|1[0-9]|2[0-4])\b:?"
    },
    "%I": {
        "description": "Hour (12-hour clock) as a zero-padded decimal number.",
        "example": "07",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b(0[0-9]|1[0-2])\b:?"
    },
    "%-I": {
        "description": "Hour (12-hour clock) as a decimal number. (Platform specific)",
        "example": "7",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b([0-9]|1[0-2])\b:?"
    },
    "%p": {
        "description": "Locale’s equivalent of either AM or PM.",
        "example": "AM",
        "prefixes": [],
        "suffixes": [],
        "regex": r"\b(am|pm)\b"
    },
    "%M": {
        "description": "Minute as a zero-padded decimal number.",
        "example": "06",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b(0[0-9]|[1-5][0-9])\b:?"
    },
    "%-M": {
        "description": "Minute as a decimal number. (Platform specific)",
        "example": "6",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b([0-9]|[1-5][0-9])\b:?"
    },
    "%S": {
        "description": "Second as a zero-padded decimal number.",
        "example": "05",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b(0[0-9]|[1-5][0-9])\b:?"
    },
    "%-S": {
        "description": "Second as a decimal number. (Platform specific)",
        "example": "5",
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b([0-9]|[1-5][0-9])\b:?"
    },
    "%f": {
        "description": "Microsecond as a decimal number, zero-padded to 6 digits.",
        "example": 0,
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": r":?\b(\d{6})\b:?"
    },
    "%Z": {
        "description": "Time zone name (empty string if the object is naive).",
        "example": "UTC",
        "prefixes": [],
        "suffixes": [],
        "regex": "|".join(['acdt', 'acst', 'act', 'act', 'acwst', 'adt', 'aedt', 'aest', 'aet (aest/aedt)', 'aft', 'akdt', 'akst', 'almt', 'amst', 'amt', 'amt', 'anat', 'aqtt', 'art', 'ast', 'ast', 'awst', 'azost', 'azot', 'azt', 'bnt', 'biot', 'bit', 'bot', 'brst', 'brt', 'bst', 'bst', 'bst', 'btt', 'cat', 'cct', 'cdt', 'cdt', 'cest', 'cet', 'chadt', 'chast', 'chot', 'chost', 'chst', 'chut', 'cist', 'ckt', 'clst', 'clt', 'cost', 'cot', 'cst', 'cst', 'cst', 'ct (cst/cdt)', 'cvt', 'cwst', 'cxt', 'davt', 'ddut', 'dft', 'easst', 'east', 'eat', 'ect', 'ect', 'edt', 'eest', 'eet', 'egst', 'egt', 'est', 'et (est/edt)', 'fet', 'fjt', 'fkst', 'fkt', 'fnt', 'galt', 'gamt', 'get', 'gft', 'gilt', 'git', 'gmt', 'gst', 'gst', 'gyt', 'hdt', 'haec', 'hst', 'hkt', 'hmt', 'hovst', 'hovt', 'ict', 'idlw', 'idt', 'iot', 'irdt', 'irkt', 'irst', 'ist', 'ist', 'ist', 'jst', 'kalt', 'kgt', 'kost', 'krat', 'kst', 'lhst', 'lhst', 'lint', 'magt', 'mart', 'mawt', 'mdt', 'met', 'mest', 'mht', 'mist', 'mit', 'mmt', 'msk', 'mst', 'mst', 'mut', 'mvt', 'myt', 'nct', 'ndt', 'nft', 'novt', 'npt', 'nst', 'nt', 'nut', 'nzdt', 'nzst', 'omst', 'orat', 'pdt', 'pet', 'pett', 'pgt', 'phot', 'pht', 'phst', 'pkt', 'pmdt', 'pmst', 'pont', 'pst', 'pwt', 'pyst', 'pyt', 'ret', 'rott', 'sakt', 'samt', 'sast', 'sbt', 'sct', 'sdt', 'sgt', 'slst', 'sret', 'srt', 'sst', 'sst', 'syot', 'taht', 'tha', 'tft', 'tjt', 'tkt', 'tlt', 'tmt', 'trt', 'tot', 'tst', 'tvt', 'ulast', 'ulat', 'utc', 'uyst', 'uyt', 'uzt', 'vet', 'vlat', 'volt', 'vost', 'vut', 'wakt', 'wast', 'wat', 'west', 'wet', 'wib', 'wit', 'wita', 'wgst', 'wgt', 'wst', 'yakt', 'yekt'])
    },
    "%j": {
        "description": "Day of the year as a zero-padded decimal number.",
        "example": "251",
        "prefixes": [],
        "suffixes": [],
        "regex": r"\b(00\d|0\d\d|[1-2]\d\d|3[0-6][0-6])\b"
    },
    "%-j": {
        "description": "Day of the year as a decimal number. (Platform specific)",
        "example": "251",
        "prefixes": [],
        "suffixes": [],
        "regex": r"\b(\d|\d\d|[1-2]\d{2}|3[0-6]{2})\b"
    },
    "%U": {
        "description": "Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.",
        "example": "36",
        "prefixes": ["cw", "wk"],
        "suffixes": [],
        "regex": r"(cw |wk )?\b(0\d|[1-4]|5[0-4])\b( cw| wk)?"
    },
    "%-U": {
        "description": "Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)",
        "example": "36",
        "prefixes": ["cw", "wk"],
        "suffixes": [],
        "regex": r"(cw |wk )?\b(\d|[1-4]\d|5[0-4])\b( cw| wk)?"
    },
    "%W": {
        "description": "Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.",
        "example": "35",
        "prefixes": ["cw", "wk"],
        "suffixes": [],
        "regex": r"(cw |wk )?\b(0\d|[1-4]|5[0-4])\b( cw| wk)?"
    },
    "%-W": {
        "description": "Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)",
        "example": "35",
        "prefixes": ["cw", "wk"],
        "suffixes": [],
        "regex": r"(cw |wk )?\b(\d|[1-4]\d|5[0-4])\b( cw| wk)?"
    },
    # "%c": {
    #     "description": "Locale’s appropriate date and time representation.",
    #     "example": "Sun Sep 8 07:06:05 2013",
    #     "prefixes": [],
    #     "suffixes": [],
    #     "regex": ""
    # },
    # "%x": {
    #     "description": "Locale’s appropriate date representation.",
    #     "example": '09/08/13',
    #     "prefixes": [],
    #     "suffixes": [],
    #     "regex": ""
    # },
    # "%X": {
    #     "description": "Locale’s appropriate time representation.",
    #     "example": '07:06:05',
    #     "prefixes": [],
    #     "suffixes": [],
    #     "regex": ""
    # },
    "%%": {
        "description": "A literal '%' character.",
        "example": "%",
        "prefixes": [],
        "suffixes": [],
        "regex": "%"
    },
}

def get_basic_regex(code: str):
    return BASIC_CODES[code]["regex"]

COMPLEX_CODES = {

}