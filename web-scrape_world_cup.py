__author__  = "Benjamin Jones"
__credits__ = "Mike Holmes" 
__license__ = "No license, feel free to use, edit and distribute" 
__version__ = "1.0.1"
__email__   = "benjamin.t.jones@accenture.com"

############## Libraries we are going to use ###############

import requests                 # you need this to connect to the webpage
from bs4 import BeautifulSoup   # you need this to interpret the webpage
from twilio.rest import Client  # you need this to text the results to yourself

############## Our Methods ###############

def getMessageContents(url):
    # with open('cache.html', 'rb') as f:
    #     soup = BeautifulSoup(f.read(), 'html.parser')
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    html_results = soup.find_all( ["ul", "li"]) # "ul" and "li" are just the tags in Telegraph HTML that we search by
    
    # Clean the results of this
    cleanList = [] # Create an empty list
    for html_line in html_results: # Run through each line individually
        if html_line.string != None: # Because we're only looking for Strings, anything else is None.
            # print(html_line.string)
            cleanList.append(html_line.string)
    textMessage = 'Latest 5 World Cup Results: \n' + '\n'.join(cleanList[-5:])
    print("Message to send: ")
    print(textMessage)
    return textMessage # If I call the method, this is what I get back

def textMe(textMessage, accountSID, authToken, twilioNumber, myNumber):
    texter = Client(accountSID, authToken) # Creates the Object from the library we imported at the top
    # This is what actually sends the message!
    texter.messages.create(
        body  =textMessage,
        from_ =twilioNumber,
        to    =myNumber
    )
    print('Text sent successfully!')

############## Does it work?? ###############

URL = "https://www.telegraph.co.uk/world-cup/2018/06/26/world-cup-2018-fixtures-complete-schedule-match-results-far/"

ACCOUNT_SID     = "ACce41806def7e3deea7c85ee1d49d1a3e"
AUTH_TOKEN      = "6d1c06d14a6fa98eb891a844a8e50634"
TWILIO_NUMBER   = "+441557280042"
MY_NUMBER       = "+447453506915"

TEXT_MESSAGE = getMessageContents(URL)
textMe(TEXT_MESSAGE, ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, MY_NUMBER)