
Exercices : cp, ln, mv et motifs génériques


-----------------------------------------------------------------
Partie 1 : Commandes cp, mv, ln (60 minutes)

Exercice 1.1 : Copies basiques
Objectif : Maîtriser cp avec différentes options

# 1. Créez cette structure
mkdir -p ~/exercice_cp/{source,destination,backup}
cd ~/exercice_cp/source
touch {fichier1,fichier2,fichier3}.txt
echo "contenu secret" > secret.txt

# 2. Copie simple
cp fichier1.txt ../destination/

# 3. Copie multiple
cp fichier2.txt fichier3.txt ../destination/

# 4. Copie interactive (demande confirmation si existe)
cp -i fichier1.txt ../destination/

# 5. Copie en préservant les attributs
cp -p secret.txt ../destination/

# 6. Copie récursive d'un dossier
cp -r ../source ../backup/

# Vérifiez avec
ls -la ../destination/
ls -la ../backup/
Solution attendue :

# Structure créée
# destination/ contient les 4 fichiers
# backup/source/ contient aussi les 4 fichiers


-----------------------------------------------------------------
Exercice 1.2 : Déplacements et renommages
Objectif : Comprendre les subtilités de mv

# 1. Préparation
cd ~
mkdir -p exercice_mv/{docs,archives,temp}
cd exercice_mv
touch {rapport,note,liste}.txt

# 2. Déplacer un fichier
mv rapport.txt docs/

# 3. Renommer un fichier
mv note.txt note_importante.txt

# 4. Déplacer et renommer en même temps
mv liste.txt archives/liste_ancienne.txt

# 5. Déplacer plusieurs fichiers
mv *.txt docs/ 2>/dev/null

# 6. Déplacer interactif
mv -i docs/rapport.txt temp/

# Vérifiez
find . -type f
Solution :

./docs/note_importante.txt
./archives/liste_ancienne.txt
./temp/rapport.txt

-----------------------------------------------------------------
Exercice 1.3 : Liens symboliques et physiques
Objectif : Différencier ln avec et sans -s

# 1. Préparation
cd ~
mkdir exercice_ln
cd exercice_ln
echo "Contenu original" > original.txt

# 2. Lien physique (hard link)
ln original.txt lien_physique.txt

# 3. Lien symbolique
ln -s original.txt lien_symbolique.txt

# 4. Comparez
ls -li
# Notez le même inode pour original.txt et lien_physique.txt

# 5. Modifiez via le lien physique
echo "Modification" >> lien_physique.txt

# 6. Vérifiez les trois
cat original.txt
cat lien_physique.txt
cat lien_symbolique.txt

# 7. Supprimez l'original
rm original.txt

# 8. Que se passe-t-il ?
cat lien_physique.txt  # Fonctionne toujours
cat lien_symbolique.txt  # Lien cassé
ls -l lien_symbolique.txt
Questions de compréhension :

Pourquoi lien_physique.txt fonctionne encore après suppression de l'original ?
Que montre ls -l pour le lien symbolique cassé ?

-----------------------------------------------------------------
Partie 2 : Motifs génériques (60 minutes)

Exercice 2.1 : Patterns basiques
Objectif : Utiliser *, ?, []

# 1. Créez des fichiers de test
mkdir -p ~/exercice_patterns
cd ~/exercice_patterns
touch {a,b,c}{1,2,3}.txt
touch {x,y,z}_{jan,feb,mar}.log
touch image{1..5}.{jpg,png,gif}
touch rapport_{2020..2024}_{01..12}.pdf

# 2. Utilisez * pour tout sélectionner
ls *.txt
ls *.log
ls *.pdf

# 3. Utilisez ? pour un caractère
ls ?1.txt        # a1.txt, b1.txt, c1.txt
ls ?_jan.log     # x_jan.log, y_jan.log, z_jan.log

# 4. Utilisez [] pour un ensemble
ls [ab]*.txt     # fichiers commençant par a ou b
ls *[0-9].jpg    # image1.jpg, image2.jpg...
ls rapport_202[0-3]_*.pdf  # 2020 à 2023

# 5. Combinez
ls [xyz]_[fj]*.log
Solution :

ls [ab]*.txt : a1.txt, a2.txt, a3.txt, b1.txt, b2.txt, b3.txt
ls *[0-9].jpg : image1.jpg à image5.jpg
ls [xyz]_[fj]*.log : x_feb.log, x_jan.log, y_feb.log, y_jan.log, z_feb.log, z_jan.log


-----------------------------------------------------------------
Exercice 2.2 : Patterns avancés avec expansion
Objectif : Utiliser {} et ..

