import numpy as np
import pandas as pd
import os
import h5py

# GENERATE INPUT FILE(S) #

# Leer el archivo CSV
SAG = pd.read_csv('src/example_data/SAG_top1000_snp120_2.csv')

redshift = [0.117]

# SAG: M_star_bulge, M_star_disk, SFR_bulge, SFR-SFR_bulge, MZ_gas_bulge/M_gas_bulge, MZ_gas_disk/M_gas_disk 
# Cols of the csv: mstardisk,mstarspheroid,sfr,sfrspheroid,mzgasdisk,mzgasspheroid,mcolddisk,halomass,mbh,mhot,mcoldspheroid

# Crear nuevas columnas adicionales (por ejemplo, con valores aleatorios)
# Puedes modificar esta parte para añadir las columnas que necesites con los valores que desees
additional_columns = {
    'zgasdisk': np.array(SAG['mzgasdisk'])/np.array(SAG['mcolddisk']),
    'zgasspheroid': np.array(SAG['mzgasspheroid'])/np.array(SAG['mcoldspheroid']),
    'sfrdisk': np.array(SAG['sfr'])-np.array(SAG['sfrspheroid']),
    'col1': np.zeros(len(SAG)),
    'Rhm_disk': np.zeros(len(SAG)),
    'Rhm_bulge': np.zeros(len(SAG)),
    'Mdot_stb': np.zeros(len(SAG)),
    'Mdot_hh': np.zeros(len(SAG)),
    'Lagn': np.zeros(len(SAG)),
    'R band SDSS (Apparent magnitude, attenuated': np.zeros(len(SAG)),
    'col8': np.zeros(len(SAG)),
    'col9': np.zeros(len(SAG)),
    'col10': np.zeros(len(SAG)),
}

# Añadir las columnas adicionales al DataFrame
for col, values in additional_columns.items():
    print(col, values)
    SAG[col] = values

# Reordenar las columnas del DataFrame según el orden deseado
# Debes especificar el orden exacto de las columnas aquí
desired_order = [
    'mstardisk', 'mstarspheroid', 'sfrdisk', 'sfrspheroid', 'zgasdisk',
    'zgasspheroid', 'mcolddisk', 'halomass', 'mbh', 'mhot', 'col1', 'Rhm_disk', 'Rhm_bulge', 'mzgasdisk', 'mzgasspheroid',
    'Mdot_stb', 'Mdot_hh', 'Lagn', 'R band SDSS (Apparent magnitude, attenuated', 'mcoldspheroid', 'col8', 'col9', 'col10'
]

SAG = SAG[desired_order]

# Convertir el DataFrame a formato de texto con notación científica
def format_number(num):
    return f"{num:.18e}"

with open('src/example_data/SAG_top1000_snp120.txt', 'w') as f:
    for _, row in SAG.iterrows():
        formatted_row = " ".join(format_number(num) for num in row)
        f.write(formatted_row + "\n")

print("Archivo TXT generado correctamente.")


