"""
geospatial_utils.py

A collection of simple geospatial plotting functions using matplotlib.
These functions help visualize coordinate points, polygons, and mock choropleth maps.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np

def plot_coordinates(coords, title="Coordinate Plot"):
    """
    Plot a list of (lon, lat) coordinate tuples on a 2D matplotlib plot.

    Args:
        coords (list of tuple): List of (longitude, latitude) tuples.
        title (str): Title of the plot.
    """
    lons, lats = zip(*coords)
    plt.figure(figsize=(6, 6))
    plt.plot(lons, lats, 'ro-', markersize=5)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_simple_polygon(polygon_coords, title="Polygon Plot"):
    """
    Plot a polygon defined by a list of (lon, lat) coordinates.

    Args:
        polygon_coords (list of tuple): Coordinates forming the polygon.
        title (str): Title of the plot.
    """
    lons, lats = zip(*polygon_coords)
    plt.figure(figsize=(6, 6))
    plt.fill(lons, lats, color='skyblue', alpha=0.7, edgecolor='black')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(title)
    plt.grid(True)
    plt.show()


def plot_population_choropleth(polygons, population_data, title="Population Choropleth"):
    """
    Plot a mock population choropleth using colored polygons.

    Args:
        polygons (list of list of tuple): List of polygons, each defined by (lon, lat) points.
        population_data (list of float): Population values for each polygon.
        title (str): Title of the plot.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    patches = []

    for poly in polygons:
        polygon = Polygon(poly, closed=True)
        patches.append(polygon)

    # Normalize population values to 0-1 for colormap
    norm = plt.Normalize(min(population_data), max(population_data))
    colors = plt.cm.viridis(norm(population_data))

    collection = PatchCollection(patches, facecolor=colors, edgecolor='black', linewidth=1)
    ax.add_collection(collection)

    ax.autoscale_view()
    ax.set_aspect('equal', 'box')
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title(title)
    
    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])  # Only needed for matplotlib < 3.1
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label("Population")

    plt.grid(True)
    plt.show()
