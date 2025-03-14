import plotly.express as px
import pandas as pd
import os

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

