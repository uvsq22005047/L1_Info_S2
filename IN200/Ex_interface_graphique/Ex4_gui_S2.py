#librairie
import tkinter as tk

#création des variables globals et des constantes
LARGEUR_CADRE = 500
HAUTEUR_CADRE = 500
fond_couleur = "white"
x0_carre, y0_carre, x1_carre, y1_carre = LARGEUR_CADRE/2-25, HAUTEUR_CADRE/2-25, LARGEUR_CADRE/2+25, HAUTEUR_CADRE/2+25

#création de la fenetre graphique
fenetre = tk.Tk()

#créations des fonctions
def clic(event):
    """
    Si l'on clique dans le carré, celui ci rétreci de 10 pixel, si l'on clique à l'exterieur, il s'agrendit de 10 pixel
    """
    global x0_carre, y0_carre, x1_carre, y1_carre
    if x0_carre < event.x < x1_carre and y0_carre < event.y < y1_carre:
        if x1_carre - x0_carre >= 20:
            x0_carre += 5
            y0_carre += 5
            x1_carre -= 5
            y1_carre -= 5
    else:
        if x1_carre - x0_carre <= 100:
            x0_carre -= 5
            y0_carre -= 5
            x1_carre += 5
            y1_carre += 5
    cadre.delete('all')
    cadre.create_rectangle(x0_carre, y0_carre, x1_carre, y1_carre, fill="red")


def pause():
    """
    suspend le programme
    """
    cadre.unbind("<Button-1>")
    button_pause_restart.config(text="Restart", command=restart)

def restart():
    """
    remet le programme là où il en étais
    """
    cadre.bind("<Button-1>", clic)
    button_pause_restart.config(text="Pause", command=pause)

#créations des widgets
cadre = tk.Canvas(fenetre, width=LARGEUR_CADRE, height=HAUTEUR_CADRE, bg=fond_couleur)
button_pause_restart = tk.Button(fenetre, text="Pause", command=pause)

#création des items
cadre.create_rectangle(x0_carre, y0_carre, x1_carre, y1_carre, fill="red")

#positionement des widget
cadre.grid()
button_pause_restart.grid()

#liaison d'un evénement sur un widget à une fonction
cadre.bind("<Button-1>", clic)

#lancement de la fenetre grafique
fenetre.mainloop()