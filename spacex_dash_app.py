import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

def create_app(csv='spacex_launch_dash.csv'):
 df=pd.read_csv(csv); app=Dash(__name__); sites=sorted(df['Launch Site'].unique())
 app.layout=html.Div([html.H1('SpaceX Launch Dashboard'),dcc.Dropdown(id='site-dropdown',options=[{'label':'All Sites','value':'ALL'}]+[{'label':s,'value':s} for s in sites],value='ALL',searchable=True),dcc.Graph(id='success-pie-chart'),dcc.RangeSlider(id='payload-slider',min=0,max=10000,step=1000,value=[0,10000],marks={i:str(i) for i in range(0,10001,1000)}),dcc.Graph(id='success-payload-scatter-chart')])
 @app.callback(Output('success-pie-chart','figure'),Input('site-dropdown','value'))
 def pie(site):
  if site=='ALL':
   counts=df.groupby('Launch Site',as_index=False)['class'].sum(); return px.pie(counts,names='Launch Site',values='class',title='Successful landings by site')
  counts=df.loc[df['Launch Site']==site,'class'].value_counts().rename_axis('Outcome').reset_index(name='Count')
  return px.pie(counts,names='Outcome',values='Count',title=site)
 @app.callback(Output('success-payload-scatter-chart','figure'),Input('site-dropdown','value'),Input('payload-slider','value'))
 def scatter(site,bounds):
  sub=df[df['Payload Mass (kg)'].between(*bounds)]
  if site!='ALL': sub=sub[sub['Launch Site']==site]
  return px.scatter(sub,x='Payload Mass (kg)',y='class',color='Booster Version Category',hover_data=['Launch Site'])
 return app
if __name__=='__main__': create_app().run(debug=False,port=8050)
