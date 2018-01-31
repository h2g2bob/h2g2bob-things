"""Picks a random point on a sphere, and prints a link to openstreetmap for it
"""
import math
import random

tau = 2*math.pi

def random_point():
    print("https://www.openstreetmap.org/search?query={lat:.6f},{lng:.6f}#map=10/{lat:.6f}/{lng:.6f}".format(
        lat=math.asin(random.uniform(-1, +1)) * (360./tau),
        lng=random.uniform(-tau/2, +tau/2) * (360./tau),
        ))

if __name__ == '__main__':
	random_point()
