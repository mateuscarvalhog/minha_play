from django.test import TestCase
from django.test import Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import Faixa
import time

# Create your tests here.
class UnitTests(TestCase):
    def setUp(self):
        Faixa.objects.create(nome="Crazy Train", artista="Ozzy Osbourne", url="https://www.youtube.com/watch?v=tMDFv5m18Pw", letra="Apenas para teste")

    def testingCreate(self):
        test = Faixa.objects.get(nome="Crazy Train")
        self.assertEqual(test.artista, "Ozzy Osbourne")
    
    def testingUpdate(self):
        test = Faixa.objects.get(nome="Crazy Train")
        test.nome = "Mr. Crowley"
        test.url = "https://www.youtube.com/watch?v=G3LvhdFEOqs"
        test.save()
        self.assertEqual(test.nome, "Mr. Crowley")
        self.assertEqual(test.url, "https://www.youtube.com/watch?v=G3LvhdFEOqs")
    
    def testingDelete(self):
        test = Faixa.objects.get(nome="Crazy Train")
        test.delete()

class IntegrationTests(TestCase):
    def setUp(self):
        self.c = Client()
        Faixa.objects.create(nome="Crazy Train", artista="Ozzy Osbourne", url="https://www.youtube.com/watch?v=tMDFv5m18Pw", letra="Apenas para teste")
    
    def testingFunctionalCreate(self):
        print(self.c.get('/createFaixa/'))
        
    def testingFunctionalRead(self):
        print(self.c.get('/readFaixa/'))

    def testingFunctionalUpdate(self):
        print(self.c.get('/updateFaixa/'))
    
    def testingFunctionalDelete(self):
        print(self.c.get('/deleteFaixa/'))

class SeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()
    
    def testingCreateSelenium(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_xpath('/html/body/div/button/a').click()
        
        nome = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/input')
        nome.send_keys('Bible Black')
        
        artista = self.browser.find_element_by_xpath('/html/body/div/form/div[2]/input')
        artista.send_keys('Heaven and Hell')
        
        numero = self.browser.find_element_by_xpath('/html/body/div/form/div[4]/input')
        numero.click()  # para autocomplete com Vagalume API e Ajax
        numero.send_keys('https://www.youtube.com/watch?v=EKyEbjcvUag')
        
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div/form/div[5]/button[1]').click()   

    def testingUpdateSelenium(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td[5]/a').click()
        
        numero = self.browser.find_element_by_xpath('/html/body/div/form/div[4]/input')
        numero.send_keys('&list=RDvjVkXlxsO8Q&index=2')
        
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div/form/div[5]/button[1]').click()
    
    def testingBrowseSelenium(self):
        self.browser.get('http://127.0.0.1:8000/')
        
        nome = self.browser.find_element_by_xpath('/html/body/div/div/form/input[2]')
        nome.send_keys('Rainbow')

        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div/div/form/button').click()
    
    def testingDeleteSelenium(self):
        self.browser.get('http://127.0.0.1:8000/')

        self.browser.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[5]/a').click()