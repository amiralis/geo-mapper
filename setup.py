from setuptools import setup

import geomap


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='geomap',
      version=geomap.__version__,
      description='Generate a map of geolocations',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Visualization',
      ],
      url='https://github.com/amiralis/geo-mapper',
      author='Amirali Sanatinia',
      author_email='amirali@ccs.neu.edu',
      license='Apache 2',
      packages=['geomap'],
      scripts=['bin/geo-map'],
      install_requires=[
          'basemap',
          'matplotlib'
      ],
      include_package_data=True)

