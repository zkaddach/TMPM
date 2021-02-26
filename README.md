# TMPM Text mining for Perfect Memory 
TMPM allows you to perform text analysis. 

With TMPM you will be able to : 
* Extract entities detected with your text (for now through Text Razor API).
* Collect information for each person detected within the entities of the text.
* Retrieve common properties between persons. 

## collapsible markdown?

<details><summary>CLICK ME</summary>
<p>

#### yes, even hidden code blocks!

```python
print("hello world!")
```

</p>
</details>

## Documentation
The general documentation of the project has not been generated yet. 
Nevertheless we provide a log board containing explanation regarding the architecture of this API in the Management folder.  

## Getting Started
This API can run in docker or on any UNIX operating system. Choose your prefered method of installation.

### Docker Images from Github Packages

1. To get the docker image from Github packages run `docker pull docker.pkg.github.com/zkaddach/tmpm/tmpm_backend:0.0.1` to pull the image.
2. To start TMPM Back End,
    * Run `docker run -p 8888:8888 docker.pkg.github.com/zkaddach/tmpm/tmpm_backend:1.0.0`

### Docker
1. Clone this repo from Github into your install folder, then run `docker build -t tmpm:back_end .` to build the image.
2. To start TMPM Back End,
    * Run `docker run -d -p 8888:8888 --rm tmpm:back_end`

### Non-Docker install 

#### UNIX, with a python 3 installation 
1. Clone this repo from Github into your install folder, go into `src/back_end`, and from a python 3 installation, run `pip3 install -r requirements.txt` to install the dependencies.
2. To start TMPM, run `python3 run.py --port 8888`. This process will run in the console. This allows you to use the run.py command line arguments (`--port` and `--host`).

## Running
Now that you have set up the API, and it is correctly running you can execute requests using the POST method. 
you can do so with **curl** for example. 
`curl -d @pytest/json_schemas/simple_request.json -H 'Content-Type: application/json' 0.0.0.0:8888/text_workflow`
Where *pytest/json_schemas/simple_request.json* is the JSON file containing the request and follows this schema: 

```json
{
  "text":
    [ "Jean Dujardin is the president of France. ",
      "Pharrell Williams is an awesome musician from America.",
      "Raphael Nadal is the winner of the Rolland Garros 2020"
    ]
}
```

Note that the *text* key can be an array (like the example) or a single text. 
You can save the output in a JSON file as follows : 
`curl -d @pytest/json_schemas/simple_request.json -H 'Content-Type: application/json' 0.0.0.0:8888/text_workflow -o output.json`

The output will also be a JSON object following the format: 
```json
{
  "persons": [
        {
            "label": "Pharrell Williams",
            "description": "American singer, rapper, songwriter, record producer, fashion designer, and entrepreneur",
            "wikidataId": "Q14313",
            "id": "1",
            "type": "['MusicalArtist', 'Agent', 'Person', 'Artist']",
            "entityId": "Pharrell Williams",
            "wikiLink": "http://en.wikipedia.org/wiki/Pharrell_Williams",
            "matchedText": "Pharrell Williams",
            "entityEnglishId": "Pharrell Williams",
            "gender": "male",
            "birth_date": "1973-04-05",
            "birth_place": "Virginia Beach",
            "educated_at": "Northwestern University",
            "family_name": "Williams",
            "given_name": "Pharrell",
            "occupation": "singer",
            "citizenship": "United States of America",
            "spouse": "Helen Lasichanh",
            "ethnic_group": "African Americans",
            "age": "47"
        }
  ],
  "common_properties": {
        "occupation": {
            "singer": [
                "Pharrell Williams"
            ],
            "film actor": [
                "Jean Dujardin"
            ]
        },
        "spouse": {
            "Helen Lasichanh": [
                "Pharrell Williams"
            ],
            "Nathalie P\u00e9chalat": [
                "Jean Dujardin"
            ]
        },
        "ethnic_group": {
            "African Americans": [
                "Pharrell Williams"
            ]
        },
        "educated_at": {
            "Northwestern University": [
                "Pharrell Williams"
            ]
        },
        "birth_place": {
            "Virginia Beach": [
                "Pharrell Williams"
            ],
            "Rueil-Malmaison": [
                "Jean Dujardin"
            ]
        },
        "birth_date": {
            "1973-04-05": [
                "Pharrell Williams"
            ],
            "1972-06-19": [
                "Jean Dujardin"
            ]
        },
        "family_name": {
            "Williams": [
                "Pharrell Williams"
            ],
            "Dujardin": [
                "Jean Dujardin"
            ]
        },
        "gender": {
            "male": [
                "Pharrell Williams",
                "Jean Dujardin"
            ]
        },
        "given_name": {
            "Pharrell": [
                "Pharrell Williams"
            ],
            "Jean": [
                "Jean Dujardin"
            ]
        },
        "citizenship": {
            "United States of America": [
                "Pharrell Williams"
            ],
            "France": [
                "Jean Dujardin"
            ]
        },
        "age": {
            "47": [
                "Pharrell Williams"
            ],
            "48": [
                "Jean Dujardin"
            ]
        }
    }
}
```

## Configuration
For now here are the configurations possible : 
* you can change the default host and port values for the server as long as the route endpoint. 
* You can change the properties used to collect data from wikidata for each entity. You can also manage the API keys and define other entity extractors and researchers.
* You can change the logs format. 

### Port
Default port is 8888. You can change it if you wish, for example to expose it on port 8889:

* `docker run -d -p 8889:8888 --rm tmpm:back_end`
* `python3 run.py --port 8889`

### Console and Logging

The logging is made up of 2 components : the Bottle logging and the EMMA logging.

* The console outputs both
* The TMPM logs are available (by default) in `logs/app.log` (and are rotated).
* For docker we suggest you set the `logs/` folder as a persistent storage



### Environment
This section will be completed when we will implement different configuration 
environments for example for the development, testing and production. 

### Installing the Front End
For now we didn't complete the development of the Front end. 
