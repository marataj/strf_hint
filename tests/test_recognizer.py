"""
Module containing unit tests for recognizer.py module.

"""
import string

import pytest

from source.recognizer import Recognizer
from source.strf_codes import FieldTypes


@pytest.fixture
def recognizer():
    yield Recognizer()


@pytest.mark.parametrize(
    "input_str, exp_output, exp_mask, exp_types",
    [
        (
            "7:20 PM",
            "%-I:%M %p",
            "111111111",
            [FieldTypes.HOURS, FieldTypes.MINUTES, FieldTypes.AM_PM],
        ),
        (
            "2023-11-21, 7:20 PM",
            "%Y-%m-%d, %-I:%M %p",
            "1111111100111111111",
            [
                FieldTypes.HOURS,
                FieldTypes.MINUTES,
                FieldTypes.AM_PM,
                FieldTypes.YEAR,
                FieldTypes.MONTH_NUM,
                FieldTypes.MONTHDAY_NUM,
            ],
        ),
        (
            "day: Tue 2023-NOV-06 time: 17:20:50",
            "day: Tue %Y-%b-%d time: %H:%M:%S",
            "00000000011111111000000011111111",
            [
                FieldTypes.HOURS,
                FieldTypes.MINUTES,
                FieldTypes.YEAR,
                FieldTypes.MONTH_NAME,
                FieldTypes.MONTHDAY_NUM,
                FieldTypes.SECONDS,
            ],
        ),
    ],
)
def test_match_patterns(input_str, exp_output, exp_mask, exp_types, recognizer):
    recognizer.matched_mask = "0" * len(input_str)
    assert recognizer._match_patterns(input_str) == exp_output
    assert set(recognizer.matched_types) == set(exp_types)
    assert recognizer.matched_mask == exp_mask


def test_retrieve_unmatched(recognizer):
    recognizer.matched_mask = "0011100000001111"
    assert recognizer._retrieve_unmatched("unhhhmatchedhhhh") == [
        ("un", (0, 2)),
        ("matched", (5, 12)),
    ]


@pytest.mark.parametrize(
    "char, group",
    [
        ("a", "letters"),
        ("Z", "letters"),
        ("X", "letters"),
        ("1", "digits"),
        ("0", "digits"),
        (" ", "whitespace"),
        ("\n", "whitespace"),
        (":", "punctuation"),
        ("/", "punctuation"),
    ],
)
def test_check_string_group(char, group, recognizer):
    assert recognizer._check_string_group(char) == group


@pytest.mark.parametrize(
    "text, exp_result",
    [
        (
            "another-1-components:2222 ::",
            ["another", "-", "1", "-", "components", ":", "2222", " ", "::"],
        ),
        (
            "2023-11:01 Tue 17:100000000000:test",
            [
                "2023",
                "-",
                "11",
                ":",
                "01",
                " ",
                "Tue",
                " ",
                "17",
                ":",
                "100000000000",
                ":",
                "test",
            ],
        ),
        (
            "2023-11-28, 11:38",
            ["2023", "-", "11", "-", "28", ",", " ", "11", ":", "38"],
        ),
        (
            "Sunday2023_March_22_CW12_10_20_PM",
            [
                "Sunday",
                "2023",
                "_",
                "March",
                "_",
                "22",
                "_",
                "CW",
                "12",
                "_",
                "10",
                "_",
                "20",
                "_",
                "PM",
            ],
        ),
    ],
)
def test_split_format_components(text, exp_result, recognizer):
    assert recognizer._split_format_components(text) == exp_result


@pytest.mark.parametrize(
    "input_str, matched_mask, matched_types, exp_result",
    [
        (
            "%Y-%m 07:20pm CW20",
            "111110000000000000",
            [FieldTypes.YEAR, FieldTypes.MONTH_NUM],
            "%Y-%m %I:%M%p CW%U",
        ),
        (
            "Jan, Sun, %Y-%m-%d",
            "000000000011111111",
            [FieldTypes.YEAR, FieldTypes.MONTH_NUM, FieldTypes.MONTHDAY_NUM],
            "%b, %a, %Y-%m-%d",
        ),
        (
            "251 day of the year: Jan, Sun, %Y-%m-%d",
            "0000000000000000000000000000000011111111",
            [FieldTypes.YEAR, FieldTypes.MONTH_NUM, FieldTypes.MONTHDAY_NUM],
            "%j day of the year: %b, %a, %Y-%m-%d",
        ),
    ],
)
def test_recognize_single_codes(
    input_str, matched_mask, matched_types, exp_result, recognizer
):
    recognizer.matched_mask = matched_mask
    recognizer.matched_types = matched_types
    assert recognizer._recognize_single_codes(input_str) == exp_result


@pytest.mark.parametrize(
    "input_str, exp_result",
    [
        ("2022-04-12, sunday, 14:30", "%Y-%m-%d, %A, %H:%M"),
        ("March 11th 2023 9:30 PM", "%B %dth %Y %-I:%M %p"),
        ("19:19:19.100000", "%H:%M:%S.%f"),
        ("WK30, 2023", "WK%U, %Y"),
        ("(22:13), today is tuesday, 18 Mar 2021", "(%H:%M), today is %A, %d %b %Y"),
        ("Day: Sunday, 2022-Nov-30, 9:30 PM", "Day: %A, %Y-%b-%d, %-I:%M %p")
    ],
)
def test_encode_format(input_str, exp_result, recognizer):
    assert recognizer.encode_format(input_str) == exp_result
