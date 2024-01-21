# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:49:40 2021

@author: Mario
Učitavanje država i gradova (https://geopandas.org/en/stable/docs/user_guide/mapping.html)
"""
import geopandas
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
fig, ax = plt.subplots(1, 1, figsize=(25, 25))
world.boundary.plot(ax=ax, marker='o', color='blue', markersize=5)
cities.plot(ax=ax, marker='o', color='red', markersize=10);