from django.test import TestCase

# Create your tests here.
#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Testing
from comments.models import Comment,AnswerComment
from users.models import User
from courses.models import LearningPath, Course, Lesson

class CommentModelTest(TestCase):
    
    @classmethod

    def setUpTestData(cls):
        #Set up foreign keys test objects
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_learning_path = LearningPath.objects.create(title='Test LearningPath',active_flag=True)
        test_course =  Course.objects.create(title='Test Course',duration=1,teacher=test_user,learning_path=test_learning_path,active_flag=True)
        test_lesson = Lesson.objects.create(title='Test Lesson', teacher=test_user,course=test_course)

        #Create a Comment and a AnswerComment
        test_comment = Comment.objects.create(user=test_user,lesson=test_lesson,body="This is a test comment",active_flag=True)
        AnswerComment.objects.create(user=test_user,comment=test_comment,body="This is a test answer comment",active_flag=True)
    
     
    def test_comment_body_content(self):
        test_comment = Comment.objects.get(id=1)
        comment_body_content = test_comment.body
        self.assertEqual(comment_body_content,'This is a test comment')
    
    def test_answer_comment_body_content(self):
        test_answer_comment = AnswerComment.objects.get(id=1)
        answer_comment_body_content = test_answer_comment.body
        self.assertEqual(answer_comment_body_content,'This is a test answer comment')
    
    '''
    LABEL TESTS TO DO
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
        object = Comment.objects.get(id=1)
        self.assertTrue(object.active_flag)

    '''