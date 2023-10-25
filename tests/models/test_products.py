import pytest

from product.factories import ProductFactory

@pytest.fixture
def product_creation():
    return ProductFactory(name='MyProduct', price=20.99)

@pytest.mark.django_db
def test_create_product(product_creation):
    assert product_creation.name == 'MyProduct'