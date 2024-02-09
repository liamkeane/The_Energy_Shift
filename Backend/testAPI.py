import unittest
import api


class APITester(unittest.TestCase):
    '''
    A suite of tests for the EnergyProductionAPI classes' methods
    Please note, your current working directory must be the Backend folder for all tests to work
    because otherwise api will not be imported 
    '''

    def setUp(self):
        '''
        Set up the test methods by creating an instance of the EnergyProductionAPI class with our
        csv passed in as data
        '''
        self.energyTest = api.EnergyProductionAPI()
        self.maxDiff = None

    def test_validState_getEnergyForState(self):
        '''
        Test to see if getEnergyForState() can successfully return the correct float
        when given the valid input of 'Al'
        '''
        result = self.energyTest.getEnergyForState("Al")
        self.assertEqual(result, 142733.34)

    def test_invalidState_getEnergyForState(self):
        '''
        Test to see if getEnergyForState() can successfully return a message to the user when
        their input is invalid
        '''
        result = self.energyTest.getEnergyByCategoryForState(56)

        self.assertEqual(
            result, 'Invalid input. Please enter a state abbreviation (not a full name)')

    def test_validState_getEnergyByCategoryForState(self):
        '''
        Test to see if getEnergyByCategoryForState() can successfully return the correct list of
        floats when given the valid input of 'Wisconsin'
        '''
        result = self.energyTest.getEnergyByCategoryForState("Al")
        self.assertEqual(result, {'Other renewables': 3805.24, 'Conventional hydroelectric': 11520.8, 'Nuclear': 46036.5, 'All solar': 37.12})

    def test_invalidState_getEnergyByCategoryForState(self):
        '''
        Test to see if getEnergyByCategoryForState() can successfully return a message to the user
        when their input is invalid
        '''
        result = self.energyTest.getEnergyByCategoryForState(56)

        self.assertEqual(
            result, 'Invalid input. Please enter a state abbreviation (not a full name)')

    def test_validState_getTotalEnergyForStateByMonth(self):
        '''
        Test to see if getTotalEnergyForStateByMonth() can successfully return the correct float
        value when given the valid input of "Al"
        '''
        result = self.energyTest.getTotalEnergyForStateByMonth("Al")

        self.assertEqual(result, [12574.68, 11267.83, 10343.43, 8972.6, 11274.04,
                         12255.95, 13545.99, 13862.05, 12089.57, 11731.84, 12408.92, 12406.44])

    def test_invalidState_getTotalEnergyForStateByMonth(self):
        '''
        Test to see if getTotalEnergyForStateByMonth() can successfully return a message to the user
        when their input is invalid
        '''
        result = self.energyTest.getTotalEnergyForStateByMonth("Montreal")

        self.assertEqual(
            result, 'Invalid input. Please enter a state abbreviation (not a full name)')

    def test_validState_getTotalRenewableEnergyByState(self):
        '''
        Test to see if getTotalRenewableEnergyByState() can successfully return the correct float
        value when given the valid input of "Al"
        '''
        result = self.energyTest.getTotalRenewableEnergyByState("Al")
        self.assertEqual(result, 61399.66)

    def test_invalidState_getTotalRenewableEnergyByState(self):
        '''
        Test to see if getTotalRenewableEnergyByState() can successfully return a message to the 
        user when their input is invalid
        '''
        result = self.energyTest.getTotalEnergyForStateByMonth(56)

        self.assertEqual(
            result, 'Invalid input. Please enter a state abbreviation (not a full name)')


if __name__ == '__main__':
    unittest.main()
