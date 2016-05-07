from setuptools import setup, find_packages
import codecs
import os
import re
import sys
 
here = os.path.abspath(os.path.dirname(__file__))
 
with open("build_requires.txt") as file:
    install_requires = [dep.strip() for dep in file.readlines()]
 
with open("tests_require.txt") as file:
    tests_require = [dep.strip() for dep in file.readlines()]
 
 
setup(
    name='OpenCAD',
    description='CAD software that provides power tools and automation for engineers and alike.'
    version='0.0.1',
    long_description=(
        "This is a prototype for OpenCAD, an open source software for computer aided "
        "drafting (CAD) along with providing powerful tools and automation for engineers, "
        "architects and alike. OpenCAD's philosophy is to reduce mundane tasks in pumping "
        "out a massive plan-set with one hell of a deadline, by letting the drafter do "
        "simple drafting once again. OpenCAD feels as simple as pen on paper with a scale "
        "while providing a considerable amount of complexity and automation and the users "
        "direction. "
        )
    url='https://github.com/spasztor/OpenCAD',
    author='Szabolcs Pasztor',
    author_email='szabolcs1992@gmail.com',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Business Information',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='OpenCAD, CAD',
    packages=find_packages(exclude=[]),
    py_modules=[],
    install_requires=install_requires,
    tests_require=tests_require,
    package_data={},
    entry_points={
        'console_scripts': [
            'project=project.main:main',
        ],
    },
)
