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
def split_dataset(horses):
    keys = sorted(horses.keys())
    random.seed(1)
    random.shuffle(keys)

    l = len(keys)
    horses_train = [horses[k] for k in keys[l/2:]]
    horses_test = [horses[k] for k in keys[:l/2]]

    # Remove horses who have less than 4 races
    horses_train = [h for h in horses_train if len(h.races) > 6]
    horses_test = [h for h in horses_test if len(h.races) > 6]

    #horses_train = [h for h in horses_train if sorted(horse.races, key=lambda x:x.date, reverse=False)[0].horse_age > 4]

    return horses_train, horses_test

''' Computes the mean relative absolute error '''
def mean_relative_absolute_error(predicted_values, actual_values):
    N = len(predicted_values)
    differences = np.subtract(predicted_values,actual_values)
    differences = differences/actual_values
    return difference/N

def mean_relative_squared_error(predicted_values, actual_values):
    N = len(predicted_values)
    differences = np.subtract(actual_values, predicted_values)
    differences = differences/actual_values
    differences = differences * differences
    np.sqrt(differences)
    return difference/N

def main():
    '''

    '''

if __name__ == "__main__":
    main()