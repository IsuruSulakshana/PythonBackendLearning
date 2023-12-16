from django.shortcuts import render

# Create your views here.
def posts(request):
    return render(request,'posts.html')

def post(request,pid):
    return render(request,'post.html')

