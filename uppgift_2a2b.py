import plotly.express as px
import pandas as pd
import os
# Uppgift 2a
# Läser in Excel-filen med betygsdata
# Anger  att header-raden är rad 7 från 0 
header_row = 7  
df = pd.read_excel("betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1B", engine="openpyxl", header=header_row)

# Byt namn på första kolumnen till läsår eftersom den innehåller årtalen
df.rename(columns={"Unnamed: 0": "Läsår"}, inplace=True)

# Skriver ut alla kolumnnamn 
print("Kolumnnamn innan vi byter namn:")
print(df.columns.value_counts())  # Visar om det finns dubbletter

# Filtrera så att vi endast har de rader som innehåller årtalen 2018/19 – 2022/23
df = df[df["Läsår"].astype(str).str.match(r"^\d{4}/\d{2}$")] #gpts tips på formeln

# Bytt namn på kolumner för Andel utan godkänt betyg 
# Om det redan finns en kolumn som heter totalt undviker vi att byta till samma namn
if "Totalt" in df.columns:
    df.rename(columns={"Totalt.2": "Totalt (%)", "Flickor.2": "Flickor (%)", "Pojkar.2": "Pojkar (%)"}, inplace=True)
else:
    df.rename(columns={"Totalt.2": "Totalt", "Flickor.2": "Flickor", "Pojkar.2": "Pojkar"}, inplace=True)

# Skriv ut kolumnnamnen efter att vi bytt namn
print("Kolumnnamn efter namnbyte:")
print(df.columns)

# Väljer de rätta kolumnerna för diagrammet
if "Totalt (%)" in df.columns:
    korrekt_kolumner = ["Totalt (%)", "Flickor (%)", "Pojkar (%)"]
else:
    korrekt_kolumner = ["Totalt", "Flickor", "Pojkar"]

# Kontrollera att de valda kolumnerna finns i DataFrame, annars stoppa programmet
förlorade_kolumner = [kol for kol in korrekt_kolumner if kol not in df.columns]
if förlorade_kolumner:
    raise ValueError(f"Följande kolumner saknas: {förlorade_kolumner}")

# Skapar ett linjediagram med plotly express
fig = px.line(df, x="Läsår", # X-axeln visar olika läsår 2018/19 - 2022/23
              y=korrekt_kolumner, # Y-axeln visar andelen elever utan godkänt betyg (%)
              markers=True, # Lägger till punkter på linjerna för att tydliggöra värdena
              title="Andel elever utan godkänt betyg (2018-2023)",  # Titel för diagrammet
              labels={"value": "Andel elever (%)", "variable": "Kön", "Läsår": "Läsår"}) # Anpassar etiketter

# Anpassar utseendet på grafen # - Ökar linjebredden för bättre synlighet
# Gör markörerna större så att datapunkterna blir tydligare
# Lägger till tydliga titlar på x- och y-axlarna
fig.update_traces(line=dict(width=3), marker=dict(size=8))  # Gör linjerna tjockare (3 px) och förstorar markörerna (8 px)
fig.update_yaxes(title_text="Andel elever utan godkänt betyg (%)") # Sätter en tydlig titel på y-axeln så att det framgår vad som mäts
fig.update_xaxes(title_text="Läsår") # Sätter en tydlig titel på x-axeln så att det framgår vilka årtal som visas

# Sparar filen i mappen visualiseringar
html_path = "visualiseringar/andel_elever_utan_godkänt.html"
fig.write_html(html_path)

print(f"Grafen har sparats som HTML: {html_path}")

# Visa grafen i webbläsaren
fig.show()

# 2B 

#Läser in Excel-filen betyg o prov riksnivå
header_row = 7  # Radnumret där kolumnrubrikerna börjar
df = pd.read_excel("betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1B", engine="openpyxl", header=header_row)

# Bytt namn på första kolumnen till Läsår
df.rename(columns={"Unnamed: 0": "Läsår"}, inplace=True)

#  Filtrera ut endast läsår 2018/19 – 2022/23
df = df[df["Läsår"].astype(str).str.match(r"^\d{4}/\d{2}$")] # gpts tips Den filtrerar alltså ut endast de rader där Läsår är skrivet som YYYY/YY



