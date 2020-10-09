# TMPM Text mining for Perfect Memory 

TMPM allows you to perform text analysis. 

With TMPM you will be able to : 
* Extract entities detected with your text (for now through Text Razor API).
* Collect information for each person detected within the entities of the text.
* Retrieve common properties between persons. 

## Documentation

The general documentation of the project has not been generated yet. 
Nevertheless we provide a log board containing explanation regarding the architecture of this API in the Management folder.  

## Getting Started
tsstfffssss
This API can run in docker or on any UNIX operating system. Choose your prefered method of installation.


### Docker

1. Clone this repo from Github into your install folder, then run `docker build -t tmpm:back_end .` to build the image.
2. To start TMPM Back End,
    * Run `docker run -d -p 8888:8888 --rm tmpm:back_end`

### Non-Docker install 

#### UNIX, with a python 3 installation 

1. Clone this repo from Github into your install folder, go into `src/back_end`, and from a python 3 installation, run `pip3 install -r requirements.txt` to install the dependencies.
2. To start TMPM, run `python3 run.py --port 8888`. This process will run in the console. This allows you to use the run.py command line arguments (`--port` and `--host`).

### Docker Images on the Github Packages

To be able to deploy EMMA in ACS, we want to upload the major versions of EMMA on the [Artifactory](https://repository.rnd.amadeus.net). Look for `EMMA` on the Artifactory once it is published (check the upload date for the more recent packages). We do not know yet how to manage configuration and running arguments.

## Configuration



## Running

### Port

Default port is 8888. You can change it if you wish, for example to expose it on port 8889:

* `docker run -d -p 8889:8888 --rm emma:back_end`
* `python3 run.py --port 8889`

### Console and Logging

The logging is made up of 2 components : the Bottle logging and the EMMA logging.

* The console outputs both
* The TMPM logs are available (by default) in `logs/app.log` (and are rotated).
* For docker we suggest you set the `logs/` folder as a persistent storage

### Database

EMMA is compatible with SQLite. Therefore, the database is stored on disk (by default in `data/emma.db`)

* For docker we suggest you set the `data` folder as a persistent storage
* If you need compatibility with a database server, see `app/models/database.py` to add compatibility for your technology (for ex MySQL).

### Environment

EMMA Back end supports 2 running environments : `prod`, `test` and `dev`

* `prod`: This is the default mode
* `test`: This enables the Bottle debug mode, making Bottle more verbose.
* `dev`: This enables the Bottle debug mode and allows the Bottle engine to reload at each file change. Beware however that Bottle launches a 2nd thread of itself, and the 1st one will still be running without being reloaded. This causes EMMA to run twice, so twice the same log lines,etc (need to rewrite the run.py to fix). To run in `dev` (or `test`) enviroment:

  * `python run.py --environment dev`
  * `sh ./start.sh -e dev`
  * Specifying the environment in docker is not yet compatible, but you can add it easily (add an ENTRYPOINT in the Dockerfile, and add a command line option with `docker run`).



### Installing the Front End

Once you have installed the back end you can move on to install the front end. For that you will need the backend's address (to allow the front end to target the back end API).\
When you start running the back end in docker or locally, you will see :

    Bottle v0.12.17 server starting up (using WSGIRefServer())...
    Listening on http://0.0.0.0:8888/
    Hit Ctrl-C to quit.

In this example, the address you need to provide in the front end configuration is `http://my.machine.amadeus.com:8888/`

In case you're launching EMMA on a VM without console logging, you can check your machine's full address with `echo http://$(hostname -f):8888`. Change the `8888` port in the previous instruction if you have chosen to use another port.
