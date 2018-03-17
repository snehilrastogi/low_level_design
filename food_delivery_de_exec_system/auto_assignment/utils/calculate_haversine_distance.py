import math

from auto_assignment import constants


class CalculateHaversineDistance(object):
    @classmethod
    def calculate(self, r_pos, de_pos):
        r_lat, r_long = r_pos
        de_lat, de_long = de_pos
        radius = constants.EARTH_RADIUS
        distance_lat = math.radians(de_lat - r_lat)
        distance_long = math.radians(de_long - r_long)
        haversine_bearing = math.sin(distance_lat / 2) * math.sin(distance_lat / 2) + math.cos(math.radians(r_lat)) \
                                                                                      * math.cos(
            math.radians(de_lat)) * math.sin(distance_long / 2) * math.sin(
            distance_long / 2)
        final_haversine_bearing = 2 * math.atan2(math.sqrt(haversine_bearing), math.sqrt(1 - haversine_bearing))
        haversine_distance = radius * final_haversine_bearing
        return haversine_distance
