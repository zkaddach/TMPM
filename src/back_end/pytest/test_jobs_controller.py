# Imports of internal libraries
import unittest 

class JobsControllerTest(unittest.TestCase):

	""" Test case for testing the 'random' module. """

	def setUp(self):
		""" Initialize the tests. 
			Called before each test method. 
		"""

		pass

	def tearDown(self):
		""" Called after each test method. """

		pass

	def test_sample(self):
		""" Method for testing the 'random.sample' function. """

		sample = random.sample(self.listOfValues, 5)
		for each in sample: 
			self.assertIn(each, self.listOfValues)

		with self.assertRaises(ValueError):
			random.sample(self.listOfValues, 11)