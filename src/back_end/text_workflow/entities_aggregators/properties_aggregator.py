
# Imports of application files
from text_workflow.entity import Person


class PropertiesAggregator:
	""" Properties Aggregator class : Grouping entities per properties methods."""

	@staticmethod
	def get_persons(entities_list):
		"""Return a list of Person objects."""

		# List is empty
		if not bool(entities_list):
			return None
		# Getting Persons
		persons = []
		for entity in entities_list:
			if isinstance(entity, Person):
				persons.append(entity)
		return persons

	@staticmethod
	def get_common_tree(entities_list):
		"""Return a 'tree' grouping entities per property values.
		ARGUMENT:
			* entities_list : array of entities
		"""

		prop_list = set()
		tree = {}

		# Get all properties
		for entity in entities_list:
			for key in entity.properties.keys():
				prop_list.add(key)

		for key in prop_list:
			tree[key] = {}
			for entity in entities_list:
				try:
					if not str(entity.properties[key]) in tree[key]:
						tree[key][str(entity.properties[key])] = []
					tree[key][str(entity.properties[key])].append((entity.label, entity))
				except KeyError:
					pass
		return tree
