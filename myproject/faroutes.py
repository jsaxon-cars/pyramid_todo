from myproject import models
import logging

log = logging.getLogger(__name__)


def includeme(config):
    settings = config.registry.settings.get('myproject.fa_settings}}', {})

    # Example to add a specific model
    config.formalchemy_model("/todo", package='myproject',
                             model='myproject.models.ToDo')
                             **settings)

    log.info('myproject.faroutes loaded')
