import random, datetime, operator, re
from race_parser import RaceParser
from horse_parser_no_handicaps import HorseParser
from sklearn import linear_model

def split_dataset(horses):
    keys = sorted(horses.keys())
    random.seed(1)
    random.shuffle(keys)

    l = len(keys)
    horses_train = [horses[k] for k in keys[l/2:]]
    horses_test = [horses[k] for k in keys[:l/2]]

    return horses_train, horses_test

def compute_vector(horse):
    vector = []
    sorted_races = sorted(horse.races, key=lambda x:x.date, reverse=True)
    speed_in_next_race = sorted_races[0].horse_speed

    # Only compute previous featuer using all the races except last race
    average_speed = 0.0
    average_rating = 0.0
    average_odds = 0.0
    
    for r in sorted_races[1:]:
        average_speed += r.horse_speed
        average_rating += r.horse_rating
        average_odds += r.horse_odds

    no_of_races = len(sorted_races[1:])
    vector.append(average_speed)
    vector.append(average_rating)
    vector.append(average_odds)

    vector = [a/no_of_races for a in vector]
    return vector, sorted_races[0].horse_speed


def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    horses_train_98, horses_test_98 = split_dataset(horses98)

    horses_train_98 = [h for h in horses_train_98 if len(h.races) > 4]

    X_train = []
    y_train = []

    for h in horses_train_98:
        v,s = compute_vector(h)
        X_train.append(v)
        y_train.append(s)
    
    clf = linear_model.LinearRegression()
    clf.fit(X_train, y_train)
    print clf.coef_

                
        




if __name__ == "__main__":
    main()