#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy as np
    err = net_worths - predictions  # computer error
    absErr = abs(err)  # compute abs error
    smallIdx = np.argsort(absErr, axis=0)  # sort indices
    finIdx = smallIdx[0:81]  # picking only 81 of the 80 values
    
    
    cleaned_data = zip(ages[finIdx], net_worths[finIdx], err[finIdx])
    
    return cleaned_data