# 1. Créez une structure complexe
cd ~
mkdir exercice_advanced
cd exercice_advanced
touch file{A..C}{1..3}.txt
touch log_{2020..2023}_{Q1..Q4}.txt
touch backup_{01..12}_{mon,tue,wed,thu,fri}.tar.gz

# 2. Expansion numérique
echo fichier{1..10}.txt
echo mois_{01..12}.log

# 3. Expansion avec step
echo {0..100..10}       # 0 10 20 ... 100
echo image{000..010..2}.jpg

# 4. Expansion combinée
touch projet_{A,B,C}_v{1..3}.zip

# 5. Utilisation pratique
mkdir -p archive/{2020..2023}/{Q1,Q2,Q3,Q4}
Question : Quelle commande crée tous les fichiers data_jan_01.txt à data_dec_31.txt ?


-----------------------------------------------------------------
Exercice 2.3 : Négation avec [!] ou [^]
Objectif : Exclure des caractères

# 1. Créez des fichiers
cd ~
mkdir exercice_negation
cd exercice_negation
touch {a,b,c,d,e,f,g}{1,2,3}.dat
touch {test,prod,dev}_{backup,log,config}.txt

# 2. Exclure des lettres
ls [^aeiou]*.dat          # Pas de début par voyelle
ls [!aeiou]*.dat          # Même chose (ancienne syntaxe)

# 3. Exclure des chiffres
ls *[!0-9].dat            # Ne finit PAS par un chiffre

# 4. Combinaisons
ls [a-c][!2].dat          # a ou b ou c, suivi de pas 2
ls test_[!b]*.txt         # test_ pas suivi de b


-----------------------------------------------------------------
Partie 3 : Combinaison commandes + patterns (60 minutes)

Exercice 3.1 : Nettoyage intelligent
Objectif : Utiliser mv avec patterns

# 1. Créez un désordre organisé
cd ~
mkdir -p menage
cd menage
touch old_report.txt new_data.csv temporary.tmp backup.bak
touch {1..5}_old.log {1..5}_new.log
touch image_{1..3}.jpg image_{1..3}.png
touch .hidden_file temporary_*

# 2. Déplacez tous les .log dans un dossier logs
mkdir logs
mv *.log logs/

# 3. Renommez les fichiers _old en _archived
for f in *_old.*; do
    mv "$f" "${f/_old/_archived}"
done

# 4. Supprimez les temporaires (simulation d'abord)
echo "Fichiers à supprimer:"
ls *tmp *bak *temp* 2>/dev/null
# Puis pour de vrai (décommentez) :
# rm *tmp *bak *temp*

# 5. Organisez par type
mkdir images documents
mv *.jpg *.png images/
mv *.txt *.csv *.pdf documents/ 2>/dev/null


-----------------------------------------------------------------
Exercice 3.2 : Backup sélectif
Objectif : cp avec filtrage

# 1. Environnement de projet
cd ~
mkdir -p mon_projet/{src,docs,dist,backup}
cd mon_projet/src
touch {main,utils,config}.py
touch {test,api}.js
touch README.md .env config.json
touch old_version.py temporary.tmp

# 2. Backup uniquement les fichiers Python
cp *.py ../backup/

# 3. Backup sans les temporaires
cp [!.]* ../dist/ 2>/dev/null  # Exclut les fichiers cachés
# OU
shopt -s extglob  # Active les patterns étendus
cp !(*.tmp|*~) ../dist/ 2>/dev/null

# 4. Backup récursif avec exclusion
cd ..
mkdir backup_complet
cp -r !(backup*|dist) backup_complet/


-----------------------------------------------------------------
Exercice 3.3 : Liens pour organisation
Objectif : Utiliser ln avec patterns

# 1. Structure de projet
cd ~
mkdir -p projet_web/{css,js,img,dist}
cd projet_web/css
touch {style,reset,print}.css
cd ../js
touch {app,utils,dom}.js
cd ../img
touch {logo,banner,icon}.{png,jpg}

# 2. Créez des liens vers les derniers fichiers modifiés
cd ..
ln -s css/style.css current_style.css
ln -s js/app.js main.js


Bonnes pratiques enseignées : Bonne pratique
Toujours tester avec echo ou ls avant rm, mv, cp

Utiliser -i (interactif) quand on débute
Les patterns ne marchent pas sur les fichiers cachés (.) sans option
Guillemets pour les variables dans les boucles : "$f"

Vérifier avec ls -l après les opérations sur les liens
Commandes de vérification utiles : Vérification


# Voir les inodes
ls -li

# Voir seulement les liens
ls -l | grep '^l'

# Compter les fichiers
find . -type f | wc -l

# Vérifier les doublons
find . -type f -exec md5sum {} \; | sort | uniq -d