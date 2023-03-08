from classes import *


class Visiteur: 
    
    def visitVoiture(self, voiture, args):
        print("Je suis une voiture")
        voiture.moteur.accept(self, args)
        for roue in voiture.roues:
            roue.accept(self, args)
        voiture.carrosserie.accept(self, args)
        
    def visitMoteur(self, moteur, args):
        print("Je suis un moteur")
        
    def visitRoue(self, roue, args):
        print("Je suis une roue")
    
    def visitCarrosserie(self, carrosserie, args):
        print("Je suis une carrosserie")

if __name__ == '__main__':
    voiture = Voiture()
    visiteur = Visiteur()
    voiture.accept(visiteur)