from django.shortcuts import render
from django.http import JsonResponse
from .models import ProjectModel

def home(request):

    data = ProjectModel.objects.first()
    likes = data.like
    dislikes = data.dislike
    
    context = {'like':likes , 'dislike' : dislikes}

    return render(request , 'templates/home.html' , context)


def like(request):
    data = ProjectModel.objects.first()
    data.like += 1
    data.save()

    # print(data.like)
    # print(data.dislike)

    context = {"like":data.like , "dislike" : data.dislike}


    return JsonResponse(context)

def dislike(request):
    data = ProjectModel.objects.first()
    data.dislike += 1
    data.save()
    context = {"like":data.like , "dislike" : data.dislike}


    return JsonResponse(context)

