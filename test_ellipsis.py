import unittest

import ellipsis


class DefaultEllipsisFormatterTestCase(unittest.TestCase):

    def setUp(self):
        self.ellipsis_formatter = ellipsis.EllipsisFormatter()

    def test_length_short(self):
        input_string = "Hola"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(len(formatted_string), 4)

    def test_length_long(self):
        input_string = "Hola " * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertLessEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_length_long_sentence(self):
        input_string = "Hola que tal, blablabla. Te mola mi pistola?"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertLessEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_length_long_no_spaces(self):
        input_string = "Hola" * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_correct_short(self):
        input_string = "Hola"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola")

    def test_correct_long(self):
        input_string = "Hola " * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola Hola Hola Hola Hola [...]")

    def test_correct_long_sentence(self):
        input_string = "Hola que tal, blablabla. Te mola mi pistola?"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola que tal, blablabla. [...]")

    def test_correct_long_no_spaces(self):
        input_string = "Hola" * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "HolaHolaHolaHolaHolaHolaHol[...]")


class Max16Min8EllipsisFormatterTestCase(unittest.TestCase):

    def setUp(self):
        self.ellipsis_formatter = ellipsis.EllipsisFormatter(max_len=16, min_len=8)

    def test_length_short_long(self):
        input_string = "Hola holablablabla"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(len(formatted_string), 16)

    def test_length_long(self):
        input_string = "Hola " * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertLessEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_length_long_sentence(self):
        input_string = "Hola que tal, blablabla. Te mola mi pistola?"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertLessEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_length_long_no_spaces(self):
        input_string = "Hola" * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_correct_short(self):
        input_string = "Hola"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola")

    def test_correct_long(self):
        input_string = "Hola " * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola Hola [...]")

    def test_correct_long_sentence(self):
        input_string = "Hola que tal, blablabla. Te mola mi pistola?"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola que [...]")

    def test_correct_long_no_spaces(self):
        input_string = "Hola" * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "HolaHolaHol[...]")


class Max16EllipsisFormatterTestCase(unittest.TestCase):

    def setUp(self):
        self.ellipsis_formatter = ellipsis.EllipsisFormatter(max_len=16)

    def test_length_short(self):
        input_string = "Hola"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(len(formatted_string), 4)

    def test_length_long(self):
        input_string = "Hola " * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertLessEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_length_long_sentence(self):
        input_string = "Hola que tal, blablabla. Te mola mi pistola?"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertLessEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_length_long_no_spaces(self):
        input_string = "Hola" * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertGreater(len(formatted_string), self.ellipsis_formatter.min_len)
        self.assertEqual(len(formatted_string), self.ellipsis_formatter.max_len)

    def test_correct_short(self):
        input_string = "Hola"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola")

    def test_correct_long(self):
        input_string = "Hola " * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola Hola [...]")

    def test_correct_long_sentence(self):
        input_string = "Hola que tal, blablabla. Te mola mi pistola?"
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "Hola que [...]")

    def test_correct_long_no_spaces(self):
        input_string = "Hola" * 32
        formatted_string = self.ellipsis_formatter.format(input_string)
        self.assertEqual(formatted_string, "HolaHolaHol[...]")


if __name__ == "__main__":
    unittest.main()

