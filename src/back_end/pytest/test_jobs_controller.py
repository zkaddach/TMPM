# Imports of external libraries
import requests
from boddle import boddle
import jsonschema

# Imports of internal libraries
import unittest 
import json

# Import application files
from controllers.jobs_controller import JobsController

class JobsControllerTest(unittest.TestCase):

	""" Test case for testing the 'JobsController' class. """

	with open(
			"./pytest/json_schemas/validate_response.json",
			"r"
	) as json_file:
		RESPONSE_SCHEMA = json.load(json_file)

	def setUp(self):
		""" Initialize the tests. 
			Called before each test method. 
		"""

		pass

	def tearDown(self):
		""" Called after each test method. """

		pass

	def test_add_text_workflow_job(self):
		""" Method for testing the 'JobsController.add_text_workflow_job' function. """

		# Testing with valid request (valid parameters)
		with open("./pytest/json_schemas/simple_request.json", 'r') as f:
			valid_parameters = json.load(f)
		with boddle(json=valid_parameters):
			result = JobsController.add_text_workflow_job()
			# Test type of the response (should be string)
			self.assertEqual(type(result), str)
			# Test JSON schema of the response
			self.assertEqual(jsonschema.validate(json.loads(result), JobsControllerTest.RESPONSE_SCHEMA), None)


