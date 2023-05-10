from classes import Voiture


class Visiteur:

    def visit(self, ast, args=None):
        ast.accept(self, args)

    def visitVoiture(self, voiture, args):
        print("Je suis une voiture")
        self.visit(voiture.moteur, args)
        # voiture.moteur.accept(self, args)
        for roue in voiture.roues:
            # roue.accept(self, args)
            self.visit(roue)
        # voiture.carrosserie.accept(self, args)
        self.visit(voiture.carrosserie)

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
