from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.common.exceptions import WebDriverException

class UserUsesApp(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

     #initial visit only:
     #A user is invited to enter their name (mainly for identification purposes)
     #user clicks new account choice
     #user is taken to page to start. 
    # def test_template_returned(self):
        # self.browser.get(self.live_server_url)
        # #self.assertEqual(self.title, 'Famous Budget Application')
        # #self.assertTemplateUsed(self, 'setup.html')
    
    #here, we enter categories, groupings, any existing data (such as avg monthly spent), 
     # if a new user, are welcomed & given brief overview, else taken to their budget data
    # def test_get_index_page(self):
        # self.browser.get(self.live_server_url)
        # nameInput = self.browser.find_element_by_id('id_new_item')
        # # The missing girl puts in her name
        # usersName = 'Hello New User'
        # # nameInput.send_keys(usersName)
        # # nameInput.send_keys(Keys.ENTER)
        # userNameInApp = self.browser.find_element_by_tag_name('h2')
        # self.assertEqual(usersName, userNameInApp.text) 

    def test_get_index_pageenter_name_gives_appropriate_response(self):
        self.browser.get(self.live_server_url)
        nameInput = self.browser.find_element_by_id('id_new_item')
        # The missing girl puts in her name
        usersName = 'Rowan'
        nameInput.send_keys(usersName)
        nameInput.send_keys(Keys.ENTER)
        userNameInApp = self.browser.find_element_by_tag_name('h2')
        # self.assertEqual(usersName, userNameInApp.text) 
        assert 'Rowan' in self.browser.page_source

     # if it is the users first time they see predefined categories

     # if returning, they see their categories

     # the user returns and sees their budget categories as well, previously entered figures