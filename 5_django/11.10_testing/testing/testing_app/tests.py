from django.test import SimpleTestCase

# Create your tests here.

#class of test inheriting from SimpleTestCase

class SimpleViewTests(SimpleTestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Welcome to the homepage!")
        
    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, "About us page.")

