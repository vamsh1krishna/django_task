from import_export import resources
from .models import Products

class ProductResource(resources.Resource):
    class Meta:
        model=Products
    ...