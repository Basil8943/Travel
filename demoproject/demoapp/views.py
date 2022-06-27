from django.shortcuts import render

# Create your views here.
from demoapp.models import shop,background,traditional,kerala


def home(request):
    dis=shop.objects.all()
    back=background.objects.all()
    trad=traditional.objects.all()
    ker=kerala.objects.all()
    return render(request,"home.html",{'mobile':dis,'backimg':back,'dance':trad,'kerala':ker})