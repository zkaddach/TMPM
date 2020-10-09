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
This API can run in docker or on any UNIX operating system. Choose your prefered method of installation.

### Docker Images from Github Packages

1. To get the docker image from Github packages run `docker pull docker.pkg.github.com/zkaddach/tmpm/tmpm_backend:0.0.1` to pull the image.
2. To start TMPM Back End,
    * Run `docker run -p 8888:8888 docker.pkg.github.com/zkaddach/tmpm/tmpm_backend:0.0.1`
### Docker

1. Clone this repo from Github into your install folder, then run `docker build -t tmpm:back_end .` to build the image.
2. To start TMPM Back End,
    * Run `docker run -d -p 8888:8888 --rm tmpm:back_end`

### Non-Docker install 

#### UNIX, with a python 3 installation 

1. Clone this repo from Github into your install folder, go into `src/back_end`, and from a python 3 installation, run `pip3 install -r requirements.txt` to install the dependencies.
2. To start TMPM, run `python3 run.py --port 8888`. This process will run in the console. This allows you to use the run.py command line arguments (`--port` and `--host`).


## Configuration


## Running

### Port

Default port is 8888. You can change it if you wish, for example to expose it on port 8889:

* `docker run -d -p 8889:8888 --rm tmpm:back_end`
* `python3 run.py --port 8889`

### Console and Logging

The logging is made up of 2 components : the Bottle logging and the EMMA logging.

* The console outputs both
* The TMPM logs are available (by default) in `logs/app.log` (and are rotated).
* For docker we suggest you set the `logs/` folder as a persistent storage

### Database


### Environment


### Installing the Front End
