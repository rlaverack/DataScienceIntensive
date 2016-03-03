#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    error_list = []
    i = 0
    for key in predictions:
        error = net_worths[i][0] - predictions[i][0]
        cleaned_data.append((ages[i][0],net_worths[i][0],error))
        error_list.append(error)
        i+=1
    error_list.sort(reverse=True)
    top_err = error_list[80]
    cleaned_data = [i for i in cleaned_data if i[2] >= top_err]

    return cleaned_data
