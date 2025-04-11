import wikipediaapi

headers={
    "User-Agent":"mypython/2.0 (kevinadagbe@gmail.com)"
}
language='fr'
search ="python"

wiki_wiki = wikipediaapi.Wikipedia(language='fr', user_agent='mypython/2.0 (kevinadagbe@gmail.com)').page(search)

print(wiki_wiki.text)