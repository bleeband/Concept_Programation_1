# Cours : Système de fichiers Linux - Commandes essentielles

## Partie théorique

### 1. Introduction au système de fichiers Linux

**Structure hiérarchique** :

```txt
/ (racine)
├── home/ (dossiers utilisateurs)
├── etc/ (fichiers de configuration)
├── var/ (fichiers variables)
├── tmp/ (fichiers temporaires)
└── ...
```

**Concepts clés** :

- Tout est fichier (y compris les périphériques)
- Sensibilité à la casse : `Fichier.txt` ≠ `fichier.txt`
- Le caractère `.` désigne le dossier courant
- Le caractère `..` désigne le dossier parent
- Les fichiers cachés commencent par `.` (ex: `.bashrc`)

### 2. La commande `ls` - Lister les fichiers

**Syntaxe** :

```bash
ls [options] [chemin]
```

**Options principales** :

- `-l` : format long (permissions, propriétaire, taille, date)
- `-a` : afficher tous les fichiers (y compris cachés)
- `-h` : tailles humainement lisibles (avec -l)
- `-t` : trier par date de modification
- `-r` : ordre inverse
- `-R` : récursif (sous-dossiers)

### 3. La commande `cd` - Changer de répertoire

**Syntaxe** :

```bash
cd [chemin]
```

**Chemins spéciaux** :

- `.` : dossier courant
- `..` : dossier parent
- `~` : dossier home de l'utilisateur
- `-` : dossier précédent
- `/` : racine du système

### 4. La commande `mkdir` - Créer des répertoires

**Syntaxe** :

```bash
mkdir [options] nom_dossier
```

**Options principales** :

- `-p` : créer les parents si nécessaire (arborescence)
- `-v` : mode verbeux (affiche ce qui est créé)

### 5. La commande `touch` - Créer/modifier des fichiers

**Syntaxe** :

```bash
touch [options] nom_fichier
```

**Fonctionnalités** :

- Crée un fichier vide s'il n'existe pas
- Met à jour la date d'accès et modification si le fichier existe
- Peut créer plusieurs fichiers en une commande

---

## Partie pratique : Exercices guidés (90 minutes)

### Exercice 1 : Exploration du système

**Objectif** : Comprendre la structure avec `ls` et `cd`

```bash
# 1. Vérifiez où vous êtes
pwd

# 2. Listez le contenu de votre dossier home
ls ~

# 3. Listez en format long
ls -l ~

# 4. Listez avec les fichiers cachés
ls -la ~

# 5. Allez dans le dossier /tmp
cd /tmp

# 6. Retournez à votre dossier home
cd ~

# 7. Allez dans /var/log et listez le contenu
cd /var/log
ls -l

# 8. Retournez au dossier précédent
cd -
```

### Exercice 2 : Navigation et création de structure

**Objectif** : Maîtriser `cd`, `mkdir` et les chemins relatifs/absolus

```bash
# 1. Créez un dossier "projets" dans votre home
mkdir ~/projets

# 2. Allez dans ce dossier
cd ~/projets

# 3. Créez une arborescence pour un projet web
mkdir -p mon_site/{css,js,images,docs}

# 4. Vérifiez la structure créée
ls -R

# 5. Retournez au dossier parent de "projets"
cd ../..

# 6. Créez une structure complexe en une commande
mkdir -p ~/organisation/{2024/{janvier,fevrier,mars},archives,en_cours}

# 7. Allez dans le dossier "en_cours"
cd ~/organisation/en_cours
```

### Exercice 3 : Manipulation de fichiers avec `touch`

**Objectif** : Créer et organiser des fichiers

```bash
# 1. Retournez dans votre dossier home
cd ~

# 2. Créez un dossier "exercices_terminal"
mkdir exercices_terminal
cd exercices_terminal

# 3. Créez plusieurs fichiers vides en une commande
touch fichier1.txt fichier2.txt fichier3.md

# 4. Créez des fichiers avec des extensions différentes
touch script.sh configuration.conf readme.txt

# 5. Créez des fichiers dans des sous-dossiers existants
touch mon_site/css/style.css mon_site/js/script.js

# 6. Vérifiez ce qui a été créé
ls -la
```

### Exercice 4 : Combinaison des commandes

**Objectif** : Utiliser plusieurs commandes ensemble

```bash
# 1. Créez cette structure complète en une commande
mkdir -p ~/projet_complet/{src/{modules,utils},tests,docs,dist}

# 2. Allez dans le dossier src
cd ~/projet_complet/src

# 3. Créez des fichiers Python dans modules
touch modules/{calculs.py,db.py,api.py}

# 4. Créez un fichier __init__.py dans chaque dossier Python
touch modules/__init__.py utils/__init__.py

# 5. Retournez à la racine du projet
cd ~/projet_complet

# 6. Listez toute l'arborescence
find . -type f | sort
```

