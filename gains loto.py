import random

jouer = True
prix = 0
gains = 0
while jouer == True:
    def tirage(grille): #on doit faire 5 tirages alors on va pas l'écrire 5 fois 
        gagnant = random.choice(grille) # choice : trouve un numéro dans la liste donnée apres 
        return gagnant 


    prix = prix + 2
    premier = int(input("\n met ton premier numero \n")) 
    deuxieme = int(input("\n met ton  dexieme numero \n")) #c'est mon programme, c'est moi qui décide alors la faute d'orthographe reste. 
    troisieme = int(input("\n met ton troisieme numero \n"))
    quatrieme = int(input("\n met ton quatrieme numero \n"))
    cinquieme = int(input("\n met ton cinquieme numero \n"))


    grille = list(range(1,50)) # cree une liste de 50 éléments 

    premiergagnant = tirage(grille) #il fait un tirage dans la grille 
    grille.remove(premiergagnant)# il enleve de la grille la valeur gaganante 


    deuxiemegagnant = tirage(grille)#il faut le faire 5 fois pour 5 numéro gagnants 
    grille.remove(deuxiemegagnant)



    troisiemegagnant = tirage(grille)
    grille.remove(troisiemegagnant)


    quatriemegagnant = tirage(grille)
    grille.remove(quatriemegagnant)


    cinquiemegagnant = tirage(grille)
    grille.remove(cinquiemegagnant)



    nombregagnant = 0 # par defaut tu as 0 numéros gagnants 
    if premiergagnant == premier or premiergagnant == deuxieme or premiergagnant == troisieme or premiergagnant == quatrieme or premiergagnant == cinquieme:#on verifie que ton premier nombre est gagnant ou non 
        nombregagnant = nombregagnant+1

    if deuxiemegagnant == premier or deuxiemegagnant == deuxieme or deuxiemegagnant == troisieme or deuxiemegagnant == quatrieme or deuxiemegagnant == cinquieme:#pareil pour le deuxieme 
        nombregagnant = nombregagnant + 1

    if troisiemegagnant == premier or troisiemegagnant == deuxieme or troisiemegagnant == troisieme or troisiemegagnant == quatrieme or troisiemegagnant == cinquieme:# ect
        nombregagnant = nombregagnant + 1 

    if quatriemegagnant == premier or quatriemegagnant == deuxieme or quatriemegagnant == troisieme or quatriemegagnant == quatrieme or quatriemegagnant == cinquieme:
        nombregagnant = nombregagnant + 1 

    if cinquiemegagnant == premier or cinquiemegagnant == deuxieme or cinquiemegagnant == troisieme or cinquiemegagnant == quatrieme or cinquiemegagnant == cinquieme:
        nombregagnant = nombregagnant + 1


    print (premiergagnant,deuxiemegagnant,troisiemegagnant,quatriemegagnant,cinquiemegagnant)
    print(premier,deuxieme,troisieme,quatrieme,cinquieme)
    print(nombregagnant)


    if nombregagnant == 0:
        print("la francaise des jeux te remercie de ta participation, tu as perdu")

    if nombregagnant == 1:
        print("tu gagnes 2.2 euros félicitation")
        gains = gains + 2.2

    if nombregagnant == 2:
        print("tu gagnes 4.4 euros, quel venard ")
        gains = gains + 4.4

    if nombregagnant == 3:
        print("ca fait 20 euros ca c'est pas mal")
        gains = gains + 20

    if nombregagnant == 4:
        print("ca fait beaucoup de fric tu es chanceux, tiens prend tes 400 balles ")
        gains = gains + 400

    if nombregagnant == 5:
        print("que dire de plus tu as gagné au loto")
        gains = gains + 2000000

    print (f"ca t'a couté {prix}€")
    print(f"tu as gagné {gains}€")

    print("tu veux continuer a jouer ?")
    if input() != "oui":
        jouer = False
