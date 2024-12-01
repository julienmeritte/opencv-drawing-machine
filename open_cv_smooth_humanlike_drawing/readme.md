<sub>*`Un readme général est disponible à la racine du git.`*</sub>

# Sale Vador Dali

Pré-processing de l'image: Gestion des détails. La deuxième étape, appelée Sale Vador Dali, approfondit le traitement des détails de l'image par l'utilisation d'un flou. Trois flous ici sont mis en place, flou classique, flou gaussien et flou médian.
   1. Flou classique: Le flou classique supprime le contenu à haute fréquence, comme les bords, de l'image et la rend plus lisse.En général, le flou est obtenu par convolution (chaque élément de l'image est ajouté à ses voisins locaux, pondérés par le noyau) de l'image à travers un noyau de filtre passe-bas. (Source: TutorialPoint OpenCV)
   2. Flou gaussien: L'image est convoluée avec un filtre gaussien au lieu du filtre en boîte. Le filtre gaussien est un filtre passe-bas qui supprime les composantes à haute fréquence. (Source: TutorialPoint OpenCV)
   3. Flou médian: l'élément central de l'image est remplacé par la médiane de tous les pixels de la zone du noyau. Cette opération permet de traiter les bords tout en supprimant le bruit. (Source: TutorialPoint OpenCV)


### Installation du projet

`python3 -m pip install -r ./requirements.txt`

### Execution du projet

`python3 main.py`

paramètres utilisable :

`--name / -n` : corresponds au chemin d'une image voulu

`--lower / -l` : corresponds à la valeur du thresholds minimum ( conseillé entre 50 et 200 )

`--ratio / -r`   : corresponds au ratio qui permet d'avoir le thresholds maximum ( conseillé entre 2:1 et 3:1)

`--blur / -b` : permet de définir le blur voulu entre `classic` , `gaussian` et `median`

`--bintensity / -bi` : permet de définir l'intensité du blur ( chiffre impair uniquement )

exemple :

`python3 main.py --name ./images/lion.jpg --lower 100 --ratio 2 --blur gaussian --bintensity 3`

ou

`python3 main.py -n ./images/lion.jpg -l 100 -r 2 -b gaussian -bi 3`
