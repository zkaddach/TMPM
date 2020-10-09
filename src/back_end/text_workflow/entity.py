# Import from external library

# Import internal library
from datetime import datetime
import logging

# Imports of application files
from configurations.text_workflow_config import DefaultTextWorkflowConfig as workflow_config

logger = logging.getLogger("AppLogger." + __name__)


def create_entity(entity_types=None):
	"""Return the object of the Entity depending its type.
	ARGUMENTS:
		* entity_types: array of the types (or str for single value) of the entity.
	"""

	entity_types = [entity_types] if isinstance(entity_types, str) else entity_types
	if isinstance(entity_types, list):
		# Entity is a person
		if "Person" in entity_types:
			return Person()
		# No particular knowledge on the type of the entity.
		else:
			return Entity()
	# If 'type' is not an array or string
	else:
		return Entity()


class Entity:
	"""Data model / representation of an entity. """

	def __init__(self):
		"""Constructor of the Entity object. """

		self.label = "Unknown"
		self.description = "Unknown"
		self.text_razor_properties = None
		self.wikidata_id = None
		self.properties = {}

	def set_text_razor_properties(self, properties):
		"""Setter of the text_razor_properties attribute. """

		self.text_razor_properties = properties

		# Setting label
		try:
			self.label = properties['entityId']
		except KeyError as e:
			self.label = "Unknown"

		# Setting Wikidata ID
		try:
			self.wikidata_id = properties['wikidataId']
		except KeyError as e:
			self.wikidata_id = None

	def set_wikidata(self, wikidata, client):
		"""
		ARGUMENTS:
			* wikidata :
			* client :
		"""

		# Setting label
		try:
			self.label = wikidata.label
		except AttributeError as e:
			pass

		# Setting description
		try:
			self.description = wikidata.description
		except AttributeError as e:
			pass

		# Setting all properties found in the wikidata using WIKIDATA_CODES
		for prop_name, prop_code in workflow_config.WIKIDATA_CODES.items():
			prop = client.get(prop_code)
			try:
				self.properties[prop_name] = wikidata[prop]
				if hasattr(self.properties[prop_name], 'label'):
					self.properties[prop_name] = self.properties[prop_name].label
			except KeyError as e:
				logger.debug("Can't find property {0} : {1}".format(prop_name, e))
			except ValueError as e:
				logger.debug("Can't find property {0} : {1}".format(prop_name, e))

	def __eq__(self, other):
		"""Surcharge of the equal operator. """

		# Checking if other is an Entity
		if not isinstance(other, Entity):
			return False

		# Checking Label and description
		if not self.label == other.label and self.description == other.description:
			return False

		try:
			# Checking text_razor properties
			if self.text_razor_properties is not None and other.text_razor_properties is not None:
				for each in self.text_razor_properties:
					if not (self.text_razor_properties[each] == other.text_razor_properties[each]):
						return False

			# Checking properties
			if bool(self.properties) and bool(other.properties):
				for each in self.properties:
					if not (self.properties[each] == other.properties[each]):
						return False
		# Different keys in properties or text_razor_properties
		except KeyError:
			return False

		return True


class Person(Entity):
	"""Entity which is identified as a person. """

	def __init__(self):
		"""Constructor of a Person object."""

		Entity.__init__(self)

	def set_wikidata(self, wikidata, client):
		"""
		ARGUMENTS:
			* wikidata :
			* client :
		"""

		super().set_wikidata(wikidata, client)
		if 'birth_date' in self.properties:
			self.properties['age'] = datetime.today().date().year - self.properties['birth_date'].year
		else:
			logger.info("Person {0}, birth date is not known".format(self.label))
