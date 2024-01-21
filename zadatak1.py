#učitavanje modula geopandas
import geopandas as gpd
import matplotlib.pyplot as plt 
from mpl_toolkits.axes_grid1 import make_axes_locatable 

# Čitanje shapefile datoteke world.shp (format za geospacijalne vektorske podatke u GIS softverima)
world_data = gpd.read_file(r'C:\Users\Mario\Desktop\fakultet\Diplomski studij\3. semestar\Analitika u poslovanju\Projektni zadatak\geo\world.shp')
world_data 
world_data= world_data[['NAME', 'geometry']]
#  Pozivanje vrijednosti area koja označava površinu države
world_data['area'] = world_data.area
print(world_data.head(15))
# Brisanje antarktike iz geoframea
world_data = world_data[world_data['NAME'] != 'Antarctica']
#world_data.plot()

# Promjena projekcije na ravnu (epsg)
current_crs = world_data.crs   
world_data.to_crs(epsg = 3857, inplace = True)
#world_data.plot(column = 'NAME', cmap = 'seismic')

# Preračunavanje u kilometre kvadratne
world_data['area'] = world_data.area/1000000

# Dodavanje legende (promjena skale boja(cmap)- https://matplotlib.org/stable/gallery/color/colormap_reference.html i label) 
#world_data.plot(column = 'area' , cmap = 'OrRd' , legend = True, 
                #legend_kwds = {'label': "Površina država (km2.)"}, figsize = (7,7))

# Promjena veličine legendi i plota 
fig, ax = plt.subplots(figsize = (10,10))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size = "10%", pad = 0.1)
world_data.plot(column = 'area' , cmap = 'OrRd' , legend = True, 
                legend_kwds = {'label': "Površina (km2)"},
                ax = ax, cax = cax)

