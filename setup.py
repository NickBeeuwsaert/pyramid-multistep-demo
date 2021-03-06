from setuptools import setup, find_packages

setup(
    name='pyramid_multistep',
    version='0.0.0',
    author='Nick Beeuwsaert',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pyramid',
        'pyramid-beaker',
        'pyramid-jinja2',
        'WTForms'
    ],
    extras_require={
        'dev': [
            'pyramid-debugtoolbar'
        ]
    },
    entry_points={
        'paste.app_factory': [
            'main = pyramid_multistep:main'
        ]
    }
)
