#librairie
import tkinter as tk

#création des variables globals et des constantes
LARGEUR_CADRE = 500
HAUTEUR_CADRE = 500
fond_couleur = "black"
x_ligne_1, x_ligne_2 = LARGEUR_CADRE/3, (LARGEUR_CADRE/3)*2
n_croix = 0
n_carre = 0
n_cercle = 0

#création de la fenetre graphique
fenetre = tk.Tk()

#créations des fonctions
def clic(event):
    """
    créé aux endroit cliqué, une croix dans la partie gauche du cadre,
     un carré dans la partie du milieu et un cercle dans la partie droite.
    2 croix, 3 carré et 3 cercle peuvent etre créé aux maximum. 
    """
    global n_croix, n_carre, n_cercle
    if event.x < x_ligne_1 and n_croix < 2:
        cadre.create_line(event.x-25, event.y-25, event.x+25, event.y+25,
         event.x, event.y, event.x+25, event.y-25, event.x-25, event.y+25, fill="blue")
        n_croix += 1
    elif x_ligne_1 < event.x < x_ligne_2 and n_carre < 3:
        cadre.create_rectangle(event.x-25, event.y-25, event.x+25, event.y+25, fill="green")
        n_carre += 1
    elif x_ligne_2 < event.x and n_cercle < 3:
        cadre.create_oval(event.x-50, event.y-50, event.x+50, event.y+50, fill="red")
        n_cercle += 1

def redemarrer():
    """
    Reinitialise tous depuis le début
    """
    global n_croix, n_carre, n_cercle
    cadre.delete('all')
    cadre.create_line(x_ligne_1, 0, x_ligne_1, HAUTEUR_CADRE, fill="white")
    cadre.create_line(x_ligne_2, 0, x_ligne_2, HAUTEUR_CADRE, fill="white")
    n_croix = 0
    n_carre = 0
    n_cercle = 0


#créations des widgets
cadre = tk.Canvas(fenetre, width=LARGEUR_CADRE, height=HAUTEUR_CADRE, bg=fond_couleur)
button_redemarrer = tk.Button(fenetre, text="Redémarrer", command=redemarrer)

#création des items
cadre.create_line(x_ligne_1, 0, x_ligne_1, HAUTEUR_CADRE, fill="white")
cadre.create_line(x_ligne_2, 0, x_ligne_2, HAUTEUR_CADRE, fill="white")

#positionement des widget
cadre.grid()
button_redemarrer.grid()

#liaison d'un evénement sur un widget à une fonction
cadre.bind("<Button-1>", clic)

#lancement de la fenetre grafique
fenetre.mainloop()