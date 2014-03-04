import random

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

    horses_train = [h for h in horses_train if len(h.races) > 4]
    horses_test = [h for h in horses_test if len(h.races) > 4]

    return horses_train, horses_test

