import h5py

outfile = 'output/iz61/GAL_top9000_snp120.hdf5'

# Inspecting the content of an hdf5 file in the command line
# 
# h5ls GAL_top9000_snp120.hdf5
# h5ls GAL_top9000_snp120.hdf5.hdf5/data
# h5ls GAL_top9000_snp120.hdf5.hdf5/sfr_data
# 
# h5ls -d GAL_top9000_snp120.hdf5.hdf5/header
# h5ls -v GAL_top9000_snp120.hdf5.hdf5/data/Lagn
# h5ls -d GAL_top9000_snp120.hdf5.hdf5/data/Lagn
#
# Lagn                     Dataset {9000/Inf, 1/Inf}
# Mbh                      Dataset {9000/Inf, 1/Inf}
# Mdot_hh                  Dataset {9000/Inf, 1/Inf}
# Mdot_stb                 Dataset {9000/Inf, 1/Inf}
# Mhalo                    Dataset {9000/Inf, 1/Inf}
# Mhot                     Dataset {9000/Inf, 1/Inf}
# Ms_bulge                 Dataset {9000/Inf, 1/Inf}
# Type                     Dataset {9000/Inf, 1/Inf}
# lms                      Dataset {9000/Inf, 2/Inf}
# lssfr                    Dataset {9000/Inf, 2/Inf}
# m_I                      Dataset {9000/Inf, 1/Inf}
# m_K                      Dataset {9000/Inf, 1/Inf}
# m_R                      Dataset {9000/Inf, 1/Inf}
# m_R_SDSS                 Dataset {9000/Inf, 1/Inf}
#
# h5ls -d GAL_top9000_snp120.hdf5.hdf5/sfr_data/Lagn
#
# CIII1908_sfr             Dataset {2/Inf, 9000/Inf}
# CIII1908_sfr_flux        Dataset {2/Inf, 9000/Inf}
# CIV1548_sfr              Dataset {2/Inf, 9000/Inf}
# CIV1548_sfr_flux         Dataset {2/Inf, 9000/Inf}
# CIV1551_sfr              Dataset {2/Inf, 9000/Inf}
# CIV1551_sfr_flux         Dataset {2/Inf, 9000/Inf}
# Halpha_sfr               Dataset {2/Inf, 9000/Inf}
# Halpha_sfr_flux          Dataset {2/Inf, 9000/Inf}
# Hbeta_sfr                Dataset {2/Inf, 9000/Inf}
# Hbeta_sfr_flux           Dataset {2/Inf, 9000/Inf}
# HeII1640_sfr             Dataset {2/Inf, 9000/Inf}
# HeII1640_sfr_flux        Dataset {2/Inf, 9000/Inf}
# NII6548_sfr              Dataset {2/Inf, 9000/Inf}
# NII6548_sfr_flux         Dataset {2/Inf, 9000/Inf}
# NII6584_sfr              Dataset {2/Inf, 9000/Inf}
# NII6584_sfr_flux         Dataset {2/Inf, 9000/Inf}
# NV1240_sfr               Dataset {2/Inf, 9000/Inf}
# NV1240_sfr_flux          Dataset {2/Inf, 9000/Inf}
# OII3727_sfr              Dataset {2/Inf, 9000/Inf}
# OII3727_sfr_flux         Dataset {2/Inf, 9000/Inf}
# OIII1661_sfr             Dataset {2/Inf, 9000/Inf}
# OIII1661_sfr_flux        Dataset {2/Inf, 9000/Inf}
# OIII1666_sfr             Dataset {2/Inf, 9000/Inf}
# OIII1666_sfr_flux        Dataset {2/Inf, 9000/Inf}
# OIII4959_sfr             Dataset {2/Inf, 9000/Inf}
# OIII4959_sfr_flux        Dataset {2/Inf, 9000/Inf}
# OIII5007_sfr             Dataset {2/Inf, 9000/Inf}
# OIII5007_sfr_flux        Dataset {2/Inf, 9000/Inf}
# SII6717_sfr              Dataset {2/Inf, 9000/Inf}
# SII6717_sfr_flux         Dataset {2/Inf, 9000/Inf}
# SII6731_sfr              Dataset {2/Inf, 9000/Inf}
# SII6731_sfr_flux         Dataset {2/Inf, 9000/Inf}
# SiIII1883_sfr            Dataset {2/Inf, 9000/Inf}
# SiIII1883_sfr_flux       Dataset {2/Inf, 9000/Inf}
# SiIII1888_sfr            Dataset {2/Inf, 9000/Inf}
# SiIII1888_sfr_flux       Dataset {2/Inf, 9000/Inf}
# lne_sfr                  Dataset {9000/Inf, 2/Inf}
# lu_sfr                   Dataset {9000/Inf, 2/Inf}
# lz_sfr                   Dataset {9000/Inf, 2/Inf}

# READ

f = h5py.File(outfile, 'r')

header = f['header']
data = f['data']

print(list(header.attrs.items()))  
boxsize = header.attrs['volume'] **(1/3)

print([dim.label for dim in data['Mhot'].dims])
print(data['Mhot'].dims[0].label)

f.close()