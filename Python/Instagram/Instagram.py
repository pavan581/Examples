#Ecxcutable file of the respected webdriver should be in the path

from selenium import webdriver
from random import randint
from time import sleep

class Instagram(object):
    
    def __init__(self):
        
        #web selectors
        self.selectors = {
            "username_field"    : "username",
            "password_field"    : "password",
            "search_user"       : "queryBox",
            "textarea"          : "textarea",
            "notnow"            : "body > div:nth-child(20) > div > div > div > div.mt3GC > button.aOOlW.HoLwm",
            "next"              : "body > div.RnEpo.Yx5HN > div > div > div:nth-child(1) > div > div:nth-child(3) > div > button",
            "textarea"          : "//*[@id=\"react-root\"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea",
            "button_login"      : "#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > button",
            "select_user"       : "body > div.RnEpo.Yx5HN > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd > div.Igw0E.IwRSH.eGOV_.vwCYk._3wFWr > div:nth-child(1) > div > div.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button",
            "send"              : "#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_._4EzTm.JI_ht > button"
            
            }

        #initialising web driver
        self.driver = webdriver.Edge()
        self.driver.set_window_position(0,0)
        self.driver.set_window_size(500,740)

        #opening instagram in the browser
        self.driver.get('https://instagram.com')
        self._randomsleep()
        
    #Login to your instagram account
    def login(self, username, password):
    
        if len(password) < 6:
            print("Invalid password")
            return True

        #Passing username and password and clicking Log in button
        self.driver.find_element_by_name(self.selectors['username_field']).send_keys(username)
        self.driver.find_element_by_name(self.selectors['password_field']).send_keys(password)
        self.driver.find_element_by_css_selector(self.selectors['button_login']).click()
        
        self._randomsleep(6,10)

        #Checking for successful login
        if self.driver.current_url != 'https://www.instagram.com/':
            print("Logged in.")
            return False
        else:
            print("Login failure. Check your username or password.")
            return True
        self._randomsleep(1,5)

    #select the user to send the message
    def selectUser(self,user):

        try:
            self.driver.get('https://www.instagram.com/direct/new/')
            self._randomsleep()

            #search for the user
            self.driver.find_element_by_name(self.selectors['search_user']).send_keys(user)
            self._randomsleep(8,10)

            #Handling the popup for Notification permission
            while True:
                self._randomsleep(5,8)
                try:
                    self.driver.find_elements_by_css_selector(self.selectors['select_user'])[0].click()
                    self._randomsleep(3,5)
                    break
                except:
                    
                    try:
                        notNow = self.driver.find_elements_by_css_selector(self.selectors['notnow'])
                        notNow[0].click()
                    except Exception as e:
                        print(e)
    
            self.driver.find_elements_by_css_selector(self.selectors['next'])[0].click()
            self._randomsleep(1,5)
            
        except:
            print("Error getting the user.")
            return False
        else:
            print("User found.")
            return True

        
    #Send the message
    def sendMsg(self,message):
        
        self._randomsleep(1,2)
        self.driver.find_elements_by_xpath(self.selectors['textarea'])[0].send_keys(message)
        self._randomsleep(1,2)
        try:
            self.driver.find_elements_by_css_selector(self.selectors['send'])[0].click()
        except Exception as e:
            print(e)
        else:
            print("Message sent.({})".format(message))

    #Closing the window(s) after usage
    def closeBrowser(self):
        self.driver.quit()

    #Method to generate random sleep time
    def _randomsleep(self, _min=4, _max=10):
        t = randint(_min, _max)
        sleep(t)
