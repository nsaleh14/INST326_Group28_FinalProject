'''
Group 28 - Naseem Saleh, Jack Bonin, Andre Soriano
 
INST326 - Final Project
Weather App

A script that will create a weather app using a Weather API that allows the
 user to check the weather forecasts of the current date or any date in the past
 of their choosing. The user will be able to input a specific date and get
 the forecast information for that day such as temperature, humidity, condition, etc.
'''

import re
import unittest

#Unit testing:
class WeatherTest(unittest.TestCase):
    '''
    This class is for performing unit tests for the Weather class.
    
    '''
    
    def retrieve_data_test(self):
        '''
        Tests if the weather data can actually be retrieved so that it will
        be ready for parsing.
        '''
        pass
    
    def weather_value_test(self):
        '''
        Tests if the appropriate weather forecast data can be found
        and that it is not None if it should have a value.
        '''
        pass
    
    def parsing_test(self):
        '''
        Tests to see if the weather data can be appropriately parsed
        and returns an error if not.
        '''
        pass
    
    def convert_format_test(self):
        '''
        Tests to see if the data was properly converted to a specific format or not.
        '''
        pass
    
    def app_test(self):
        '''
        Tests to see if the unit tests are being tested properly and the whole app
        script is working as it should.
        '''
        pass


class Login:
    '''
    This class will allow the user to sign in or create an account, and will
    verify the user's credentials are correct to let them access the weather data.
    '''
    def __init__(self):
        
        pass
    
    def sign_up(self):
        '''
        This method will allow the user to create an account with a username and
        password so they can access the weather data in the future. It will store
        these usernames and passwords in a dictionary.
        '''
        pass
    
    def sign_in(self):
        '''
        This method will allow the user to sign into their already created account.
        '''
        pass
    
    def verify_user(self):
        '''
        This method will check the inputted username and password and verify if
        they are inside the dictionary and if they match.
        '''
        pass
    
class Weather:
    '''
    This class will access the weather forecast data, parse it, then convert it
    into a format that will allow the user to view it properly.
    '''
    
    def __init__(self):
        
        pass
    
    def retrieve_data(self):
        '''
        This method will retrieve the forecast data from the Weather API.
        '''
        pass
    
    def parse_data(self):
        '''
        This method will parse the data from the Weather API for further access.
        '''
        pass
    
    def convert_data(self):
        '''
        This method will convert the weather data to a specific format and will
        allow it to be read by the user.
        '''
        pass
    

def __main__(username, password):
    '''
    Takes in the user's credentials and uses the Login class's method "verify_user"
    to verify if they are correct. If not, it will ask them to try again or asks
    them to sign up and returns the "sign_up" method.
    After the user is properly verified and able to sign in, they will
    be able to input a specific date and get back the weather forecast 
    data for that date.
    '''
    
    pass
    
if __name__ == "__main__":
    '''Will call the main function / user input function so that the user
    will be able to login and access weather data by inputting a date.'''
    
    pass