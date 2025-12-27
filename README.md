# ZeinebVizLib

ZeinebVizLib est une bibliothèque personnelle de visualisation en Python.  
Elle propose des fonctions simples et réutilisables pour créer des graphiques stylés et des visualisations interactives, tout en respectant les bonnes pratiques de data visualisation.

---

##  Visualisations disponibles

La bibliothèque inclut plusieurs types de graphiques basés sur `matplotlib` :

- `styled_line` : courbes (line plot)
- `styled_bar` : histogrammes en barres (bar plot)
- `styled_scatter` : nuage de points (scatter plot)
- `styled_hist` : histogrammes
- `styled_box` : diagrammes en boîte (boxplot)

Tous ces graphiques partagent un **style visuel cohérent** (couleurs, polices, axes, grilles).

---

##  Carte électorale interactive (Bokeh)

Dans le cadre du quiz, une carte électorale interactive a été ajoutée à la bibliothèque en utilisant **Bokeh**.

### Caractéristiques

- Carte interactive basée sur **Bokeh**
- Niveau administratif **ADM2 (Moughataa)**
- Affichage du **candidat gagnant par moughataa**
- **Une seule carte** et **une seule échelle de couleurs**
- Palette perceptuelle **Viridis**
- Interactions disponibles :
  - Zoom
  - Déplacement (pan)
  - Info-bulles (hover)

### Bonnes pratiques appliquées

- Une seule métrique par carte : **nombre de voix du candidat gagnant**
- Une seule échelle de couleurs afin d’éviter toute interprétation trompeuse
- Exclusion explicite des **partis politiques**
- Affichage uniquement des **candidats (personnes physiques)**

Cette approche améliore le tutoriel initial basé sur GeoPandas, qui utilisait plusieurs cartes avec des échelles et palettes différentes.

---

##  Installation

Clonez le dépôt et installez la bibliothèque en mode développement :

```bash
git clone https://github.com/Zeineb-ty/zeinebvizlib.git
cd zeinebvizlib
pip install -e .
