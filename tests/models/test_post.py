import pytest

from blog.factories import Post

@pytest.fixture
def post_published():
    return Post(title='pytest with factory')


@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
