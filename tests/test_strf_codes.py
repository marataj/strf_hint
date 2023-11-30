"""
Module containing unit tests for strf_codes.py module.

"""

import pytest

from strf_hint.strf_codes import FieldTypes, StrfCodes


@pytest.fixture()
def codes():
    return StrfCodes()


@pytest.fixture()
def mocked_codes():
    mocked_codes = StrfCodes()
    mocked_codes.BASIC_CODES = {
        "%a": {
            "description": "Mocked strf-code.",
            "prefix": "pref_a",
            "suffix": "suf_a",
            "regex": "regex_a",
        },
        "%d": {
            "description": "Mocked strf-code.",
            "prefix": "pref_a",
            "suffix": "suf_d",
            "regex": "regex_d",
        },
        "%M": {
            "description": "Mocked strf-code.",
            "prefix": "pref_M",
            "suffix": "suf_M",
            "regex": "regex_M",
        },
    }
    return mocked_codes


@pytest.mark.parametrize(
    "code, affix, exp_result",
    [
        ("%d", "False", "0[1-9]|[1-2][0-9]|3[0-1]"),
        ("%d", "True", r"[-/.]?\b(0[1-9]|[1-2][0-9]|3[0-1])(th)?\b[-/.]?"),
        (
            "%a",
            "True",
            r"\b("
            + r"|".join(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
            + r")\b",
        ),
        ("%-m", "False", "[0-9]|1[0-2]"),
        ("%-m", "Word-border", r"\b([0-9]|1[0-2])\b"),
        ("%G", "True", None),
    ],
)
def test_get_regex(code, affix, exp_result, codes):
    assert codes.get_regex(code, affix) == exp_result


@pytest.mark.parametrize(
    "args, exp_result",
    [
        (["%d"], "0[1-9]|[1-2][0-9]|3[0-1]"),
        (["%d", "True"], r"[-/.]?\b(0[1-9]|[1-2][0-9]|3[0-1])(th)?\b[-/.]?"),
        (
            ["%a", "True"],
            r"\b("
            + r"|".join(["mon", "tue", "wed", "thu", "fri", "sat", "sun"])
            + r")\b",
        ),
        (["%-m"], "[0-9]|1[0-2]"),
        (["%-m", "Word-border"], r"\b([0-9]|1[0-2])\b"),
        (["%G"], None),
    ],
)
def test_get_regex_optional_affix(args, exp_result, codes):
    assert codes.get_regex(*args) == exp_result


@pytest.mark.parametrize(
    "code, exp_result",
    [
        ("%-W", FieldTypes.WEEK_NUM),
        ("%-U", FieldTypes.WEEK_NUM),
        ("%f", FieldTypes.MICROSECONDS),
        ("%-I", FieldTypes.HOURS),
        ("%X", None),
    ],
)
def test_get_type(code, exp_result, codes):
    assert codes.get_type(code) == exp_result


@pytest.mark.parametrize(
    "code, exp_result",
    [
        (r"%m,%d,%Y", [FieldTypes.MONTH_NUM, FieldTypes.MONTHDAY_NUM, FieldTypes.YEAR]),
        (
            r"%Y,%B,%d",
            [FieldTypes.YEAR, FieldTypes.MONTH_NAME, FieldTypes.MONTHDAY_NUM],
        ),
        (r"%-I\.%-M %p", [FieldTypes.HOURS, FieldTypes.MINUTES, FieldTypes.AM_PM]),
        (r"%-I\.%-M %p %X", [FieldTypes.HOURS, FieldTypes.MINUTES, FieldTypes.AM_PM]),
    ],
)
def test_get_format_types(code, exp_result, codes):
    assert codes.get_format_types(code) == exp_result


@pytest.mark.parametrize(
    "code, exp_result",
    [
        ("%a - %d - %M", "(regex_a) - (regex_d) - (regex_M)"),
        ("%a %d %M %X", "(regex_a) (regex_d) (regex_M) %X"),
        ("%a/%d/%M/%X", "(regex_a)/(regex_d)/(regex_M)/%X"),
    ],
)
def test_generate_format_regex(code, exp_result, mocked_codes):
    assert mocked_codes.generate_format_regex(code) == exp_result
