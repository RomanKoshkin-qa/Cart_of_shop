"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        #  напишите проверки на метод check_quantity
        assert product.check_quantity(100) is True
        assert product.check_quantity(1001) is False
        assert product.check_quantity(999) is True

    def test_product_buy(self, product):
        #  напишите проверки на метод buy
        product.buy(200)
        assert product.quantity == 800

    def test_product_buy_more_than_available(self, product):
        #  напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1200)

class TestCart:
    """
     Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product):
        cart = Cart()
        cart.add_product(product, 4)
        assert cart.products[product] == 4
    def test_remove_product(self, product):
        cart = Cart()
        cart.add_product(product, 4)
        cart.remove_product(product, 1)
        assert cart.products[product] == 3
        cart2 = Cart()
        cart2.add_product(product, 4)
        cart2.remove_product(product, 6)
        assert product not in cart2.products
        cart3 = Cart()
        cart3.add_product(product, 4)
        cart3.remove_product(product)
        assert product not in cart3.products
        cart4 = Cart()
        cart4.add_product(product, 4)
        cart4.remove_product(product,4)
        assert product not in cart4.products
    def test_clear(self, product):
        cart = Cart()
        cart.add_product(product, 4)
        cart.clear()
        assert cart.products == {}
    def test_get_total_price(self,product):
        cart = Cart()
        cart.add_product(product, 4)
        total = cart.get_total_price()
        assert total == 400

    def test_buy(self,product):
        cart = Cart()
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()
        cart2 = Cart()
        cart2.add_product(product, 3)
        cart2.buy()
        assert cart2.products== {}
        assert product.quantity == 997