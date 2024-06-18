import numpy as np
import pandas as pd
import os
import h5py

# GENERATE INPUT FILE(S) #

# Leer el archivo CSV
GAL = pd.read_csv('src/example_data/GAL_top1000_snp120.csv')
infile = ['src/example_data/GAL_top1000_snp120.csv']

redshift = [0.117]

# Galacticus: spheroidMassStellar,diskMassStellar, diskStarFormationRate, spheroidStarFormationRate, diskAbundancesGasMetals/diskMassGas,spheroidAbundancesGasMetals/spheroidMassGas 
# Cols of the csv: mstardisk,mstarspheroid,sfrdisk,sfrspheroid,mzgasdisk,mzgasspheroid,mcolddisk,halomass,mbh,mhot,mcoldspheroid,zgasdisk,zgasspheroid,test,test2,test3,test4,test5,test6,test7,test8,test9

# Crear nuevas columnas adicionales (por ejemplo, con valores aleatorios)
# Puedes modificar esta parte para añadir las columnas que necesites con los valores que desees
additional_columns = {
    'zgasdisk': np.array(GAL['mzgasdisk'])/np.array(GAL['mcolddisk']),
    'zgasspheroid': np.array(GAL['mzgasspheroid'])/np.array(GAL['mcoldspheroid']),
    'col1': np.zeros(len(GAL)),
    'Rhm_disk': np.zeros(len(GAL)),
    'Rhm_bulge': np.zeros(len(GAL)),
    'Mdot_stb': np.zeros(len(GAL)),
    'Mdot_hh': np.zeros(len(GAL)),
    'Lagn': np.zeros(len(GAL)),
    'R band SDSS (Apparent magnitude, attenuated': np.zeros(len(GAL)),
    'col8': np.zeros(len(GAL)),
    'col9': np.zeros(len(GAL)),
    'col10': np.zeros(len(GAL)),
}

# Añadir las columnas adicionales al DataFrame
for col, values in additional_columns.items():
    print(col, values)
    GAL[col] = values

# Reordenar las columnas del DataFrame según el orden deseado
# Debes especificar el orden exacto de las columnas aquí
desired_order = [
    'mstardisk', 'mstarspheroid', 'sfrdisk', 'sfrspheroid', 'zgasdisk',
    'zgasspheroid', 'mcolddisk', 'halomass', 'mbh', 'mhot', 'col1', 'Rhm_disk', 'Rhm_bulge', 'mzgasdisk', 'mzgasspheroid',
    'Mdot_stb', 'Mdot_hh', 'Lagn', 'R band SDSS (Apparent magnitude, attenuated', 'mcoldspheroid', 
    'test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'col8', 'col9', 'col10'
]

GAL = GAL[desired_order]

# Convertir el DataFrame a formato de texto con notación científica
def format_number(num):
    return f"{num:.18e}"

with open('src/example_data/GAL_top1000_snp120.txt', 'w') as f:
    for _, row in GAL.iterrows():
        formatted_row = " ".join(format_number(num) for num in row)
        f.write(formatted_row + "\n")

print("Archivo TXT generado correctamente.")


