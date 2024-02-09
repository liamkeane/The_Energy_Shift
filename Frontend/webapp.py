'''
Flask code to render all of our html templates with data retrieved from the backend
'''

import flask
from flask import render_template, request
import sys
sys.path.append('../Backend/')
from api import EnergyProductionAPI


# invokes Flask (creates an instance)
app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

### Helper functions for the data ###
def calculatePercentage(selectedState):
    '''
    This helper function calculates the percentage of total energy that comes from renewable sources for
    the user's selected state. It is called in theData() function
    '''

    energy = EnergyProductionAPI()

    totalEnergy = energy.getEnergyForState(selectedState)
    totalRenewableEnergy = energy.getTotalRenewableEnergyByState(selectedState)

    return round((totalRenewableEnergy/totalEnergy)*10000)/100

def extractKeys(dict):
    '''
    This helper functions extracts the keys from a given dictionary and returns them as a list
    It is called in theData() function
    '''
    return list(dict.keys())

def extractValues(dict):
    '''
    This helper function extracts the values from a given dictionary and returns them as a list
    It is called in theData() function
    '''
    return list(dict.values())

### The routes ###
@app.route('/')
def home():
    '''
    Renders the Home template which is a homepage that tells the user about the purpose of our
    site and allows them to navigate to theData page
    '''
    return render_template('home.html')


@app.route('/theData', methods=['POST', 'GET'])
def theData():
    '''
    Renders The Data template which queries data about a given state and displays visualizations
    based off their results
    '''

    energy = EnergyProductionAPI()

    # Initialize all relevant variables as none so flask knows not to render the results portion of the page
    selectedState = None
    selectedStateFullName = None
    totalEnergy = None
    totalRenewableEnergy = None
    totalEnergyByMonth = None
    totalEnergyByCategory = None
    categories = None
    categoryValue = None
    percentageRenewableEnergy = None

    # Getting data from form
    if request.method == 'POST':
        selectedState = request.form["statesSelect"]

        # Call the api to retrieve data for the chosen state
        totalEnergy = energy.getEnergyForState(selectedState)
        totalRenewableEnergy = energy.getTotalRenewableEnergyByState(selectedState)
        totalEnergyByMonth = energy.getTotalEnergyForStateByMonth(selectedState)
        totalEnergyByCategory = energy.getEnergyByCategoryForState(selectedState)
        selectedStateFullName = energy.convertAbbreviationToFullState(selectedState)

        # Parse the dictionary totalEnergyByCategory returns
        categories = extractKeys(totalEnergyByCategory)
        categoryValue = extractValues(totalEnergyByCategory)

        # Calculate the percentage of the states energy that is renewable
        percentageRenewableEnergy = calculatePercentage(selectedState)

    return render_template('theData.html', selectedState=selectedState, totalEnergy=totalEnergy,
                           totalRenewableEnergy=totalRenewableEnergy, totalEnergyByMonth=totalEnergyByMonth,
                           categories=categories, categoryValue=categoryValue, selectedStateFullName=selectedStateFullName, 
                           percentageRenewableEnergy=percentageRenewableEnergy)


@app.route('/aboutTheData')
def aboutTheData():
    '''
    Renders the About the Data template which provides the user information about our data,
    it's source and the process of choosing and working with this data
    '''
    return render_template('aboutTheData.html')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)