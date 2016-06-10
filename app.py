from flask import Flask, render_template, request, redirect, jsonify, \
    url_for
import random
import string
import logging
import json
import httplib2
import requests
from flask import make_response


app = Flask(__name__)


# Route to jQuery Examples
@app.route('/jQueryExamples', methods=['GET'])
def jQueryExamples():
	print "Show jQuery Examples"
	return render_template('jQueryExamples.html')


# Route to Typeahead Examples
@app.route('/materialTagsExamples', methods=['GET'])
def materialTagsExamples():
	print "Show mMterialTags Examples Examples"
	return render_template('materialTagsExamples.html')


# ** Example 5 **
# Autocomplete with Bloodhound with Remote data
@app.route('/bloohdhoundRemote', methods=['GET', 'POST'])
def bloohdhoundRemote():
	print "** bloohdhoundRemote() called"
	if request.method == 'POST':
		print "POST request"
	else:
		print "GET request"

	citynames = ['Amsterdam', 'London', 'Paris', 'Washington', 'Sydney', 'Melbourne']
	
	resource_list = [{'value': 'MIR:00000555', 'label': 'My WormBase RNAi'}, \
		{'value': 'MIR:11100545', 'label': 'My Wormpep'}]
	return jsonify(resource_list=resource_list, citynames=citynames)

# ** Example 4 ** 
# Autcomplete from multiple sources Bloodhound
@app.route('/multipleRemote', methods=['GET', 'POST'])
def multipleRemote():
	print " ** multipleRemote() called"
	if request.method == "POST":
		print "POST request"
	else:
		print "GET request"

	nba_teams = [{"team": "Boston Celtics"}, {"team": "Dallas Mavericks"}, {"team": "Brooklyn Nets"}]
	nhl_teams = [{"team": "New Jersey Devils"}, {"team": "New York Islanders"}, {"team": "Philadelphia Flyers"}, {"team": "Pittsburgh Penguins"}]

	return jsonify(nba_teams=nba_teams, nhl_teams=nhl_teams)


# ** Example 3 ** 
# Autocomplete method - called from Jinja template
@app.route('/datcomplete', methods=['GET', 'POST'])
def datcomplete():
	print "** datcomplete() called"
	if request.method == 'POST':
		print "POST request"
	else:
		print "GET request"

	# postData = request.form
	# print "** MyVar:", postData
	jsonData = request.json['variable']
	print jsonData

	new_data = [{'value': 'MIR:00000555', 'label': 'My WormBase RNAi'}, \
		{'value': 'MIR:00000545', 'label': 'My Wormpep'}]

	results = [{'value': 'MIR:00000466', 'label': 'WormBase RNAi'}, \
		{'value': 'MIR:00000031', 'label': 'Wormpep'}, {'value': 'MIR:00000186', 'label': 'Xenbase'}, \
		{'value': 'MIR:00000111', 'label': 'Resource 1'}, {'value': 'MIR:00000222', 'label': 'Resource 2'}, \
		{'value': 'MIR:00000333', 'label': 'Resource 3'}, {'value': 'MIR:00000444', 'label': 'Resource 4'}]
	
	results.extend(new_data)	
	return jsonify(matching_results=results)


# ** Example 1 ** 
# Autocomplete method - called from Jinja template
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = request.args.get('q')
	results = [{'value': 'MIR:00000466', 'label': 'WormBase RNAi'}, \
		{'value': 'MIR:00000031', 'label': 'Wormpep'}, {'value': 'MIR:00000186', 'label': 'Xenbase'}, \
		{'value': 'MIR:00000111', 'label': 'Resource 1'}, {'value': 'MIR:00000222', 'label': 'Resource 2'}, \
		{'value': 'MIR:00000333', 'label': 'Resource 3'}, {'value': 'MIR:00000444', 'label': 'Resource 4'}, \
		{'value': 'MIR:00000555', 'label': 'Resource 5'}, {'value': 'MIR:00000666', 'label': 'Resource 6'}]

	return jsonify(matching_results=results)
	#results = ["car", "carriage", "horse", "dog"]
	#return jsonify(matching_results=results)


# ** Example 2 **
# Autocomplete with categories
@app.route('/catcomplete', methods=['GET'])
def catcomplete():
	search = request.args.get('q')
 	category_data = [{'value': 'MIR:00000466', 'label': 'WormBase RNAi', 'category': 'Pattern Match'}, \
 	{'value': 'MIR:00000031', 'label': 'Wormpep', 'category': 'Pattern Match'}, \
 	{'value': 'MIR:00000186', 'label': 'Xenbase', 'category': 'Pattern Match'}, \
 	{'value': 'MIR:00000466', 'label': 'WormBase RNAi', 'category': ''}, \
 	{'value': 'MIR:00000111', 'label': 'Resource 1', 'category': ''}, \
 	{'value': 'MIR:00000222', 'label': 'Resource 2', 'category': ''}, \
 	{'value': 'MIR:00000333', 'label': 'Resource 3', 'category': ''}, \
 	{'value': 'MIR:00000444', 'label': 'Resource 4', 'category': ''}, \
 	{'value': 'MIR:00000555', 'label': 'Resource 5', 'category': ''}, \
 	{'value': 'MIR:00000666', 'label': 'Resource 6', 'category': ''}]
	return jsonify(category_data=category_data)


# Route to home page
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def show_home():
	return render_template('index.html')


# Main Method
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
