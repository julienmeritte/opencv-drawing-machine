<sub>*`Un readme général est disponible à la racine du git.`*</sub>

# Renoir et Blanc

Rendu de l'image. La cinquième étape, appelée Paulychrome Gauguin, va depuis le k-d tree de l'étape précédente ajouter des couleurs. Le but sera de d'analyser les couleurs de l'image, pour en récupérer une palette et redessiner l'image coloriée en plus des contours.

## Logique Algorithmique

Dans la continuité de ce qui a déjà été fait, nous utilisons la fonction kmeans de OpenCV, permettant de récupérer une palette de couleur selon un nombre voulu, une "range". Nous aurons leurs coordonnées, ainsi que leurs codes couleur. De sorte à accélérer le processus d'élaboration de la palette, nous redimensionons l'image à des valeurs inférieures seulement pour l'analyse.

Ensuite, depuis les couleurs récupérées, nous faisons le tour des coordonnées de sorte à élaborer un k-d tree depuis ces couleurs et les utiliser au sein de la fonction de dessin humanisé réalisé dans l'étape précédente. Ainsi, nous obtenons l'élaboration d'un dessin d'image au réalisme stupéfiant.

En utilisant 256 couleurs par exemple, nous arrivons à reproduire des images à l'identique.

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

`--color / -c` : permet de définir le nombre de couleur voulu

exemple :

`python3 main.py --name ./images/lion.jpg --lower 100 --ratio 2 --blur gaussian --bintensity 3 --pixel 10 --color 12`

ou

`python3 main.py -n ./images/lion.jpg -l 100 -r 2 -b gaussian -bi 3 -p 10 -c 12`
