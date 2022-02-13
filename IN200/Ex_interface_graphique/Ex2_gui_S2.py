#librairie
import tkinter as tk

#création des variables globals et des constantes
LARGEUR_CADRE = 500
HAUTEUR_CADRE = 500
fond_couleur = "white"
x0, y0, x1, y1 = None, None, None, None

#création de la fenetre graphique
fenetre = tk.Tk()
couleur_ligne = None

#créations des fonctions
def clic(event):
    """
    Créé une ligne entre deux points cliqué, la premiere ligne est bleu,
     la seconde est rouge, et au cinquieme clic toutes les lignes s'effacent
    """
    global x0, y0, x1, y1
    if couleur_ligne == "red":
        cadre.delete('all')
        couleur()
    else:
        if x0 == None and y0 == None:
            x0, y0 = event.x, event.y
        else:
            x1, y1 = event.x, event.y
            couleur()
            cadre.create_line(x0, y0, x1, y1, fill=couleur_ligne)
            x0, y0, x1, y1 = None, None, None, None

def couleur():
    """
    Change les couleurs
    """
    global couleur_ligne
    if couleur_ligne == None:
        couleur_ligne = "blue"
    elif couleur_ligne == "blue":
        couleur_ligne = "red"
    elif couleur_ligne == "red":
        couleur_ligne = None

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

#positionement des widget
cadre.grid()
button_pause_restart.grid()

#liaison d'un evénement sur un widget à une fonction
cadre.bind("<Button-1>", clic)

#lancement de la fenetre grafique
fenetre.mainloop()