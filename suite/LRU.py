# -*- coding: utf-8 -*-
from .Node import Node
from .DoublyLinkedList import DoublyLinkedList


class LRU:
	"""
	Assuming that we need to build the LRU using only Python primitives.
	"""
	def __init__(self, max_size):
		# Bare minimum checks
		assert max_size > 0
		self._max_size = max_size
		# Hash here for fast key lookup and removal
		self._lookup = {}
		self._data = DoublyLinkedList()

	def set(self, key, value):
		if key in self._lookup: 
			# Overwrite the key's value
			current_node = self._lookup[key]
			current_node.value = value

			# Mark as recently used by moving to the beginning of the list
			# 1) Remove the node from the DLL
			self._data.remove(current_node)

			# 2) Add the node back to the DLL
			self._data.append(current_node)
		else:
			# Otherwise create new node and append
			new_node = Node(key, value)
			self._lookup[key] = new_node
			self._data.append(new_node)

		# If more than max capacity
		if len(self._lookup) > self._max_size:
			# Evict the last recently used
			# Pop the last element
			stale_node = self._data.pop()
			
			# Remove the key from the _lookup
			del self._lookup[stale_node.key]


	def get(self, key):
		# If key does not exist, don't do anything
		if key not in self._lookup: return 

		# Key exist, need to refresh to be recently used
		current_node = self._lookup[key]
		self._data.remove(current_node)
		self._data.append(current_node)
		return current_node.value


	def __repr__(self):
		return self._data.__repr__()
