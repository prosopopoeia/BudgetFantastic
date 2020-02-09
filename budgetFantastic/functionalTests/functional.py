from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.common.exceptions import WebDriverException

class UserUsesApp(StaticLiveServerTestCase):

     def setUp(self):
         self.browser = webdriver.Firefox()
         
         
     def tearDown(self):
         self.browser.quit()
         
     #A user is invited to enter their name (mainly for identification purposes)
     # if a new user, are welcomed & given brief overview, else taken to their budget data
     def test_enter_name_gives_appropriate_response(self):
         self.browser.get(self.live_server_url)
         nameInput = self.browser.find_element_by_id('id_users_name')
         # The missing girl puts in her name
         usersName = 'Rowen'
         nameInput.send_keys(usersName)
         nameInput.send_keys(Keys.ENTER)
         userNameInApp = self.browser.find_element_by_tag_name('h2')
         self.assertEqual(usersName, userNameInApp) 
     
     # if it is the users first time they see predefined categories
     
     # if returning, they see their categories

     
     ## ...
     
     # the user returns and sees their budget categories as well, previously entered figures
     
     
     ## ...
     
     
     
     