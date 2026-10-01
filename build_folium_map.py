import pandas as pd
import folium
from folium.plugins import MarkerCluster, MousePosition
from math import radians, sin, cos, sqrt, atan2

def make_map(csv='spacex_launch_geo.csv'):
 df=pd.read_csv(csv); m=folium.Map(location=[31,-96],zoom_start=4)
 for name,row in df.groupby('Launch Site')[['Lat','Long']].first().iterrows():
  folium.CircleMarker([row.Lat,row.Long],radius=8,popup=name,color='blue').add_to(m)
 cluster=MarkerCluster().add_to(m)
 for _,r in df.iterrows():
  folium.Marker([r['Lat'],r['Long']],popup=f"{r['Launch Site']} / Class {r['class']}",icon=folium.Icon(color='green' if r['class']==1 else 'red')).add_to(cluster)
 MousePosition().add_to(m)
 row=df[df['Launch Site']=='CCAFS SLC-40'].iloc[0]; p=[row['Lat'],row['Long']]; q=[28.56367,-80.57163]
 la1,lo1,la2,lo2=map(radians,p+q); a=sin((la2-la1)/2)**2+cos(la1)*cos(la2)*sin((lo2-lo1)/2)**2; distance=6373*2*atan2(sqrt(a),sqrt(1-a))
 folium.PolyLine([p,q],color='orange').add_to(m)
 folium.Marker(q,popup=f'Unverified lab reference point: {distance:.3f} km; not verified nearest coast').add_to(m)
 m.save('launch_map.html'); return m
if __name__=='__main__': make_map()
