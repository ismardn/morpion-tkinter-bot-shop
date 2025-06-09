import tkinter.ttk  # Permet de créer une interface graphique
import tkinter.messagebox  # Permet de créer la fenêtre d'aide
import random  # Permet à l'ordinateur de sélectionner une case aléatoire

import sys
from pathlib import Path

# Obtient le chemin du répertoire de main.pyw
CHEMIN_MAIN = str(Path(__file__).resolve().parent).replace("\\", "/")


def main():  # Fonction principale qui est lancée pour démarrer le programme
    global fenetre  # Permet de créer des widgets sur la fenêtre à l'aide d'autres fonctions

    fenetre = tkinter.Tk()  # Création de la fenêtre

    fenetre.title("Jeu du Morpion")  # Définition du titre de la fenêtre
    fenetre.geometry("896x504")  # Définition des dimensions de la fenêtre
    fenetre.resizable(width=False, height=False)  # Fenêtre non redimensionnable
    fenetre.iconbitmap(f"{CHEMIN_MAIN}/images/icone.ico")  # Définition de l'icône de la fenêtre

    interface_menu_initial()  # Affichage de menu initial

    fenetre.mainloop()  # Affichage de la fenêtre


##### Fonctions diverses #####


def emplacement_images(emplacement):  # Permet de récupérer l'emplacement des apparences pour les symboles

    if emplacement == "croix_par_defaut":
        return f"{CHEMIN_MAIN}/images/apparences/croix_par_defaut.png"
    elif emplacement == "cercle_par_defaut":
        return f"{CHEMIN_MAIN}/images/apparences/cercle_par_defaut.png"

    elif emplacement == "croix_2":
        return f"{CHEMIN_MAIN}/images/apparences/croix_2.png"
    elif emplacement == "croix_3":
        return f"{CHEMIN_MAIN}/images/apparences/croix_3.png"
    elif emplacement == "croix_4":
        return f"{CHEMIN_MAIN}/images/apparences/croix_4.png"

    elif emplacement == "cercle_2":
        return f"{CHEMIN_MAIN}/images/apparences/cercle_2.png"
    elif emplacement == "cercle_3":
        return f"{CHEMIN_MAIN}/images/apparences/cercle_3.png"
    else:
        return f"{CHEMIN_MAIN}/images/apparences/cercle_4.png"


def suppression_widgets():  # Permet de supprimer les widgets présents sur la fenêtre

    widgets = fenetre.pack_slaves()  # Récupération de l'ensemble des widgets sur la fenêtre
    for widget in widgets:  # Pour chaque widgets sur la fenêtre
        widget.pack_forget()  # Suppression du widget


def lecture_fichier(information):   # Permet de récupérer les informations contenu dans le fichier "sauvegarde.txt"
    global contenu_fichier  # Permet de réutiliser le contenu du fichier dans les autres fonctions

    with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "r") as fichier_sauvegarde: # Ouverture du fichier "sauvegarde.txt" en tant que lecture seule (r)
        contenu_fichier = fichier_sauvegarde.readlines()    # Stockage de l'ensemble des lignes du fichier texte dans une liste
        fichier_sauvegarde.close()  # Fermeture du fichier

    informations_fichier = [ligne.split(" ")[2] for ligne in contenu_fichier]   # Stockage, dans une liste, du troixième élément de la liste, à l'aide de la séparation par espace, de chaque ligne, correspondant aux informations nécessaires

    nombre_pieces = int(informations_fichier[0].replace("\n", ""))  # Suppression du retour à ligne ("\n") et convertion du nombre de pièces en entier (int) afin d'effectuer des additions/soustractions qu'on stocke dans une variable
    apparences_definies = informations_fichier[1].replace("\n", "").split(",")  # Suppression du retour à ligne ("\n"), et stockage des apparences définies sous forme de liste, à l'aide de la séparation par virgule
    apparences_achetees = informations_fichier[2]   # Stockage des apparences achetées dans une variable

    if information == "nombre_pieces":
        return nombre_pieces
    elif information == "croix_definie":
        return apparences_definies[0]
    elif information == "cercle_defini":
        return apparences_definies[1]
    else:
        return apparences_achetees


def ecriture_nombre_pieces(action): # Permet de retirer/d'ajouter des pièces en fonction de la situation

    nombre_pieces = lecture_fichier("nombre_pieces")    # Stokage du nombre de pièces dans une variable

    if action == "victoire":    # Si cette fonction est appelée lors d'une victoire contre l'ordinateur de niveau "Moyen"
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde: # Ouverture du fichier "sauvegarde.txt" en tant qu'écriture (w)
            nombre_pieces += 1  # Incrémentation de 1 du nombre de pièces
            contenu_fichier[0] = "[nombre_pieces] : " + str(nombre_pieces) + "\n"   # Modification de la partie du fichier concernée (ici, la ligne n°1, c'est-à-dire le nombre de pièces)
            fichier_sauvegarde.writelines(contenu_fichier)  # Réécriture du fichier avec le contenu modifié
            fichier_sauvegarde.close()
        return " (+1 pièce : Vous avez actuellement " + str(lecture_fichier("nombre_pieces")) + " pièce(s))"    # Retourne le texte supplémentaire à afficher lorsque le joueur gagne contre l'ordinateur de niveau "Moyen"
    else:
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            nombre_pieces -= 5  # Retrait de 5 pièces au nombre total de pièces
            contenu_fichier[0] = "[nombre_pieces] : " + str(nombre_pieces) + "\n"
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        return "Vous avez actuellement " + str(lecture_fichier("nombre_pieces")) + " pièce(s)"  # Retourne le nombre de pièces actuelles


def fenetre_aide(): # Permet de créer une boîte de message contenant les informations qui expliquent en quoi consiste le programme
    tkinter.messagebox.showinfo(title="Aide", message='FONCTIONNALITÉS\n\n - Le mode "Jeu contre l\'ordinateur", dans lequel on peut choisir la difficulté de l\'ordinateur contre laquelle on veut jouer :\n     - Le niveau "Faible" (l\'ordinateur joue aléatoirement)\n     - le niveau "Moyen" (l\'ordinateur attaque et défend simplement, si deux mêmes symboles sont alignés)\n     - Le niveau "Invincible" (où l\'ordinateur est théoriquement invincible)\n\n - Le mode "Un contre Un", où deux joueurs différents peuvent s\'affronter sur le même ordinateur\n\n - La "Boutique", qui permet d\'acheter des apparences pour les symboles à l\'aide de pièces gagnées contre l\'ordinateur de niveau "Moyen" (Vous ne perdez pas votre nombre de pièces gagnées, les formes achetées, ainsi que les formes définies lors de la femeture du programme.)\n\nRÈGLES DU JEU\n\n Les règles du morpion sont très simples : sur une grille de 3 cases sur 3 cases, le but du jeu est d’aligner 3 symboles identiques (croix ou cercle) horizontalement, verticalement ou en diagonale, et les deux joueurs posent leur forme chacun leur tour (Le joueur possédant la croix commence). La partie se termine quand l’un des joueurs a aligné ses 3 symboles (il y a alors un vainqueur), ou lorsque la grille est complétée sans que 3 symboles identiques soient alignés (il y a alors égalité).')    # Crée une boîte de message de type "Info" nommée "Aide" dans laquelle sont expliquées les fonctionnalités et les règles du jeu


##############################

##### Création des interfaces des menus ######


