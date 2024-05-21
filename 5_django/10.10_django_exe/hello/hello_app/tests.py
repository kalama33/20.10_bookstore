from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here

class HomePageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')
        
    def test_template_content(self):
        response = self.client.get(reverse('home'))
        print(response.status_value)
        print(response.content)
        self.assertContains(response,'<h1>Homepage<h1>')
        self.assrtIn(b'<h1>Homepage<h1>', response.content)
        

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('about/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response,'about.html')
        
    def test_template_content(self):
        response = self.client.get(reverse('about'))
        print(response.status_value)
        print(response.content)
        self.assertContains(response,'<h1>About page<h1>')
        self.assrtIn(b'<h1>About page<h1>', response.content)