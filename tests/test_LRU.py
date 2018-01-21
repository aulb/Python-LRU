import sys
sys.path.append('..')

from unittest import TestCase
from LRU import LRU

class TestLRU(TestCase):
	def setUp(self):
		# Setup an empty LRU
		empty = LRU(1)

		# Setup an LRU with one element
		one = LRU(1)
		one.set('1', 'test')

		# Setup an LRU with more than one element
		many = LRU(10)
		many.set('1', 'test')


	def test_length(self):
		pass
