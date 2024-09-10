from django.http import JsonResponse
from .models import Cat
from django.views.decorators.csrf import csrf_exempt
import json

def get_cats(request):
    cats = Cat.objects.all().values('id', 'name', 'age', 'breed')
    return JsonResponse(list(cats), safe=False)

# Insert cat into database with user defined custom parameters if request is POST
@csrf_exempt
def insert_cat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cat = Cat(name=data['name'], age=data['age'], breed=data['breed'])
        # cat = Cat(name=request.POST['name'], age=request.POST['age'], breed=request.POST['breed'])
        cat.save()
        return JsonResponse({'message': 'Cat inserted successfully!'})
    else:
        return JsonResponse({'message': 'Invalid request method!'})
