myproject README
==================

Getting Started
---------------

Get your virtual environment rocking with Virtualenv Burrito:

% curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
% source ~/.venvburrito/startup.sh

Create a new virtual environment:
% mkvirtualenv pyramid

Be in this directory and:
% pip install -r requirements.txt
% initialize_myproject_db development.ini

Serve the project:
% pserve development.ini

Navigate to http://localhost:6543/todo
Navigate to http://localhost:6543/admin

