Pyramid To Do MVC Platform README
=================================

This repo provides a playground for Pyramid development by allowing implementing the TODOMVC frameworks.

Currently it uses the non framework pure javascript one.

The Pyramid Environment has been "pip freeze"d with the following inclusions and configurations to sortof mirror what Django provides out of the box:
* SQLalchemy - allowing an ORM
* formalchemy - for an admin tool
* jinja2 - for templates though this right now will have a major conflict with the other client side rendering templates.  We'll need to look at the best way to handle client versus server side templates in this project.
* There is no user authentication like the Django admin stuff.


Get your virtual environment rocking with Virtualenv Burrito:

	% curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
	% source ~/.venvburrito/startup.sh

Create a new virtual environment:

	% mkvirtualenv pyramid

Be in this directory and:

	% pip install -r requirements.txt
	% initialize_myproject_db development.ini

Serve the project:
 
	% pserve development.ini --reload

Try It Out!
-----------

* Navigate to http://localhost:6543/todo
* Navigate to http://localhost:6543/admin

