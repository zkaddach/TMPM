# Imports of external libraries
from bottle import abort
import requests

# Import internal libraries

# Imports of application files
from configurations.text_workflow_config import DefaultTextWorkflowConfig as workflow_config
from text_workflow.entity import create_entity


class TextRazorAPI:
	def __init__(self, text, params):
		"""Constructor of the TextRazorAPI class.
		ARGUMENTS
			* text: str of the text to be analyzed
			* params: dict of different parameters regarding the request to the API.
				{
					extractors: EXTRACTORS,
				}
		"""

		self.req_data = {
			"apiKey": workflow_config.TEXT_RAZOR_API_KEY,
			"text": text,
			"extractors": params["extractors"]
		}

	def extract(self):
		"""Extract entities from the text using the TextRazorAPI.
		OUTPUT:
			* entities: list of objects Entity
		"""

		# Sending request to TextRazorAPI
		try:
			print(self.req_data)
			req = requests.post(
				workflow_config.TEXT_RAZOR_API_ENDPOINT,
				data=self.req_data
			).json()
		except ValueError as e:
			return abort(
				requests.codes.SERVICE_UNAVAILABLE,
				"Sorry an error occurred on request to TextRazorAPI  : {0}".format(e)
			)
		except requests.ConnectionError as e:
			return abort(
				requests.codes.SERVICE_UNAVAILABLE,
				"Sorry impossible to connect to TextRazorAPI : {0}".format(e)
			)
		# Testing response from TextRazorAPI and the text analysis
		try:
			if req['ok'] is not True:
				raise ValueError(req['error'])
		except ValueError as e:
			return abort(
				requests.codes.SERVICE_UNAVAILABLE,
				"Sorry TextRazorAPI was not able to analyze the text : {0}".format(e)
			)

		# Storing the response of the API
		response = req['response']

		# Creating entities and returning them as a list
		entities = []
		for entity in response['entities']:
			entities.append(create_entity(entity['type']))
			entities[-1].set_text_razor_properties(entity)

		return entities
