
import folium
from folium.plugins import MarkerCluster

# 1. Criar um objeto de mapa
mymap = folium.Map(location=[latitude, longitude], zoom_start=12)

# 2. Adicionar um marcador ao mapa
folium.Marker(location=[latitude, longitude], popup='Marcador 1').add_to(mymap)

# 3. Adicionar um círculo ao mapa
folium.Circle(location=[latitude, longitude], radius=1000, color='blue', fill=True).add_to(mymap)

# 4. Adicionar uma linha poligonal ao mapa
folium.PolyLine(locations=[[lat1, lon1], [lat2, lon2]], color='red').add_to(mymap)

# 5. Adicionar um polígono ao mapa
folium.Polygon(locations=[[lat1, lon1], [lat2, lon2], [lat3, lon3]], color='green').add_to(mymap)

# 6. Adicionar um mapa coroplético ao mapa
folium.Choropleth(geo_data=geo_json_data, data=data, key_on='feature.properties.id', fill_color='YlGnBu').add_to(mymap)

# 7. Adicionar um mapa de calor ao mapa
folium.plugins.HeatMap(data=[[lat1, lon1], [lat2, lon2], [lat3, lon3]]).add_to(mymap)

# 8. Adicionar um controle de camadas ao mapa
folium.LayerControl().add_to(mymap)

# 9. Adicionar um marcador com ícone personalizado
folium.Marker(location=[latitude, longitude], popup='Marcador 2', icon=folium.CustomIcon(icon_image='custom_icon.png', icon_size=(30, 30))).add_to(mymap)

# 10. Salvar o mapa em um arquivo HTML
mymap.save('meu_mapa.html')

# Exemplo adicional: Adicionar um cluster de marcadores ao mapa
marker_cluster = MarkerCluster().add_to(mymap)
folium.Marker(location=[lat1, lon1], popup='Marcador A').add_to(marker_cluster)
folium.Marker(location=[lat2, lon2], popup='Marcador B').add_to(marker_cluster)

# Exibir o mapa
mymap
