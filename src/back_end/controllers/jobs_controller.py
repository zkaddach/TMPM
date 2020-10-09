# Imports of external libraries
from bottle import request, abort
from requests import codes as http
import jsonschema

# Imports of internal libraries
import json
import logging
import concurrent.futures

# Imports of application files
from models.text_job import TextJob

logger = logging.getLogger("AppLogger." + __name__)


class JobsController:
	"""
		Thread to handle user requests to start a Job. 
	"""

	with open(
			"./controllers/json_schemas/add_job.json",
			"r"
	) as json_file:
		ADD_SCHEMA = json.load(json_file)

	@staticmethod
	def add_text_workflow_job():

		# LOG New text job
		logger.info("User launched new text workflow job.")

		req = request.json

		# Make sure JSON data is valid 
		try:
			jsonschema.validate(req, JobsController.ADD_SCHEMA)
		except Exception as e:
			return abort(http.BAD_REQUEST, "Invalid parameters : {0}".format(e))

		with concurrent.futures.ThreadPoolExecutor() as executor:
			try:
				# Converting text from list to str
				if isinstance(req["text"], list):
					req["text"] = " ".join(req["text"])
				return executor.submit(TextJob(req["text"]).execute_workflow).result()
			except TimeoutError as e:
				return abort(http.REQUEST_TIMEOUT, "Sorry your request was too long to process Timeout : {0}".format(e))
