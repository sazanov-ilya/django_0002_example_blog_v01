# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


# python manage.py test
class BlogTests(TestCase):

    def setUp(self):
        """ setUp добавляется образец записи блога для тестирования и дальнейшего подтверждения,
            что строки и содержимое работают верно
        """
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        """ Тест функции __str__ модели Post
        """
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):  # new
        """ Предполагается, что URL для нашего теста — post/1/.
            Здесь только одна запись, и 1 — ее первичный ключ
        """
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        """  test_post_list_view
        """
        # test_post_list_view
        response = self.client.get(reverse('home'))
        # который подтверждает, что домашняя страница возвращает HTTP код состояния 200,
        self.assertEqual(response.status_code, 200)
        # содержит правильный текст в теге body
        self.assertContains(response, 'Nice body content')
        # и использует правильный шаблон home.html.
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        """ В конечном итоге test_post_detail_view проверяет,
            работает ли индивидуальная страница записи правильно
        """
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')

        # Корректная страница возвращает код 200,
        self.assertEqual(response.status_code, 200)
        # а поврежденная страница возвращает ошибку 404
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        # Чтобы протестировать представление для создания (create), создается новая запись
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })
        # Затем нужно убедиться, что ответ действительно получен (Код HTTP состояния 200)
        self.assertEqual(response.status_code, 200)
        # и содержит новый заголовок и тело статьи с текстом.
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        # Чтобы протестировать представление для обновления записи (update),
        # требуется получить доступ к первой записи, у которой pk равен 1,
        # который передается как единственный аргумент
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        # Затем подтверждается факт перенаправления с HTTP кодом 302
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        """ Тест удаления """
        response = self.client.post(
            reverse('post_delete', args='1'))
        #   После удаления записи должен появиться HTTP код состояния 302,
        #   и произведено перенаправление на главную страницу,
        #   так как удаленного элемента больше не существует
        self.assertEqual(response.status_code, 302)
