from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from  selenium.common.exceptions import WebDriverException
from django.test import Client
from fantasticApp.models import User, Category
import time

class UserUsesApp(StaticLiveServerTestCase):
    def setUp(self):
        #Ssuper().setUpClass()
        self.selenium = WebDriver()
        # self.browser = webdriver.Firefox()
    def tearDown(self):
        #self.browser.quit()
        self.selenium.quit()
        #super().tearDownClass()
        
    
    # #initial visit only:
    # #A user is invited to enter their user name (mainly for identification purposes)
     
    # ##IF (FIRST TIME USE)
    # #user sees fields to enter category, user enters
        # #-cat name
    # #page displays category with 'add' button (to record category transaction)
    # def test_new_user_create_new_cat(self):
    
        # self.selenium.get(self.live_server_url)
        # nameInput = self.selenium.find_element_by_name('users_name')
        # usersName = 'Rowan'
        # nameInput.send_keys(usersName)
        # nameInput.send_keys(Keys.ENTER)
        # time.sleep(2)
        
        # cat_name_input = self.selenium.find_element_by_name('category_name')
        # cat  = 'banking'
        # cat_name_input.send_keys(cat)
        # cat_name_input.send_keys(Keys.ENTER)        
        # time.sleep(1)
        
        # result = self.selenium.find_element_by_id('option2')
        # self.assertIn('banking', result.text)        
     
        
    # #User sees category added and is prompted for another, adds one, 
    # #and sees a list of both categories
    # def test_user_adds_categories_and_sees_list(self):
        # self.selenium.get(self.live_server_url)
        # nameInput = self.selenium.find_element_by_name('users_name')
        # usersName = 'Rowan'
        # nameInput.send_keys(usersName)
        # nameInput.send_keys(Keys.ENTER)
        # time.sleep(2)
        
        # cat_name_input = self.selenium.find_element_by_name('category_name')
        # cat  = 'cat1'
        # cat_name_input.send_keys(cat)
        # cat_name_input.send_keys(Keys.ENTER)        
        # time.sleep(1)
          
        # cat_name_input2 = self.selenium.find_element_by_name('category_name')          
        # cat  = 'cat2'
        # cat_name_input2.send_keys(cat)
        # cat_name_input2.send_keys(Keys.ENTER)        
        # time.sleep(1)
        
        # self.assertEqual(User.objects.count(), 1)
        # self.assertEqual(Category.objects.count(), 2)
        
    
    ##User clicks button to add transaction
    ##User sees category transaction page: Cat name, monthly total, and crud options
    def test_user_sees_cat_interface(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/fantasticApp/catlist/brick/")
        )
        time.sleep(3)
        ##TBDDDDD
    # def test_user_can_modify category(self):
        # self.selenium.get(self.live_server_url)
        
       
     
     
     #USER IS PRESENTED WITH A TEXTBOX,'CATERGORY' AND A 2ND, AMOUNT(BOTH BLANK) AND AN OPTION FOR ADDING ADDITIONAL CATEGORIES
    # def test_user_can_add_category(self):
        # self.selenium.get(self.live_server_url)
        # nameInput = self.selenium.find_element_by_id('users_name')
        # usersName = 'Rowan'
        # nameInput.send_keys(usersName)
        # nameInput.send_keys(Keys.ENTER)
        # time.sleep(1)
        # #self.assertIn
        # cli = Client()
        
        # self.assertEqual(self.selenium.page_source, cli.post('/fantasticApp/setup/', {'item_text': 'Rowen'}))
         
    





    # def wait_for_text(self, text_item):
        # start_time = time.time()
        # while True:
            # try:
                # table = self.browser.find_element_by_id('id_list_table')
                # rows = table.find_elements_by_tag_name('tr')
                # self.assertIn(row_text, [row.text for row in rows])
                # return
            # except (AssertionError, WebDriverException) as e:
                # if time.time() - start_time > MAX_WAIT:
                    # raise e
                # time.sleep(0.5)
        
     
     ##Else IF (RETURNING USER)
     #User see previously save data
     
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

    # def test_get_index_pageenter_name_gives_appropriate_response(self):
        # #   self.selenium.get(f'{self.live_server_url}/fantasticApp/getnam/<str>/')
        # self.selenium.get(self.live_server_url)
        
        
        # time.sleep(3.5)
        # #self.selenium.get(self.live_server_url)
        # nameInput = self.selenium.find_element_by_id('id_new_item')
        # # The missing girl puts in her name
        # usersName = 'Rowan'
        # nameInput.send_keys(usersName)
        # nameInput.send_keys(Keys.ENTER)
        # time.sleep(3.5)
        # userNameInApp = self.selenium.find_element_by_tag_name('h2')
        # self.assertIn(usersName, userNameInApp.text) 
        #assert 'Rowan' in self.selenium.page_source

     # if it is the users first time they see predefined categories

     # if returning, they see their categories

     # the user returns and sees their budget categories as well, previously entered figures