__author__ = 'Amirali Sanatinia'

"""
    geomap

    This module implements the mapping and visualizations.
    :copyright: (c) 2014 by Amirali Sanatinia
    :license: Apache 2, see LICENSE for more details
"""


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


class Map(object):
    """ Map object """

    def __init__(self, projection='gall', fig_x=20, fig_y=10, lats=None, lons=None):
        self.fig = plt.figure(figsize=(fig_x, fig_y))
        self._map = Basemap(projection=projection)
        self.lats = lats
        self.lons = lons

    def add_coordinates(self, lats, lons):
        """ Add coordinates, ([latitude], [longitude]) """

        self.lats = lats
        self.lons = lons

    def generate_map(self, draw_countries=True, drawcoastlines=True,
                     continents_color='#A0A0A0', mapboundary_color='#f4f4f4',
                     marker_size=6, marker='ro',
                     output=None):
        """ Generate the map, if not output is specified draw on screen """

        if drawcoastlines:
            self._map.drawcoastlines()

        if draw_countries:
            self. _map.drawcountries()

        # fill continents
        self._map.fillcontinents(color=continents_color)
        #draw boundaries
        self._map.drawmapboundary(fill_color=mapboundary_color)

        x, y = self._map(self.lons, self.lats)

        # Plot them using round markers of size 6
        self._map.plot(x, y, marker, markersize=marker_size)
        if output:
            plt.savefig(output, bbox_inches='tight')
            plt.close()
            return
            
        # If no output is chosen, show the map
        plt.show()







