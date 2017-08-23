# Function: Herfindahl-Hirschman Index(HHI)   
# Version: 1.0
# Date: Feb 23, 2017
# Author: Jing Chen


#
#Input variable:
# A: n*m matrix where 
#         n:  # of observations 
#         m: employment distribution
#Output variable:
# hhi: a n-element list with HHI


def hhi(A):
    import numpy as np
    A=np.float64(A)
    row_sums=np.sum(A,axis=1)
    new_A=A/row_sums[:,np.newaxis]
    square_A = np.multiply(new_A,new_A)
    hhi=np.sum(square_A,axis=1)
    return hhi
    