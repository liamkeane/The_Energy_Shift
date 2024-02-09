import psycopg2
from psycopg2 import sql
import psqlConfig


class EnergyProductionAPI:
    '''
    A class with methods that execute SQL queries to retrieve data from our Postgresql database
    '''

    def __init__(self):
        '''
        Read in our csv data set and initialize a list of all states as an instance variable
        '''

        self.conn = psycopg2.connect(
            database=psqlConfig.database, user=psqlConfig.user, password=psqlConfig.password, host='localhost')

        self.cursor = self.conn.cursor()

        self.abbreviationToStateDictionary = {'AL': 'alabama', 'AK': 'alaska', 'AZ': 'arizona', 'AR': 'arkansas',
                                              'CA': 'california', 'CO': 'colorado', 'CT': 'connecticut', 'DE': 'delaware',
                                              'FL': 'florida', 'GA': 'georgia', 'HI': 'hawaii', 'ID': 'idaho', 'IL': 'illinois',
                                              'IN': 'indiana', 'IA': 'iowa', 'KS': 'kansas', 'KY': 'kentucky', 'LA': 'louisiana',
                                              'ME': 'maine', 'MD': 'maryland', 'MA': 'massachusetts', 'MI': 'michigan',
                                              'MN': 'minnesota', 'MS': 'mississippi', 'MO': 'missouri', 'MT': 'montana',
                                              'NE': 'nebraska', 'NV': 'nevada', 'NH': 'new_hampshire', 'NJ': 'new_jersey',
                                              'NM': 'new_mexico', 'NY': 'new_york', 'NC': 'north_carolina', 'ND': 'north_dakota',
                                              'OH': 'ohio', 'OK': 'oklahoma', 'OR': 'oregon', 'PA': 'pennsylvania',
                                              'RI': 'rhode_island', 'SC': 'south_carolina', 'SD': 'south_dakota', 'TN': 'tennessee',
                                              'TX': 'texas', 'UT': 'utah', 'VT': 'vermont', 'VA': 'virginia', 'WA': 'washington',
                                              'WV': 'west_virginia', 'WI': 'wisconsin', 'WY': 'wyoming'}

    '''
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "WI" or "wi" or "Wi" or even "wI"

        -A not valid state (either as a string or another data-types)
            -Input: 'Wisconsin' or 56 or 'Test' or True or 'Bilbo Baggins'

    '''

    def getEnergyForState(self, stateAbbreviation):
        '''
            Sums all electricity generation by all catagories in a given state

            Retrieves columns in the current working dataset pertaining to each category of electricity
            generation for a single state, sums the values in these columns and returns that number

            Args:
                state: a string indicating an abbreviation of a specified state

            Returns:
                returns a float indicating the sum of the total electricity generation for the
                provided state
        '''

        # Try to run the function as normal
        try:
            correctedStateAbbreviation = ''
            # check if the input is a string
            if type(stateAbbreviation) == str:
                correctedStateAbbreviation = stateAbbreviation.upper()

            # If the state has valid input, run the function
            if correctedStateAbbreviation in self.abbreviationToStateDictionary:

                # Turn abbreviation into valid full name of state here:
                fullStateName = self.convertAbbreviationToFullState(
                    stateAbbreviation)

                # Build the query parameterized query string and execute the query
                self.cursor.execute(sql.SQL("SELECT total FROM {} WHERE categoryofproduction = 'All fuels';").format(
                    sql.Identifier(fullStateName)))

                stateEnergySumList = self.cursor.fetchall()

                # Extract the sum out of list of a single tuple returned from the query
                stateEnergySum = stateEnergySumList[0][0]

                return stateEnergySum

            # If the state inputted is not valid, tell the user
            else:
                return 'Invalid input. Please enter a state abbreviation (not a full name)'

        # Handle an exception by telling the user to enter a valid state and printing out the exception
        except Exception as e:
            raise Exception('Fatal error', e)

    '''
    Equivalence Classes:
        -Valid state (as a string):
            -Input: "WI" or "wi" or "Wi" or even "wI"

        -A not valid state (either as a string or another data-types)
            -Input: 'Wisconsin' or 56 or 'Test' or True or 'Bilbo Baggins'

    '''

    def getTotalRenewableEnergyByState(self, stateAbbreviation):
        '''
            Sums and returns the total amount of renewable energy for the specified state

            Retrieves columns in the current working dataset pertaining to each category of renewable
            electricity generation for each state in a specific month, sums the values in these columns
            and returns that number

            Args:
                state: a string indicating an abbreviation of a specified state

            Returns:
                returns an integer indicating the sum of the total electricity generation from renewable sources
                for the current state in the current working dataset

        '''

        # Try to run the function as normal
        try:
            correctedStateAbbreviation = ''
            # check if the input is a string
            if type(stateAbbreviation) == str:
                correctedStateAbbreviation = stateAbbreviation.upper()

            # If the state valid input run the function as normal
            if correctedStateAbbreviation in self.abbreviationToStateDictionary:
                # Turn abbreviation into valid full name of state here:
                fullStateName = self.convertAbbreviationToFullState(
                    stateAbbreviation)

                # Build the query parameterized query string and execute the query
                self.cursor.execute(sql.SQL("SELECT SUM(total) FROM {} WHERE categoryofproduction <> 'All fuels'").format(
                    sql.Identifier(fullStateName)))

                renewableEnergySumList = self.cursor.fetchall()

                # Extract the sum out of list of a single tuple returned from the query
                renewableEnergySum = renewableEnergySumList[0][0]

                return renewableEnergySum

            # If the state inputted is not valid, tell the user
            else:
                return 'Invalid input. Please enter a state abbreviation (not a full name)'

        # Handle an exception by telling the user to enter a valid state, printing out the exception
        except Exception as e:
            raise Exception('Fatal error', e)

    '''
    Equivalence Classes:
        -A valid state (only in America)
            -Input: "WI" or "wi" or "Wi" or even "wI"

        -A string that is not a state
            -Input: 'Montreal' or '12'
    '''

    def getTotalEnergyForStateByMonth(self, stateAbbreviation):
        '''
            Retrieves monthly total electricity generation throughout the year for a given state

            Retrieves each individual column in the row labeled 'All fuels', returning those numbers in a sequential
            list of floats.

            Args:
                state: a string indicating one of the 50 states in America
            Returns:
                returns a list where each element indicates the sum of the total electricity generation of a respective
                month in the year for the given state. Note: the list will be in sequential order (Jan, Feb, ... Dec)
        '''
        try:
            correctedStateAbbreviation = ''
            # check if the input is a string
            if type(stateAbbreviation) == str:
                correctedStateAbbreviation = stateAbbreviation.upper()

            # If the state valid input run the function as normal
            if correctedStateAbbreviation in self.abbreviationToStateDictionary:
                # Turn abbreviation into valid full name of state here:
                fullStateName = self.convertAbbreviationToFullState(
                    stateAbbreviation)

                # Build the query parameterized query string and execute the query
                self.cursor.execute(sql.SQL("SELECT january, february, march, april, may, june, july, august, september, october, november, december FROM {} WHERE categoryofproduction = 'All fuels'").format(
                    sql.Identifier(fullStateName)))

                listOfSumsForMonths = self.cursor.fetchall()

                # Create the list to be returned in the result dictionary
                parsedListOfSums = []

                # Extract the value of each month stored in the single tuple returned from the query
                for i in range(12):
                    parsedListOfSums.append(listOfSumsForMonths[0][i])

                return parsedListOfSums

            # If the state inputted is not valid, tell the user
            else:
                return 'Invalid input. Please enter a state abbreviation (not a full name)'

        # Handle an exception by telling the user to enter a valid state and printing out the exception
        except Exception as e:
            raise Exception('Fatal error', e)

    '''
    Equivalence Classes:
        -A valid state (only in America)
            -Input: "WI" or "wi" or "Wi" or even "wI"

        -A string that is not a state
            -Input: 'Montreal' or '12'
    '''

    def getEnergyByCategoryForState(self, stateAbbreviation):
        '''
            Returns the total energy by category of energy for a specified state

            Retrieves columns in the current working dataset pertaining to the categories of renewable
            energy production for a specified state and sums up all of the values of the categories for
            each month's record and returns this data as a object where the keys are the category of
            renewable energy production and the values are the summed value that was calculated

            Arguments:
                state: a string indicating an abbreviation of a state

            Returns:
                a dictionary where the keys are the category of renewable energy production and the values
                are the total energy produced in that category in the specified state across all months
                of the year
        '''

        try:
            correctedStateAbbreviation = ''
            # check if the input is a string
            if type(stateAbbreviation) == str:
                correctedStateAbbreviation = stateAbbreviation.upper()

            # If the state valid input run the function as normal
            if correctedStateAbbreviation in self.abbreviationToStateDictionary:
                # Turn abbreviation into valid full name of state here:
                fullStateName = self.convertAbbreviationToFullState(
                    stateAbbreviation)

                # Build the query parameterized query string and execute the query
                self.cursor.execute(sql.SQL("SELECT categoryofproduction, total FROM {} WHERE categoryofproduction != 'All fuels'").format(
                    sql.Identifier(fullStateName)))

                listOfSumsForCategories = self.cursor.fetchall()

                '''Creates a dictionary from the result of the query and where the keys are months
                and the values are the total amount of renewable energy produced in that month'''
                dictOfSumsForCategories = {}

                for category in listOfSumsForCategories:
                    dictOfSumsForCategories[category[0]] = category[1]

                return dictOfSumsForCategories

            # If the state inputted is not valid, tell the user
            else:
                return 'Invalid input. Please enter a state abbreviation (not a full name)'

        # Handle an exception by telling the user to enter a valid state and printing out the exception
        except Exception as e:
            raise Exception('Fatal error', e)

    def convertAbbreviationToFullState(self, stateAbbreviation):
        '''
        This helper function takes in a state abbreviation as a string and returns the corresponding full state name
        '''

        return self.abbreviationToStateDictionary[stateAbbreviation.upper()]


if __name__ == "__main__":
    print('Database connection successful')
