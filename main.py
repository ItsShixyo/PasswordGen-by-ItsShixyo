# coding=latin-1

from copy import copy
from tkinter import *
from random import randint, choice
import string

def GeneratePassword():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join (choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def Copy():
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password_entry.get())

# Créer le fenêtre
window = Tk()

# Personnaliser la fenêtre
window.title("Test Tkinter 2")
window.geometry("1600x900")
window.minsize(480,360)
window.iconbitmap("F:\Codes\Programmation\PyCharm\Test Tkinter 2\istockphoto-1147979646-612x612.ico")
window.config(background = '#4E76FD')

# Créer la frame principale
frame = Frame(window, bg = '#4E76FD')

# Importation d'image
width = 300
height = 300
image = PhotoImage(file = "F:\Codes\Programmation\PyCharm\Test Tkinter 2\password.png").zoom(15).subsample(32)
canvas = Canvas(frame, width = width, height = height, bg = '#4E76FD', bd = 0, highlightthickness = 0 )
canvas.create_image(width/2, height/2, image = image)
canvas.grid(row = 0, column = 0, sticky = W)

# Créer une sous boite
right_frame = Frame(frame,bg = '#4E76FD')

# Créer un titre
label_title = Label(right_frame, text = "Mot de passe", font = ("Calibri", 20), bg = '#4E76FD', fg = 'white')
label_title.pack()

# Créer un champ / entrée / input
password_entry = Entry(right_frame, font = ("Calibri", 20), bg = '#4E76FD', fg = 'white')
password_entry.pack()

# Créer un bouton Générer
generate_password_button = Button(right_frame, text = "Générer", font = ("Calibri", 20), bg = '#4E76FD', fg = 'white', command = GeneratePassword)
generate_password_button.pack(fill = X)

# Créer un bouton Copier
generate_password_button = Button(right_frame, text = "Copier", font = ("Calibri", 20), bg = '#4E76FD', fg = 'white', command = Copy)
generate_password_button.pack(fill = X)

# On place la sous boite à droite de la frame principal
right_frame.grid(row = 0, column = 1, sticky = W)

# Afficher la frame
frame.pack(expand = YES)

# Création d'une barre de menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = "Nouveau", command = GeneratePassword)
file_menu.add_command(label = "Quitter", command = window.quit)
menu_bar.add_cascade(label = "Fichier", menu = file_menu)

# Configurer fenêtre pour ajouter barre de menu
window.config(menu = menu_bar)

# Afficher la fenêtre
window.mainloop()
