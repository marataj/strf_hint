"""
This module contains datetime codes.

"""

CODES = {
    "%a": {
        "description": "Weekday as locale’s abbreviated name.",
        "example": "Sun",
        "values": ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'],
        "prefixes": [],
        "suffixes": [],
        "regex": "|".join(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
    },
    "%A": {
        "description": "Weekday as locale’s full name.",
        "example": "Sunday",
        "values": ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
        "prefixes": [],
        "suffixes": [],
        "regex": "|".join(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
    },
    "%w": {
        "description": "Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.",
        "example": '0',
        "values": [str(x) for x in range(7)],
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": "[0-6]"
    },
    "%d": {
        "description": "Day of the month as a zero-padded decimal number.",
        "example": "08",
        "values": ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": "0[1-9]|[1-2][0-9]|3[0-1]"
    },
    "%-d": {
        "description": "Day of the month as a decimal number. (Platform specific)",
        "example": "8",
        "values": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": "[1-9]|[1-2][0-9]|[0-1]"
    },
    "%b": {
        "description": "Month as locale’s abbreviated name.",
        "example": "Sep",
        "values": ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
        "prefixes": [],
        "suffixes": [],
        "regex": "|".join(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    },
    "%B": {
        "description": "Month as locale’s full name.",
        "example": "September",
        "values": ['january', 'february', 'march', 'april', 'may', 'jun', 'july', 'august', 'september', 'october', 'november', 'december'],
        "prefixes": [],
        "suffixes": [],
        "regex": "|".join(['january', 'february', 'march', 'april', 'may', 'jun', 'july', 'august', 'september', 'october', 'november', 'december'])
    },
    "%m": {
        "description": "Month as a zero-padded decimal number.",
        "example": "09",
        "values": ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',],
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": "0[1-9]|1[0-2]"
    },
    "%-m": {
        "description": "Month as a decimal number. (Platform specific)",
        "example": "9",
        "values": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',],
        "prefixes": ["-", "/", "."],
        "suffixes": ["-", "/", "."],
        "regex": "[0-9]|1[0-2]"
    },
    "%y": {
        "description": "Year without century as a zero-padded decimal number.",
        "example": "13",
        "values": [*[f"0{x}" for x in range(10)], *[str(y) for y in range(10, 100)]],
        "prefixes": [],
        "suffixes": [],
        "regex": "\d{4}"
    },
    "%Y": {
        "description": "Year with century as a decimal number.",
        "example": "2013",
        "values": [str(x) for x in range(5000)],
        "prefixes": [],
        "suffixes": [],
        "regex": "\d{1,4}"
    },
    "%H": {
        "description": "Hour (24-hour clock) as a zero-padded decimal number.",
        "example": "07",
        "values": [*[f"0{x}" for x in range(10)], *[str(y) for y in range(10, 24)]],
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": "0[0-9]|1[0-9]|2[0-4]"
    },
    "%-H": {
        "description": "Hour (24-hour clock) as a decimal number. (Platform specific)",
        "example": "7",
        "values": [str(x) for x in range(24)],
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": "[0-9]|1[0-9]|2[0-4]"
    },
    "%I": {
        "description": "Hour (12-hour clock) as a zero-padded decimal number.",
        "example": "07",
        "values": [*[f"0{x}" for x in range(10)], *[str(y) for y in range(10, 13)]],
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": "0[0-9]|1[0-2]"
    },
    "%-I": {
        "description": "Hour (12-hour clock) as a decimal number. (Platform specific)",
        "example": "7",
        "values": [str(x) for x in range(13)],
        "prefixes": [":"],
        "suffixes": [":"],
        "regex": "[0-9]|1[0-2]"
    },
    "%p": {
        "description": "Locale’s equivalent of either AM or PM.",
        "example": "AM",
        "values": ["am", "pm"],
        "prefixes": [],
        "suffixes": [],
    },
    "%M": {
        "description": "Minute as a zero-padded decimal number.",
        "example": "06",
        "values": [*[f"0{x}" for x in range(10)], *[str(y) for y in range(10, 60)]],
        "prefixes": [":"],
        "suffixes": [":"],
    },
    "%-M": {
        "description": "Minute as a decimal number. (Platform specific)",
        "example": "6",
        "values": [str(x) for x in range(60)],
        "prefixes": [":"],
        "suffixes": [":"],
    },
    "%S": {
        "description": "Second as a zero-padded decimal number.",
        "example": "05",
        "values": [*[f"0{x}" for x in range(10)], *[str(y) for y in range(10, 60)]],
        "prefixes": [":"],
        "suffixes": [":"],
    },
    "%-S": {
        "description": "Second as a decimal number. (Platform specific)",
        "example": "5",
        "values": [str(x) for x in range(60)],
        "prefixes": [":"],
        "suffixes": [":"],
    },
    # "%f": {
    #     "description": "Microsecond as a decimal number, zero-padded to 6 digits.",
    #     "example": 0,
    #     "values": [f'{n:06}' for n in range(1000000)],
    #     "prefixes": [":"],
    #     "suffixes": [":"],
    # },
    "%Z": {
        "description": "Time zone name (empty string if the object is naive).",
        "example": "UTC",
        "values": ['acdt', 'acst', 'act', 'act', 'acwst', 'adt', 'aedt', 'aest', 'aet (aest/aedt)', 'aft', 'akdt', 'akst', 'almt', 'amst', 'amt', 'amt', 'anat', 'aqtt', 'art', 'ast', 'ast', 'awst', 'azost', 'azot', 'azt', 'bnt', 'biot', 'bit', 'bot', 'brst', 'brt', 'bst', 'bst', 'bst', 'btt', 'cat', 'cct', 'cdt', 'cdt', 'cest', 'cet', 'chadt', 'chast', 'chot', 'chost', 'chst', 'chut', 'cist', 'ckt', 'clst', 'clt', 'cost', 'cot', 'cst', 'cst', 'cst', 'ct (cst/cdt)', 'cvt', 'cwst', 'cxt', 'davt', 'ddut', 'dft', 'easst', 'east', 'eat', 'ect', 'ect', 'edt', 'eest', 'eet', 'egst', 'egt', 'est', 'et (est/edt)', 'fet', 'fjt', 'fkst', 'fkt', 'fnt', 'galt', 'gamt', 'get', 'gft', 'gilt', 'git', 'gmt', 'gst', 'gst', 'gyt', 'hdt', 'haec', 'hst', 'hkt', 'hmt', 'hovst', 'hovt', 'ict', 'idlw', 'idt', 'iot', 'irdt', 'irkt', 'irst', 'ist', 'ist', 'ist', 'jst', 'kalt', 'kgt', 'kost', 'krat', 'kst', 'lhst', 'lhst', 'lint', 'magt', 'mart', 'mawt', 'mdt', 'met', 'mest', 'mht', 'mist', 'mit', 'mmt', 'msk', 'mst', 'mst', 'mut', 'mvt', 'myt', 'nct', 'ndt', 'nft', 'novt', 'npt', 'nst', 'nt', 'nut', 'nzdt', 'nzst', 'omst', 'orat', 'pdt', 'pet', 'pett', 'pgt', 'phot', 'pht', 'phst', 'pkt', 'pmdt', 'pmst', 'pont', 'pst', 'pwt', 'pyst', 'pyt', 'ret', 'rott', 'sakt', 'samt', 'sast', 'sbt', 'sct', 'sdt', 'sgt', 'slst', 'sret', 'srt', 'sst', 'sst', 'syot', 'taht', 'tha', 'tft', 'tjt', 'tkt', 'tlt', 'tmt', 'trt', 'tot', 'tst', 'tvt', 'ulast', 'ulat', 'utc', 'uyst', 'uyt', 'uzt', 'vet', 'vlat', 'volt', 'vost', 'vut', 'wakt', 'wast', 'wat', 'west', 'wet', 'wib', 'wit', 'wita', 'wgst', 'wgt', 'wst', 'yakt', 'yekt'],
        "prefixes": [],
        "suffixes": [],
    },
    "%j": {
        "description": "Day of the year as a zero-padded decimal number.",
        "example": "251",
        "values": [f'{n:03}' for n in range(1, 367)],
        "prefixes": [],
        "suffixes": [],
    },
    "%-j": {
        "description": "Day of the year as a decimal number. (Platform specific)",
        "example": "251",
        "values": [str(x) for x in range(1, 367)],
        "prefixes": [],
        "suffixes": [],
    },
    "%U": {
        "description": "Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.",
        "example": "36",
        "values": [f'{n:02}' for n in range(1, 55)],
        "prefixes": ["cw", "wk"],
        "suffixes": [],
    },
    "%-U": {
        "description": "Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)",
        "example": "36",
        "values": [str(x) for x in range(1, 55)],
        "prefixes": ["cw", "wk"],
        "suffixes": [],
    },
    "%W": {
        "description": "Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.",
        "example": "35",
        "values": [f'{n:02}' for n in range(1, 55)],
        "prefixes": ["cw", "wk"],
        "suffixes": [],
    },
    "%-W": {
        "description": "Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)",
        "example": "35",
        "values": [str(x) for x in range(1, 55)],
        "prefixes": ["cw", "wk"],
        "suffixes": [],
    },
    "%c": {
        "description": "Locale’s appropriate date and time representation.",
        "example": "Sun Sep 8 07:06:05 2013",
        "values": [],
        "prefixes": [],
        "suffixes": [],
    },
    "%x": {
        "description": "Locale’s appropriate date representation.",
        "example": '09/08/13',
        "values": [],
        "prefixes": [],
        "suffixes": [],
    },
    "%X": {
        "description": "Locale’s appropriate time representation.",
        "example": '07:06:05',
        "values": [],
        "prefixes": [],
        "suffixes": [],
    },
    "%%": {
        "description": "A literal '%' character.",
        "example": "%",
        "values": ["%"],
        "prefixes": [],
        "suffixes": [],
    },
}
