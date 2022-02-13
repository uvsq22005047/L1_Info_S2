#librairie
import tkinter as tk

#création des variables globals et des constantes
LARGEUR_CADRE = 600
HAUTEUR_CADRE = 600
fond_couleur = "white"
x_ligne_1, x_ligne_2 = LARGEUR_CADRE/3, (LARGEUR_CADRE/3)*2
couleur_1, couleur_2 = "red", "blue"

#création de la fenetre graphique
fenetre = tk.Tk()

#créations des fonctions
def clic(event):
    """
    déplace les lignes vers là où on a cliqué
    """
    global x_ligne_1, x_ligne_2
    if event.x < x_ligne_1:
        x_ligne_1 -= 10
        x_ligne_2 -= 10
    elif x_ligne_1 < event.x < x_ligne_2:
        x_ligne_1 += 10
        x_ligne_2 -= 10
    else:
        x_ligne_1 += 10
        x_ligne_2 += 10
    couleur()
    cadre.delete('all')
    cadre.create_line(x_ligne_1, 0, x_ligne_1, HAUTEUR_CADRE, fill=couleur_1)
    cadre.create_line(x_ligne_2, 0, x_ligne_2, HAUTEUR_CADRE, fill=couleur_2)
    

def couleur():
    """
    échange la couleur des lignes
    """
    global couleur_1, couleur_2
    couleur_1, couleur_2 = couleur_2, couleur_1

def recommencer():
    """
    réinitialise le programme
    """
    global x_ligne_1, x_ligne_2, couleur_1, couleur_2
    x_ligne_1, x_ligne_2 = LARGEUR_CADRE/3, (LARGEUR_CADRE/3)*2
    couleur_1, couleur_2 = "red", "blue"
    cadre.delete('all')
    cadre.create_line(x_ligne_1, 0, x_ligne_1, HAUTEUR_CADRE, fill=couleur_1)
    cadre.create_line(x_ligne_2, 0, x_ligne_2, HAUTEUR_CADRE, fill=couleur_2)


#créations des widgets
cadre = tk.Canvas(fenetre, width=LARGEUR_CADRE, height=HAUTEUR_CADRE, bg=fond_couleur)
button_recommencer = tk.Button(fenetre, text="Recommencer", command=recommencer)

#création des items
cadre.create_line(x_ligne_1, 0, x_ligne_1, HAUTEUR_CADRE, fill=couleur_1)
cadre.create_line(x_ligne_2, 0, x_ligne_2, HAUTEUR_CADRE, fill=couleur_2)

#positionement des widget
cadre.grid()
button_recommencer.grid()

#liaison d'un evénement sur un widget à une fonction
cadre.bind("<Button-1>", clic)

#lancement de la fenetre grafique
fenetre.mainloop()