myproject README
==================

Getting Started
---------------

% curl -s https://raw.github.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL
% source ~/.venvburrito/startup.sh
% mkvirtualenv pyramid
Automatically does this: % cd <directory containing this file>
Don't need to do this:  % python setup.py develop
% pip install -r requirements.txt
% initialize_myproject_db development.ini
% pserve development.ini
% go to http://localhost:6543/todo
% go to http://localhost:6543/admin

