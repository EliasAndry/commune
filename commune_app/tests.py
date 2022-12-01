import pytest

from . import models 


USER_ID = 209908173
USER_FIRST_NAME = "Elias"
USER_LAST_NAME = "Assy"
USER_EMAIL = "elias.a-98@outlook.com"
USER_PHONE_NUMBER = "+972543821183"

CHORE_TITLE = "Dishes"
CHORE_DATE = (1997, 10, 19)
CHORE_DESCRIPTION = "Clean the Dishes"
CHORE_ASSIGN = "Elias"


@pytest.fixture
def user1():
    return models.User(
        id=USER_ID,
        first_name=USER_FIRST_NAME,
        last_name=USER_LAST_NAME,
        email=USER_EMAIL,
        phone_number=USER_PHONE_NUMBER
    )


@pytest.fixture
def chore0(user1):
    return models.Chore(title=CHORE_TITLE, date=CHORE_DATE, description=CHORE_DESCRIPTION, assign=user1)


class TestChoreModel:
    def test_new_chore(self, chore0):
        assert chore0.title == CHORE_TITLE
        assert chore0.date == CHORE_DATE
        assert chore0.description == CHORE_DESCRIPTION
        assert chore0.assign.first_name == "Elias"
        assert len(chore0.title) <= 50
        assert len(chore0.description) <= 300

    @pytest.mark.django_db()
    def test_get_chore_by_title(self, user1, chore0):
        user1.save()
        chore0.save()
        assert models.Chore.get_chore_by_title("Dishes") == chore0
