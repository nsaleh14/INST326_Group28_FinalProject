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
import time
import requests


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
    
    def sign_up(self, input_username, input_password, registered_users):
        '''
        This method will allow the user to create an account with a username and
        password so they can access the weather data in the future. It will store
        these usernames and passwords in a dictionary.
        '''
        self.registered_users = {}
        
        if input_username not in registered_users:
            registered_users[input_username] = input_password
            
        else:
            Login.sign_in
        
        pass
    
    def sign_in(self):
        '''
        This method will allow the user to sign into their already created account.
        '''
        
        
        
        pass
    
    def verify_user(self, input_username):
        '''
        This method will check the inputted username and password and verify if
        they are inside the dictionary and if they match.
        '''
        
        if input_username in self.registered_users:
            Login.sign_in
            
        else:
            #repeat ask input or ask if they need to create an account
            Login.sign_up
        
        
        pass
    
class Weather:
    '''
    This class will access the weather forecast data, parse it, then convert it
    into a format that will allow the user to view it properly.
    '''
    
    def __init__(self):
        
        pass
    
    def get_user_input():
        ''' Or would this go under the main()? or delete main()?
        
        Ask the user if they want past data or future//today's data.
        Or use the datetime module to see if the date entered is today's date
         or before today's date and get the corresponding data from the api
         
         but also ask after if user wants specific data such as temperature, etc.
         or wants all the information.
         If chose one, ask them again if they want
         another thing or just continue to get the data, or figure out
         how to get multiple user input for each information type at once.
         Or just give them all information automatically.
         
         If gives past date, should they give a single date or a date range?
         If single date, automatically give data for seven days from that date
         including that date ?
         
         Also check for valid input, use try/except within a while loop ?
         
        '''
    
    def get_forecast_data():
        '''Access an api with forecast data for today's date/the week.'''
        
        pass
    
    def get_past_data():
        '''Access a different api for historical weather data.
        
        or just use the same api?
        https://open-meteo.com/en/docs
        
        https://open-meteo.com/en/docs/historical-weather-api'''
        
        pass
    
    def retrieve_data(self):
        '''
        This method will retrieve the forecast data from the Weather API.
        '''
        #https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/maryland/2000-01-01/2024-12-10?unitGroup=us&key=YOUR_API_KEY&contentType=json'
        
        # or use Meteostat for historical data
        # weather.gov for forecast
        # or api.met.no/weatherapi for forecast?
        
        resp = requests.get(f'')
        
        return(resp)
    
        pass
    
    def parse_data(self, resp):
        '''
        This method will parse the data from the Weather API for further access.
        '''
        
        time.sleep(1)
        
        pass
    
    def convert_data(self, resp):
        '''
        This method will convert the weather data to a specific format and will
        allow it to be read by the user.
        '''
        
        resp = resp.json()
        
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