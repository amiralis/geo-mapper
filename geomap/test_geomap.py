import geomap


def test_generate_map():
    m = geomap.Map()
    m.add_coordinates([], [])
    m.generate_map(output='map.png')

test_generate_map()
