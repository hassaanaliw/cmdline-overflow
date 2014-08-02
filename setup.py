from setuptools import setup
import os

VERSION = '1.2.0'


setup(
    author='Hassaan Ali Wattoo',
    author_email='hassaanaliw@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 2.7',

    ],
    description='Get the latest topics for each topic and category of StackOverflow',
    entry_points={
        'console_scripts': 'overflow=overflow:parser',
    },
    long_description=(
        open('README.rst').read() + '\n' +
        open(os.path.join('docs', 'HISTORY.txt')).read() + '\n' +
        open(os.path.join('docs', 'CONTRIBUTORS.txt')).read()
    ),
    include_package_data=True,
    keywords='analytics python scraping statistics',
    license='GPL',

    name='overflow',
    py_modules=[
        'overflow',
    ],

    url='https://github.com/hassaanaliw/cmdline-overflow',
    version=VERSION,
    zip_safe=True,
)
