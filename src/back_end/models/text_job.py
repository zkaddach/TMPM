# Import external libraries
import requests
from bottle import abort

# Import internal libraries
from datetime import datetime
import logging
from pprint import pprint

# Imports of application files
from configurations.text_workflow_config import DefaultTextWorkflowConfig as Config
from text_workflow.entities_extractors import ENTITIES_EXTRACTOR_BUILDER
from text_workflow.entities_researchers import ENTITIES_RESEARCHER_BUILDER
from text_workflow.entities_aggregators import PropertiesAggregator

logger = logging.getLogger("AppLogger." + __name__)
logger.setLevel(logging.INFO)


class TextJob:

	def __init__(self, text, user_id=None, config=Config):
		""" Constructor of TextJob class. """

		# Configurable attributes
		self.extraction_parameters = {
			"extractors": "entities",
		}
		self.text = text
		self.user = user_id
		self.config = config

		# Generated job information attributes
		self.starting_time = datetime.now()
		self._status = None

		# Computed attributes of interest
		self.entities = []

	def execute_workflow(self):
		""" Executing the text workflow according to TextJob Configuration """

		self.status = self.config.WORKFLOW_STATUS[0]

		# Entities extraction
		self.status = self.config.WORKFLOW_STATUS[1]
		try:
			self.entities = ENTITIES_EXTRACTOR_BUILDER[
				self.config.ENTITIES_EXTRACTOR
			](
				self.text,
				self.extraction_parameters
			).extract()
		except KeyError as e:
			return abort(
				requests.codes.BAD_REQUEST,
				"Error can't find the correct parameters or response from TextRazorAPI : {0}".format(e)
			)

		# Search information on entities and collect them
		self.status = self.config.WORKFLOW_STATUS[2]
		for entity in self.entities:
			try:
				ENTITIES_RESEARCHER_BUILDER[self.config.ENTITIES_RESEARCHER]().collect(entity)
			except Exception as e:
				return abort(
					requests.codes.BAD_REQUEST,
					"Error can't find the correct parameters or response from WikidataAPI : {0}".format(e)
				)

		# Aggregating entities
		persons = PropertiesAggregator.get_persons(self.entities)
		common_tree = PropertiesAggregator.get_common_tree(persons)

		print("###############################################\n\n")
		pprint(common_tree)

		# Completing the workflow and returning results
		self.status = self.config.WORKFLOW_STATUS[3]
		r = "\n\n------------------------------------------------------\n"
		r += "Successfully collected information for entities:\n"
		r += "------------------------------------------------------\n\n"
		return r

	@property
	def status(self):
		"""Getter of the status attribute."""

		return self._status

	@status.setter
	def status(self, new_status):
		"""Setter of the status attribute. """

		self._status = new_status
		logger.info(self.status)
