import factory

from .models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    is_active = factory.Iterator([True, False])
    
    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('pystr')
    price = factory.Faker('pyint', min_value=0, max_value=1000)
    is_active = factory.Iterator([True, False])
    category = factory.LazyAttribute(CategoryFactory)
    
    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for category in extracted:
                self.category.add(category)
    
    class Meta:
        model = Product