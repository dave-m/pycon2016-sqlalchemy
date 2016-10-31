from setuptools import setup, find_packages

package = 'pycon2016-sqlalchemy'
version = '0.1'

def _get_readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name=package,
    version=version,
    description=_get_readme(),
    url='',
    author="David Mcilwee",
    author_email="david@mcilwee.me",
    packages=find_packages(''),
    install_requires=[
        'sqlalchemy',
        'jupyter'
    ]
)
