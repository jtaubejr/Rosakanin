from django.shortcuts import render

#This is the homepage.
def home(request):
    return render(request, 'compendiums/home.html', {'title': 'Homepage'})

#This is the Anna Williams page.
def anna(request):
    return render(request, 'compendiums/anna.html', {'title': 'Anna Williams'})

#This is the Armor King page.
def armor_king(request):
    return render(request, 'compendiums/armor_king.html', {'title': 'Armor King'})

#This is the Eliza page.
def eliza(request):
    return render(request, 'compendiums/eliza.html', {'title': 'Eliza'})

#This is the Julia Chang pageself.
def julia(request):
    return render(request, 'compendiums/julia.html', {'title': 'Julia Chang'})

#This is the Leo Kliesen pageself.
def leo(request):
    return render(request, 'compendiums/leo.html', {'title': 'Leo Kliesen'})

#This is the Negan pageself.
def negan(request):
    return render(request, 'compendiums/negan.html', {'title': 'Negan'})

#This is the Zafina pageself.
def zafina(request):
    return render(request, 'compendiums/zafina.html', {'title': 'Zafina'})
