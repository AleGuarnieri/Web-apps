# Link to Heroku webbapp: https://web-app-python-example-1.herokuapp.com/

# Installation
In order to run this web app you will need to install: flask, plotly

# Motivation
I implemented this web-app as part of a course on Data science to learn how to use a web app to show your results in a dashboard. 

# File Description
worldbank.py is the main package which needs to be run to initialize the app
wrangling_scripts contains the script used to wrangle data from worldbank data folder
worldbankapp contains the script to connect front-end and back-end and the templates in HTML to be rendered in the website

# Details
The front-end is implemented using Bootstrap while the back-end using Flask. The data are wrangled and then sent to the front-end where an HTML renders the results in the expected way.
In order to run the app, you need to execute python worldbank.py on your local repository and then once the app is running, you can see it on http://localhost:3001

# Acknowledgements
Data provider: "World bank data". The tutorial was found on the Udacity platform