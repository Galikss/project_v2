from django_elasticsearch_dsl import DocType, Index
from ecomapp.models import Product

products = Index("products")

@products.doc_type
class ProductDocument (DocType):
    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'description',
            'image',

        ]
