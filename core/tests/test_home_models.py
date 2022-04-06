import pytest
from home.models import MainPageStatisticNumber, KeyPublications, FamousGraduates
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_note_in_media_models():
    static_number = MainPageStatisticNumber.objects.create(
        number="404", description="pytest"
    )

    assert static_number.number == "404"
    assert static_number.description == "pytest"


@pytest.mark.django_db
def test_key_publications_model():
    article = KeyPublications.objects.create(
        title="pytest-title",
        journal="pytets-science",
        publicationUrl="https://pytest.com",
    )

    assert article.title == "pytest-title"
    assert article.publicationUrl == "https://pytest.com"
