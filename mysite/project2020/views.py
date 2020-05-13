from django.shortcuts import render

def index(request):
    template = loader.get_template('project2020/style.css')
    context = {
    'lat' : 1
    }
    return HttpResponse(template.render(context, request))
