import pandas as pd
import numpy as np
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
import plotly.graph_objects as go
import plotly.express as px
import unicodedata
from shapely.geometry import Point
from geopandas import GeoDataFrame
#import geoplot as gplt
#import geoplot.crs as gcrs
import warnings
from numpy import mean
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot

ind_st = gpd.read_file('C:/Users/jayav/PycharmProjects/GIS/GIS_Project/data/Indian_states.shp')
data = pd.read_csv('C:/Users/jayav/PycharmProjects/GIS/GIS_Project/data/air-quality-india.csv')
latlong = pd.read_csv('C:/Users/jayav/PycharmProjects/GIS/GIS_Project/data/India Cities LatLng.csv')

print(data.head())

sns.countplot(x='Year', data=data)



