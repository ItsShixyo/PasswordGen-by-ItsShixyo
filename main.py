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

# Cr�er le fen�tre
window = Tk()

# Personnaliser la fen�tre
window.title("Test Tkinter 2")
window.geometry("1600x900")
window.minsize(480,360)
window.iconbitmap("F:\Codes\Programmation\PyCharm\Test Tkinter 2\istockphoto-1147979646-612x612.ico")
window.config(background = '#4E76FD')

# Cr�er la frame principale
frame = Frame(window, bg = '#4E76FD')

# Importation d'image
width = 300
height = 300
image = PhotoImage(file = "F:\Codes\Programmation\PyCharm\Test Tkinter 2\password.png").zoom(15).subsample(32)
canvas = Canvas(frame, width = width, height = height, bg = '#4E76FD', bd = 0, highlightthickness = 0 )
canvas.create_image(width/2, height/2, image = image)
canvas.grid(row = 0, column = 0, sticky = W)

# Cr�er une sous boite
right_frame = Frame(frame,bg = '#4E76FD')

# Cr�er un titre
label_title = Label(right_frame, text = "Mot de passe", font = ("Calibri", 20), bg = '#4E76FD', fg = 'white')
label_title.pack()

# Cr�er un champ / entr�e / input
password_entry = Entry(right_frame, font = ("Calibri", 20), bg = '#4E76FD', fg = 'white')
password_entry.pack()

# Cr�er un bouton G�n�rer
generate_password_button = Button(right_frame, text = "G�n�rer", font = ("Calibri", 20), bg = '#4E76FD', fg = 'white', command = GeneratePassword)
generate_password_button.pack(fill = X)

# Cr�er un bouton Copier
generate_password_button = Button(right_frame, text = "Copier", font = ("Calibri", 20), bg = '#4E76FD', fg = 'white', command = Copy)
generate_password_button.pack(fill = X)

# On place la sous boite � droite de la frame principal
right_frame.grid(row = 0, column = 1, sticky = W)

# Afficher la frame
frame.pack(expand = YES)

# Cr�ation d'une barre de menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = "Nouveau", command = GeneratePassword)
file_menu.add_command(label = "Quitter", command = window.quit)
menu_bar.add_cascade(label = "Fichier", menu = file_menu)

# Configurer fen�tre pour ajouter barre de menu
window.config(menu = menu_bar)

# Afficher la fen�tre
window.mainloop()
