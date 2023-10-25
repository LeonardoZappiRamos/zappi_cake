import pytest

from order.factories import OrderFactory

@pytest.fixture
def order_creation():
    return OrderFactory()

@pytest.mark.django_db
def test_create_product(order_creation):
    order = OrderFactory()
    assert type(order_creation) == type(order) 