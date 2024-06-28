import pytest

from app.kuma.models import Producto, Categoria

@pytest.mark.django_db
def test_product_creation():

    category, created = Categoria.objects.get_or_create(nombre='HDD')
    product = Producto.objects.create(
        sku=123,
        nombre='Producto',
        descripcion='Un producto',
        stock = 1200,
        precio = 2300,
        categoria_id= category,
        imagen_url='C:/Users/marce/Downloads/1000-anverso'

    )
    assert product.nombre == 'Producto'
    
@pytest.mark.django_db
def test_category_creation():

    category = Categoria.objects.create(
        nombre = 'Nueva'
    )
    assert category.nombre == 'Nueva'