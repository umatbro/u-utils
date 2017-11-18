from unittest import TestCase
from um import utils


class TestRemap(TestCase):
    def test_regular_values(self):
        mapped = utils.remap(10, 0, 100, 0, 1000)
        self.assertEqual(mapped, 100)

    def test_out_of_range(self):
        result = utils.remap(100, 0, 10, 0, 100)
        self.assertEqual(result, 1000)

    def test_negative_out_of_range(self):
        result = utils.remap(-100, 0, 10, 0, 100)
        self.assertEqual(result, -1000)


class TestConstrain(TestCase):
    def test_regular_values_in_range(self):
        result = utils.constrain(10, 100, 0)
        self.assertEqual(result, 10)

    def test_regular_values_below_range(self):
        result = utils.constrain(-1, 0, 10)
        self.assertEqual(result, 0)

    def test_regular_values_above_range(self):
        result = utils.constrain(11, 0, 10)
        self.assertEqual(result, 10)

    def test_max_val_lt_min_val(self):
        result = utils.constrain(-1, 10, 0)
        self.assertEqual(result, 0)

    def test_negative_values(self):
        result = utils.constrain(100, -10, -1)
        self.assertEqual(result, -1)

    def test_negative_values_below_range(self):
        result = utils.constrain(-100, -10, -1)
        self.assertEqual(result, -10)


class TestAddTuples(TestCase):
    def test_simple_addition(self):
        """Example: (1, 3, 5) + (3, 3, 3) = (4, 6, 8)"""
        self.assertTupleEqual(
            utils.add_tuples((1, 3, 5), (3, 3, 3)),
            (4, 6, 8)
        )

    def test_add_different_size_tuples(self):
        self.assertTupleEqual(
            utils.add_tuples((1, 3, 5), (3, 3)),
            (4, 6)
        )


class TestSubTuples(TestCase):
    def test_simple_subtraction(self):
        """Example: (1, 3, 5) - (3, 3, 3) = (-2, 0, 2)"""
        self.assertTupleEqual(
            utils.sub_tuples((1, 3, 5), (3, 3, 3)),
            (-2, 0, 2)
        )

    def test_different_size_tuples(self):
        self.assertTupleEqual(
            utils.sub_tuples((1, 3, 5), (3, 3)),
            (-2, 0)
        )


class TestMergeDicts(TestCase):
    def test_merge_dicts(self):
        self.assertDictEqual(
            utils.merge_dicts(
                {1: 'one', 2: 'two', 4: 'four'},
                {1: 'one1', 3: 'three'},
                {5: 'five'},
                {}
            ),
            {1: 'one1', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
        )
