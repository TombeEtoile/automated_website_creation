from collections import Counter
import json
from stop_words import stopwords  # Assurez-vous que "stopwords" est défini dans un fichier local ou un module
import math

french_stopwords = set(stopwords)  # Convertir en set pour une recherche plus rapide

target_query = "Quelle chaussure de sport choisir pour courir un marathon"


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def count_word_occurrences(text):
    words = text.lower().split()  # Découpe le texte en mots
    filtered_words = [word.strip(",.!?:;") for word in words if word not in french_stopwords and word.isalpha()]
    word_counts = Counter(filtered_words)
    return word_counts


def set_tuples():
    """Rassemble les mots-clés des fichiers JSON en un dictionnaire global."""
    global_word_counts = Counter()
    for x in range(1, 4):
        file_path = f"mock_{x}.json"
        data = load_json(file_path)
        all_text = " ".join(data.get("p", []))
        word_occurrences = count_word_occurrences(all_text)
        global_word_counts.update(word_occurrences)

    # Diviser chaque valeur par 3, arrondir à l'entier supérieur et retourner le résultat
    combined_keywords = [(word, math.ceil(count / 3)) for word, count in global_word_counts.most_common(20)]
    return combined_keywords


def count_words_in_p(data):
    """Compter le nombre total de mots dans les paragraphes d'un JSON."""
    paragraphs = data.get("p", [])
    total_words = sum(len(paragraph.split()) for paragraph in paragraphs)  # Compte les mots dans chaque paragraphe
    return total_words


def words_number():
    """Identifie le fichier avec le plus grand nombre de mots et affiche les résultats."""
    max_words = 0  # Nombre maximum de mots trouvé
    max_file = ""  # Nom du fichier avec le plus de mots

    for x in range(1, 4):  # Boucle de 1 à 3 inclus
        file_path = f"mock_{x}.json"

        # Charger les données
        data = load_json(file_path)

        # Compter le nombre total de mots dans les paragraphes
        total_words = count_words_in_p(data)

        # print(f"mock_{x}.json contient {total_words} mots dans les paragraphes.")

        # Identifier le fichier avec le plus de mots
        if total_words > max_words:
            max_words = total_words
            max_file = file_path

    # Afficher le résultat final
    # print(f"\nLe fichier avec le plus de mots est {max_file} avec un total de {max_words} mots.")
    return max_words


def extract_data_without_p():
    """Extrait les données des JSON sans la clé 'p' et les organise en dictionnaire de tuples."""
    result = {}
    for x in range(1, 4):  # Boucle pour mock_1.json, mock_2.json, mock_3.json
        file_path = f"mock_{x}.json"

        # Charger le fichier JSON
        data = load_json(file_path)

        # Extraire les données sans la clé 'p'
        data_without_p = {key: value for key, value in data.items() if key != "p"}

        # Convertir les données en tuple
        result[f"mock_{x}"] = tuple(data_without_p.items())

    return result


def prompt_chat_gpt():
    """Génère une requête pour ChatGPT en fonction des mots-clés."""
    combined_keywords = set_tuples()
    extracted_data = extract_data_without_p()
    prompt = (f"Tu es un expert de la rédaction SEO.\n"
              f"Je vais te donner un dictionnaire de tuples.\n"
              f"Les clés de chaque tuple sont les mots qui reviennent le plus pour la requête '{target_query}'.\n"
              f"Tu dois rédiger un contenu de {words_number()} mots.\n"
              f"La valeur de chacune de ces clés représente le nombre de fois que la clé doit apparaître dans ton contenu.\n"
              f"Voici le dictionnaire : {combined_keywords}\n"
              f"Tu dois aussi prendre en compte les plans des trois sites se plaçant premier sur cette requête pour créer un plan le plus complet possible. Voici les 3 plans sous format Json :\n"
              f"{extracted_data}"
              f"Rédige un contenu optimisé pour cette requête en respectant ces indications.")
    return prompt


if __name__ == "__main__":
    '''
    # Imprimer les mots-clés combinés
    print("\n=== Top 20 des mots-clés combinés ===")
    print(set_tuples())

    # Identifier le fichier contenant le plus de mots
    print("\n=== Analyse du fichier avec le plus de mots ===")
    print(words_number())

    # Exécuter la fonction et afficher le résultat
    extracted_data = extract_data_without_p()
    print("\n=== Données extraites sans 'p' ===")
    print(json.dumps(extracted_data, indent=4, ensure_ascii=False))
    '''

    # Générer et afficher le prompt pour ChatGPT
    print("\n=== Prompt pour ChatGPT ===")
    print(prompt_chat_gpt())
