import numpy as np
import pylab as pl
import random
import matplotlib.pyplot as plt
from race_parser_no_handicaps import RaceParserNoHandicaps
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset, r1
from sklearn import linear_model, cross_validation
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

''' Regression Experiment: Baseline experiment '''

def compute_vector(horse):
    vector = []

    # Races sorted in ascending order - last race is most recent
    sorted_races = sorted(horse.races, key=lambda x:x.date, reverse=False)

    # Determine the next race of the horse between 4 and the second last race
    next_race_number = random.randint(max(4,len(horse.races)/2), len(horse.races)-2)
    speed_in_next_race = sorted_races[next_race_number].horse_speed

    # Retrieve and append previous race information
    previous_race = sorted_races[next_race_number - 1]
    vector.append(previous_race.horse_speed)

    return vector, speed_in_next_race

def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    print ''' HorsesBorn98 Dataset '''
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
    print ''

    horses_98_X_test = []
    horses_98_y_test = []
    for h in horses_test_98:
        v,s = compute_vector(h)
        horses_98_X_test.append(v)
        horses_98_y_test.append(s)

    print 'No. of instances in testing set:'
    print len(horses_98_X_test)
    print len(horses_98_y_test)
    print ''
    
    # Create linear regression object
    regr98 = linear_model.LinearRegression(fit_intercept=True)

    # Train the model using the training sets
    regr98.fit(np.array(horses_98_X_train), np.array(horses_98_y_train))

    # Print Coefficients
    print 'Coefficients:'
    print regr98.coef_
    print ''

    print 'Intercept: '
    print regr98.intercept_
    print ''

    # Predict using the testing set
    horses_98_y_pred = regr98.predict(horses_98_X_test)

    print 'Mean squared error:'
    print mean_squared_error(horses_98_y_test, horses_98_y_pred)
    print ''

    print 'Mean absolute error:'
    print mean_absolute_error(horses_98_y_test, horses_98_y_pred)
    print ''

    print 'R2 Score:'
    print r2_score(horses_98_y_test, horses_98_y_pred)
    print ''

    print '1-R1 Score:'
    print r1(horses_98_y_test, horses_98_y_pred)
    print ''

    print ''' HorsesBorn05 Dataset '''
    horses_train_05, horses_test_05 = split_dataset(horses05)

    horses_05_X_train = []
    horses_05_y_train = []
    for h in horses_train_05:
        v,s = compute_vector(h)
        horses_05_X_train.append(v)
        horses_05_y_train .append(s)

    print 'No. of instances in training set:'
    print len(horses_05_X_train)
    print len(horses_05_y_train)
    print ''

    horses_05_X_test = []
    horses_05_y_test = []
    for h in horses_test_05:
        v,s = compute_vector(h)
        horses_05_X_test.append(v)
        horses_05_y_test.append(s)

    print 'No. of instances in testing set:'
    print len(horses_05_X_test)
    print len(horses_05_y_test)
    print ''
    
    # Create linear regression object
    regr05 = linear_model.LinearRegression(fit_intercept=True)

    # Train the model using the training sets
    regr05.fit(np.array(horses_05_X_train), np.array(horses_05_y_train))

    # Coefficients
    print 'Coefficients:'
    print regr05.coef_
    print ''

    print 'Intercept: '
    print regr05.intercept_
    print ''

    # Predict using the testing set
    horses_05_y_pred = regr05.predict(horses_05_X_test)

    print 'Mean squared error:'
    print mean_squared_error(horses_05_y_test, horses_05_y_pred)
    print ''

    print 'Mean absolute error:'
    print mean_absolute_error(horses_05_y_test, horses_05_y_pred)
    print ''

    print 'R2 Score:'
    print r2_score(horses_05_y_test, horses_05_y_pred)
    print ''

    print '1-R1 Score:'
    print r1(horses_05_y_test, horses_05_y_pred)
    print ''

if __name__ == "__main__":
    main()