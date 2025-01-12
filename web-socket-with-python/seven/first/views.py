from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def hello(request):
    return HttpResponse('hello def is run')

def user(request):
    data={
       'contex': [
            {'name':'pooya',
                 'age':20,
                 'gen':'mel'
            },
            {'name':'ahmad',
                 'age':20,
                 'gen':'mel'
            },
            {'name':'sahar',
                 'age':23,
                 'gen':'famel'
            },
            {'name':'sadaf',
                 'age':23,
                 'gen':'famel'
            }
        ]
    }
    return render(request,'index.html',data)