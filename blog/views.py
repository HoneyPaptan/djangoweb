from django.shortcuts import render
from .models import blogPost, mainedits

def home(request):
    mainedit = mainedits.objects.all()
    
    blog = blogPost.objects.all()
    blogpost = blogPost.objects.get(pk=1)
    context={
        'mainedit': mainedit, 
      'blog':blog,
      'blogpost':blogpost,
    
    } 

    
    return render(request, "home.html", context)
def about(request):
    return render(request, "about.html")
def blogs(request):
    blog = blogPost.objects.all()
    context  ={
        'blog': blog
    }

   
   


    
    
    return render(request, "blogs.html", context)
def newsletter(request):
    return render(request, "newsletter.html")



def searched(request):
    if request.method == 'POST':
      title= request.POST["searchedblog"]
     
    
    searched = blogPost.objects.get(title=title)

    context = {
        'searched': searched
    }

    return render(request, "searched.html", context)



def blog(request,slug):
    details = blogPost.objects.get(slug=slug)
   
   
    # blogpost = blogPost.objects.get(pk=1)
    context={
       
      'details':details,
      
      
    
    } 
  
  
    return render(request, "blog.html", context)
