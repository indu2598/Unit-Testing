from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib
from .models import HashModel
from django.core.exceptions import ValidationError
import time
# Create your tests here.

class FunctionalTestCase(TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r"C:\Users\shubham\Downloads\chromedriver_win32\chromedriver.exe")
    def test_thereIsHomePage(self):
        self.wd.get('http://localhost:8000/')
        self.assertIn("Enter text here",self.wd.page_source)
        # assert self.wd.page_source.find("Congratulations")
    
    def test_hashOfHello(self):
        self.wd.get('http://localhost:8000/')
        text = self.wd.find_element_by_id('id_text')
        text.send_keys("hello")
        self.wd.find_element_by_name('submit').click()
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',self.wd.page_source)
    
    def test_hashAjax(self):
        self.wd.get('http://localhost:8000/')
        text = self.wd.find_element_by_id('id_text')
        text.send_keys("hello")
        time.sleep(5)
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.wd.page_source)

    def tearDown(self):
        self.wd.quit()
    


class UnitTestCase(TestCase):
    def test_home_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response,'hashing/home.html')
    
    def test_hashForm(self):
        form = HashForm(data = {'text': "hello"})
        self.assertTrue(form.is_valid())

    def test_hashFuncWork(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',text_hash)
    
    def saveHash(self):
        hash = HashModel()
        hash.text="hello"
        hash.hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        hash.save()
        return hash

    def test_hashObject(self):
        hash = self.saveHash()
        pulled_hash = HashModel.objects.get(hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
        self.assertEqual(hash.text , pulled_hash.text)

    def test_viewingHash(self):
        hash = self.saveHash()
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response,'hello')

    def test_badHash(self):
        def badHash():
            hash = HashModel()
            hash.hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824jkfjdkgdfkg"
            hash.full_clean()
        self.assertRaises(ValidationError, badHash)
