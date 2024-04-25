# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/24/2024
# Description: create the function definition
def fall_distance(t):
    """ Calculate the fall distance due to gravity in a specific time period.
    where d is the distance, g is 9.8, and t is the time in seconds that
    the object has been falling"""
    g = 9.8
    d = 0.5 * g * t**2
    return d
