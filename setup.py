from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.0'
DESCRIPTION = '...'
PACKAGE_NAME = 'fakedata'
AUTHOR = 'Jose Angel Colin Najera'
EMAIL = 'josecolin99@gmail.com'
GITHUB_URL = 'https://github.com/Josecolin99/...'

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points={
        "console_scripts":
            ["nombre del comando=nombre del paquete.__main__:main"]
    },
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'FakeData',
        'Fake Data',
        'fakedata',
        'faked ata',
        'Data',
        'data'
    ],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)