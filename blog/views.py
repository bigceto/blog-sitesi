from django.shortcuts import render,HttpResponse

def post_list (request):
    selam = "Burada Gönderiler Listelenir"
    return HttpResponse (selam)

def post_update (request):
    selam1 = "Burada Gönderi Güncellenecektir"
    return HttpResponse (selam1)

def post_delete (request):
    selam2 = "<b>Burada Gönderi Silinecektir</b>"
    return HttpResponse (selam2)

def post_create (request):
    selam3 = "<b>Burada Gönderiler Eklenir</b>"
    return HttpResponse (selam3)


def sanatcilar(request, sayi):
    sanatcilar_sozluk = {
        '1':    'Eminem',
        '2':    'Sila',
        '3':    'Sezen Aksu',
        '4':    'Ahmet Kaya',
        '5':    'Teoman',
        '6':    'Tarkan',
        '7':    'Clean Bandit',
        '8':    'Anne Marie',
        '9':    'Beyonce',
        'eminem':   "without me"
    }


    sanatci=sanatcilar_sozluk.get(sayi,"Bu id numarasına ait sanatci bulunamadi")
    return HttpResponse (sanatci)