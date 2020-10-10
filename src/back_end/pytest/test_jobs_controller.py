# Imports of external libraries
import requests
from boddle import boddle

# Imports of internal libraries
import unittest 
import json

# Import application files
from controllers.jobs_controller import JobsController

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

	def test_correct_input_output(self):
		""" Method for testing the 'random.sample' function. """

		with open("pytest/curl_request.json", 'r') as f:
			parameters = json.load(f)
		with boddle(json=parameters):
			result = JobsController.add_text_workflow_job()
			self.assertEqual(type(result), str)
