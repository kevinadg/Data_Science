from googlesearch import search

# Termes de recherche
query = "Python programming tutorial"

# Effectuer la recherche Google
for result in search(query, num_results=5):
    print(f"Title: {result.split(' ')[0]}")  # Affiche seulement le titre
    print(f"URL: {result}")
    print("-" * 40)
