import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import plotly.graph_objs as go
import plotly.colors
import requests
import itertools

def return_figures(state=''):
  
  if type(state) is dict:
    state = list(state.keys())[0]

  #setting per_page to 50, the number of pages is 162, so to prevent error a limit on the number of calls was set (200)

  if state:
      state_param = '&by_state='+state
  else:
      state_param = ''
      
  """city = ''
  if city:
      city_param = '&by_city='+city
  else:
      city_param = ''"""
      
  test_list = []
  
  try:
    for i in range(30): 
        #r = requests.get('https://api.openbrewerydb.org/breweries?per_page=50&page='+str(i)+state_param+city_param+'&sort=-id') # uncomment to use also city as a filter. It needs to be passed from the front end
        r = requests.get('https://api.openbrewerydb.org/breweries?per_page=50&page='+str(i)+state_param+'&sort=-id')
        if len(r.text) != 2:
          test_list.append(r.json())
        else:
          break
  except:
    print('could not load data ', indicator)

  test_list = list(itertools.chain.from_iterable(test_list))
  df = json_normalize(test_list)

  # fifth chart NEW
  graph_five = []
  df_five = df.groupby('state')['id'].count().reset_index()
  
  graph_five.append(
      go.Bar(
      x = df_five['state'].to_list(),
      y = df_five['id'].to_list()
      )
  )

  layout_five = dict(title = 'Number of breweries in the selected state',
                xaxis = dict(title = 'State',),
                yaxis = dict(title = '# Breweries')
                )

  # sixth chart NEW
  graph_six = []
  df_six = df.groupby(['state', 'brewery_type'])['id'].count().reset_index()
  
  graph_six.append(
    go.Pie(
      labels = df_six['brewery_type'].to_list(),
      values = df_six['id'].to_list()
      ))

  layout_six = dict(title = 'Percentage of breweries per type in the selected state')
  
  # append all charts
  figures = []
  figures.append(dict(data=graph_five, layout=layout_five))
  figures.append(dict(data=graph_six, layout=layout_six))
  
  return figures

def return_figures_init():
  graph_five = []
  graph_five.append(
      go.Bar(
      x = [],
      y = []
      )
  )

  layout_five = dict(title = 'Number of breweries in the selected state',
                xaxis = dict(title = 'State',),
                yaxis = dict(title = '# Breweries')
                )

  graph_six = []
  graph_six.append(
    go.Pie(
      labels = [],
      values = []
      ))

  layout_six = dict(title = 'Percentage of breweries per type in the selected state')
  
  figures = []
  figures.append(dict(data=graph_five, layout=layout_five))
  figures.append(dict(data=graph_six, layout=layout_six))
  
  return figures
