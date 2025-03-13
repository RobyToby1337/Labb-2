import plotly.express as px
import pandas as pd
import os

# Läser in Excel-filen med betygsdata
# Anger  att header-raden är rad 7 från 0 
header_row = 7  
df = pd.read_excel("betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1B", engine="openpyxl", header=header_row)
