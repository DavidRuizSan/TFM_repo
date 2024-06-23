import numpy as np
import pandas as pd
import os
import h5py

# GENERATE INPUT FILE(S) #

# Leer el archivo CSV
SAG = pd.read_csv('input_data/SAG_top3000_snp120.csv')

redshift = [0.117]

# SAG: M_star_bulge, M_star_disk, SFR_bulge, SFR-SFR_bulge, MZ_gas_bulge/M_gas_bulge, MZ_gas_disk/M_gas_disk 
# Cols of the csv: mstardisk,mstarspheroid,sfr,sfrspheroid,mzgasdisk,mzgasspheroid,mcolddisk,halomass,mbh,mhot,mcoldspheroid

# Crear nuevas columnas adicionales (por ejemplo, con valores aleatorios)
# Puedes modificar esta parte para añadir las columnas que necesites con los valores que desees
additional_columns = {
    'zgasdisk': np.divide(SAG['mzgasdisk'], SAG['mcolddisk'], out=np.zeros_like(SAG['mzgasdisk'], dtype=float), where=SAG['mcolddisk']!=0),
    #'zgasdisk': np.array(SAG['mzgasdisk'])/np.array(SAG['mcolddisk']),
    'zgasspheroid': np.divide(SAG['mzgasspheroid'], SAG['mcoldspheroid'], out=np.zeros_like(SAG['mzgasspheroid'], dtype=float), where=SAG['mcoldspheroid']!=0),
    #'zgasspheroid': np.array(SAG['mzgasspheroid'])/np.array(SAG['mcoldspheroid']),
    'sfrdisk': np.array(SAG['sfr'])-np.array(SAG['sfrspheroid']),
    'col1': np.zeros(len(SAG)),
    'Rhm_disk': np.zeros(len(SAG)),
    'Rhm_bulge': np.zeros(len(SAG)),
    'Mdot_stb': np.zeros(len(SAG)),
    'Mdot_hh': np.zeros(len(SAG)),
    'Lagn': np.zeros(len(SAG)),
    'R band SDSS (Apparent magnitude, attenuated': np.zeros(len(SAG)),
    'col2': np.zeros(len(SAG)),
    'col3': np.zeros(len(SAG)),
    'col4': np.zeros(len(SAG)),
    'col5': np.zeros(len(SAG)),
    'col6': np.zeros(len(SAG)),
    'col7': np.zeros(len(SAG)),
    'col8': np.zeros(len(SAG)),
    'col9': np.zeros(len(SAG)),
    'col10': np.zeros(len(SAG)),
    'col11': np.zeros(len(SAG)),
    'col12': np.zeros(len(SAG)),
    'col13': np.zeros(len(SAG)),
    'col14': np.zeros(len(SAG)),
    'col15': np.zeros(len(SAG)),
    'col16': np.zeros(len(SAG)),
    'col17': np.zeros(len(SAG)),
    'col18': np.zeros(len(SAG)),
}

# Añadir las columnas adicionales al DataFrame
for col, values in additional_columns.items():
    #print(col, values)
    SAG[col] = values

# Reordenar las columnas del DataFrame según el orden deseado
# Debes especificar el orden exacto de las columnas aquí
desired_order = [
    'mstardisk', 'mstarspheroid', 'sfrdisk', 'sfrspheroid', 'zgasdisk', 'zgasspheroid', 
    'mcolddisk', 'halomass', 'mbh', 'mhot', 'col1', 'Rhm_disk', 'Rhm_bulge', 'mzgasdisk', 'mzgasspheroid',
    'Mdot_stb', 'Mdot_hh', 'Lagn', 'R band SDSS (Apparent magnitude, attenuated', 'mcoldspheroid', 
    'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 
    'col11', 'col12', 'col13', 'col14', 'col15', 'col16', 'col17', 'col18'
]

SAG = SAG[desired_order]

# Convertir el DataFrame a formato de texto con notación científica
def format_number(num):
    return f"{num:.18e}"

with open('input_data/SAG_top3000_snp120.txt', 'w') as f:
    for _, row in SAG.iterrows():
        formatted_row = " ".join(format_number(num) for num in row)
        f.write(formatted_row + "\n")

print("Archivo TXT generado correctamente.")


