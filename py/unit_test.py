import unittest
from py.ContestAlgorithm_2020 import run, readFileContent


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/1.in')), 5)

    def test_case_2(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/2.in')), 7)

    def test_case_3(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/3.in')), 7)

    def test_case_4(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/4.in')), 8)

    def test_case_5(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/5.in')), 704)

    def test_case_6(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/6.in')), 84675)

    def test_case_7(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/7.in')), 31)

    def test_case_8(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/8.in')), 37)

    def test_case_9(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/9.in')), 116)

    def test_case_10(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/10.in')), 167)

    def test_case_11(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/11.in')), 1026)

    def test_case_12(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/12.in')), 2877)

    def test_case_13(self):
        self.assertEqual(run(readFileContent('C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase/13.in')), 4121)


if __name__ == '__main__':
    unittest.main()