def interface_menu_initial():   # Création de l'interface initiale, lancée au lancement du programme
    global croix, cercle    # Permet aux autres fonctions de modifier/d'utiliser l'apparence de la croix/du cercle
    global image_croix_par_defaut, image_croix_2, image_croix_3, image_croix_4, image_cercle_par_defaut, image_cercle_2, image_cercle_3, image_cercle_4 # Permet d'afficher les apparences des croix/cercles dans la "Boutique"
    global OPTIONS_NIVEAU   # Permet aux autres fonctions de récupérer le niveau de l'ordinteur
    global page_precedente  # Permet d'ajouter/de modifier la fonctionnalité de "Retour Arrière"
    global informations_gagnant, bouton_recommencer # Permet aux autres fonctions d'afficher/de modifier les informations concernant le gagnant ainsi que le bouton recommencer
    global CHEMIN_DOSSIER_apparences    # Permet de récupérer l'emplacement des apparences (pour les comparer)

    suppression_widgets()   # Supression des anciens widgets (utile si la fonctionnalité "Retour Arrière" est utilisée)

    bouton_jouer_contre_ordi = tkinter.Button(fenetre, text="Jouer contre l'ordinateur", font=("Calibri", 25), command=interface_menu_jeu_ordinateur)
    bouton_jouer_a_deux = tkinter.Button(fenetre, text="Jouer à deux", font=("Calibri", 25), command=interface_jeu_un_contre_un)
    bouton_boutique = tkinter.Button(fenetre, text="Accéder à la Boutique", font=("Calibri", 25), command=interface_boutique)
    label_nombre_pieces = tkinter.Label(fenetre, text="Vous avez actuellement " + str(lecture_fichier("nombre_pieces")) + " pièce(s)", font=("Calibri", 25), fg="#E9A200")

    bouton_jouer_contre_ordi.pack(expand=tkinter.YES)
    bouton_jouer_a_deux.pack(expand=tkinter.YES)
    bouton_boutique.pack(expand=tkinter.YES)
    label_nombre_pieces.pack(expand=tkinter.YES)

    aide = tkinter.Menu(fenetre)
    aide.add_command(label="Aide", command=fenetre_aide)
    fenetre.config(menu=aide)
    
    CHEMIN_DOSSIER_apparences = f"{CHEMIN_MAIN}/images/apparences/"
    
    croix = tkinter.PhotoImage(file=(CHEMIN_DOSSIER_apparences + lecture_fichier("croix_definie") + ".png"))
    cercle = tkinter.PhotoImage(file=(CHEMIN_DOSSIER_apparences + lecture_fichier("cercle_defini") + ".png"))

    OPTIONS_NIVEAU = ["Faible", "Moyen", "Invincible"]

    image_croix_par_defaut = tkinter.PhotoImage(file=emplacement_images("croix_par_defaut"))
    image_croix_2 = tkinter.PhotoImage(file=emplacement_images("croix_2"))
    image_croix_3 = tkinter.PhotoImage(file=emplacement_images("croix_3"))
    image_croix_4 = tkinter.PhotoImage(file=emplacement_images("croix_4"))

    image_cercle_par_defaut = tkinter.PhotoImage(file=emplacement_images("cercle_par_defaut"))
    image_cercle_2 = tkinter.PhotoImage(file=emplacement_images("cercle_2"))
    image_cercle_3 = tkinter.PhotoImage(file=emplacement_images("cercle_3"))
    image_cercle_4 = tkinter.PhotoImage(file=emplacement_images("cercle_4"))

    page_precedente = tkinter.Menu(fenetre)
    page_precedente.add_command(label="Retour Arrière")

    informations_gagnant = tkinter.Label(fenetre, text="", font=("Calibri", 15))
    bouton_recommencer = tkinter.Button(fenetre, text="Recommencer", font=("Calibri", 12))


def interface_menu_jeu_ordinateur():
    global menu_deroulant_niveau

    suppression_widgets()

    label_niveau_ordi = tkinter.Label(fenetre, text="Niveau de l'ordinateur :", font=("Calibri", 25))
    menu_deroulant_niveau = tkinter.ttk.Combobox(fenetre, values=OPTIONS_NIVEAU, width=10, font=("Calibri", 15), state="readonly")
    menu_deroulant_niveau.set(OPTIONS_NIVEAU[0])
    espace_menu_ordinateur_1 = tkinter.Label(fenetre, text="\n", font=("Calibri", 15))
    espace_menu_ordinateur_2 = tkinter.Label(fenetre, text="\n", font=("Calibri", 15))
    bouton_jouer = tkinter.Button(fenetre, text="Jouer", font=("Calibri", 20), command=interface_jeu_contre_ordinateur)

    label_niveau_ordi.pack(expand=tkinter.YES)
    menu_deroulant_niveau.pack(expand=tkinter.YES)
    espace_menu_ordinateur_1.pack(expand=tkinter.YES)
    espace_menu_ordinateur_2.pack(expand=tkinter.YES)
    bouton_jouer.pack(expand=tkinter.YES)

    if page_precedente.entrycget("Retour Arrière", "label") == "Retour Arrière":
        page_precedente.delete("Retour Arrière")
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_initial)
    else:
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_initial)
    fenetre.config(menu=page_precedente)


def interface_jeu_contre_ordinateur():
    global jeu_a_deux

    jeu_a_deux = False

    affichage_interface_grille()

    if page_precedente.entrycget("Retour Arrière", "label") == "Retour Arrière":
        page_precedente.delete("Retour Arrière")
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_jeu_ordinateur)
    else:
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_jeu_ordinateur)
    fenetre.config(menu=page_precedente)

    bouton_recommencer['command'] = interface_jeu_contre_ordinateur


def interface_jeu_un_contre_un():
    global jeu_a_deux

    jeu_a_deux = True

    affichage_interface_grille()

    if page_precedente.entrycget("Retour Arrière", "label") == "Retour Arrière":
        page_precedente.delete("Retour Arrière")
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_initial)
    else:
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_initial)
    fenetre.config(menu=page_precedente)

    bouton_recommencer['command'] = interface_jeu_un_contre_un


