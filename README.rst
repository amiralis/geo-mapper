Geo Mapper
==========

Generate a map of geolocations

.. image:: https://github.com/amiralis/geo-mapper/blob/master/include/map.png


Example
-------

To use as a library. ::

    >>> import geomap
    >>> m = geomap.Map(args.projection)
    >>> lon =[37.7833, ...]
    >>> lat = [-122.4167, ...]
    >>> m.add_coordinates(lon, lat)
    # to show the map
    >>> m.generate_map()
    # to save to a file
    >>> m.generate_map(output='map.png')

To use as a standalone program. ::

    # to show the map
    $ geo-map coordinates.txt
    # to save to a file
    $ geo-map coordinates.txt -o map.pdf

The input is a comma separated values (CSV) file, the first value is the
longitude and the second values is the latitude. ::

    37.7833, -122.4167
    42.3581, 71.0636
    .
    .
    .


Installation
------------

To install geomap, simply: ::

    $ pip install geomap