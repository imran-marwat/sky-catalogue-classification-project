from math import pi

col_names = ["RA", "DEC", "XMIN", "XMAX", "YMIN", "YMAX", "AREA", "IPEAK", "COSMAG", "ISKY", "XCEN_I", "YCEN_I", "A_U", "B_U", "THETA_U", "A_I", "B_I", "THETA_I", "CLASS", "P_A", "AP1", "AP2", "AP3", "AP4", "AP5", "AP6", "AP7", "AP8", "BLEND", "QUALITY", "N(0,1)", "PRFMAG", "C_COSMAG", "C_PRFMAG", "RA_SDSS", "DEC_SDSS", "GMAG_SDSS", "RMAG_SDSS", "IMAG_SDSS", "CLASS_SDSS"]

#irrelevant_indices = [0, 1, 2, 3, 4, 5, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30]

relevant_indices = [6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39]

def add_ellipticity_df(df):
    return df.assign(ELLIPTICITY = 1 - (df.B_I/df.A_I))

def add_filling_factor(df):
    return df.assign(FILLING_FACTOR = df.AREA / (pi * df.A_U * df.B_U))

def ellipticity(a_i, b_i):
    return (1 - (b_i/a_i))

def filling_factor(area, a_u, b_u):
    return area / (pi * a_u * b_u)

def normalise_sdss_class(df):
    classes = {
        6: 2,
        3: 1
    }
    df['CLASS_SDSS'] = df['CLASS_SDSS'].apply(lambda x: classes[x])
   
