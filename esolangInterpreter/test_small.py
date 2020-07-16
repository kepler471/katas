import unittest
from esolangInterpreter.small import interpreter


class MyTestCase(unittest.TestCase):
    def test80(self):
        # Flips the leftmost cell of the tape
        result = interpreter("*", "00101100")
        self.assertEqual(result, "10101100")

    def test70(self):
        # Flips the second and third cell of the tape
        result = interpreter(">*>*", "00101100")
        self.assertEqual(result, "01001100")

    def test60(self):
        # Flips all the bits in the tape
        result = interpreter("*>*>*>*>*>*>*>*", "00101100")
        self.assertEqual(result, "11010011")

    def test10(self):
        # Flips all the bits that are initialized to 0
        result = interpreter("*>*>>*>>>*>*", "00101100")
        self.assertEqual(result, "11111111")

    def test11(self):
        # Goes somewhere to the right of the tape and then flips all bits
        # that are initialized to 1, progressing leftwards through the tape
        result = interpreter(">>>>>*<*<<*", "00101100")
        self.assertEqual(result, "00000000")

    def test1(self):
        result = interpreter("*[*[*]]", "0")
        self.assertEqual(result, "0")

    def test2(self):
        result = interpreter("[*[*]]", "00101100")
        self.assertEqual(result, "00101100")

    def test3(self):
        result = interpreter("[[*]]", "00101100")
        self.assertEqual(result, "00101100")

    def test_run_loop(self):
        result = interpreter("*[>*]", "00101100")
        self.assertEqual(result, "11001100")

    def test_nested_loop(self):
        result = interpreter("*[>*[*]]", "00101100")
        self.assertEqual(result, "10101100")

    def test_simple_loop(self):
        result = interpreter("*[>*]", "00000000000")
        self.assertEqual(result, "11111111111")

    def test_skip_loop(self):
        result = interpreter("[[*[>***>>>>>>]>]*]", "110")
        self.assertEqual(result, "000")

    def test_skip_loop2(self):
        result = interpreter("[[*[>***>>[>>>[]>>>]>>[>>>]>[>>>]>]>]*]", "110")
        self.assertEqual(result, "000")

    def test_nested_loop2(self):
        result = interpreter("[[*[>***>>[>>>[]>>>]>>[>>>]>[>>>]>]>]*]*", "110")
        self.assertEqual(result, "000")


if __name__ == '__main__':
    unittest.main()