def interface_boutique():
    global label_nombre_pieces, label_informations_selection
    global bouton_selection_croix_par_defaut, bouton_selection_croix_2, bouton_selection_croix_3, bouton_selection_croix_4, bouton_selection_cercle_par_defaut, bouton_selection_cercle_2, bouton_selection_cercle_3, bouton_selection_cercle_4

    suppression_widgets()

    label_nombre_pieces = tkinter.Label(fenetre, text="Vous avez " + str(lecture_fichier("nombre_pieces")) + " pièce(s)", font=("Calibri", 25), fg="#E9A200")

    DIMENSIONS_CANVAS_SYMBOLES = 110

    cadre_haut = tkinter.Frame(fenetre)

    cadre_haut_gauche = tkinter.Frame(cadre_haut)
    cadre_haut_gauche.pack(side=tkinter.LEFT)

    cadre_haut_gauche_2 = tkinter.Frame(cadre_haut_gauche)
    cadre_haut_gauche_2.pack(side=tkinter.RIGHT)
    espace_cadre_haut_gauche = tkinter.Label(cadre_haut_gauche_2, text="     ", font=("Calibri", 15))
    espace_cadre_haut_gauche.pack(side=tkinter.LEFT)

    cadre_haut_pour_espace = tkinter.Frame(cadre_haut)
    cadre_haut_pour_espace.pack(side=tkinter.RIGHT)
    espace_cadre_haut = tkinter.Label(cadre_haut_pour_espace, text="     ", font=("Calibri", 15))
    espace_cadre_haut.pack(side=tkinter.LEFT)

    cadre_haut_droit = tkinter.Frame(cadre_haut_pour_espace)
    cadre_haut_droit.pack(side=tkinter.RIGHT)

    cadre_haut_droit_2 = tkinter.Frame(cadre_haut_droit)
    cadre_haut_droit_2.pack(side=tkinter.RIGHT)
    espace_cadre_haut_droit = tkinter.Label(cadre_haut_droit_2, text="     ", font=("Calibri", 15))
    espace_cadre_haut_droit.pack(side=tkinter.LEFT)

    cadre_croix_par_defaut = tkinter.LabelFrame(cadre_haut_gauche)
    cadre_croix_par_defaut.pack(side=tkinter.LEFT)
    canvas_croix_par_defaut = tkinter.Canvas(cadre_croix_par_defaut, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_croix_par_defaut.pack()
    canvas_croix_par_defaut.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_croix_par_defaut)
    bouton_selection_croix_par_defaut = tkinter.Button(cadre_croix_par_defaut, text="", font=("Calibri", 10), command=selection_croix_par_defaut)
    bouton_selection_croix_par_defaut.pack(fill=tkinter.X)

    cadre_croix_2 = tkinter.LabelFrame(cadre_haut_gauche_2)
    cadre_croix_2.pack(side=tkinter.RIGHT)
    canvas_croix_2 = tkinter.Canvas(cadre_croix_2, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_croix_2.pack()
    canvas_croix_2.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_croix_2)
    bouton_selection_croix_2 = tkinter.Button(cadre_croix_2, text="", font=("Calibri", 10), command=selection_croix_2)
    bouton_selection_croix_2.pack(fill=tkinter.X)

    cadre_croix_3 = tkinter.LabelFrame(cadre_haut_droit)
    cadre_croix_3.pack(side=tkinter.LEFT)
    canvas_croix_3 = tkinter.Canvas(cadre_croix_3, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_croix_3.pack()
    canvas_croix_3.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_croix_3)
    bouton_selection_croix_3 = tkinter.Button(cadre_croix_3, text="", font=("Calibri", 10), command=selection_croix_3)
    bouton_selection_croix_3.pack(fill=tkinter.X)

    cadre_croix_4 = tkinter.LabelFrame(cadre_haut_droit_2)
    cadre_croix_4.pack(side=tkinter.RIGHT)
    canvas_croix_4 = tkinter.Canvas(cadre_croix_4, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_croix_4.pack()
    canvas_croix_4.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_croix_4)
    bouton_selection_croix_4 = tkinter.Button(cadre_croix_4, text="", font=("Calibri", 10), command=selection_croix_4)
    bouton_selection_croix_4.pack(fill=tkinter.X)

    espace_cadre_haut_bas = tkinter.Label(fenetre, text="")

    cadre_bas = tkinter.Frame(fenetre)

    cadre_bas_gauche = tkinter.Frame(cadre_bas)
    cadre_bas_gauche.pack(side=tkinter.LEFT)

    cadre_bas_gauche_2 = tkinter.Frame(cadre_bas_gauche)
    cadre_bas_gauche_2.pack(side=tkinter.RIGHT)
    espace_cadre_bas_gauche = tkinter.Label(cadre_bas_gauche_2, text="     ", font=("Calibri", 15))
    espace_cadre_bas_gauche.pack(side=tkinter.LEFT)

    cadre_bas_pour_espace = tkinter.Frame(cadre_bas)
    cadre_bas_pour_espace.pack(side=tkinter.RIGHT)
    espace_cadre_bas = tkinter.Label(cadre_bas_pour_espace, text="     ", font=("Calibri", 15))
    espace_cadre_bas.pack(side=tkinter.LEFT)

    cadre_bas_droit = tkinter.Frame(cadre_bas_pour_espace)
    cadre_bas_droit.pack(side=tkinter.RIGHT)

    cadre_bas_droit_2 = tkinter.Frame(cadre_bas_droit)
    cadre_bas_droit_2.pack(side=tkinter.RIGHT)
    espace_cadre_bas_droit = tkinter.Label(cadre_bas_droit_2, text="     ", font=("Calibri", 15))
    espace_cadre_bas_droit.pack(side=tkinter.LEFT)

    cadre_cercle_par_defaut = tkinter.LabelFrame(cadre_bas_gauche)
    cadre_cercle_par_defaut.pack(side=tkinter.LEFT)
    canvas_cercle_par_defaut = tkinter.Canvas(cadre_cercle_par_defaut, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_cercle_par_defaut.pack()
    canvas_cercle_par_defaut.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_cercle_par_defaut)
    bouton_selection_cercle_par_defaut = tkinter.Button(cadre_cercle_par_defaut, text="", font=("Calibri", 10), command=selection_cercle_par_defaut)
    bouton_selection_cercle_par_defaut.pack(fill=tkinter.X)

    cadre_cercle_2 = tkinter.LabelFrame(cadre_bas_gauche_2)
    cadre_cercle_2.pack(side=tkinter.RIGHT)
    canvas_cercle_2 = tkinter.Canvas(cadre_cercle_2, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_cercle_2.pack()
    canvas_cercle_2.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_cercle_2)
    bouton_selection_cercle_2 = tkinter.Button(cadre_cercle_2, text="", font=("Calibri", 10), command=selection_cercle_2)
    bouton_selection_cercle_2.pack(fill=tkinter.X)

    cadre_cercle_3 = tkinter.LabelFrame(cadre_bas_droit)
    cadre_cercle_3.pack(side=tkinter.LEFT)
    canvas_cercle_3 = tkinter.Canvas(cadre_cercle_3, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_cercle_3.pack()
    canvas_cercle_3.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_cercle_3)
    bouton_selection_cercle_3 = tkinter.Button(cadre_cercle_3, text="", font=("Calibri", 10), command=selection_cercle_3)
    bouton_selection_cercle_3.pack(fill=tkinter.X)

    cadre_cercle_4 = tkinter.LabelFrame(cadre_bas_droit_2)
    cadre_cercle_4.pack(side=tkinter.RIGHT)
    canvas_cercle_4 = tkinter.Canvas(cadre_cercle_4, width=DIMENSIONS_CANVAS_SYMBOLES, height=DIMENSIONS_CANVAS_SYMBOLES)
    canvas_cercle_4.pack()
    canvas_cercle_4.create_image(DIMENSIONS_CANVAS_SYMBOLES / 2, DIMENSIONS_CANVAS_SYMBOLES / 2, image=image_cercle_4)
    bouton_selection_cercle_4 = tkinter.Button(cadre_cercle_4, text="", font=("Calibri", 10), command=selection_cercle_4)
    bouton_selection_cercle_4.pack(fill=tkinter.X)

    label_informations_selection = tkinter.Label(fenetre, text="", font=("Calibri", 20))

    label_nombre_pieces.pack(expand=tkinter.YES)
    cadre_haut.pack()
    espace_cadre_haut_bas.pack(expand=tkinter.YES)
    cadre_bas.pack()
    label_informations_selection.pack(expand=tkinter.YES)

    label_informations_selection['text'] = ""

    etat_apparences()

    if page_precedente.entrycget("Retour Arrière", "label") == "Retour Arrière":
        page_precedente.delete("Retour Arrière")
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_initial)
    else:
        page_precedente.add_command(label="Retour Arrière", command=interface_menu_initial)
    fenetre.config(menu=page_precedente)


##############################################

##### Création de la grille #####


def creation_grille():  # Crée la grille
    global grille  # Permet d'apporter des modifications à la grille avec les autres fonctions
    global DIMENSIONS_GRILLE  # Permet de réutiliser les dimensions de la grille dans les autres fonctions

    DIMENSIONS_GRILLE = 420  # On définit les dimensions de la grille

    grille = tkinter.Canvas(fenetre, width=DIMENSIONS_GRILLE, height=DIMENSIONS_GRILLE)  # Création d'un canvas pour y insérer la grille

    ##### Délimitation de la grille #####
    grille.create_image(DIMENSIONS_GRILLE / 2, DIMENSIONS_GRILLE / 2, image=contour_grille)  # Affichage du contour de la grille
    ### Création des lignes/colonnes ###
    grille.create_line(0 + 15, DIMENSIONS_GRILLE / 3, DIMENSIONS_GRILLE - 15, DIMENSIONS_GRILLE / 3, fill="black", width=6)
    grille.create_line(0 + 15, DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3, DIMENSIONS_GRILLE - 15, DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3, fill="black", width=6)
    grille.create_line(DIMENSIONS_GRILLE / 3, DIMENSIONS_GRILLE - 15, DIMENSIONS_GRILLE / 3, 0 + 15, fill="black", width=6)
    grille.create_line(DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3, DIMENSIONS_GRILLE - 15, DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3, 0 + 15, fill="black", width=6)
    #####################################

    grille.bind("<Button-1>", clic_grille)  # On associe le clic gauche de la souris sur la grille à l'éxecution de la fonction "clic_grille"


