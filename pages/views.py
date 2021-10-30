from django.shortcuts import render, redirect
from pages.models import Page

   
def pages_slug(request, slug):
    url = '/' + slug + '/'
    print(url)
    try:
        page = Page.objects.get(url=url)
        print(page)
        template = 'pages/default.html'
        
        context = {
            'page': page
        }
        return render(request, template, context)
    except Page.DoesNotExist:
        return redirect('/')
        
