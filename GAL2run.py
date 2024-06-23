import numpy as np
import pandas as pd
import os
import h5py

# GENERATE INPUT FILE(S) #

# Leer el archivo CSV

fpath = ['input_data/GAL_top3000_snp120.csv']
GAL = pd.read_csv(fpath[0])
# redshifts = [0.117]

# Galacticus: spheroidMassStellar,diskMassStellar, diskStarFormationRate, spheroidStarFormationRate, diskAbundancesGasMetals/diskMassGas,spheroidAbundancesGasMetals/spheroidMassGas 
# Cols of the csv: mstardisk,mstarspheroid,sfrdisk,sfrspheroid,mzgasdisk,mzgasspheroid,mcolddisk,halomass,mbh,mhot,mcoldspheroid,zgasdisk,zgasspheroid,test,test2,test3,test4,test5,test6,test7,test8,test9

# Crear nuevas columnas adicionales (por ejemplo, con valores aleatorios)
# Puedes modificar esta parte para añadir las columnas que necesites con los valores que desees
additional_columns = {
    'zgasdisk': np.divide(GAL['mzgasdisk'], GAL['mcolddisk'], out=np.zeros_like(GAL['mzgasdisk'], dtype=float), where=GAL['mcolddisk']!=0),
    #'zgasdisk': np.array(GAL['mzgasdisk'])/np.array(GAL['mcolddisk']),
    'zgasspheroid': np.divide(GAL['mzgasspheroid'], GAL['mcoldspheroid'], out=np.zeros_like(GAL['mzgasspheroid'], dtype=float), where=GAL['mcoldspheroid']!=0),
    #'zgasspheroid': np.array(GAL['mzgasspheroid'])/np.array(GAL['mcoldspheroid']),
    'col1': np.zeros(len(GAL)),
    'Rhm_disk': np.zeros(len(GAL)),
    'Rhm_bulge': np.zeros(len(GAL)),
    'Mdot_stb': np.zeros(len(GAL)),
    'Mdot_hh': np.zeros(len(GAL)),
    'Lagn': np.zeros(len(GAL)),
    'R band SDSS (Apparent magnitude, attenuated': np.zeros(len(GAL)),
    'col2': np.zeros(len(GAL)),
    'col3': np.zeros(len(GAL)),
    'col4': np.zeros(len(GAL)),
    'col5': np.zeros(len(GAL)),
    'col6': np.zeros(len(GAL)),
    'col7': np.zeros(len(GAL)),
    'col8': np.zeros(len(GAL)),
    'col9': np.zeros(len(GAL)),
    'col10': np.zeros(len(GAL)),
    'col11': np.zeros(len(GAL)),
    'col12': np.zeros(len(GAL)),
    'col13': np.zeros(len(GAL)),
    'col14': np.zeros(len(GAL)),
    'col15': np.zeros(len(GAL)),
    'col16': np.zeros(len(GAL)),
    'col17': np.zeros(len(GAL)),
    'col18': np.zeros(len(GAL)),
}

# Añadir las columnas adicionales al DataFrame
for col, values in additional_columns.items():
    #print(col, values)
    GAL[col] = values

# Reordenar las columnas del DataFrame según el orden deseado
# Debes especificar el orden exacto de las columnas aquí
desired_order = [
    'mstardisk', 'mstarspheroid', 'sfrdisk', 'sfrspheroid', 'zgasdisk', 'zgasspheroid', 
    'mcolddisk', 'halomass', 'mbh', 'mhot', 'col1', 'Rhm_disk', 'Rhm_bulge', 'mzgasdisk', 'mzgasspheroid',
    'Mdot_stb', 'Mdot_hh', 'Lagn', 'R band SDSS (Apparent magnitude, attenuated', 'mcoldspheroid', 
    'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 
    'col11', 'col12', 'col13', 'col14', 'col15', 'col16', 'col17', 'col18'
]

GAL = GAL[desired_order]

# Convertir el DataFrame a formato de texto con notación científica
def format_number(num):
    return f"{num:.18e}"

with open('input_data/GAL_top3000_snp120.txt', 'w') as f:
    for _, row in GAL.iterrows():
        formatted_row = " ".join(format_number(num) for num in row)
        f.write(formatted_row + "\n")

print("Archivo TXT generado correctamente.")


