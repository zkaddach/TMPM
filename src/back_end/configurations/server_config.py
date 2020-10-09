from controllers.jobs_controller import JobsController

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8888


def setup(app):
	""" Setting up routes of the server. """

	app.route("/text_workflow", method="POST", callback=JobsController.add_text_workflow_job)