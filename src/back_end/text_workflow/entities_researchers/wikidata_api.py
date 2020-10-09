# Import of internal libraries
import logging

# Imports of external libraries

from bottle import abort
import requests
from wikidata.client import Client

logger = logging.getLogger("AppLogger." + __name__)
logger.setLevel(logging.INFO)


class WikidataAPI:

	def collect(self, entity):
		"""Collecting information of entity from WikidataAPI
		ARGUMENTS:
			* entity: Entity Object
		"""

		entity_data = None
		client = None

		# Get entity wikidata from wikidata
		try:
			client = Client()  # doctest: +SKIP
			if hasattr(entity, 'wikidata_id') and entity.wikidata_id is not None:
				entity_data = client.get(entity.wikidata_id, load=True)
			else:
				logger.info("Entity {0} has no attribute wikidata_id.".format(entity.label))
		# Error with client value
		except ValueError as e:
			return abort(
				requests.codes.SERVICE_UNAVAILABLE,
				"Sorry the WikidataAPI is not responding : {0}".format(e)
			)
		# Error with request
		except requests.HTTPError as e:
			logger.info("Entity {0} has no valid wikidataId: {1}".format(entity.label, e))
		# Error with connection
		except requests.ConnectionError as e:
			return abort(
				requests.codes.SERVICE_UNAVAILABLE,
				"Sorry impossible to connect to WikidataAPI : {0}".format(e)
			)

		# Updating the Entity with the new collected data
		if entity_data is not None:
			entity.set_wikidata(entity_data, client)

		return "Nothing to return"
