from django.shortcuts import redirect, render
from .forms import HashForm
from .models import HashModel
import hashlib
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try: 
                HashModel.objects.get(hash = text_hash)
            except HashModel.DoesNotExist:
                hash = HashModel()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash',hash = text_hash)

    form = HashForm()
    return render(request, 'hashing/home.html', {'form':form})

def hash(request, hash):
    hash = HashModel.objects.get(hash=hash)
    return render(request, 'hashing/hash.html', {'hash':hash})

def quickhash(request):
    text = request.GET['text']
    return JsonResponse({'hash':hashlib.sha256(text.encode('utf-8')).hexdigest()})


