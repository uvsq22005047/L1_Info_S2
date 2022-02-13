#librairie
import tkinter as tk

#création des variables globals et des constantes
LARGEUR_CADRE = 500
HAUTEUR_CADRE = 500
fond_couleur = "black"
x0_CARRE, y0_CARRE, x1_CARRE, y1_CARRE = LARGEUR_CADRE/2-50, HAUTEUR_CADRE/2-50, LARGEUR_CADRE/2+50, HAUTEUR_CADRE/2+50
couleur_carre = "red"

#création de la fenetre graphique
fenetre = tk.Tk()

#créations des fonctions
def clic(event):
    """
    le carré change de couleur entre le bleu et le rouge à chaque clic.
    Si on clic en dehors du carré, ce dernier ce fige et ne peut plus changer de couleur
    """
    global couleur_carre
    if x0_CARRE < event.x < x1_CARRE and y0_CARRE < event.y < y1_CARRE:
        if couleur_carre == "red":
            couleur_carre = "blue"
        else:
            couleur_carre = "red"   
        cadre.itemconfigure(carre, fill=couleur_carre)
    else:
        cadre.unbind("<Button-1>")


def recommencer():
    """
    réinitialise tous depuis le début
    """
    global couleur_carre
    couleur_carre = "red"
    cadre.itemconfigure(carre, fill=couleur_carre)
    cadre.bind("<Button-1>", clic)


#créations des widgets
cadre = tk.Canvas(fenetre, width=LARGEUR_CADRE, height=HAUTEUR_CADRE, bg=fond_couleur)
button_recommencer = tk.Button(fenetre, text="Recommencer", command=recommencer)

#création des items
carre = cadre.create_rectangle(x0_CARRE, y0_CARRE, x1_CARRE, y1_CARRE, fill=couleur_carre)

#positionement des widget
cadre.grid()
button_recommencer.grid()

#liaison d'un evénement sur un widget à une fonction
cadre.bind("<Button-1>", clic)

#lancement de la fenetre grafique
fenetre.mainloop()