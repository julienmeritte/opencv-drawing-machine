<sub>*`Un readme général est disponible à la racine du git.`*</sub>

# Zhang GUI

Rendu de l'image. La troisième étape, appelée Zhang GUI, récupère les contours isolés de l'image pour les dessiner à l'écran. Nous utilisons TurtlePython pour transformer les les pixels noirs de l'image binaire au thresholding et les faire apparaître à l'écran. Le programme dessine de haut en bas et rafrachit selon un nombre de pixels donné.


## Logique Algorithmique

L'algorithme naïf parcourt chaque ligne de l'image binaire, une par une en commençant par le haut.
Pour des raisons de performance, le tracer d'update graphique est désactivé.
Pour chaque ligne, on vérifie chaque pixel un à un, si le pixel est égal à 0 (noir), on le dessine et on update le rendu, avant de redesactiver le traceur.
Une variable est ajoutée pour compter les pixels à dessiner, lorsque le seuil désigné est atteint, on update le rendu et redésactive le traceur. Ceci permet de déterminer la vitesse de rendu, soit au plus lent en temps réel, soit plus rapidement avec un nombre de pixel par rendu plus élevé.

### Installation des dépendances

`python3 -m pip install -r ./requirements.txt`

### Lancement du programme

`python3 main.py`

paramètres utilisable :

`--name / -n` : corresponds au chemin d'une image voulu

`--lower / -l` : corresponds à la valeur du thresholds minimum ( conseillé entre 50 et 200 )

`--ratio / -r`   : corresponds au ratio qui permet d'avoir le thresholds maximum ( conseillé entre 2:1 et 3:1)

`--blur / -b` : permet de définir le blur voulu entre `classic` , `gaussian` et `median`

`--bintensity / -bi` : permet de définir l'intensité du blur ( chiffre impair uniquement )

`--pixel / -p` : Détermine le nombre de pixel à rendre à la fois, déterminant la vitesse de rendu

exemple :

`python3 main.py --name ./images/lion.jpg --lower 100 --ratio 2 --blur gaussian --bintensity 3 --pixel 50`

ou

`python3 main.py -n ./images/lion.jpg -l 100 -r 2 -b gaussian -bi 3 -p 50`
