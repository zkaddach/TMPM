# Import internal libraries
from abc import abstractmethod, ABCMeta


class EntitiesExtractor(metaclass=ABCMeta):

	@abstractmethod
	def extract(self):
		"""Extract entities from the given text.
		OUTPUT:
			* entities: list of objects Entity
		"""

		pass
