from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders
from destination_dog.models import Article, Dotm, Dog, Event, Service


#class GeneralTests(TestCase):
    #def test_serving_static_files(self):
     #   """
     #   If using static media result is not NONE once it finds blah.jpg.
     #   If not using static media, delete this test
     #   """
    #    result = finders.find('images/blah.jpg')
    #    self.assertIsNotNone(result)

class HomePageTests(TestCase):
    def test_home_using_template(self):
        """
        Check the template used to render home page
        """
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'destination_dog/home.html')

    def test_index_contains_message(self):
        """
        Check if there is the message 'all about the destination'
        """
        response = self.client.get(reverse('home'))
        self.assertIn(b'all about the destination', response.content)

    #def test_dog_picture_displayed(self):
        """
        Check if there's an image called 'blah.jpg' on the home page
        """
     #   response = self.client.get(reverse('home'))
     #   self.assertIn(b'img src="/static/images/blah.jpg', response.content)

    def test_index_has_title(self):
        """
        Check to make sure that the title tag has been used and
        template contains html
        """
        response = self.client.get(reverse('home'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title', response.content)

class AboutPageTests(TestCase):
    def test_about_contains_create_message(self):
        """
        Check if the about page is there, and it contains the specified message
        'DestinationDog will provide advice and guidance to prospective owners'
        """
        response = self.client.get(reverse('about'))
        self.assertIn(b'DestinationDog will provide advice and guidance to prospective owners', response.content)

    #def test_about_contain_image(self):
    #    """
    #    If we have an image on the about page, otherwise delete.
    #    Check is there is an image on the about page.
    #    """
    #    response = self.client.get(reverse('about'))
    #    self.assertIn(b'img src="/media/', response.content)

    def test_about_using_template(self):
        """
        Check the template used to render about page
        """
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'destination_dog/about.html')

class ModelTests(TestCase):

    def setUp(self):
        """
        Check that the population script exists and is correct
        """
        try:
            from population_script import populate
            populate()
        except ImportError:
            print('The module population_script does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_article(self, name):
        """
        Check that article is present in the database
        """
        try:
            article = Article.objects.get(name=name)
        except Article.DoesNotExist:
            article = None
        return article

    def get_dog_of_the_month(self, dog):
        """
        Check that the dog of the moment exists
        """
        try:
            dotm = Dotm.objects.get(dog=dog)
        except Dotm.DoesNotExist:
            dotm = None
        return dotm

    def get_event(self, name):
        """
        Check that event exists
        """
        try:
            event = Event.objects.get(name=name)
        except Event.DoesNotExist:
            event = None
        return event

    def get_service(self, name):
        """
        Check that service exists
        """
        try:
            service = Service.objects.get(name=name)
        except Service.DoesNotExist:
            service = None
        return service

    def get_dog(self, name):
        """
        Check that dog exists
        """
        try:
            dog = Dog.objects.get(name=name)
        except Dog.DoesNotExist:
            dog = None
        return dog

    def test_adopt_dog_article(self):
        article = self.get_article('Adopt A Dog')
        self.assertIsNotNone(article)


    # # def test_slug_line_creation(self):
    #"""
   #slug_line_creation checks to make sure that when we add an article
   #an appropriate slug line is created
    #"""
