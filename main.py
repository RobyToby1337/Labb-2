import pandas as pd  # Importerar pandas-biblioteket för att hantera och bearbeta data

# Läs in Excel-filen som innehåller statistik för nationella prov
file_path = "riket2023_åk9_np.xlsx"

# Läser in ett specifikt ark (exempel: "Matematik") från Excel-filen
# Skippar de första 6 raderna eftersom de innehåller metadata och rubriker
df = pd.read_excel(file_path, sheet_name="Matematik", skiprows=6, header=0)

# Sätter nya kolumnnamn för att matcha uppgiften och göra tabellen mer läsbar
df.columns = ["Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)", 
              "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)", 
              "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]

# Tar bort rader som saknar data i kolumnerna "Plats" och "Huvudman"
# Detta förhindrar att onödiga tomma rader skrivs ut
df = df.dropna(subset=["Plats", "Huvudman"])

# Återställer indexet efter att rader har tagits bort för att hålla en ren tabell
df.reset_index(drop=True, inplace=True)

# Skriver ut de första raderna av data för att verifiera att allt ser korrekt ut
print(df)