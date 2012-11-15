from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.registry.settings['jinja2'] = {
        'block_start_string': '[%',
        'block_end_string': '%]',
        'variable_start_string': '[[',
        'variable_end_string': ']]'
    }
    config.include('pyramid_jinja2')
    print config.get_jinja2_environment()
    config.include('myproject.fainit')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('todo', '/todo')
    config.scan()
    return config.make_wsgi_app()

