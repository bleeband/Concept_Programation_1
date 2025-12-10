## Partie 1 : Découverte du terminal et premières commandes (45 min)

### 1. Présentation du terminal (15 min)

**Objectif** : Comprendre ce qu'est le terminal et à quoi il sert

**Explications** :

- Le terminal est une interface texte pour communiquer avec l'ordinateur
- Alternative aux interfaces graphiques (clic de souris)
- Historique : vient des terminaux physiques connectés aux mainframes
- Aujourd'hui : émulateur de terminal dans une fenêtre

**Analogies** :

- "Conversation avec l'ordinateur"
- "Boîte de dialogue texte" avec le système

### 2. Ouvrir le terminal (10 min)

**Exercice 1.1 : Différentes méthodes**

```bash
# Méthode 1 : Raccourci clavier
Ctrl + Alt + T

# Méthode 2 : Menu Applications
# → Terminal ou GNOME Terminal

# Méthode 3 : Recherche
# Super (Windows) + taper "terminal"
```

**Exercice 1.2 : Personnalisation basique**

- Agrandir/réduire la fenêtre
- Changer la taille de la police (Ctrl + + / Ctrl + -)
- Observer les onglets (Ctrl + Shift + T)

### 3. Premières commandes (20 min)

**Exercice 1.3 : Commandes de base**

```bash
# Savoir qui je suis
whoami

# Voir où je suis
pwd

# Voir ce qu'il y a autour de moi
ls

# Nettoyer l'écran
clear

# Afficher un message
echo "Bonjour les étudiants !"
```

**Exercice 1.4 : Découverte visuelle**

```bash
# Tester chaque commande et observer le résultat
# Noter ce qui change après chaque commande
```

---

## Partie 2 : Terminal, shell et composition des commandes (45 min)

### 1. Terminal et shell (15 min)

**Explications** :

- **Terminal** : La fenêtre, l'interface physique
- **Shell** : Le programme qui interprète les commandes (Bash, Zsh, etc.)
- Relation : Terminal ←→ Shell ←→ Système d'exploitation

**Exercice 2.1 : Identifier son shell**

```bash
# Voir quel shell j'utilise
echo $SHELL

# Voir la version de bash
bash --version
```

**Exercice 2.2 : Comprendre l'invite de commande**

```
utilisateur@nom-machine:~$
```

- Décortiquer chaque élément
- Que signifie le `~` ? (dossier home)
- Que signifie le `$` ? (prêt pour commande utilisateur)

### 2. Composition d'une commande (30 min)

**Structure type** :

```
commande [options] [arguments]
```

**Exercice 2.3 : Commandes simples**

```bash
# Commande sans option ni argument
date

# Commande avec option
ls -l

# Commande avec argument
ls /home

# Commande avec option et argument
ls -l /home
```

**Exercice 2.4 : Options courtes vs longues**

```bash
# Option courte (souvent -lettre)
ls -a

# Option longue (souvent --mot)
ls --all

# Combinaison d'options courtes
ls -la
```

**Exercice 2.5 : Arguments multiples**

```bash
# Un argument
echo "Bonjour"

# Multiple arguments
echo "Bonjour" "à" "tous"

# Arguments avec espaces
echo "Bonjour à tous les étudiants"
```

---

## Partie 3 : Système d'aide - Manuel et help (45 min)

### 1. Présentation du manuel (15 min)

**Explications** :

- `man` = manual = manuel de référence
- Documentation officielle des commandes
- Existe pour presque toutes les commandes

**Exercice 3.1 : Accéder au manuel**

```bash
# Manuel de la commande ls
man ls

# Navigation dans man :
# - Espace : page suivante
# - b : page précédente
# - /motif : rechercher
# - q : quitter
```

**Exercice 3.2 : Structure d'une page man**

- NAME : nom et brève description
- SYNOPSIS : syntaxe d'utilisation
- DESCRIPTION : explication détaillée
- OPTIONS : liste des options
- EXAMPLES : exemples d'utilisation

### 2. Utilisation du manuel (15 min)

**Exercice 3.3 : Recherche dans man**

```bash
# Rechercher "option" dans man ls
man ls
/option

# Voir les sections
man ls
/EXAMPLES

# Quitter
q
```

**Exercice 3.4 : Manuel de différentes commandes**

```bash
man pwd
man echo
man cd
# (cd est une commande built-in, son man est dans bash)
```

### 3. Utilisation de --help et aide intégrée (15 min)

**Exercice 3.5 : Alternative à man**

```bash
# Aide rapide avec --help
ls --help

# Comparer avec man ls
# Quelle est la différence ?
```

**Exercice 3.6 : Commandes intégrées**

```bash
# Pour les commandes bash intégrées
help cd
help echo

# Voir toutes les commandes intégrées
help
```

**Exercice 3.7 : Quand utiliser quoi ?**

- `man` : documentation complète
- `--help` : aide rapide
- `help` : pour commandes intégrées

---

## Partie 4 : History, raccourcis et mise en pratique (45 min)

### 1. La commande history (20 min)

**Exercice 4.1 : Découverte de l'historique**

```bash
# Voir les dernières commandes
history

# Voir les 10 dernières commandes
history 10

# Rechercher une commande dans l'historique
history | grep "ls"
```

**Exercice 4.2 : Réutiliser l'historique**

```bash
# Exécuter la dernière commande
!!

# Exécuter une commande par son numéro
!123

# Exécuter la dernière commande commençant par...
!ls
!echo
```

**Exercice 4.3 : Nettoyer l'historique**

```bash
# Vider l'historique
history -c

# Vérifier qu'il est vide
history
```

### 2. Raccourcis clavier essentiels (15 min)

**Exercice 4.4 : Raccourcis de navigation**

```bash
# Flèche Haut : commande précédente
# Flèche Bas : commande suivante

# Ctrl + A : aller au début de la ligne
# Ctrl + E : aller à la fin de la ligne

# Ctrl + U : effacer depuis le curseur jusqu'au début
# Ctrl + K : effacer depuis le curseur jusqu'à la fin

# Ctrl + W : effacer le mot précédent
```

**Exercice 4.5 : Raccourcis d'exécution**

```bash
# Tab : auto-complétion
# (taper "ec" puis Tab)
echo

# Ctrl + R : recherche dans l'historique
# (taper Ctrl + R puis "ls")

# Ctrl + C : interrompre
# (lancer "sleep 10" puis Ctrl + C)

# Ctrl + D : fermer le terminal
```

### 3. Session pratique guidée (10 min)

**Exercice 4.6 : Parcours complet**

```bash
# 1. Ouvrir le terminal
# 2. Vérifier où je suis (pwd)
# 3. Voir le contenu (ls)
# 4. Consulter le manuel de ls (man ls)
# 5. Utiliser une option de ls (ls -l)
# 6. Afficher un message (echo)
# 7. Voir l'historique (history)
# 8. Réutiliser une commande (flèche haut)
# 9. Nettoyer l'écran (clear)
```

## Fiche mémo

### Commandes essentielles

- `pwd` - Voir où je suis
- `ls` - Voir le contenu
- `clear` - Nettoyer l'écran
- `man` - Manuel des commandes
- `history` - Historique des commandes

### Raccourcis clavier

- `Tab` : Auto-complétion
- `Flèches Haut/Bas` : Navigation historique
- `Ctrl + C` : Arrêter
- `Ctrl + R` : Rechercher historique
- `Ctrl + A/E` : Début/Fin de ligne

### Structure commande

```
commande -option argument
```

### Aide

- `man commande` : Documentation complète
- `commande --help` : Aide rapide
- `help commande` : Commandes intégrées