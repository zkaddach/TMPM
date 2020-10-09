
##############################################################################
#                       ENTITY EXTRACTION
##############################################################################

class DefaultTextWorkflowConfig:

	WORKFLOW_STATUS = [
		"Initialization of the workflow...",
		"Extracting entities...",
		"Collecting data for entities...",
		"Aggregating entities...",
		"Workflow completed. Done."
	]

	EXTRACTION_PARAMETERS = {
			"extractors": "entities",
	}
	ENTITIES_EXTRACTOR = "TextRazorAPI"
	TEXT_RAZOR_API_KEY = "5d0f7bdc557d2195cfc7290b5b54a676d99bf1212d0428c187cc84c7"
	TEXT_RAZOR_API_ENDPOINT = "https://api.textrazor.com/"

	ENTITIES_RESEARCHER = "WikidataAPI"
	WIKIDATA_CODES = {
		'gender': "P21",
		'birth_date': "P569",
		'image': "P18",
		'birth_place': "P19",
		'death_date': "P570",
		'educated_at': "P69",
		'family_name': "P734",
		'given_name': "P735",
		'occupation': "P106",
		'field_of_work': "P101",
		'position_held': "P39",
		'citizenship': "P27",
		'child': "P40",
		'spouse': "P26",
		'marriage_place': "P2842",
		'ethnic_group': "P172"
	}
