from django.shortcuts import render
from .models import Memory, BabyPhoto, OurPhoto

def home(request):
    return render(request, 'love_site/home.html')

def main_site(request):
    return render(request, 'love_site/main.html')

def memories(request):
    memories_list = Memory.objects.all().order_by('-created_date')
    return render(request, 'love_site/memories.html', {'memories': memories_list})

def gallery(request):
    # Получаем фото из обеих моделей
    baby_photos = BabyPhoto.objects.all().order_by('-uploaded_date')
    our_photos = OurPhoto.objects.all().order_by('-uploaded_date')
    
    # Создаем список кортежей (фото, тип)
    all_photos = []
    
    for photo in baby_photos:
        all_photos.append({
            'photo': photo,
            'type': 'baby',
            'image_url': photo.image.url,
            'title': photo.title,
            'description': photo.description,
            'uploaded_date': photo.uploaded_date
        })
    
    for photo in our_photos:
        all_photos.append({
            'photo': photo,
            'type': 'our',
            'image_url': photo.image.url,
            'title': photo.title,
            'description': photo.description,
            'uploaded_date': photo.uploaded_date
        })
    
    # Сортируем по дате
    all_photos.sort(key=lambda x: x['uploaded_date'], reverse=True)
    
    return render(request, 'love_site/gallery.html', {'photos': all_photos})

def treasure(request):
    photos = BabyPhoto.objects.all().order_by('-uploaded_date')
    return render(request, 'love_site/treasure.html', {'photos': photos})

def our_photos(request):
    photos = OurPhoto.objects.all().order_by('-uploaded_date')
    return render(request, 'love_site/our_photos.html', {'photos': photos})

def secret(request):
    if request.method == 'POST':
        if request.POST.get('password') == 'мяу':
            return render(request, 'love_site/secret_message.html')
        else:
            return render(request, 'love_site/secret.html', {'error': 'Неверный пароль'})
    return render(request, 'love_site/secret.html')