import pytest

from api.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
        email="dark.melocoto@bol.com.br",
        username="d4rk_mecoto",
        user_pass="iloveliverpo@777",
        first_name="Paulin",
        last_name="Pinho",
        country="Brasil",
        state="Bahia",
        city="Xique-Xique",
        postal_code="12345-789",
        address="R. dos Otarios, nº00"
    )

    assert user.username == "d4rk_mecoto"
    assert user.first_name == "Paulin"
    assert user.country == "Brasil"
    assert user.city == "Xique-Xique"
    assert user.id is not None


