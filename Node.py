class Node:
	"""
	Node with two pointers.
	"""
	def __init__(self, key, value, next=None, prev=None):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None
