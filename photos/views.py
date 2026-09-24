from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def add_photo(request: HttpRequest) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')


def photo_details(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-details-page.html')


def edit_photo(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')

