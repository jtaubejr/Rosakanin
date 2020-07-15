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
    return render(request, 'compendiums/Negan/negan.html', {'title': 'Negan'})

def neganGrabs(request):
    return render(request, 'compendiums/Negan/neganGrabs.html', {'title': 'Negan Grabs'})

def neganPunishment(request):
    return render(request, 'compendiums/Negan/neganPunishment.html', {'title': 'Negan Punishment'})

def neganCombos(request):
    return render(request, 'compendiums/Negan/neganCombos.html', {'title': 'Negan Combos'})

def neganWall(request):
    return render(request, 'compendiums/Negan/neganWall.html', {'title': 'Negan Wall/Floor Stuff'})

#This is the Nina Williams pageself.
def nina(request):
    return render(request, 'compendiums/nina.html', {'title': 'Nina'})

#This is the Zafina pageself.
def zafina(request):
    return render(request, 'compendiums/zafina.html', {'title': 'Zafina'})

#This is the Seth pageself. =======================SFV=========================
def seth(request):
    return render(request, 'compendiums/Seth/seth.html', {'title': 'Seth'})

def sethCombos(request):
    return render(request, 'compendiums/Seth/sethCombos.html', {'title': 'Seth Combos'})
