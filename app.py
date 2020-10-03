from random import choice
from flask import Flask, render_template, session


app = Flask(__name__)
app.debug = True
app.secret_key = 'serfvsrjkhghgv djghrghb sd hsgbkgh aerkg   r'
@app.route('/')
def vyber():
    return render_template("vyber.html")




@app.route('/kamen')
def kamen():
    Prohra = "Prohra"
    Vyhra = "Výhra"
    Remiza = "Remíza"
    cervena = "red"
    zelena = "green"
    nic = "blue"
    vysledek = choice([Prohra, Vyhra, Remiza])
    if not 'vr_hr' in session:
        session['vr_hr'] = 0


    if not 'vr_pc' in session:
        session['vr_pc'] = 0

    if not 'vr_no' in session:
        session['vr_no'] = 0


    hrac = "Kámen"
    pocitac = choice(["Kámen", "Nůžky", "Papír"])
    if pocitac == "Papír":
        vysledek = Prohra
        barva = cervena
        session['vr_pc'] = session['vr_pc']+1
    if pocitac == "Nůžky":
        vysledek = Vyhra
        barva = zelena
        session['vr_hr'] = session['vr_hr']+1
    if pocitac == "Kámen":
        vysledek = Remiza
        barva = nic
        session['vr_no'] = session['vr_no']+1


    return render_template("hra.html",pocitac=pocitac,hrac=hrac,vysledek=vysledek,barva=barva,pc=session['vr_pc'],hr=session['vr_hr'],no=session['vr_no'])

@app.route('/nuzky')
def nuzky():
    Prohra = "Prohra"
    Vyhra = "Výhra"
    Remiza = "Remíza"
    cervena = "red"
    zelena = "green"
    nic = "blue;"
    if not 'vr_no' in session:
        session['vr_no'] = 0

    vysledek = choice([Prohra, Vyhra, Remiza])
    if not 'vr_hr' in session:
        session['vr_hr'] = 0


    if not 'vr_pc' in session:
        session['vr_pc'] = 0


    hrac = "Nůžky"
    pocitac = choice(["Kámen", "Nůžky", "Papír"])
    if pocitac == "Papír":
        vysledek = Vyhra
        barva = zelena
        session['vr_hr'] = session['vr_hr']+1
    if pocitac == "Nůžky":
        vysledek = Remiza
        barva = nic
        session['vr_no'] = session['vr_no']+1
    if pocitac == "Kámen":
        vysledek = Prohra
        barva = cervena
        session['vr_pc'] = session['vr_pc']+1
    return render_template("hra.html",pocitac=pocitac,hrac=hrac,vysledek=vysledek,barva=barva,pc=session['vr_pc'],hr=session['vr_hr'],no=session['vr_no'])

@app.route('/papir')
def papir():
    Prohra = "Prohra"
    Vyhra = "Výhra"
    Remiza = "Remíza"
    cervena = "red"
    zelena = "green"
    nic = "blue"
    if not 'vr_no' in session:
        session['vr_no'] = 0

    vysledek = choice([Prohra, Vyhra, Remiza])
    if not 'vr_hr' in session:
        session['vr_hr'] = 0


    if not 'vr_pc' in session:
        session['vr_pc'] = 0


    hrac = "Papír"
    pocitac = choice(["Kámen", "Nůžky", "Papír"])
    if pocitac == "Papír":
        vysledek = Remiza
        barva = nic
        session['vr_no'] = session['vr_no']+1
    if pocitac == "Nůžky":
        vysledek = Prohra
        barva = cervena
        session['vr_pc'] = session['vr_pc']+1
    if pocitac == "Kámen":
        vysledek = Vyhra
        barva = zelena
        session['vr_hr'] = session['vr_hr']+1
    return render_template("hra.html",pocitac=pocitac,hrac=hrac,vysledek=vysledek,barva=barva,pc=session['vr_pc'],hr=session['vr_hr'],no=session['vr_no'])

if __name__ == '__main__':
    app.run()
