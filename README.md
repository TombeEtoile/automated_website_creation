# Optimisateur de Contenu SEO

Un outil automatisé pour analyser et optimiser le contenu SEO à partir de données récupérées sur des pages web. Ce projet combine le scraping, le traitement de texte et l'analyse des mots-clés pour aider à la rédaction de contenus SEO optimisés.

## Fonctionnalités

- **Scraping de données** :
  - Récupération des balises `title`, `h1-h6`, et `p` des pages web.
- **Analyse des mots-clés** :
  - Extraction des mots-clés les plus fréquents tout en supprimant les mots parasites (*stop words*).
  - Comptage des occurrences des mots-clés et regroupement des résultats.
- **Comparaison entre pages** :
  - Analyse comparative de plusieurs pages sur un même sujet.
  - Calcul du fichier avec le plus grand nombre de mots.
- **Export des résultats** :
  - Génération de données en JSON et création d'un prompt optimisé pour ChatGPT.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les logiciels suivants :

- Python 3.8 ou supérieur
- Pip pour gérer les dépendances

## Installation

Clonez le projet depuis ce repository :

```bash
git clone https://github.com/ton_nom_utilisateur/nom_du_projet.git
