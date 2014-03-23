import numpy as np
import pylab as pl
import random
import matplotlib.pyplot as plt
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset
from sklearn import linear_model, cross_validation
from sklearn.metrics import mean_absolute_error, mean_squared_error

''' Regression Model : Basic '''

def compute_vector(horse):
    horse_vector = []

    # Races sorted in ascending order - last race is most recent
    sorted_races = sorted(horse.races, key=lambda x:x.date, reverse=False)

    # Determine the next race of the horse between 4 and the second last race
    next_race_number = random.randint(3, len(sorted_races)-2)
    speed_in_next_race = sorted_races[next_race_number].horse_speed

    # Compute and append lifetime features
    average_speed = 0.0
    average_odds = 0.0
    average_prize_money = 0.0
    average_distance = 0.0

    for r in sorted_races[:next_race_number]:
        average_speed += r.horse_speed
        average_odds += r.horse_odds
        average_distance += r.distance
        average_prize_money += r.prize

    vector.append(average_speed)
    vector.append(average_odds)
    vector.append(average_prize_money)   
    vector.append(average_distance)
    
    no_of_races = len(sorted_races[:next_race_number])
    vector = [a/no_of_races for a in vector]

    # Retrieve and append previous race information
    previous_race = sorted_races[next_race_number - 1]
    vector.append(previous_race.horse_age)
    vector.append(previous_race.no_of_runners)
    vector.append(previous_race.distance)
    vector.append(previous_race.prize)
    vector.append(previous_race.horse_odds)
    vector.append(previous_race.horse_speed)
    vector.append(previous_race.weight_carried)
    vector.append(previous_race.jockeys_claim)
    vector.append(previous_race.horse_comptime)
    vector.append(previous_race.stall_no)

    return vector, speed_in_next_race

def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParserNoHandicaps('./../Data/born98.csv').races
    races05 = RaceParserNoHandicaps('./../Data/born05.csv').races

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

    # Cross-validation
    cv_scores_98 = cross_validation.cross_val_score(regr98, np.array(horses_98_X_train), np.array(horses_98_y_train), scoring='mean_squared_error', cv=5)

    #print regr98.coeff_

    # Print CV scores
    print '5-fold CV scores using MSE:'
    print cv_scores_98
    print ''

    # Mean and SD of estimate score
    print 'Mean of scores: ' + str(cv_scores_98.mean())
    print 'SD of scores: ' + str(cv_scores_98.std() * 2)
    print ''

    # Train the model using the training sets
    regr98.fit(np.array(horses_98_X_train), np.array(horses_98_y_train))

    # Coefficients
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

    ''' ell1 and ell2 metrics computed using actual speeds and those predicted using the training set '''

    print 'ell1:'
    print ell1(horses_98_y_train, regr98.predict(horses_98_X_train))
    print ''

    print 'ell2:'
    print ell2(horses_98_y_train, regr98.predict(horses_98_X_train))
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

    # Cross-validation
    cv_scores_05 = cross_validation.cross_val_score(regr05, np.array(horses_05_X_train), np.array(horses_05_y_train), scoring='mean_squared_error', cv=5)

    # Print CV scores
    print '5-fold CV scores using MSE:'
    print cv_scores_05
    print ''

    # Mean and SD of estimate score
    print 'Mean of scores: ' + str(cv_scores_05.mean())
    print 'SD of scores: ' + str(cv_scores_05.std() * 2)
    print ''

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

    ''' ell1 and ell2 metrics computed using actual speeds and those predicted using the training set '''

    print 'ell1:'
    print ell1(horses_05_y_train, regr05.predict(horses_05_X_train))
    print ''

    print 'ell2:'
    print ell2(horses_05_y_train, regr98.predict(horses_05_X_train))
    print ''



if __name__ == "__main__":
    main()