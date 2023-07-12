import pytest

from parse_ranges.parse_ranges import parse_ranges


class TestParseRanges:
    def test_input_type_str(self):
        with pytest.raises(TypeError):
            list(parse_ranges(10))

    def test_base_problem(self):
        assert list(parse_ranges("1-2,4-4,8-13")) == [
            1,
            2,
            4,
            8,
            9,
            10,
            11,
            12,
            13,
        ]
        assert list(parse_ranges("0-0, 4-8, 20-20, 43-45")) == [
            0,
            4,
            5,
            6,
            7,
            8,
            20,
            43,
            44,
            45,
        ]

    def test_bonus_1(self):
        numbers = parse_ranges("100-10000")
        assert next(numbers) == 100
        assert next(numbers) == 101

    def test_bonus_2(self):
        assert list(parse_ranges("0,4-8,20,43-45")) == [
            0,
            4,
            5,
            6,
            7,
            8,
            20,
            43,
            44,
            45,
        ]

    def test_bonus_3(self):
        assert list(parse_ranges("0, 4-8, 20->exit, 43-45")) == [
            0,
            4,
            5,
            6,
            7,
            8,
            20,
            43,
            44,
            45,
        ]
