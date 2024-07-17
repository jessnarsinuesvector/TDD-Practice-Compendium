from pathlib import Path
from unittest import TestCase

from src.rules.valid_numeral_sequence import ValidNumeralSequence


class TestValidNumeralSequence(TestCase):
    def setUp(self):
        roman_numeral_map_file_path = Path.resolve(Path(__file__).parent.parent.parent.resolve() / 'src/data'                                                                                    '/roman_numeral_map.json')
        self.rule = ValidNumeralSequence(roman_numeral_map_file_path)

    def test_can_load_numeral_map_file(self):
        self.assertNotEqual(self.rule.numeral_map, {})

    def test_can_validate_false_if_left_character_is_more_than_two_levels_lower(self):
        self.assertFalse(self.rule.is_valid("XC"))
        self.assertFalse(self.rule.is_valid("IXL"))

    def test_can_validate_false_if_sequence_is_within_restricted_sequences(self):
        self.assertFalse(self.rule.is_valid("VX"))
        self.assertFalse(self.rule.is_valid("LL"))

    def test_can_validate_false_if_left_character_is_one_level_lower_but_repeats_more_than_once(self):
        self.assertFalse(self.rule.is_valid("XXL"))

    def test_can_validate_true_if_sequence_is_valid(self):
        self.assertTrue(self.rule.is_valid("XL"))