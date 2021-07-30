from django.test import TestCase

# Create your tests here.
#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Testing
from courses.models import LearningPath

class LearningPathModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        LearningPath.objects.create(title="This is a title",description="An this the description",active_flag=True)
        
    def test_title_label(self):
        title=LearningPath.objects.get(id=1)
        field_label = LearningPath._meta.get_field('title').verbose_name
        self.assertEqual(field_label,'title')
    
    def test_description_label(self):
        description=LearningPath.objects.get(id=1)
        field_label = LearningPath._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'description')
    
    def test_title_max_length(self):
        title=LearningPath.objects.get(id=1)
        max_length = LearningPath._meta.get_field('title').max_length
        self.assertEqual(max_length,50)
    
    def test_active_flag_default_value(self):
        object = LearningPath.objects.get(id=1)
        self.assertTrue(object.active_flag)