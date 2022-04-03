from django.test import RequestFactory
from django.urls import reverse
from blog.views import post_detail, post_list, weAreInMedia
from mixer.backend.django import mixer
from blog.models import Post as modelPost
import pytest
import blog


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
        path = reverse('blog:post_detail', kwargs = {
            'year' : 2020,
            'month' : 7,
            'day' : 16,
            'post' : 'pokori-lunu-vmeste-s-lunar-zebro'})
        request = RequestFactory().get(path)
        response = post_detail(request, year='2020', month='7', day='16', post='pokori-lunu-vmeste-s-lunar-zebro')
        
        assert response.status_code == 200



