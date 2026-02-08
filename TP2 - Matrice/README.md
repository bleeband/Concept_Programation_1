# Énoncé du TP : Chemin le plus long dans une matrice

## Objectif

Créer un programme qui génère une matrice aléatoire et trouve la longueur du chemin le plus long possible en ne se déplaçant que vers des cellules adjacentes de valeur strictement inférieure.

## Spécifications

Le programme doit demander à l'utilisateur :

    ✅ Le nombre de lignes de la matrice (entier positif)
    ✅ Le nombre de colonnes de la matrice (entier positif)
    ✅ La valeur maximale pour les nombres aléatoires (entier positif ≥ 1)

### 2. Génération de la matrice

    ✅ Générer une matrice de dimensions (lignes × colonnes)
    ✅ Remplir chaque cellule avec un entier aléatoire entre 1 et la valeur maximale saisie
    ✅ Afficher la matrice générée de manière claire

### 3. Règles du chemin

    ✅ On peut partir de n'importe quelle cellule
    ✅ On ne peut se déplacer que vers les 4 directions (haut, bas, gauche, droite)
    ✅ On ne peut aller que vers une cellule dont la valeur est **strictement inférieure**
    ✅ On ne peut pas sortir des limites de la matrice
    ✅ Objectif : trouver la **longueur** (nombre de cellules) du chemin le plus long possible

### 4. Gestion des exceptions (OBLIGATOIRE)

Vous devez gérer les exceptions suivantes :

    ✅ **ValueError** : Lorsque l'utilisateur n'entre pas un nombre entier
    ✅ **Valeurs négatives ou nulles** : Pour les dimensions et la valeur maximale
    ✅ **Dimensions trop grandes** : Proposer une limite raisonnable (ex: 7×7 maximum)
    ✅ **Toute autre erreur inattendue** avec un message clair

### 5. Fonctionnalités attendues

    ✅ Saisie sécurisée avec re-saisie en cas d'erreur
    ✅ Affichage clair de la matrice avec ses indices
    ✅ Calcul et affichage de la longueur du chemin le plus long
    ✅ Possibilité de relancer le programme sans le quitter


### 6. Contraintes techniques

    ✅ N'utilisez aucune librairie externe (seulement `random` pour les nombres aléatoires)
    ✅ Le code doit être bien structuré avec des fonctions
    ✅ Les messages d'erreur doivent être explicites
    ✅ Gestion propre de tous les cas d'erreur

### 7. Plus

    ✅ Afficher un exemple de chemin qui atteint la longueur maximale
    ✅ Afficher des statistiques sur la matrice (min, max, moyenne)
    ** Proposer différentes stratégies de génération de matrice

### 8. Exemples d'exécution

**Exemple 1 (saisie correcte)** :

```
=== CHEMIN LE PLUS LONG DANS UNE MATRICE ===

Entrez le nombre de lignes : 3
Entrez le nombre de colonnes : 3
Entrez la valeur maximale pour les nombres aléatoires : 10

Matrice 3x3 générée :
1  2  3
4  5  6
7  8  9


Calcul en cours...
Longueur du chemin le plus long : 5
```

**Exemple 2 (gestion d'erreur)** :

```
Entrez le nombre de lignes : abc
ERREUR : Veuillez entrer un nombre entier valide.

Entrez le nombre de lignes : -3
ERREUR : Le nombre de lignes doit être positif.

Entrez le nombre de lignes : 20
ERREUR : La matrice est trop grande. Maximum : 7 lignes.
```

