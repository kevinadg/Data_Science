from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random

# Configurer Selenium pour éviter la détection
options = Options()
options.add_argument("--headless")  # Mode sans affichage
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Lancer Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Charger la page Amazon Espagne
url = "https://www.amazon.es/s?k=Google+Pixel+9+Pro+Noir"
driver.get(url)

# Attendre un temps aléatoire pour éviter la détection
time.sleep(random.uniform(3, 6))

# Extraire le HTML après chargement du JavaScript
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Débogage : afficher les titres des produits trouvés
products = soup.select(".s-main-slot .s-result-item")
for item in products:
    title = item.select_one("h2 a span")
    if title:
        print(f"🔍 Produit trouvé : {title.text.strip()}")

# Trouver le premier Google Pixel 9 Pro Noir
pixel_9_pro = None
for item in products:
    title = item.select_one("h2 a span")
    price_whole = item.select_one(".a-price-whole")
    price_fraction = item.select_one(".a-price-fraction")
    reviews = item.select_one(".a-size-base.s-underline-text")  # Nombre d'avis
    link = item.select_one("h2 a")

    if title and price_whole and link:
        product_name = title.text.strip()
        if "Pixel 9 Pro" in product_name and "Noir" in product_name:  # Filtrer le bon modèle
            price = f"{price_whole.text}{price_fraction.text if price_fraction else ''} €"
            review_count = reviews.text.strip() if reviews else "0"  # Gérer le cas sans avis
            product_link = f"https://www.amazon.es{link['href']}"
            pixel_9_pro = (product_name, price, review_count, product_link)
            break  # Sortir dès qu'on trouve un produit valide

# Affichage des résultats
if pixel_9_pro:
    print(f"\n✅ Produit trouvé : {pixel_9_pro[0]}")
    print(f"💰 Prix : {pixel_9_pro[1]}")
    print(f"❤️ Nombre de J'aime (Avis) : {pixel_9_pro[2]}")
    print(f"🔗 Lien : {pixel_9_pro[3]}")
else:
    print("\n❌ Aucun Google Pixel 9 Pro Noir trouvé.")
