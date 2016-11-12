from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(
        settings=settings
    )

    config.add_static_view(
        name='static',
        path='pyramid_multistep:static'
    )

    config.include(
        'pyramid_multistep.views.default',
        route_prefix='/'
    )

    return config.make_wsgi_app()
