
# coding: utf-8

# In[85]:


from robobrowser import RoboBrowser
import folium
import geocoder
import pandas

datosTabla = pandas.read_excel('primer-semestre-2018.xlsx')


# In[86]:


datosTabla.head()


# In[87]:


datosTabla.keys()


# In[89]:


datosTabla['NOMBRE'] 


# In[91]:


datosTabla.dtypes


# In[92]:


print(datosTabla['CALLE']+datosTabla['NUMERO'].astype(str))


# In[93]:


datosTablaFiltrada = datosTabla.filter(items=['NOMBRE', 'TIPO', 'CALLE', 'NUMERO', 'CAPITAL'])
datosTablaFiltrada


# In[94]:


len(datosTablaFiltrada)


# In[95]:


datosTablaFiltrada['CAPITAL'].astype(str).max()


# In[96]:


datosTablaFiltrada.keys()


# In[97]:


datos = datosTablaFiltrada.to_dict(orient='split')
datos


# In[98]:


datos.keys()


# In[99]:


datos['data']


# In[100]:


datos['columns']


# In[135]:


datosTabla = datos['data']
datosTabla[0]


# In[136]:


datosTabla = datosTabla[:500]
datosTabla


# In[137]:


len(datosTabla)


# In[138]:


listaUbicaciones = []
for nombre, tipo, calle, numero, capital in datosTabla:
    lugar = calle + str(numero) + ", LA REINA, CHILE"
    #print(lugar)
    latitudLongitud = geocoder.google(lugar).latlng
    #print(latitudLongitud)
    capitalLocal = str(capital)
    local = [nombre,tipo,capitalLocal,latitudLongitud]
    listaUbicaciones.append(local)
    


# In[139]:


listaUbicaciones


# In[140]:


len(listaUbicaciones)


# In[141]:


# LIMPIAR UBICACIONES ERRONEAS (NONE)
listaUbicaciones=[[nombre, tipo, capitalLocal, latitudLongitud] for nombre, tipo, capitalLocal, latitudLongitud in listaUbicaciones if latitudLongitud != None]


# In[142]:


len(listaUbicaciones)


# In[143]:


max(listaUbicaciones)


# In[144]:


mapaLocales = folium.Map(location=[-33.4550553, -70.5411876])
mapaLocales


# In[145]:


mapaLocales = folium.Map(
    location = [-33.4550553, -70.5411876],
    zoom_start = 13
)

for nombre, tipo, capital, ubicacion in listaUbicaciones:
    folium.Marker(ubicacion, popup=nombre).add_to(mapaLocales)
    
mapaLocales


# In[157]:


mapaLocales = folium.Map(
    location = [-33.4550553, -70.5411876],
    tiles='Stamen Toner',
    zoom_start = 13
)

def coloracionCirculo(capital):
    if int(capital) < 500000:
        return 'red'
    elif int(capital) >= 500000:
        return 'green'
    else:
        return 'blue'

for nombre, tipo, capital, ubicacion in listaUbicaciones:
    folium.Circle(
        ubicacion,
        popup = nombre,
        fill = True,
        fill_color = coloracionCirculo(capital),
        color = coloracionCirculo(capital),
        radius = int(capital)/500000000
    ).add_to(mapaLocales)
mapaLocales