### Exercice 5 : Options avancées de `ls`

**Objectif** : Exploiter pleinement la commande `ls`

```bash
# 1. Allez dans /usr/bin
cd /usr/bin

# 2. Listez les 10 premiers fichiers par ordre alphabétique
ls | head -10

# 3. Listez les fichiers triés par taille (du plus grand au plus petit)
ls -lS | head -10

# 4. Listez les fichiers modifiés récemment
ls -lt | head -10

# 5. Listez avec les tailles en Ko, Mo, Go
ls -lh | head -10

# 6. Comptez le nombre total de fichiers
ls -1 | wc -l
```

### Exercice 6 : Scénario professionnel

**Objectif** : Réaliser une tâche réaliste de programmeur

```bash
# 1. Créez un environnement pour un projet Python
mkdir -p ~/pyproject/{src,tests,docs,data}

# 2. Créez la structure des sources
mkdir -p ~/pyproject/src/{models,controllers,views,utils}

# 3. Créez les fichiers Python nécessaires
touch ~/pyproject/src/__init__.py
touch ~/pyproject/src/models/__init__.py
touch ~/pyproject/src/models/user.py
touch ~/pyproject/src/models/product.py

# 4. Créez les fichiers de test
touch ~/pyproject/tests/test_models.py
touch ~/pyproject/tests/test_controllers.py

# 5. Créez la documentation
touch ~/pyproject/docs/{index.md,api.md,install.md}

# 6. Vérifiez la structure finale
cd ~/pyproject
find . -type f | sort
```

### Exercice 7 : Challenge - Organisation efficace

**Objectif** : Optimiser l'organisation avec les commandes apprises

```bash
# 1. Créez cette structure en minimum de commandes :
# ~/entreprise/
# ├── clients/
# │   ├── actifs/
# │   └── archives/
# ├── factures/
# │   ├── 2024/
# │   └── 2023/
# └── projets/
#     ├── en_cours/
#     └── termines/

mkdir -p ~/entreprise/{clients/{actifs,archives},factures/{2024,2023},projets/{en_cours,termines}}

# 2. Créez des fichiers de test dans chaque section
touch ~/entreprise/clients/actifs/client{1..3}.txt
touch ~/entreprise/factures/2024/facture{1..5}.pdf
touch ~/entreprise/projets/en_cours/projet_{a..c}.md

# 3. Naviguez et vérifiez
cd ~/entreprise
ls -R | grep -v '^\.' | head -20
```

---

## Partie consolidation (30 minutes)

### Quiz rapide

1. Quelle commande utilisez-vous pour voir les fichiers cachés ?
2. Comment créer un dossier et ses sous-dossiers en une commande ?
3. Que fait `cd -` ?
4. Comment lister les fichiers par date de modification ?
5. Comment créer 5 fichiers en une seule commande ?

### Bonnes pratiques à retenir

1. **Toujours vérifier où vous êtes** avec `pwd` avant de créer des fichiers
2. **Utiliser `-p` avec `mkdir`** pour éviter les erreurs de chemins
3. **Combiner les options** de `ls` pour une visualisation optimale
4. **Utiliser le completion** (Tab) pour éviter les fautes de frappe
5. **Vérifier avec `ls`** après chaque création/modification

### Projet final

Créez l'environnement de travail idéal pour un développeur :

```bash
# Structure recommandée pour un développeur
mkdir -p ~/dev/{workspace,learning,tools,backup}

# Dans workspace : vos projets
mkdir -p ~/dev/workspace/{python_projects,web_projects,scripts}

# Dans learning : vos exercices
mkdir -p ~/dev/learning/{bash,python,git,docker}

# Créez des fichiers de démarrage dans chaque catégorie
touch ~/dev/learning/bash/{notes.md,exercises.sh,cheatsheet.md}
```

---

## Commandes de référence rapide

```bash
# Navigation
pwd                     # Montre le chemin courant
cd chemin               # Change de dossier
cd ~                    # Retour au home
cd ..                   # Dossier parent

# Visualisation
ls                      # Liste simple
ls -l                   # Liste détaillée
ls -la                  # Tout avec détails
ls -lh                  # Tailles lisibles
ls -t                   # Tri par date

# Création
mkdir dossier           # Crée un dossier
mkdir -p d1/d2/d3       # Crée l'arborescence
touch fichier           # Crée un fichier vide
touch f1 f2 f3          # Crée plusieurs fichiers
```