import numpy as np
import pandas as pd
import os
import h5py

# GENERATE INPUT FILE(S) #

# Leer el archivo CSV
SAGE = pd.read_csv('src/example_data/SAGE_top1000_snp120.csv')

redshift = [0.117]

# SAGE: mstar_spheroid, mstar-mstar_spheroid, sfr_spheroid, sfr_disk, zgas_spheroid, zgas_disk  
# Cols of the csv: mstardisk,mstarspheroid,sfr,sfrspheroid,mzgasdisk,mzhothalo,mcolddisk,halomass,mbh,mhot

# Crear nuevas columnas adicionales (por ejemplo, con valores aleatorios)
# Puedes modificar esta parte para añadir las columnas que necesites con los valores que desees
additional_columns = {
    'zgasdisk': np.array(SAGE['mzgasdisk'])/np.array(SAGE['mcolddisk']),
    'mcoldspheroid': np.array(SAGE['mhot'])-np.array(SAGE['mcolddisk']),
    'zgasspheroid': (np.array(SAGE['mzhothalo'])-np.array(SAGE['mzgasdisk']))/(np.array(SAGE['mhot'])-np.array(SAGE['mcolddisk'])),
    'col1': np.zeros(len(SAGE)),
    'Rhm_disk': np.zeros(len(SAGE)),
    'Rhm_bulge': np.zeros(len(SAGE)),
    'col2': np.zeros(len(SAGE)),
    'Mdot_stb': np.zeros(len(SAGE)),
    'Mdot_hh': np.zeros(len(SAGE)),
    'Lagn': np.zeros(len(SAGE)),
    'R band SDSS (Apparent magnitude, attenuated': np.zeros(len(SAGE)),
    'col8': np.zeros(len(SAGE)),
    'col9': np.zeros(len(SAGE)),
    'col10': np.zeros(len(SAGE)),
}

# Añadir las columnas adicionales al DataFrame
for col, values in additional_columns.items():
    print(col, values)
    SAGE[col] = values

# Reordenar las columnas del DataFrame según el orden deseado
# Debes especificar el orden exacto de las columnas aquí
desired_order = [
    'mstardisk', 'mstarspheroid', 'sfrdisk', 'sfrspheroid', 'zgasdisk',
    'zgasspheroid', 'mcolddisk', 'halomass', 'mbh', 'mhot', 'col1', 'Rhm_disk', 'Rhm_bulge', 'mzgasdisk', 'col2',
    'Mdot_stb', 'Mdot_hh', 'Lagn', 'R band SDSS (Apparent magnitude, attenuated', 'mcoldspheroid', 'col8', 'col9', 'col10'
]

SAGE = SAGE[desired_order]

# Convertir el DataFrame a formato de texto con notación científica
def format_number(num):
    return f"{num:.18e}"

with open('src/example_data/SAGE_top1000_snp120.txt', 'w') as f:
    for _, row in SAGE.iterrows():
        formatted_row = " ".join(format_number(num) for num in row)
        f.write(formatted_row + "\n")

print("Archivo TXT generado correctamente.")


