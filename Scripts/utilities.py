import random
import numpy as np

''' Returns the races which contain the records of all horses in the dataset '''
def get_full_races(races):
    full_races = {}
    
    for r in races:
        if len(races[r].horses) == races[r].no_of_runners:
            full_races[races[r].race_key] = races[r]

    return full_races

''' Split dataset into training and testing set '''
def split_dataset(horses_dict):
    keys = sorted(horses_dict.keys())
    random.seed(1)
    random.shuffle(keys)

    length = len(keys)
    horses_train = [horses_dict[k] for k in keys[length/2:]]
    horses_test = [horses_dict[k] for k in keys[:length/2]]

    # Remove horses who have less than 7 races
    horses_train = [h for h in horses_train if len(h.races) > 5]
    horses_test = [h for h in horses_test if len(h.races) > 5]

    return horses_train, horses_test

''' Not used'''
def ell1(actual_values, predicted_values):
    N = len(predicted_values)
    differences = np.subtract(predicted_values,actual_values)
    differences = differences/actual_values
    return sum(differences)/float(N)

''' Not used '''
def ell2(actual_values, predicted_values):
    N = len(predicted_values)
    differences = np.subtract(actual_values, predicted_values)
    differences = differences/actual_values
    differences = differences * differences
    np.sqrt(differences)
    return sum(differences)/float(N)

''' Computes the 1-R1 score '''
def r1(actual_values, predicted_values):
    mean_actual_values = np.mean(actual_values)
    N = len(actual_values)

    err_differences = np.subtract(actual_values, predicted_values)
    abs_err_differences = np.absolute(err_differences)
    abs_sum_err_differences = np.sum(abs_err_differences)

    mean_differences = np.subtract(actual_values,mean_actual_values)
    abs_mean_differences = np.absolute(mean_differences)
    abs_sum_mean_differences = np.sum(abs_mean_differences)

    r1_score = np.divide(abs_sum_err_differences, abs_sum_mean_differences)

    return r1_score

def main():
    '''

    '''

if __name__ == "__main__":
    main()