import tkinter as tk
from tkinter import messagebox
import random
import string
import time
from threading import Thread

# Fonction pour générer un mot de passe
def generer_mot_de_passe():
    longueur = int(entree_longueur.get())
    caracteres = ""
    if var_minuscule.get():
        caracteres += string.ascii_lowercase
    if var_majuscule.get():
        caracteres += string.ascii_uppercase
    if var_chiffres.get():
        caracteres += string.digits
    if var_symboles.get():
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner au moins un type de caractère.")
        return

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    entree_mot_de_passe.delete(0, tk.END)
    entree_mot_de_passe.insert(0, mot_de_passe)

# Fonction pour l'animation "Matrix" avec des 0 et 1
def matrix_animation():
    for _ in range(20):
        for y in range(20):
            # Création aléatoire d'une séquence de 0 et 1 en vert
            label_matrix = tk.Label(fenetre, text=random.choice(["0", "1"]), fg="#00FF00", bg="black", font=("Courier", 12))
            label_matrix.place(x=random.randint(0, 400), y=y*20)
            fenetre.update()
            time.sleep(0.05)
            label_matrix.destroy()

# Démarre l'animation et génère un mot de passe en parallèle
def start_generation():
    Thread(target=matrix_animation).start()
    fenetre.after(1000, generer_mot_de_passe)  # Démarre la génération de mot de passe après 1 seconde

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("400x400")
fenetre.config(bg="black")

# Longueur du mot de passe
label_longueur = tk.Label(fenetre, text="Longueur du mot de passe :", fg="#00FF00", bg="black")
label_longueur.pack(pady=5)
entree_longueur = tk.Entry(fenetre, fg="black", bg="#00FF00", width=5)
entree_longueur.insert(0, "12")  # Longueur par défaut
entree_longueur.pack(pady=5)

# Options de caractères
var_minuscule = tk.BooleanVar()
var_majuscule = tk.BooleanVar()
var_chiffres = tk.BooleanVar()
var_symboles = tk.BooleanVar()

checkbox_minuscule = tk.Checkbutton(fenetre, text="Lettres minuscules", variable=var_minuscule, fg="#00FF00", bg="black", selectcolor="black")
checkbox_minuscule.pack()
checkbox_majuscule = tk.Checkbutton(fenetre, text="Lettres majuscules", variable=var_majuscule, fg="#00FF00", bg="black", selectcolor="black")
checkbox_majuscule.pack()
checkbox_chiffres = tk.Checkbutton(fenetre, text="Chiffres", variable=var_chiffres, fg="#00FF00", bg="black", selectcolor="black")
checkbox_chiffres.pack()
checkbox_symboles = tk.Checkbutton(fenetre, text="Symboles", variable=var_symboles, fg="#00FF00", bg="black", selectcolor="black")
checkbox_symboles.pack()

# Champ pour afficher le mot de passe généré
label_mot_de_passe = tk.Label(fenetre, text="Mot de passe généré :", fg="#00FF00", bg="black")
label_mot_de_passe.pack(pady=5)
entree_mot_de_passe = tk.Entry(fenetre, width=30, fg="black", bg="#00FF00")
entree_mot_de_passe.pack(pady=5)

# Bouton pour générer le mot de passe
bouton_generer = tk.Button(fenetre, text="Générer le mot de passe", command=start_generation, fg="#00FF00", bg="black")
bouton_generer.pack(pady=10)

# Affichage de la fenêtre
fenetre.mainloop()