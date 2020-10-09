# File presentation 
import unittest 
import random 

class RandomTest(unittest.TestCase):

	""" Test case for testing the 'random' module. """

	def setUp(self):
		""" Initialize the tests. 
			Called before each test method. 
		"""

		self.listOfValues = list(range(10))

	def tearDown(self):
		""" Called after each test method. """

		pass

	def test_choice(self):
		""" Method for testing the 'random.choice' function. 
			Tests if the choosed value is in the original list. 
		"""
		
		choice = random.choice(self.listOfValues)
		self.assertIn(choice, self.listOfValues)

	def test_shuffle(self):
		""" Method for testing the 'random.shuffle' function. """

		random.shuffle(self.listOfValues)
		self.listOfValues.sort()
		self.assertEqual(self.listOfValues, list(range(10)))

	def test_sample(self):
		""" Method for testing the 'random.sample' function. """

		sample = random.sample(self.listOfValues, 5)
		for each in sample: 
			self.assertIn(each, self.listOfValues)

		with self.assertRaises(ValueError):
			random.sample(self.listOfValues, 11)