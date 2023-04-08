from django.shortcuts import render
from .models import main_card, akustikamain, aksessuarmain, phonemain, maintext
from .forms import UsersForm


def macbro(request):
    product = main_card.objects.all()
    akustika = akustikamain.objects.all()
    aksessuar = aksessuarmain.objects.all()
    phone = phonemain.objects.all()
    textfooter = maintext.objects.all()
    return render(request, "main/macbro-glavniy.html", {"product": product,
                                                        "akustika": akustika,
                                                        "aksessuar": aksessuar,
                                                        "phone": phone,
                                                        "text": textfooter})
