import pandas


# ==========================================
# CHARGEMENT DES DONNEES
# ==========================================

# Informations sur les acteurs
actors = pandas.read_csv(
    r"C:\Users\masao.depre\IMDB\movie_actors.basics.tsv",
    sep="\t",
    na_values=["\\N"]
)

# Liste des acteurs présents dans chaque film
actor_movies = pandas.read_csv(
    r"C:\Users\masao.depre\IMDB\movie.actors.tsv",
    sep="\t",
    na_values=["\\N"]
)

# Notes IMDb des films
ratings = pandas.read_csv(
    r"C:\Users\masao.depre\IMDB\title.ratings.tsv",
    sep="\t",
    na_values=["\\N"]
)


# ==========================================
# PROFIL D'UN ACTEUR
# ==========================================

def profil_acteur():

    nom = input("\nEntrez le nom d'un acteur/actrice : ")

    # Recherche de l'acteur
    resultat = actors[
        actors["primaryName"].str.lower() == nom.lower()
    ]

    # Si aucun acteur n'est trouvé
    if resultat.empty:
        print("Cet acteur/actrice n'existe pas dans la base.")

    else:
        # On récupère la première ligne trouvée
        acteur = resultat.iloc[0]

        # Identifiant IMDb de l'acteur
        nconst = acteur["nconst"]

        # On récupère tous les films de cet acteur
        films_acteur = actor_movies[
            actor_movies["nconst"] == nconst
        ]

        # On ajoute les notes IMDb des films
        films_acteur = pandas.merge(
            films_acteur,
            ratings,
            on="tconst",
            how="inner"
        )

        # Calcul de la note moyenne
        note_moyenne = films_acteur["averageRating"].mean()

        # Affichage du profil
        print("\n==============================")
        print("       PROFIL ACTEUR")
        print("==============================")

        print("Nom :", acteur["primaryName"])
        print("Année de naissance :", acteur["birthYear"])

        if pandas.isna(acteur["deathYear"]):
            print("Statut : vivant")
        else:
            print("Année de décès :", acteur["deathYear"])

        print("Nombre de films notés :", len(films_acteur))
        print(
            "Note moyenne de la filmographie :",
            round(note_moyenne, 2),
            "/ 10"
        )


# ==========================================
# MENU PRINCIPAL
# ==========================================

def run():

    while True:

        print("\n==============================")
        print("       IMDB EXPLORER")
        print("==============================")
        print("a - Profil d'un acteur/actrice")
        print("b - Top 5 des films")
        print("q - Quitter")

        choix = input("\nVotre choix : ").lower()

        if choix == "a":
            profil_acteur()

        elif choix == "b":
            print("Vous avez choisi le top 5 des films.")

        elif choix == "q":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


# ==========================================
# LANCEMENT DU PROGRAMME
# ==========================================

if __name__ == "__main__":
    run()