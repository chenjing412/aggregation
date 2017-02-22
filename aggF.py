# Function: Aggregation   
# Version: 1.0
# Date: Feb 22, 2017
# Author: Jing Chen


def aggF (r):
#
#Input variable:
# r: the row aggregation scheme. 
#Output variable:
#S: the aggregation matrix given by the aggregation scheme r.
# Reference: Stair (2013): An Aggregation Matrix MatLab Function.
    import numpy as np
    row=r
    col=np.array(range(len(r)))
    data=np.array([1]*len(r))
    from scipy.sparse import coo_matrix
    s = coo_matrix((data, (row, col)), shape=(max(r)+1, len(r))).toarray()
    # start from zero
    return (s)








