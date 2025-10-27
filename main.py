"""Programme affichant les nombres premiers de 0 à 100."""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """Renvoie True si p est premier, sinon False"""
    if p in (1, 0):
        return False
    if p==2:
        return True
    for d in range(2, int(sqrt(p))+1):
        if p%d == 0:
            return False
    return True

#### Fonction principale


def main():
    """Affiche les nombres premiers de 0 à 100"""
    # vos appels à la fonction secondaire ici
    borne_droite = 100
    print(f"Les nombres premiers de 0 à {borne_droite} sont : ")
    for n in range(borne_droite):
        if isprime(n):
            print(n, end=", ")

if __name__ == "__main__":
    main()