def clic_grille(event):
    global position_x, position_y

    position_x = event.x
    position_y = event.y

    if jeu_a_deux:
        if tour == "X":
            tour_joueur("X", 2)
        else:
            tour_joueur("O", 2)
    else:
        if tour == "X":
            tour_joueur("X", 1)


def affichage_interface_grille():  # Met en place les élements nécessaires à la création de la grille
    global emplacement_grille
    global tour
    global cases_remplies
    global contour_grille

    suppression_widgets()

    emplacement_grille = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]  # Création de la grille du morpion

    tour = "X"  # Tour par défaut (La croix commence)

    cases_remplies = 0  # Permet de savoir lorsque la grille est remplie

    informations_gagnant['text'] = ""  # Supprime le contenu du texte donnant des indications sur la fin du jeu

    contour_grille = tkinter.PhotoImage(file=f"{CHEMIN_MAIN}/images/contour_grille.png")

    creation_grille()

    grille.pack()
    informations_gagnant.pack()


#################################

##### Création du jeu #####


def tour_jeu(joueur, emplacement, nombre_joueurs):
    global emplacement_grille
    global tour
    global cases_remplies
    global emplacement_tour_precedent

    if joueur == "X":
        symbole = croix
    else:
        symbole = cercle

    if nombre_joueurs == 1:
        message_victoire = 'Vous avez gagné !'
    else:
        message_victoire = 'Le Joueur "' + joueur + '" a gagné !'

    if emplacement == "haut_gauche":
        grille.create_image((DIMENSIONS_GRILLE / 3) / 2 + 7, (DIMENSIONS_GRILLE / 3) / 2 + 7, image=symbole)
    elif emplacement == "haut_milieu":
        grille.create_image(DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, (DIMENSIONS_GRILLE / 3) / 2 + 7, image=symbole)
    elif emplacement == "haut_droit":
        grille.create_image(DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2 - 7, (DIMENSIONS_GRILLE / 3) / 2 + 7, image=symbole)
    elif emplacement == "milieu_gauche":
        grille.create_image((DIMENSIONS_GRILLE / 3) / 2 + 7, DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, image=symbole)
    elif emplacement == "centre":
        grille.create_image(DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, image=symbole)
    elif emplacement == "milieu_droit":
        grille.create_image(DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2 - 7, DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, image=symbole)
    elif emplacement == "bas_gauche":
        grille.create_image((DIMENSIONS_GRILLE / 3) / 2 + 7, DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2 - 7, image=symbole)
    elif emplacement == "bas_milieu":
        grille.create_image(DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2 - 7, image=symbole)
    else:
        grille.create_image(DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2 - 7, DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2 - 7, image=symbole)

    if emplacement == "haut_gauche":
        emplacement_grille[0][0] = joueur
        emplacement_tour_precedent = "haut_gauche"
    elif emplacement == "haut_milieu":
        emplacement_grille[0][1] = joueur
        emplacement_tour_precedent = "haut_milieu"
    elif emplacement == "haut_droit":
        emplacement_grille[0][2] = joueur
        emplacement_tour_precedent = "haut_droit"
    elif emplacement == "milieu_gauche":
        emplacement_grille[1][0] = joueur
        emplacement_tour_precedent = "milieu_gauche"
    elif emplacement == "centre":
        emplacement_grille[1][1] = joueur
        emplacement_tour_precedent = "centre"
    elif emplacement == "milieu_droit":
        emplacement_grille[1][2] = joueur
        emplacement_tour_precedent = "milieu_droit"
    elif emplacement == "bas_gauche":
        emplacement_grille[2][0] = joueur
        emplacement_tour_precedent = "bas_gauche"
    elif emplacement == "bas_milieu":
        emplacement_grille[2][1] = joueur
        emplacement_tour_precedent = "bas_milieu"
    else:
        emplacement_grille[2][2] = joueur
        emplacement_tour_precedent = "bas_droit"

    if joueur == "X":
        tour = "O"
    else:
        tour = "X"

    cases_remplies += 1

    if verification_fin_de_jeu() == True:
        if joueur == "X" or nombre_joueurs == 2:
            if nombre_joueurs == 1 and menu_deroulant_niveau.get() == "Moyen":
                message_victoire += ecriture_nombre_pieces("victoire")
            informations_gagnant['text'] = message_victoire
        else:
            informations_gagnant['text'] = "L'ordinateur a gagné !"
        bouton_recommencer.pack(expand=tkinter.YES)
    elif verification_fin_de_jeu() == "cases_remplies":
        informations_gagnant['text'] = 'Égalité !'
        bouton_recommencer.pack(expand=tkinter.YES)
    elif nombre_joueurs == 1 and joueur == "X":
        jeu_ordinateur()


