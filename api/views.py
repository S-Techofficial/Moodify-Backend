from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'info': 'Music Website', 'members': ['Sumit', 'Devansh', 'Shashikant']})
