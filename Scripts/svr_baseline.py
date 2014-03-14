import numpy as np
import pylab as pl
import random
import matplotlib.pyplot as plt
from collections import Counter
from race_parser_no_handicaps import RaceParserNoHandicaps
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset
from sklearn.svm import SVR 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, explained_variance_score

''' svression Experiment 3: Baseline experiment '''

def compute_vector(horse):
    vector = []
    sorted_races = sorted(horse.races, key=lambda x:x.date, reverse=False)

    # Determine the next race of the horse between 4 and the second last race
    next_race_number = random.randint(3, len(sorted_races)-2)
    speed_in_next_race = sorted_races[next_race_number].horse_speed

    # Compute and append lifetime features
    average_speed = 0.0
    average_rating = 0.0
    average_odds = 0.0
    average_prize_money = 0.0
    average_distance = 0.0
    
    for r in sorted_races[:next_race_number]:
        average_speed += r.horse_speed
        average_rating += r.horse_rating
        average_odds += r.horse_odds
        average_distance += r.distance
        average_prize_money += r.prize

    vector.append(average_speed)
    vector.append(average_rating)
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
    vector.append(previous_race.horse_rating)
    vector.append(previous_race.horse_speed)

    return vector, speed_in_next_race

def plot_speeds(speeds, colour, title):
    plt.plot(speeds, colour)
    plt.xlabel('Data Points')
    plt.ylabel('Speed (miles/hour')
    #plt.title(title)
    plt.show()


def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParserNoHandicaps('./../Data/born98.csv').races
    races05 = RaceParserNoHandicaps('./../Data/born05.csv').races

    ''' HorsesBorn98 Dataset '''
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
    
    # Create svr object
    svr98 = SVR(kernel='poly', C=1e3, gamma=0.1)

    # Train the model using the training sets
    svr98.fit(horses_98_X_train, horses_98_y_train)

    horses_98_y_pred = svr98.predict(horses_98_X_test)

    # Explained variance score: 1 is perfect prediction
    print 'Variance score:'
    print svr98.score(horses_98_X_test, horses_98_y_test)
    print ''

    print 'Mean absolute error:'
    print mean_absolute_error(horses_98_y_test, horses_98_y_pred)
    print ''

    print 'Explained variance:'
    print explained_variance_score(horses_98_y_test, horses_98_y_pred)
    print ''

    print 'Mean squared error:'
    print mean_squared_error(horses_98_y_test, horses_98_y_pred)
    print ''

    print 'R2 score:'
    print r2_score(horses_98_y_test, horses_98_y_pred)
    print ''


    ''' HorsesBorn05 Dataset '''
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
    
    # Create linear svression object
    svr05 = SVR(kernel='poly', C=1e3, gamma=0.1)

    # Train the model using the training sets
    svr05.fit(horses_05_X_train, horses_05_y_train)

    horses_05_y_pred = svr05.predict(horses_05_X_test)

    # Explained variance score: 1 is perfect prediction
    print 'Variance score:'
    print svr05.score(horses_05_X_test, horses_05_y_test)
    print ''

    print 'Mean absolute error:'
    print mean_absolute_error(horses_05_y_test, horses_05_y_pred)
    print ''

    print 'Explained variance:'
    print explained_variance_score(horses_05_y_test, horses_05_y_pred)
    print ''

    print 'Mean squared error:'
    print mean_squared_error(horses_05_y_test, horses_05_y_pred)
    print ''

    print 'R2 score:'
    print r2_score(horses_05_y_test, horses_05_y_pred)
    print ''


    # Plots
    
    

    plot_speeds(horses_98_y_pred, 'r', 'Predicted Speeds for Horses1998 Test Set')
    plot_speeds(horses_98_y_test, 'r', 'Actual Speeds for Horses1998 Test Set')

    plot_speeds(horses_05_y_pred, 'b', 'Predicted Speeds for Horses2005 Test Set')
    plot_speeds(horses_05_y_test, 'b', 'Actual Speeds for Horses2005 Test Set')

    #plot_pred_and_true(horses_05_y_pred, horses_05_y_test)
    #speed_counts(horses_05_y_pred, horses_05_y_test)


if __name__ == "__main__":
    main()