import pandas as pd  # Importerar pandas-biblioteket för att hantera och bearbeta data
import matplotlib.pyplot as plt #Importerar matplotlib för att kunna skapa graferna
import os # hanterar filsystem och mappar
import plotly.express as px  # Skapar interaktiva grafer med Plotly

# Läser in Excel-filen som innehåller statistik för nationella prov
file_path = "riket2023_åk9_np.xlsx"

# Lista över ämnen som ska läsas in
subjects = ["Engelska", "Matematik", "Svenska", "Svenska som andraspråk"]
dataframes = {}  # Dictionary för att spara varje ämnes data

# Loopar genom varje ämne och läser in datan
for subject in subjects:
    df = pd.read_excel(file_path, sheet_name=subject, skiprows=6, header=0)

    # Sätter nya kolumnnamn för att matcha uppgiften och göra tabellen mer läsbar
    df.columns = ["Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)", 
                  "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)", 
                  "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]

    # Tar bort rader som saknar data i kolumnerna Plats och Huvudman
    df = df.dropna(subset=["Plats", "Huvudman"])

    # Återställer index efter att rader har tagits bort för att hålla en ren tabell
    df.reset_index(drop=True, inplace=True)
    dataframes[subject] = df

# Skriver ut de första raderna av varje ämne
for subject, df in dataframes.items():
    print(f"Förhandsgranskning av {subject}:")
    print(df.head())  # Skriver ut de första 5 raderna för varje ämne

# Loopar genom alla ämnen och säkerställer att rätt datatyper används
for subject, df in dataframes.items():
    df["Huvudman"] = df["Huvudman"].astype(str)  # Konvertera Huvudman till text

    for category in ["Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]:
        df[category] = pd.to_numeric(df[category], errors="coerce")  # Konverterar till numeriskt format

# Skapat en stapelgraf för totala poäng per huvudman
# Se till att mappen visualiseringar finns
os.makedirs("visualiseringar", exist_ok=True)

# Skapar en stapelgraf för varje ämne
for subject, df in dataframes.items():
    plt.figure(figsize=(8, 5))
    plt.bar(df["Huvudman"], df["Totalt (poäng)"], color=['blue', 'green', 'red', 'purple'])

    # Lägg till etiketter och titel
    plt.xlabel("Huvudman")
    plt.ylabel("Totalt (poäng)")
    plt.title(f"Totala poäng per huvudman - {subject}")

    # Spara grafen i undermappen visualiseringar
    plt.savefig(f"visualiseringar/totala_poäng_{subject}.png")

    # Visa grafen
    plt.show()

    # Skapar en subplot-graf för varje ämne
for subject, df in dataframes.items():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Lista med kategorier och färger
    categories = ["Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]
    colors = ["green", "red", "blue"]

    # Loopar igenom kategorierna och ritar upp stapeldiagram
    for i, category in enumerate(categories):
        axes[i].bar(df["Huvudman"], df[category], color=colors[i])  # Stapeldiagram
        axes[i].set_title(f"{category} - {subject}")  # Titel för subplot
        axes[i].set_xlabel("Huvudman")  # X-axel etikett
        axes[i].set_ylabel("Poäng")  # Y-axel etikett
        axes[i].tick_params(axis="x", rotation=45)  # Rotera x-etiketter för bättre läsbarhet // gpt tips

    # Lagt till en huvudtitel för hela figuren 
    plt.suptitle(f"Poängfördelning per huvudman - {subject}", fontsize=14)

    # Justerat layout så att allt ser bra ut
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Sparat figuren i visualiseringsmappen
    plt.savefig(f"visualiseringar/poängfördelning_{subject}.png")

    # Visar diagrammet
    plt.show()

    # Filnamn för datasetet
file_path = "betyg_o_prov_riksnivå.xlsx"

    # Läser in Tabell 1B från Excel-filen
sheet_name = "Tabell 1B"
df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=5, header=0)

