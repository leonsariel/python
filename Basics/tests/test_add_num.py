# _*_ coding: utf-8 _*_
from unittest import TestCase
import test

__author__ = 'Di Meng'
__date__ = '1/12/2018 11:35 AM'


class TestAdd_num(TestCase):
    def test_add_num(self):
        self.assertEqual(test.add_num(1,2),3)

