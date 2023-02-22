
import random

class grille: #la personne remplit sa grille 
    def __init__(self):#5 numeros chois plus le complementaire 
        self.numero1 = None
        self.numero2 = None
        self.numero3 = None
        self.numero4 = None
        self.numero5 = None
        self.numerocomp = None
        self.numero = [0] * 5

    def choisistesnumeros(self):
        def verifnumero(num, a, b):#methode pour verifier si un numero est bien compris entre 2 bornes (pour les 5 premiers 0:50, pour le complementaire 0:10)
            while num <= a or num > b:
                print("choisis un nombre valide")
                num = int(input())#si c'est pas valide, la personne rechoisis 
            return num

        def pasdeduplicata(self):#methode pour verifier que chaque nombre choisis est unique 
            self.numero = [self.numero1, self.numero2, self.numero3, self.numero4, self.numero5]
            if len(set(self.numero)) != len(self.numero):#les sets ne permettent pas de duplicata alors lors de la conversion les duplicatas sont supprimes 
                return False
            else:
                return True

        while pasdeduplicata(self) == False:
            self.numero1 = verifnumero(int(input("chois ton premier numero ")), 0, 50)#on applique les verifications a tous les nombres 
            self.numero2 = verifnumero(int(input("chois ton second numero ")), 0, 50)
            self.numero3 = verifnumero(int(input("chois ton troisieme numero ")), 0, 50)
            self.numero4 = verifnumero(int(input("chois ton quatrieme numero ")), 0, 50)
            self.numero5 = verifnumero(int(input("chois ton cinquieme numero ")), 0, 50)
            self.numerocomp = verifnumero(int(input("chois ton numero complémentaire ")), 0, 9)
        return [self.numero1,self.numero2,self.numero3,self.numero4,self.numero5,self.numerocomp]#on renvoie une liste avec les numeros choisis 


class francaisedesjeux: 
    def __init__(self):#les numeros gagnants von etre choisis 
        self.grille = list(range(50))
        self.gagnant1 = None
        self.gagnant2 = None
        self.gagnant3 = None
        self.gagnant4 = None
        self.gagnant5 = None
        self.gagnantcomp = None

    def lesgagnants(self):


        def tirage(self):
            gagnant = random.choice(self.grille) #on choisis un nulero dans la grille de 0 a 5 au hasard 
            self.grille.remove(gagnant)#on le supprime de la grille pour s'assurer de ne pas avoir de doubles 
            return gagnant

        self.gagnant1 = tirage(self)
        self.gagnant2 = tirage(self)
        self.gagnant3 = tirage(self)
        self.gagnant4 = tirage(self)
        self.gagnant5 = tirage(self)
        self.gagnantcomp = random.choice(list(range(9)))#le numero complementaire c'est particulier 
        return [self.gagnant1,self.gagnant2,self.gagnant3,self.gagnant4,self.gagnant5,self.gagnantcomp]#on renvoie une liste avec les numeros gagnatns 


class verif:
    def __init__(self):
        self.nombregaganant = 0

    def cinqpremiers(self,grille1,grille2):#on obtient le nombre de numeros gagnants 
        for i in grille1[0:5]:
            self.nombregaganant += grille2[0:5].count(i)
        print(self.nombregaganant)
        return self.nombregaganant

    def comp(self,grille1,grille2):#on verifie si le complementaire est gagant 
        if grille1[5] == grille2[5]:
            return True
        else:
            return False


def gains(nombregagnant,nombrecomplementaire):
    gains = 0
    if nombregagnant == 0:
        print("la francaise des jeux te remercie de ta participation, tu as perdu")

    if nombregagnant == 1:
        print("tu gagnes 2.2 euros félicitation")
        gains = gains + 2.2

    if nombregagnant == 2:
        print("tu gagnes 4.4 euros, quel venard ")
        gains = gains + 4.4
        if nombrecomplementaire == True:
            print("et avec le complementraire ca fait 10 balles !!")
            gains = gains + 5.6

    if nombregagnant == 3:
        print("ca fait 20 euros ca c'est pas mal")
        gains = gains + 20
        if nombrecomplementaire == True:
            print("et tu as aussi le complementaire quelle chance, 50 euros c'est pas mal !!")
            gains = gains +30

    if nombregagnant == 4:
        print("ca fait beaucoup de fric tu es chanceux, tiens prend tes 400 balles ")
        gains = gains + 400
        if nombrecomplementaire == True:
            print("et le complementaire en plus, ce soir c'est champagne ! 1000 euros  !!")
            gains = gains + 600

    if nombregagnant == 5:
        print("que dire de plus tu as gagné au loto")
        gains = gains + 2000000
        if nombrecomplementaire == True:
            print("ca y est tu es riche il y a plus rien a ajouter  !!")
            gains = gains +1800000

    return gains
jouer = True
prix = 0 
argentgagne = 0
while jouer == True:
    prix = prix + 2
    jeu = grille()
    gl = jeu.choisistesnumeros()
    print(gl)
    arnaque = francaisedesjeux()
    gg = arnaque.lesgagnants()
    print(gg)
    victoire = verif()
    nombredegagné = victoire.cinqpremiers(gl,gg)
    victoires = verif()
    complementairegagné = victoires.comp(gl,gg)
    argentgagne = gains(nombredegagné,complementairegagné)
    

    print (f"ca t'a couté {prix}€")
    print(f"tu as gagné {argentgagne}€")

    print("tu veux continuer a jouer ?")
    if input() != "oui":
            jouer = False
