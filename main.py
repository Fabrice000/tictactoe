from tkinter import *
# afficher le joueur qui gagne
def print_winner():
    global win 
    if win is False:
        win = True
        print("Le joueur ", curent_player, "à gagné le jeu.")
# changement de joueur tour a tour
def switch_player():
    global curent_player
    if curent_player == 'X':
        curent_player ='0'
    else:
        curent_player = 'X'
# verificatiopn de la victoire d'un joueur
def check_win(clicked_row,clicked_col):
    count = 0

    # detection de la victoire horizontale
    for i in range(3):
        current_button = buttons[i][clicked_row]
        

        if current_button['text'] == curent_player:
            count += 1

    if count == 3:
        print_winner()
    count = 0

    # detection de la victoire verticale
    for j in range(3):
        current_button = buttons[clicked_col][j]
        
        if current_button['text'] == curent_player:
            count += 1

    if count == 3:
       print_winner()

    count = 0


    # detection de la victoire diagonale
    for i in range(3):
        current_button = buttons[i][i]
        
        if current_button['text'] == curent_player:
            count += 1

    if count == 3:
        print_winner()

    count = 0

    # detection de la victoire diagonale inversé
    for i in range(3):
        current_button = buttons[ 2 -i][i]
        
        if current_button['text'] == curent_player:
            count += 1

    if count == 3:
       print_winner()

# detection d'un match nul
    if win is False:
        count = 0
        for col in range (3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button ['text']== '0':
                    count += 1
        if count == 9:
            print("Match nul..")
# creation des symboles 
def place_symbol(row, column):

    clicked_button = buttons[column][row]
    # annulation de l'ajout d'un symbole sur un autre 
    if clicked_button['text'] == "":
        clicked_button.config(text=curent_player)
        check_win(row, column)
        switch_player()


# fonction pour creer la grille 


def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = Button(
                root, font=("Arial", 50),
                width=5,height=3,
                command=lambda r=row,c=column:place_symbol(r,c),
                )
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

# variables du jeu
buttons = []
curent_player = 'X'
win = False

# creer la fenetre du jeu 
root = Tk()
# personnalisation de la fenetre 
root.title("TicTacToe")
# taille minimum de la fenetre
root.minsize(500, 500)
# appelle de la fonction qui dessine les grilles
draw_grid()
root.mainloop()