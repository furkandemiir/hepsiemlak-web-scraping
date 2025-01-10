from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Start the WebDriver
driver = webdriver.Chrome()  # Open the browser using ChromeDriver

# List to hold the ads
listings = []

# Navigate through 20 pages
for page in range(1, 20):
    url = f'https://www.hepsiemlak.com/buca-kiralik?page={page}'
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    # Find the ad cards
    listing_items = driver.find_elements(By.CLASS_NAME, 'listing-item')

    for listing in listing_items:
        try:
            # Extract price, title, location, number of rooms, area, and other information
            fiyat = listing.find_element(By.CLASS_NAME, 'list-view-price').text
            baslik = listing.find_element(By.TAG_NAME, 'h3').text
            konum = listing.find_element(By.CLASS_NAME, 'list-view-location').text

            detay = listing.find_element(By.CLASS_NAME, 'short-property').text.split("\n")
            oda_sayisi = detay[1] if len(detay) > 0 else ''
            alan = detay[2] if len(detay) > 1 else ''
            bina_yasi = detay[3] if len(detay) > 2 else ''

            # Add the ad data to the list
            listings.append({
                'Fiyat': fiyat,
                'Başlık': baslik,
                'Konum': konum,
                'Oda Sayısı': oda_sayisi,
                'Alan': alan,
                'Bina Yaşı': bina_yasi,
            })
        except Exception as e:
            print(f'Error: {e}')
            continue

# Close the browser
driver.quit()

# Convert the data to a DataFrame and save to an Excel file
df = pd.DataFrame(listings)

def temizle_fiyat(fiyat):
    # TL ve boşlukları kaldırarak sadece sayıları tut
    fiyat = re.sub(r'[^\d]', '', fiyat)  # Sadece sayısal karakterleri al
    return int(fiyat) if fiyat else None  # Boşsa None döner

# Fiyat sütununu temizleyip sayısal değere çevir
df['Fiyat'] = df['Fiyat'].apply(temizle_fiyat)

# Alan sütunundaki metrekare birimini kaldırma
def temizle_alan(alan):
    alan = re.sub(r'[^\d]', '', alan)  # Sadece sayısal karakterleri al
    return int(alan) if alan else None

df['Alan'] = df['Alan'].apply(temizle_alan)

# Temizlenmiş veri setini kaydetme
df.to_excel('temizlenmis_veri.xlsx', index=False)
print("Temizlenmiş veri başarıyla kaydedildi: temizlenmis_veri.xlsx")