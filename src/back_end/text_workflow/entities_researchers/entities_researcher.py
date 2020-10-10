# Import of internal libraries
from abc import abstractmethod, ABCMeta


class EntitiesResearcher(metaclass=ABCMeta):

	@abstractmethod
	def collect(self, entity):
		"""Collecting information of a given entity object.
		ARGUMENTS:
			* entity: Entity Object
		"""

		pass
