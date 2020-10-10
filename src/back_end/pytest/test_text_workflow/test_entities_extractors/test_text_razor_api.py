# Import from internal library
import unittest

# Import from application
from text_workflow.entities_extractors.text_razor_api import TextRazorAPI
from text_workflow.entity import Entity


class TextRazorAPITest(unittest.TestCase):

	def test_extract_output_type(self):
		"""Testing if the response type of the extract method is valid."""

		# Test if the output is a list of entities with request containing entites
		text = "Rafael Nadal and Stan Wawrinka as long as Roger Federer are tennis players."
		params = {"extractors": ["entities"]}

		result = TextRazorAPI(text, params).extract()
		self.assertIsInstance(result, list)
		if result:
			for each in result:
				self.assertIsInstance(each, Entity)


if __name__ == '__main__':
	unittest.main()
