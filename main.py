import pandas as pd  # Importerar pandas-biblioteket för att hantera och bearbeta data
import matplotlib.pyplot as plt #Importerar matplotlib för att kunna skapa graferna


# Läs in Excel-filen som innehåller statistik för nationella prov
file_path = "riket2023_åk9_np.xlsx"

# Läser in ett specifikt ark (exempel: Matematik) från Excel-filen
# Skippar de första 6 raderna eftersom de innehåller metadata och rubriker
df = pd.read_excel(file_path, sheet_name="Matematik", skiprows=6, header=0)

# Sätter nya kolumnnamn för att matcha uppgiften och göra tabellen mer läsbar
df.columns = ["Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)", 
              "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)", 
              "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]

# Tar bort rader som saknar data i kolumnerna Plats och Huvudman
# Detta förhindrar att onödiga tomma rader skrivs ut
df = df.dropna(subset=["Plats", "Huvudman"])

# Återställer indexet efter att rader har tagits bort för att hålla en ren tabell
df.reset_index(drop=True, inplace=True)

# Skriver ut de första raderna av data för att verifiera att allt ser korrekt ut
print(df)

# Sett till att Huvudman är strängar och att Totalt (poäng) är numeriskt
df["Huvudman"] = df["Huvudman"].astype(str)

# Se till att poängkolumnerna är numeriska
for category in ["Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]:
    df[category] = pd.to_numeric(df[category], errors="coerce")

# Skapat en stapelgraf för totala poäng per huvudman
plt.figure(figsize=(8, 5))  # Storlek på diagrammet
plt.bar(df["Huvudman"], df["Totalt (poäng)"], color=['blue', 'green', 'red', 'purple'])

# Lägg till etiketter och titel
plt.xlabel("Huvudman")
plt.ylabel("Totalt (poäng)")
plt.title("Totala poäng per huvudman")

# Spara grafen i undermappen visualiseringar
plt.savefig("visualiseringar/totala_poäng.png")

# Visa grafen
plt.show()

# Skapatt en figur med tre subplots (1 rad, 3 kolumner)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Lista med kategorier och färger
categories = ["Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]
colors = ["green", "red", "blue"]

# Loopa genom kategorierna och ritar upp stapeldiagramt
for i, category in enumerate(categories): # Foorloop
    axes[i].bar(df["Huvudman"], df[category], color=colors[i])  # Stapeldiagram
    axes[i].set_title(category)  # Titel för subplot
    axes[i].set_xlabel("Huvudman")  # X-axel etikett
    axes[i].set_ylabel("Poäng")  # Y-axel etikett
    axes[i].tick_params(axis="x", rotation=45)  # Rotera x-etiketter för bättre läsbarhet //gpt tips

# Lagt till en huvudtitel för hela figuren 
plt.suptitle("Poängfördelning per huvudman", fontsize=14)

# Justerat layout så att allt ser bra ut
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Sparat figuren i visualiseringsmappen
plt.savefig("visualiseringar/poängfördelning.png")

# Visar diagrammet
plt.show()