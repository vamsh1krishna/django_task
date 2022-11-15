# django_task

one can access all products http://localhost:8000/products/


one can search with <product_name> with POST method at http://localhost:8000/product_search/
      with payload {
                   "product" : "product_name"                    
              }
returns first 5 values with given product name


search product with <product_name> with GET method at http://localhost:8000/product_details/?product=product_name
