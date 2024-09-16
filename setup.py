from setuptools import setup # type: ignore

setup(
    name='python-ddd-estructure-example',
    version='0.1',
    entry_points={
        'console_scripts': [
            'start=app.main:main_function',
        ],
    },
)
