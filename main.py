'''On importe sys pour pouvoir augmenter le nombre de récursion maximales.'''
import sys

#### Fonctions secondaires

sys.setrecursionlimit(1500) # On augmente le nombre maximum de récursions.

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon
    un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    let = []
    occ = []
    combi = []
    k = -1 # Compteur initial du nombre d'occurences.
    taille = len(s)

    for i in range (taille) :
        if s[i] is s[i-1] : # Si le caractère est similaire au précédent.
            k = k+1 # Compteur à l'intérieur de la boucle.
        elif i == len(s) :
            break
        else :
            let.append(s[i-1]) # Si le caractère est différent du précédent.
            k = k+1
            occ.append(k)
            k = 0 # Réinitialisation du compteur interne pour le caractère suivant.
    else :
        let.append(s[i]) # Cas pour le dernier caractère.
        occ.append(k+1)


    for item in zip(let,occ) : # On regroupe les lettres et leurs occurences dans une liste.
        combi.append(item)

    return combi


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    de manière récursive.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences).
    """

    if not s : # Cas de la chaîne vide.
        return []

    k = 1 # On compte combien de fois le premier caractère se répète.
    while k < len(s) and s[k] == s[0]:
        k = k + 1

    return [(s[0], k)] + artcode_r(s[k:]) # On renvoie le tuple du premier caractère avec son nombre
                                          # d'occurrences, puis on appelle récursivement le reste
                                          # de la chaîne.


#### Fonction principale


def main():
    '''On essaye les fonctions itérative et récursives sur un exemple.'''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
