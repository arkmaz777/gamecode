from django.test import TestCase

from django.test import TestCase
from .views import result_evaluation

class ResultEvaluationTests(TestCase):
    def test_different_values(self):
        result = result_evaluation(['J', 'Q', 'K'])
        self.assertEqual(result, 0)

    def test_all_same_values_for_J(self):
        result = result_evaluation(['J', 'J', 'J'])
        self.assertEqual(result, 1)

    def test_all_same_values_for_Q(self):
        result = result_evaluation(['Q', 'Q', 'Q'])
        self.assertEqual(result, 2)

    def test_all_same_values_for_K(self):
        result = result_evaluation(['K', 'K', 'K'])
        self.assertEqual(result, 3)

    def test_same_value_for_A(self):
        result = result_evaluation(['A', 'A', 'A'])
        self.assertEqual(result, 4)

    def test_invalid_length_raises_exception(self):
        with self.assertRaises(ValueError):
            result_evaluation(['J', 'Q'])

