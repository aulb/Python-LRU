# -*- coding: utf-8 -*-
import unittest
from suite.LRU import LRU


class TestLRU(unittest.TestCase):
	def setUp(self):
		# Setup an empty LRU
		self.empty = LRU(1)

		# Setup an LRU with one element
		self.one = LRU(1)
		self.one.set('a', 'test_init_one')

		# Setup an LRU with more than one element
		self.many = LRU(3)
		self.many.set('a', 'test_many_init_a')
		self.many.set('b', 'test_many_init_b')
		self.many.set('c', 'test_many_init_c')


	def test_main(self):
		# test a populated
		self.assertEqual(self.one.get('a'), 'test_init_one')

		# test set overwrite
		self.one.set('a', 'test_one_overwrite')		
		self.assertEqual(self.one.get('a'), 'test_one_overwrite')

		# test set overwrite new key
		self.one.set('b', 'test_one_new_key_evict')
		self.assertEqual(self.one.get('b'), 'test_one_new_key_evict')

		# test a, b, c populated
		self.assertEqual(self.many.get('b'), 'test_many_init_b')
		self.assertEqual(self.many.get('a'), 'test_many_init_a')
		self.assertEqual(self.many.get('c'), 'test_many_init_c')

		# test eviction order
		self.many.set('d', 'test_eviction_order')
		self.assertEqual(self.many.get('b'), None) # Should be gone
		self.assertEqual(self.many.get('d'), 'test_eviction_order')
		self.assertEqual(self.many.get('a'), 'test_many_init_a')
		self.assertEqual(self.many.get('c'), 'test_many_init_c')


if __name__ == '__main__':
	unittest.main()
