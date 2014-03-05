import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from race_parser_no_handicaps import RaceParserNoHandicaps
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset

def goings_vs_speed(horses_train):
    # Get the goings in the training set
    goings = set()
    for h in horses_train:
        for r in h_tr.races:
            goings.add(r.going)

def age_vs_speed(horses_train):
    average_speeds_per_age = Counter()
    for h in horses_train:
        for r in h.races:
            average_speeds_per_age[r.horse_age] = r.horse_speed

    ages = average


def rating_vs_speed(horses_train):
    ratings_and_speeds = Counter()
    for h in horses_train:
        for r in h.races:
            ratings_and_speeds[r.horse_rating] = r.horse_speed

    ratings = ratings_and_speeds.keys()
    speeds = [ratings_and_speeds[r] for r in ratings]

    # Plot scatter graph of rating vs. speed
    plt.scatter(ratings, speeds, color='black')
    plt.show()

'''
def class_vs_speed(horses_training_set):
'''

def prize_money_vs_speed(horses_training_set):
    prize_money_and_speeds = Counter()
    for h in horses_train:
        for r in h.races:
            prize_money_and_speeds[r.prize] = r.horse_speed

    prize_money = prize_money_and_speeds.keys()
    speeds = [prize_money_and_speeds[r] for r in ratings]

def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParserNoHandicaps('./../Data/born98.csv').races
    races05 = RaceParserNoHandicaps('./../Data/born05.csv').races

    horses_train_98, horses_test_98 = split_dataset(horses98)
    horses_train_05, horses_test_05 = split_dataset(horses05)

    print 'HorsesBorn98 Training Set:'
    print 'No. of horses: ' + str(len(horses_train_98))
    rating_vs_speed(horses_train_98)


    print 'HorsesBorn05 Training Set:'
    print 'No. of horses: ' + str(len(horses_train_05))






if __name__ == "__main__":
    main()