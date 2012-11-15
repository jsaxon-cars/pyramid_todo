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
    jinja_settings = {
        'block_start_string': '[%',
        'block_end_string': '%]',
        'variable_start_string': '[[',
        'variable_end_string': ']]'
    }
    config.registry.settings['jinja2'] = jinja_settings
    config.include('pyramid_jinja2')
    config.include('myproject.fainit')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('todo', '/todo')
    config.scan()
    import pdb; pdb.set_trace()
    return config.make_wsgi_app()

