from django.test import RequestFactory
from django.urls import reverse
from blog.views import post_detail, post_list, weAreInMedia
from mixer.backend.django import mixer
import pytest
from blog.models import Post


@pytest.mark.django_db
class TestViews:

    def test_post_list(self):
        path = reverse('blog:post_list') 
        request = RequestFactory().get(path)

        response = post_list(request)
        assert response.status_code == 200

    def test_weAreInMedia(self):
        path = reverse('blog:media_notes') 
        request = RequestFactory().get(path)

        response = weAreInMedia(request)
        assert response.status_code == 200

    def test_post_detail(self):
        post = Post.published.latest('publish')
        path = reverse('blog:post_detail', kwargs = {
            'year' : post.year,
            'mounth' : post.month,
            'day' : post.day,
            'slug' : post.slug})
        request = RequestFactory().get(path)

        response = post_detail(request, post.year, post.month, post.day, post.slug)
        assert response.status_code == 200
        

