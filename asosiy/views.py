from django.shortcuts import render
from.models import *
def home(sorov):
    return render(sorov,'home.html')



def blog(sorov):
    content = {
        "maqolalar": Maqola.objects.all()

    }
    return render(sorov,'blog.html',content)

# Vazifa
# 1-topshiriq . maqola.htmldan foydalanib tanlangan maqolaning matnini ko'rsatuvchi view yozing.

def maqola(sorov, maqola_id):
    maqola = Maqola.objects.get(id=maqola_id)
    content = {
        "maqola": maqola
    }
    return render(sorov, 'maqola.html', content)


# 2-topshiriq about.html dagi ma'lumotlar o'rniga o'zingizga tegishli ma'lumotlarni yozib chiqing.
# static fayllarni bog'lang.

def about(sorov):
    return render(sorov,'about.html')
# 3-topshiriq Loyihani github akkauntingizga joylab linkini yuboring.