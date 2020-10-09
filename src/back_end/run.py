#####################
# File presentation #
#####################

# Imports of external libraries
from bottle import Bottle, run

# Imports of internal libraries
import argparse
import logging
import logging.config
import coloredlogs
import yaml

# Imports of application files
import configurations.server_config as server_config

# Setting Logger 
with open('configurations/loggers_config.yaml', 'r') as f:
	log_config = yaml.safe_load(f.read())
	logging.config.dictConfig(log_config)
logger = logging.getLogger("AppLogger." + __name__)
field_styles = dict(
					asctime={'color': 'green'},
					hostname={'color': 'magenta'},
					levelname={'bold': True, 'color': 'cyan'},
					name={'color': 'blue'},
					programname={'color': 'cyan'},
					username={'color': 'yellow'}
)
coloredlogs.install(level='DEBUG', logger=logger, field_styles=field_styles)


def parse_arguments():
	"""Parse the command line arguments provided to `python3 run.py`."""

	parser = argparse.ArgumentParser(description="Run the API Text Mining Perfect Memory.")
	# Host interface
	parser.add_argument(
						"-H", "--host",
						required=False,
						type=str,
						default=server_config.DEFAULT_HOST,
						dest="host",
						help="The targeted host interface. 0.0.0.0 will listen on all interfaces."
	)
	# Listening port
	parser.add_argument(
						"-p", "--port",
						required=False,
						type=int,
						default=server_config.DEFAULT_PORT,
						dest="port",
						help="The listening port.")
	return parser.parse_args()


def start_app(arguments):
	""" Start server with proper configuration and routes. """

	# LOG Starting server
	logger.info("Starting the Bottle server.")

	app = Bottle()
	server_config.setup(app)
	run(app, host=arguments.host, port=arguments.port)
	logger.info("Bottle server started.")


if __name__ == "__main__":
	args = parse_arguments()
	start_app(args)
