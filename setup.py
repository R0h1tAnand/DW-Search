# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='dw-search',
    version="1.3",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    author="R0h1tAnand",
    install_requires=["requests","argparse","termcolor","tqdm", "html5lib","bs4","PySocks"],
    description="DW-Search is a script that scrapes urls on different .onion search engines.",
    include_package_data=True,
    url='https://github.com/R0h1tAnand/DW-Search',
    entry_points = {'console_scripts': ['dw-search = dw_search.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