def verification_fin_de_jeu():  # Vérifie si le jeu peut continuer ou non

    ### Vérification des lignes/colonnes/diagonales ###
    if (emplacement_grille[0][0] == "X" and emplacement_grille[0][1] == "X" and emplacement_grille[0][2] == "X") or (emplacement_grille[0][0] == "O" and emplacement_grille[0][1] == "O" and emplacement_grille[0][2] == "O"):
        grille.unbind("<Button 1>")  # "Fige" le canvas (Empêche l'utilisateur d'intéragir avec)
        grille.create_line(0 + 30, DIMENSIONS_GRILLE / 3 - (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE / 3 - (DIMENSIONS_GRILLE / 3) / 2, fill="grey", width=4)  # Création d'une ligne à l'emplacement de la victoire (pour la mettre en valeur)
        return True  # La victoire est confirmée
    elif (emplacement_grille[1][0] == "X" and emplacement_grille[1][1] == "X" and emplacement_grille[1][2] == "X") or (emplacement_grille[1][0] == "O" and emplacement_grille[1][1] == "O" and emplacement_grille[1][2] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(0 + 30, DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, fill="grey", width=4)
        return True
    elif (emplacement_grille[2][0] == "X" and emplacement_grille[2][1] == "X" and emplacement_grille[2][2] == "X") or (emplacement_grille[2][0] == "O" and emplacement_grille[2][1] == "O" and emplacement_grille[2][2] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(0 + 30, DIMENSIONS_GRILLE - (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE - (DIMENSIONS_GRILLE / 3) / 2, fill="grey", width=4)
        return True
    elif (emplacement_grille[0][0] == "X" and emplacement_grille[1][0] == "X" and emplacement_grille[2][0] == "X") or (emplacement_grille[0][0] == "O" and emplacement_grille[1][0] == "O" and emplacement_grille[2][0] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(DIMENSIONS_GRILLE / 3 - (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE / 3 - (DIMENSIONS_GRILLE / 3) / 2, 0 + 30, fill="grey", width=4)
        return True
    elif (emplacement_grille[0][1] == "X" and emplacement_grille[1][1] == "X" and emplacement_grille[2][1] == "X") or (emplacement_grille[0][1] == "O" and emplacement_grille[1][1] == "O" and emplacement_grille[2][1] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE / 3 + (DIMENSIONS_GRILLE / 3) / 2, 0 + 30, fill="grey", width=4)
        return True
    elif (emplacement_grille[0][2] == "X" and emplacement_grille[1][2] == "X" and emplacement_grille[2][2] == "X") or (emplacement_grille[0][2] == "O" and emplacement_grille[1][2] == "O" and emplacement_grille[2][2] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(DIMENSIONS_GRILLE - (DIMENSIONS_GRILLE / 3) / 2, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE - (DIMENSIONS_GRILLE / 3) / 2, 0 + 30, fill="grey", width=4)
        return True
    elif (emplacement_grille[0][0] == "X" and emplacement_grille[1][1] == "X" and emplacement_grille[2][2] == "X") or (emplacement_grille[0][0] == "O" and emplacement_grille[1][1] == "O" and emplacement_grille[2][2] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(0 + 30, 0 + 30, DIMENSIONS_GRILLE - 30, DIMENSIONS_GRILLE - 30, fill="grey", width=4)
        return True
    elif (emplacement_grille[0][2] == "X" and emplacement_grille[1][1] == "X" and emplacement_grille[2][0] == "X") or (emplacement_grille[0][2] == "O" and emplacement_grille[1][1] == "O" and emplacement_grille[2][0] == "O"):
        grille.unbind("<Button 1>")
        grille.create_line(DIMENSIONS_GRILLE - 30, 0 + 30, 0 + 30, DIMENSIONS_GRILLE - 30, fill="grey", width=4)
        return True
    ###################################################

    elif cases_remplies == 9:  # Permet de savoir lorsque la grille est remplie
        return "cases_remplies"


###########################

##### Création de la fonction joueur et des ordinateurs #####


def tour_joueur(symbole, nombre_joueurs):  # Permet à l'utilisateur d'intéragir avec la grille

    if 0 + 5 < position_x < DIMENSIONS_GRILLE / 3 - 5:
        if 0 + 5 < position_y < DIMENSIONS_GRILLE / 3 - 5 and emplacement_grille[0][0] == "-":
            tour_jeu(symbole, "haut_gauche", nombre_joueurs)
        elif DIMENSIONS_GRILLE / 3 + 5 < position_y < DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 - 5 and emplacement_grille[1][0] == "-":
            tour_jeu(symbole, "milieu_gauche", nombre_joueurs)
        elif DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + 5 < position_y < DIMENSIONS_GRILLE - 5 and emplacement_grille[2][0] == "-":
            tour_jeu(symbole, "bas_gauche", nombre_joueurs)
    elif DIMENSIONS_GRILLE / 3 + 5 < position_x < DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 - 5:
        if 0 + 5 < position_y < DIMENSIONS_GRILLE / 3 - 5 and emplacement_grille[0][1] == "-":
            tour_jeu(symbole, "haut_milieu", nombre_joueurs)
        elif DIMENSIONS_GRILLE / 3 + 5 < position_y < DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 and emplacement_grille[1][1] == "-":
            tour_jeu(symbole, "centre", nombre_joueurs)
        elif DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + 5 < position_y < DIMENSIONS_GRILLE - 5 and emplacement_grille[2][1] == "-":
            tour_jeu(symbole, "bas_milieu", nombre_joueurs)
    elif DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + 5 < position_x < DIMENSIONS_GRILLE - 5:
        if 0 + 5 < position_y < DIMENSIONS_GRILLE / 3 - 5 and emplacement_grille[0][2] == "-":
            tour_jeu(symbole, "haut_droit", nombre_joueurs)
        elif DIMENSIONS_GRILLE / 3 + 5 < position_y < DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 - 5 and emplacement_grille[1][2] == "-":
            tour_jeu(symbole, "milieu_droit", nombre_joueurs)
        elif DIMENSIONS_GRILLE - DIMENSIONS_GRILLE / 3 + 5 < position_y < DIMENSIONS_GRILLE - 5 and emplacement_grille[2][2] == "-":
            tour_jeu(symbole, "bas_droit", nombre_joueurs)


def jeu_ordinateur():

    if menu_deroulant_niveau.get() == "Faible":
        jeu_ordinateur_aleatoire()
    elif menu_deroulant_niveau.get() == "Moyen":
        jeu_ordinateur_moyen()
    else:
        jeu_ordinateur_invincible()


def jeu_ordinateur_aleatoire():

    while True:
        position_jeu = random.randint(1, 9)

        if position_jeu == 1 and emplacement_grille[0][0] == "-":
            tour_jeu("O", "haut_gauche", 1)
            break
        if position_jeu == 2 and emplacement_grille[0][1] == "-":
            tour_jeu("O", "haut_milieu", 1)
            break
        if position_jeu == 3 and emplacement_grille[0][2] == "-":
            tour_jeu("O", "haut_droit", 1)
            break
        if position_jeu == 4 and emplacement_grille[1][0] == "-":
            tour_jeu("O", "milieu_gauche", 1)
            break
        if position_jeu == 5 and emplacement_grille[1][1] == "-":
            tour_jeu("O", "centre", 1)
            break
        if position_jeu == 6 and emplacement_grille[1][2] == "-":
            tour_jeu("O", "milieu_droit", 1)
            break
        if position_jeu == 7 and emplacement_grille[2][0] == "-":
            tour_jeu("O", "bas_gauche", 1)
            break
        if position_jeu == 8 and emplacement_grille[2][1] == "-":
            tour_jeu("O", "bas_milieu", 1)
            break
        if position_jeu == 9 and emplacement_grille[2][2] == "-":
            tour_jeu("O", "bas_droit", 1)
            break


def jeu_ordinateur_moyen():

    if not attaque_et_defense_basique(1):
        if not attaque_et_defense_basique(0):
            jeu_ordinateur_aleatoire()


def jeu_ordinateur_invincible():

    if not attaque_et_defense_basique(1):
        if not attaque_et_defense_basique(0):
            if emplacement_tour_precedent == "centre":
                tour_jeu("O", random.choice(["haut_gauche", "haut_droit", "bas_gauche", "bas_droit"]), 1)
            else:
                if emplacement_grille[1][1] == "-":
                    tour_jeu("O", "centre", 1)
                else:
                    attaque_et_defense_avancee()


def attaque_et_defense_basique(action):

    if verificateur_de_victoire_possible(emplacement_grille[0], action) == 2 and (emplacement_grille[0][0] == "-" or emplacement_grille[0][1] == "-" or emplacement_grille[0][2] == "-"):
        if emplacement_grille[0][0] == "-":
            tour_jeu("O", "haut_gauche", 1)
            return True
        elif emplacement_grille[0][1] == "-":
            tour_jeu("O", "haut_milieu", 1)
            return True
        else:
            tour_jeu("O", "haut_droit", 1)
            return True
    elif verificateur_de_victoire_possible(emplacement_grille[1], action) == 2 and (emplacement_grille[1][0] == "-" or emplacement_grille[1][1] == "-" or emplacement_grille[1][2] == "-"):
        if emplacement_grille[1][0] == "-":
            tour_jeu("O", "milieu_gauche", 1)
            return True
        elif emplacement_grille[1][1] == "-":
            tour_jeu("O", "centre", 1)
            return True
        else:
            tour_jeu("O", "milieu_droit", 1)
            return True
    elif verificateur_de_victoire_possible(emplacement_grille[2], action) == 2 and (emplacement_grille[2][0] == "-" or emplacement_grille[2][1] == "-" or emplacement_grille[2][2] == "-"):
        if emplacement_grille[2][0] == "-":
            tour_jeu("O", "bas_gauche", 1)
            return True
        elif emplacement_grille[2][1] == "-":
            tour_jeu("O", "bas_milieu", 1)
            return True
        else:
            tour_jeu("O", "bas_droit", 1)
            return True
    elif verificateur_de_victoire_possible([emplacement_grille[0][0], emplacement_grille[1][0], emplacement_grille[2][0]], action) == 2 and (emplacement_grille[0][0] == "-" or emplacement_grille[1][0] == "-" or emplacement_grille[2][0] == "-"):
        if emplacement_grille[0][0] == "-":
            tour_jeu("O", "haut_gauche", 1)
            return True
        elif emplacement_grille[1][0] == "-":
            tour_jeu("O", "milieu_gauche", 1)
            return True
        else:
            tour_jeu("O", "bas_gauche", 1)
            return True
    elif verificateur_de_victoire_possible([emplacement_grille[0][1], emplacement_grille[1][1], emplacement_grille[2][1]], action) == 2 and (emplacement_grille[0][1] == "-" or emplacement_grille[1][1] == "-" or emplacement_grille[2][1] == "-"):
        if emplacement_grille[0][1] == "-":
            tour_jeu("O", "haut_milieu", 1)
            return True
        elif emplacement_grille[1][1] == "-":
            tour_jeu("O", "centre", 1)
            return True
        else:
            tour_jeu("O", "bas_milieu", 1)
            return True
    elif verificateur_de_victoire_possible([emplacement_grille[0][2], emplacement_grille[1][2], emplacement_grille[2][2]], action) == 2 and (emplacement_grille[0][2] == "-" or emplacement_grille[1][2] == "-" or emplacement_grille[2][2] == "-"):
        if emplacement_grille[0][2] == "-":
            tour_jeu("O", "haut_droit", 1)
            return True
        elif emplacement_grille[1][2] == "-":
            tour_jeu("O", "milieu_droit", 1)
            return True
        else:
            tour_jeu("O", "bas_droit", 1)
            return True
    elif verificateur_de_victoire_possible([emplacement_grille[0][0], emplacement_grille[1][1], emplacement_grille[2][2]], action) == 2 and (emplacement_grille[0][0] == "-" or emplacement_grille[1][1] == "-" or emplacement_grille[2][2] == "-"):
        if emplacement_grille[0][0] == "-":
            tour_jeu("O", "haut_gauche", 1)
            return True
        elif emplacement_grille[1][1] == "-":
            tour_jeu("O", "centre", 1)
            return True
        else:
            tour_jeu("O", "bas_droit", 1)
            return True
    elif verificateur_de_victoire_possible([emplacement_grille[0][2], emplacement_grille[1][1], emplacement_grille[2][0]], action) == 2 and (emplacement_grille[0][2] == "-" or emplacement_grille[1][1] == "-" or emplacement_grille[2][0] == "-"):
        if emplacement_grille[0][2] == "-":
            tour_jeu("O", "haut_droit", 1)
            return True
        elif emplacement_grille[1][1] == "-":
            tour_jeu("O", "centre", 1)
            return True
        else:
            tour_jeu("O", "bas_gauche", 1)
            return True


def attaque_et_defense_avancee():

    if emplacement_grille[1][1] == "X" and (emplacement_grille[0][0] == "X" or emplacement_grille[0][2] == "X" or emplacement_grille[2][0] == "X" or emplacement_grille[2][2] == "X"):
        if emplacement_grille[0][0] == "X" or emplacement_grille[2][2] == "X":
            if emplacement_grille[0][2] == "-":
                tour_jeu("O", "haut_droit", 1)
            elif emplacement_grille[2][0] == "-":
                tour_jeu("O", "bas_gauche", 1)
            else:
                jeu_ordinateur_aleatoire()
        elif emplacement_grille[0][2] == "X" or emplacement_grille[2][0] == "X":
            if emplacement_grille[0][0] == "-":
                tour_jeu("O", "haut_gauche", 1)
            elif emplacement_grille[2][2] == "-":
                tour_jeu("O", "bas_droit", 1)
            else:
                jeu_ordinateur_aleatoire()
        else:
            jeu_ordinateur_aleatoire()
    elif (emplacement_grille[0][0] == "X" and emplacement_grille[2][2] == "X") or (emplacement_grille[0][2] == "X" and emplacement_grille[2][0] == "X"):
        if emplacement_grille[0][1] == "-":
            tour_jeu("O", "haut_milieu", 1)
        elif emplacement_grille[1][0] == "-":
            tour_jeu("O", "milieu_gauche", 1)
        elif emplacement_grille[1][2] == "-":
            tour_jeu("O", "milieu_droit", 1)
        elif emplacement_grille[2][1] == "-":
            tour_jeu("O", "bas_milieu", 1)
        else:
            jeu_ordinateur_aleatoire()
    elif ((emplacement_grille[0][0] == "X" and emplacement_grille[2][1] == "X") or (emplacement_grille[0][2] == "X" and emplacement_grille[2][1] == "X") or (emplacement_grille[0][0] == "X" and emplacement_grille[1][2] == "X") or (emplacement_grille[2][0] == "X" and emplacement_grille[1][2] == "X") or (emplacement_grille[2][0] == "X" and emplacement_grille[0][1] == "X") or (emplacement_grille[2][2] == "X" and emplacement_grille[0][1] == "X") or (emplacement_grille[0][2] == "X" and emplacement_grille[1][0] == "X") or (emplacement_grille[2][2] == "X" and emplacement_grille[1][0] == "X")) and (emplacement_grille[0][0] == "-" or emplacement_grille[0][2] == "-" or emplacement_grille[2][0] == "-" or emplacement_grille[2][2] == "-"):
        if ((emplacement_grille[0][1] == "X" and emplacement_grille[2][0] == "X") or (emplacement_grille[0][2] == "X" and emplacement_grille[1][0] == "X")) and emplacement_grille[0][0] == "-":
            tour_jeu("O", "haut_gauche", 1)
        elif ((emplacement_grille[0][0] == "X" and emplacement_grille[1][2] == "X") or (emplacement_grille[0][1] == "X" and emplacement_grille[2][2] == "X")) and emplacement_grille[0][2] == "-":
            tour_jeu("O", "haut_droit", 1)
        elif ((emplacement_grille[0][0] == "X" and emplacement_grille[2][1] == "X") or (emplacement_grille[1][0] == "X" and emplacement_grille[2][2] == "X")) and emplacement_grille[2][0] == "-":
            tour_jeu("O", "bas_gauche", 1)
        elif ((emplacement_grille[0][2] == "X" and emplacement_grille[2][1] == "X") or (emplacement_grille[1][2] == "X" and emplacement_grille[2][0] == "X")) and emplacement_grille[2][2] == "-":
            tour_jeu("O", "bas_droit", 1)
        else:
            jeu_ordinateur_aleatoire()
    elif ((emplacement_grille[0][1] == "X" and emplacement_grille[1][2] == "X") or (emplacement_grille[1][2] == "X" and emplacement_grille[2][1] == "X") or (emplacement_grille[2][1] == "X" and emplacement_grille[1][0] == "X") or (emplacement_grille[1][0] == "X" and emplacement_grille[0][1] == "X")) and (emplacement_grille[0][0] == "-" or emplacement_grille[0][2] == "-" or emplacement_grille[2][0] == "-" or emplacement_grille[2][2] == "-"):
        if emplacement_grille[0][1] == "X" and emplacement_grille[1][2] == "X":
            tour_jeu("O", "haut_droit", 1)
        elif emplacement_grille[1][2] == "X" and emplacement_grille[2][1] == "X":
            tour_jeu("O", "bas_droit", 1)
        elif emplacement_grille[2][1] == "X" and emplacement_grille[1][0] == "X":
            tour_jeu("O", "bas_gauche", 1)
        elif emplacement_grille[1][0] == "X" and emplacement_grille[0][1] == "X":
            tour_jeu("O", "haut_gauche", 1)
        else:
            jeu_ordinateur_aleatoire()
    else:
        jeu_ordinateur_aleatoire()


def verificateur_de_victoire_possible(combinaison, action):

    if action == 1:
        symbole_a_verifier = "O"
    else:
        symbole_a_verifier = "X"

    ensemble_cases = [case for case in combinaison if case == symbole_a_verifier]

    return len(ensemble_cases)


#############################################################

##### Fonctions liées aux apparences de la boutique #####


def etat_apparences():

    croix_par_defaut = emplacement_images("croix_par_defaut")
    croix_2 = emplacement_images("croix_2")
    croix_3 = emplacement_images("croix_3")
    croix_4 = emplacement_images("croix_4")

    cercle_par_defaut = emplacement_images("cercle_par_defaut")
    cercle_2 = emplacement_images("cercle_2")
    cercle_3 = emplacement_images("cercle_3")

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if apparences_achetees[0] == "0":
        bouton_selection_croix_2['text'] = "Acheter (5 pièces)"
        bouton_selection_croix_3['text'] = "Acheter (5 pièces)"
        bouton_selection_croix_4['text'] = "Acheter (5 pièces)"
        bouton_selection_cercle_2['text'] = "Acheter (5 pièces)"
        bouton_selection_cercle_3['text'] = "Acheter (5 pièces)"
        bouton_selection_cercle_4['text'] = "Acheter (5 pièces)"
    else:
        for apparence in apparences_achetees:
            if CHEMIN_DOSSIER_apparences + apparence + ".png" == croix_2:
                bouton_selection_croix_2['text'] = "Sélectionner"
                bouton_selection_croix_2['state'] = tkinter.NORMAL
            elif CHEMIN_DOSSIER_apparences + apparence + ".png" == croix_3:
                bouton_selection_croix_3['text'] = "Sélectionner"
                bouton_selection_croix_3['state'] = tkinter.NORMAL
            elif CHEMIN_DOSSIER_apparences + apparence + ".png" == croix_4:
                bouton_selection_croix_4['text'] = "Sélectionner"
                bouton_selection_croix_4['state'] = tkinter.NORMAL

            elif CHEMIN_DOSSIER_apparences + apparence + ".png" == cercle_2:
                bouton_selection_cercle_2['text'] = "Sélectionner"
                bouton_selection_cercle_2['state'] = tkinter.NORMAL
            elif CHEMIN_DOSSIER_apparences + apparence + ".png" == cercle_3:
                bouton_selection_cercle_3['text'] = "Sélectionner"
                bouton_selection_cercle_3['state'] = tkinter.NORMAL
            else:
                bouton_selection_cercle_4['text'] = "Sélectionner"
                bouton_selection_cercle_4['state'] = tkinter.NORMAL

        if "croix_2" not in apparences_achetees:
            bouton_selection_croix_2['text'] = "Acheter (5 pièces)"
        if "croix_3" not in apparences_achetees:
            bouton_selection_croix_3['text'] = "Acheter (5 pièces)"
        if "croix_4" not in apparences_achetees:
            bouton_selection_croix_4['text'] = "Acheter (5 pièces)"

        if "cercle_2" not in apparences_achetees:
            bouton_selection_cercle_2['text'] = "Acheter (5 pièces)"
        if "cercle_3" not in apparences_achetees:
            bouton_selection_cercle_3['text'] = "Acheter (5 pièces)"
        if "cercle_4" not in apparences_achetees:
            bouton_selection_cercle_4['text'] = "Acheter (5 pièces)"

    if CHEMIN_DOSSIER_apparences + lecture_fichier("croix_definie") + ".png" == croix_par_defaut:
        bouton_selection_croix_par_defaut['text'] = "Sélectionné"
        bouton_selection_croix_par_defaut['state'] = tkinter.DISABLED
    elif CHEMIN_DOSSIER_apparences + lecture_fichier("croix_definie") + ".png" == croix_2:
        bouton_selection_croix_2['text'] = "Sélectionné"
        bouton_selection_croix_2['state'] = tkinter.DISABLED
    elif CHEMIN_DOSSIER_apparences + lecture_fichier("croix_definie") + ".png" == croix_3:
        bouton_selection_croix_3['text'] = "Sélectionné"
        bouton_selection_croix_3['state'] = tkinter.DISABLED
    else:
        bouton_selection_croix_4['text'] = "Sélectionné"
        bouton_selection_croix_4['state'] = tkinter.DISABLED

    if croix_par_defaut != CHEMIN_DOSSIER_apparences + lecture_fichier("croix_definie") + ".png":
        bouton_selection_croix_par_defaut['text'] = "Sélectionner"
        bouton_selection_croix_par_defaut['state'] = tkinter.NORMAL

    if CHEMIN_DOSSIER_apparences + lecture_fichier("cercle_defini") + ".png" == cercle_par_defaut:
        bouton_selection_cercle_par_defaut['text'] = "Sélectionné"
        bouton_selection_cercle_par_defaut['state'] = tkinter.DISABLED
    elif CHEMIN_DOSSIER_apparences + lecture_fichier("cercle_defini") + ".png" == cercle_2:
        bouton_selection_cercle_2['text'] = "Sélectionné"
        bouton_selection_cercle_2['state'] = tkinter.DISABLED
    elif CHEMIN_DOSSIER_apparences + lecture_fichier("cercle_defini") + ".png" == cercle_3:
        bouton_selection_cercle_3['text'] = "Sélectionné"
        bouton_selection_cercle_3['state'] = tkinter.DISABLED
    else:
        bouton_selection_cercle_4['text'] = "Sélectionné"
        bouton_selection_cercle_4['state'] = tkinter.DISABLED

    if cercle_par_defaut != CHEMIN_DOSSIER_apparences + lecture_fichier("cercle_defini") + ".png":
        bouton_selection_cercle_par_defaut['text'] = "Sélectionner"
        bouton_selection_cercle_par_defaut['state'] = tkinter.NORMAL


def selection_croix_par_defaut():
    global croix

    croix = tkinter.PhotoImage(file=emplacement_images("croix_par_defaut"))
    emplacement_cercle_defini = lecture_fichier("cercle_defini")
    with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
        contenu_fichier[1] = '[apparences_definies] : croix_par_defaut,' + emplacement_cercle_defini + '\n'
        fichier_sauvegarde.writelines(contenu_fichier)
        fichier_sauvegarde.close()
    label_informations_selection['text'] = 'La croix par défaut a été sélectionnée'
    label_informations_selection['fg'] = "#0CC600"

    etat_apparences()


def selection_croix_2():
    global croix

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if "croix_2" in apparences_achetees:
        croix = tkinter.PhotoImage(file=emplacement_images("croix_2"))
        emplacement_cercle_defini = lecture_fichier("cercle_defini")
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            contenu_fichier[1] = '[apparences_definies] : croix_2,' + emplacement_cercle_defini + '\n'
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        label_informations_selection['text'] = 'La croix "de feu" a été sélectionnée'
        label_informations_selection['fg'] = "#0CC600"
    else:
        if lecture_fichier("nombre_pieces") >= 5:
            label_nombre_pieces['text'] = ecriture_nombre_pieces("achat")
            if apparences_achetees[0] == "0":
                ligne_apparences_achetees = '[apparences_achetees] : croix_2'
            else:
                ligne_apparences_achetees = '[apparences_achetees] : ' + lecture_fichier(apparences_achetees) + ",croix_2"
            croix = tkinter.PhotoImage(file=emplacement_images("croix_2"))
            emplacement_cercle_defini = lecture_fichier("cercle_defini")
            with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
                contenu_fichier[1] = '[apparences_definies] : croix_2,' + emplacement_cercle_defini + '\n'
                contenu_fichier[2] = ligne_apparences_achetees
                fichier_sauvegarde.writelines(contenu_fichier)
                fichier_sauvegarde.close()
            label_informations_selection['text'] = 'La croix "de feu" a été achetée et sélectionnée (-5 pièces)'
            label_informations_selection['fg'] = "#0CC600"
        else:
            label_informations_selection['text'] = "Vous devez posséder au moins 5 pièces pour acheter une apparence"
            label_informations_selection['fg'] = "#CF0000"

    etat_apparences()


def selection_croix_3():
    global croix

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if "croix_3" in apparences_achetees:
        croix = tkinter.PhotoImage(file=emplacement_images("croix_3"))
        emplacement_cercle_defini = lecture_fichier("cercle_defini")
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            contenu_fichier[1] = '[apparences_definies] : croix_3,' + emplacement_cercle_defini + '\n'
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        label_informations_selection['text'] = 'La croix "style bug" a été sélectionnée'
        label_informations_selection['fg'] = "#0CC600"
    else:
        if lecture_fichier("nombre_pieces") >= 5:
            label_nombre_pieces['text'] = ecriture_nombre_pieces("achat")
            if apparences_achetees[0] == "0":
                ligne_apparences_achetees = '[apparences_achetees] : croix_3'
            else:
                ligne_apparences_achetees = '[apparences_achetees] : ' + lecture_fichier(apparences_achetees) + ",croix_3"
            croix = tkinter.PhotoImage(file=emplacement_images("croix_3"))
            emplacement_cercle_defini = lecture_fichier("cercle_defini")
            with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
                contenu_fichier[1] = '[apparences_definies] : croix_3,' + emplacement_cercle_defini + '\n'
                contenu_fichier[2] = ligne_apparences_achetees
                fichier_sauvegarde.writelines(contenu_fichier)
                fichier_sauvegarde.close()
            label_informations_selection['text'] = 'La croix "style bug" a été achetée et sélectionnée (-5 pièces)'
            label_informations_selection['fg'] = "#0CC600"
        else:
            label_informations_selection['text'] = "Vous devez posséder au moins 5 pièces pour acheter une apparence"
            label_informations_selection['fg'] = "#CF0000"

    etat_apparences()


def selection_croix_4():
    global croix

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if "croix_4" in apparences_achetees:
        croix = tkinter.PhotoImage(file=emplacement_images("croix_4"))
        emplacement_cercle_defini = lecture_fichier("cercle_defini")
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            contenu_fichier[1] = '[apparences_definies] : croix_4,' + emplacement_cercle_defini + '\n'
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        label_informations_selection['text'] = 'La croix "style abstrait" a été sélectionnée'
        label_informations_selection['fg'] = "#0CC600"
    else:
        if lecture_fichier("nombre_pieces") >= 5:
            label_nombre_pieces['text'] = ecriture_nombre_pieces("achat")
            if apparences_achetees[0] == "0":
                ligne_apparences_achetees = '[apparences_achetees] : croix_4'
            else:
                ligne_apparences_achetees = '[apparences_achetees] : ' + lecture_fichier(apparences_achetees) + ",croix_4"
            croix = tkinter.PhotoImage(file=emplacement_images("croix_4"))
            emplacement_cercle_defini = lecture_fichier("cercle_defini")
            with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
                contenu_fichier[1] = '[apparences_definies] : croix_4,' + emplacement_cercle_defini + '\n'
                contenu_fichier[2] = ligne_apparences_achetees
                fichier_sauvegarde.writelines(contenu_fichier)
                fichier_sauvegarde.close()
            label_informations_selection['text'] = 'La croix "style abstrait" a été achetée et sélectionnée (-5 pièces)'
            label_informations_selection['fg'] = "#0CC600"
        else:
            label_informations_selection['text'] = "Vous devez posséder au moins 5 pièces pour acheter une apparence"
            label_informations_selection['fg'] = "#CF0000"

    etat_apparences()


def selection_cercle_par_defaut():
    global cercle

    cercle = tkinter.PhotoImage(file=emplacement_images("cercle_par_defaut"))
    emplacement_croix_definie = lecture_fichier("croix_definie")
    with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
        contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_par_defaut\n'
        fichier_sauvegarde.writelines(contenu_fichier)
        fichier_sauvegarde.close()
    label_informations_selection['text'] = 'Le cercle par défaut a été sélectionné'
    label_informations_selection['fg'] = "#0CC600"

    etat_apparences()


def selection_cercle_2():
    global cercle

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if "cercle_2" in apparences_achetees:
        cercle = tkinter.PhotoImage(file=emplacement_images("cercle_2"))
        emplacement_croix_definie = lecture_fichier("croix_definie")
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_2\n'
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        label_informations_selection['text'] = 'Le cercle "de feu" a été sélectionné'
        label_informations_selection['fg'] = "#0CC600"
    else:
        if lecture_fichier("nombre_pieces") >= 5:
            label_nombre_pieces['text'] = ecriture_nombre_pieces("achat")
            if apparences_achetees[0] == "0":
                ligne_apparences_achetees = '[apparences_achetees] : cercle_2'
            else:
                ligne_apparences_achetees = '[apparences_achetees] : ' + lecture_fichier(apparences_achetees) + ",cercle_2"
            cercle = tkinter.PhotoImage(file=emplacement_images("cercle_2"))
            emplacement_croix_definie = lecture_fichier("croix_definie")
            with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
                contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_2\n'
                contenu_fichier[2] = ligne_apparences_achetees
                fichier_sauvegarde.writelines(contenu_fichier)
                fichier_sauvegarde.close()
            label_informations_selection['text'] = 'Le cercle "de feu" a été acheté et sélectionné (-5 pièces)'
            label_informations_selection['fg'] = "#0CC600"
        else:
            label_informations_selection['text'] = "Vous devez posséder au moins 5 pièces pour acheter une apparence"
            label_informations_selection['fg'] = "#CF0000"

    etat_apparences()


def selection_cercle_3():
    global cercle

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if "cercle_3" in apparences_achetees:
        cercle = tkinter.PhotoImage(file=emplacement_images("cercle_3"))
        emplacement_croix_definie = lecture_fichier("croix_definie")
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_3\n'
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        label_informations_selection['text'] = 'Le cercle "d\'or" a été sélectionné'
        label_informations_selection['fg'] = "#0CC600"
    else:
        if lecture_fichier("nombre_pieces") >= 5:
            label_nombre_pieces['text'] = ecriture_nombre_pieces("achat")
            if apparences_achetees[0] == "0":
                ligne_apparences_achetees = '[apparences_achetees] : cercle_3'
            else:
                ligne_apparences_achetees = '[apparences_achetees] : ' + lecture_fichier(apparences_achetees) + ",cercle_3"
            cercle = tkinter.PhotoImage(file=emplacement_images("cercle_3"))
            emplacement_croix_definie = lecture_fichier("croix_definie")
            with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
                contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_3\n'
                contenu_fichier[2] = ligne_apparences_achetees
                fichier_sauvegarde.writelines(contenu_fichier)
                fichier_sauvegarde.close()
            label_informations_selection['text'] = 'Le cercle "d\'or" a été acheté et sélectionné (-5 pièces)'
            label_informations_selection['fg'] = "#0CC600"
        else:
            label_informations_selection['text'] = "Vous devez posséder au moins 5 pièces pour acheter une apparence"
            label_informations_selection['fg'] = "#CF0000"

    etat_apparences()


def selection_cercle_4():
    global cercle

    apparences_achetees = lecture_fichier("apparences_achetees").split(",")

    if "cercle_4" in apparences_achetees:
        cercle = tkinter.PhotoImage(file=emplacement_images("cercle_4"))
        emplacement_croix_definie = lecture_fichier("croix_definie")
        with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
            contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_4\n'
            fichier_sauvegarde.writelines(contenu_fichier)
            fichier_sauvegarde.close()
        label_informations_selection['text'] = 'Le cercle "de peinture" a été sélectionné'
        label_informations_selection['fg'] = "#0CC600"
    else:
        if lecture_fichier("nombre_pieces") >= 5:
            label_nombre_pieces['text'] = ecriture_nombre_pieces("achat")
            if apparences_achetees[0] == "0":
                ligne_apparences_achetees = '[apparences_achetees] : cercle_4'
            else:
                ligne_apparences_achetees = '[apparences_achetees] : ' + lecture_fichier(apparences_achetees) + ",cercle_4"
            cercle = tkinter.PhotoImage(file=emplacement_images("cercle_4"))
            emplacement_croix_definie = lecture_fichier("croix_definie")
            with open(f"{CHEMIN_MAIN}/sauvegarde.txt", "w") as fichier_sauvegarde:
                contenu_fichier[1] = '[apparences_definies] : ' + emplacement_croix_definie + ',cercle_4\n'
                contenu_fichier[2] = ligne_apparences_achetees
                fichier_sauvegarde.writelines(contenu_fichier)
                fichier_sauvegarde.close()
            label_informations_selection['text'] = 'Le cercle "de peinture" a été acheté et sélectionné (-5 pièces)'
            label_informations_selection['fg'] = "#0CC600"
        else:
            label_informations_selection['text'] = "Vous devez posséder au moins 5 pièces pour acheter une apparence"
            label_informations_selection['fg'] = "#CF0000"

    etat_apparences()


#########################################################

main()
