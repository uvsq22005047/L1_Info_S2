#librairie
import tkinter as tk

#création des variables globals et des constantes
LARGEUR_CADRE = 500
HAUTEUR_CADRE = 500
fond_couleur = "white"
couleur = ["green", "yellow", "blue", "black"]
x0_CARRE_VERT, y0_CARRE_VERT, x1_CARRE_VERT, y1_CARRE_VERT = 0, 0, 50, 50
x0_CARRE_JAUNE, y0_CARRE_JAUNE, x1_CARRE_JAUNE, y1_CARRE_JAUNE = 50, 0, 100, 50
x0_CARRE_BLEU, y0_CARRE_BLEU, x1_CARRE_BLEU, y1_CARRE_BLEU = 100, 0, 150, 50
x0_CERCLE, y0_CERCLE, x1_CERCLE, y1_CERCLE = LARGEUR_CADRE/2-50, HAUTEUR_CADRE/2-50, LARGEUR_CADRE/2+50, HAUTEUR_CADRE/2+50
historique = []

#création de la fenetre graphique
fenetre = tk.Tk()

#créations des fonctions
def clic(event):
    """
    lorsque l'on clic sur un carré, le cercle prend la même couleur que ce dernnier
    """
    if x0_CARRE_VERT < event.x < x1_CARRE_VERT and y0_CARRE_VERT < event.y < y1_CARRE_VERT:
        historique.append(cadre.create_oval(LARGEUR_CADRE/2-50, HAUTEUR_CADRE/2-50,
         LARGEUR_CADRE/2+50, HAUTEUR_CADRE/2+50, fill=couleur[0]))
    elif x0_CARRE_JAUNE < event.x < x1_CARRE_JAUNE and y0_CARRE_JAUNE < event.y < y1_CARRE_JAUNE:
        historique.append(cadre.create_oval(LARGEUR_CADRE/2-50, HAUTEUR_CADRE/2-50,
         LARGEUR_CADRE/2+50, HAUTEUR_CADRE/2+50, fill=couleur[1]))
    elif x0_CARRE_BLEU < event.x < x1_CARRE_BLEU and y0_CARRE_BLEU < event.y < y1_CARRE_BLEU:
        historique.append(cadre.create_oval(LARGEUR_CADRE/2-50, HAUTEUR_CADRE/2-50,
         LARGEUR_CADRE/2+50, HAUTEUR_CADRE/2+50, fill=couleur[2]))
    else:
        historique.append(cadre.create_oval(LARGEUR_CADRE/2-50, HAUTEUR_CADRE/2-50,
         LARGEUR_CADRE/2+50, HAUTEUR_CADRE/2+50, fill=couleur[3]))

def annuler():
    """
    annule tous les changements de couleur du cercle
    """
    if historique == []:
        None
    else:
        cadre.delete(historique[-1])
        del historique[-1]

#créations des widgets
cadre = tk.Canvas(fenetre, width=LARGEUR_CADRE, height=HAUTEUR_CADRE, bg=fond_couleur)
button_annuler = tk.Button(fenetre, text="Annuler", command=annuler)

#création des items
cadre.create_rectangle(x0_CARRE_VERT, y0_CARRE_VERT, x1_CARRE_VERT, y1_CARRE_VERT, fill=couleur[0])
cadre.create_rectangle(x0_CARRE_JAUNE, y0_CARRE_JAUNE, x1_CARRE_JAUNE, y1_CARRE_JAUNE, fill=couleur[1])
cadre.create_rectangle(x0_CARRE_BLEU, y0_CARRE_BLEU, x1_CARRE_BLEU, y1_CARRE_BLEU, fill=couleur[2])
cadre.create_oval(x0_CERCLE, y0_CERCLE, x1_CERCLE, y1_CERCLE, fill=couleur[3])

#positionement des widget
cadre.grid(row=0, column=1)
button_annuler.grid(row=0, column=0)

#liaison d'un evénement sur un widget à une fonction
cadre.bind("<Button-1>", clic)

#lancement de la fenetre grafique
fenetre.mainloop()