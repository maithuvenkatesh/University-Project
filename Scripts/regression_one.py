import numpy as np
import pylab as pl
from race_parser import RaceParser
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset
from sklearn import linear_model

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
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    horses_train_98, horses_test_98 = split_dataset(horses98)

    horses_98_X_train = []
    horses_98_y_train = []
    for h in horses_train_98:
        v,s = compute_vector(h)
        horses_98_X_train.append(v)
        horses_98_y_train .append(s)

    print 'No. of instances in training set:'
    print len(horses_98_X_train)
    print len(horses_98_y_train)

    horses_98_X_test = []
    horses_98_y_test = []
    for h in horses_test_98:
        v,s = compute_vector(h)
        horses_98_X_test.append(v)
        horses_98_y_test.append(s)

    print 'No. of instances in testing set:'
    print len(horses_98_X_test)
    print len(horses_98_y_test)
    
    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(horses_98_X_train, horses_98_y_train)

    # Coefficients
    print 'Coefficients:'
    print regr.coef_

    # Mean square error
    print 'Residual sum of squares:' 
    print np.mean((regr.predict(horses_98_X_test) - horses_98_y_test) ** 2)

    # Explained variance score: 1 is perfect prediction
    print 'Variance score:'
    print regr.score(horses_98_X_test, horses_98_y_test)

    '''
    # Plot outputs
    pl.scatter(horses_98_X_test, horses_98_y_test, colour='black')
    pl.plot(horses_98_X_test, regr.predict(horses_98_X_test), color='blue', linewidth=3)
    pl.xticks(())
    pl.yticks(())
    pl.show()
    '''         
        




if __name__ == "__main__":
    main()