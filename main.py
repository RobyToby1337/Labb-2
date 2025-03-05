import pandas as pd

# Läs in Excel-filen
file_path = "riket2023_åk9_np.xlsx"

# Ladda in Excel-filen och visa alla sheets
xls = pd.ExcelFile(file_path)
print("Tillgängliga sheets:", xls.sheet_names)

# Läs in ett specifikt sheet och justera antalet rader att hoppa över
df = pd.read_excel(xls, sheet_name="Matematik", skiprows=5, header=0)  # Hoppar över de första 5 raderna

# Visa de första raderna för att se om datan ser rätt ut
print(df.head())