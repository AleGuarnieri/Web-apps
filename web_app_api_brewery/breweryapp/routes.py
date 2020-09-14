from breweryapp import app

import json, plotly
from flask import render_template, request, Response, jsonify
from scripts.data import return_figures, return_figures_init


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():

	# List of states for filter
	states = ['Georgia', 'District of Columbia', 'Wyoming', 'Wisconsin',
       'West Virginia', 'Washington', 'Virginia', 'Vermont', 'Utah',
       'Texas', 'Tennessee', 'South Carolina',
       'Rhode Island', 'Pennsylvania', 'Oregon', 'Oklahoma', 'Ohio',
       'North Dakota', 'North Carolina', 'New York', 'New Mexico',
       'Nevada',
       'Mississippi', 'Minnesota', 'Michigan', 'Massachusetts',
       'Illinois', 'Idaho', 'Hawaii', 'Florida', 'FL San',
       'Colorado', 'California', 'Arkansas',
       'Arizona', 'Alaska', 'Alabama']

	# Parse the POST request states list
	if (request.method == 'POST') and request.form:
		figures = return_figures(request.form.to_dict())
		states_selected = []
		for state in request.form.lists():
			states_selected.append(state)
	
	# GET request returns all states for initial page load
	else:
		figures = return_figures_init()
		states_selected = []
		

	# plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON,
                all_states=states,
                states_selected=states_selected)
