"""CHARACTERIZATION tests for invoices.total: they pin what it does TODAY, quirks included, not what it should do."""
import unittest

from invoices import total


class TotalToday(unittest.TestCase):
    # Each line is [item, price, quantity]

    def test_adds_price_times_quantity(self):
        self.assertEqual(total([["a", 10, 2], ["b", 5, 1]], "normal"), 25)

    def test_quantity_none_counts_as_1(self):
        self.assertEqual(total([["a", 10, None]], "normal"), 10)

    def test_quirk_modifies_the_input_list(self):
        lines = [["a", 10, None]]
        total(lines, "normal")
        self.assertEqual(lines[0][2], 1)  # the caller sees the change

    def test_quantity_0_stays_0(self):
        self.assertEqual(total([["a", 10, 0]], "normal"), 0)

    def test_vip_takes_10_percent_off(self):
        self.assertEqual(total([["a", 100, 1]], "VIP"), 90.0)

    def test_quirk_lowercase_vip_gets_no_discount(self):
        self.assertEqual(total([["a", 100, 1]], "vip"), 100)

    def test_over_1000_subtracts_50(self):
        self.assertEqual(total([["a", 1100, 1]], "normal"), 1050)

    def test_exactly_1000_does_not_subtract_50(self):
        self.assertEqual(total([["a", 1000, 1]], "normal"), 1000)

    def test_quirk_vip_applies_first_and_can_cancel_the_50(self):
        self.assertEqual(total([["a", 1100, 1]], "VIP"), 990.0)    # without VIP it would be 1050
        self.assertEqual(total([["a", 2000, 1]], "VIP"), 1750.0)  # 1800 - 50

    def test_quirk_empty_list_returns_int_or_float_depending_on_customer(self):
        no_vip, with_vip = total([], "normal"), total([], "VIP")
        self.assertEqual((no_vip, type(no_vip)), (0, int))
        self.assertEqual((with_vip, type(with_vip)), (0.0, float))

    def test_rounds_to_2_decimals(self):
        self.assertEqual(total([["a", 0.1, 3]], "normal"), 0.3)

    def test_quirk_price_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            total([["a", None, 1]], "normal")


if __name__ == "__main__":
    unittest.main()
