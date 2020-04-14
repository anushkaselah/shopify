from django.http import HttpResponse
from.models import Product

# Create your views here.
def crud(reuest):
    pro=Product(name="Ankita",description="shoes",price="600.0",category="sports",discount="30.0",created_at="2020-12-04"
    )
    pro.save()
    anki=Product.objects.get(name="Ankita")
    anki.delete()

    objs =Product.objects.all()
    for obj in objs():
        print(Product.__str__(obj))
    
    return HttpResponse("Done")
        
    