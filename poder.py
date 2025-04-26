from sqlalchemy import Column, Integer, String
class Soldado():
    def __init__(self,comida,madera,oro,poder):
        self.comida = comida
        self.madera = madera
        self.oro = oro
        self.poder = poder
Jinete = Soldado(140,0,100,230)
Espadachin = Soldado(60,20,0,70)
Arqueros = Soldado(80,0,40,100)
podertotal = 0
for a in range(0,100):
    for b in range(0,100):
        for c in range(0,100):
            comida_usada= (a*Jinete.comida + b*Espadachin.comida + c*Arqueros.comida)
            madera_usada= (a*Jinete.madera + b*Espadachin.madera + c*Arqueros.madera)
            oro_usado= (a*Jinete.oro + b*Espadachin.oro + c*Arqueros.oro)
            if comida_usada <= 1200 and madera_usada <= 800 and oro_usado <= 600:
                poder= (a*Jinete.poder + b*Espadachin.poder + c*Arqueros.poder)
                if poder > podertotal:
                    podertotal = poder
                    mejorcombinacion = (a,b,c)
print("La mejor combinacion es: ", mejorcombinacion)
print("El poder total es: ", podertotal)
