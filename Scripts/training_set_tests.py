import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from race_parser_no_handicaps import RaceParserNoHandicaps
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset

''' Methods which check correlation between input variables and horse speed '''

def rating_vs_speed(horses_train):
    print 'Rating and Speed'

    ratings = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            ratings.append(r.horse_rating)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(ratings, speeds))
    print ''

    plt.scatter(ratings, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Rating')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def age_vs_speed(horses_train):
    print 'Age and Speed'

    ages = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            ages.append(r.horse_age)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(ages, speeds))
    print ''

    plt.scatter(ages, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Age')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def odds_vs_speed(horses_train):
    print 'Odds and Speed'

    odds = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            odds.append(r.horse_odds)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(odds, speeds))
    print ''

    plt.scatter(odds, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Odds')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def no_of_runners_vs_speed(horses_train):
    print 'No. of runners and Speed'

    runners = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            runners.append(r.no_of_runners)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(runners, speeds))
    print ''

    plt.scatter(runners, speeds, color='blue', s=0.7)
    plt.xlabel('No. of Runners per Race')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def prize_money_vs_speed(horses_train):
    print 'Prize Money and Speed'

    prize_money = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            prize_money.append(r.prize)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(prize_money, speeds))
    print ''
    
    plt.scatter(prize_money, speeds, color='blue', s=0.7)
    plt.xlabel('Prize Money per Race (Pound Sterling)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def race_class_vs_speed(horses_train):
    print 'Race Class and Speed'

    race_class = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            race_class.append(r.race_class)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(race_class, speeds))
    print ''

    plt.scatter(race_class, speeds, color='blue', s=0.7)
    plt.xlabel('Race Class')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def weight_vs_speed(horses_train):
    print 'Weight and Speed'

    weights_carried = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            weights_carried.append(r.weight_carried)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(weights_carried, speeds))
    print ''

    plt.scatter(weights_carried, speeds, color='blue', s=0.7)
    plt.xlabel('Weight Carried by Horse (pounds)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def jockeys_claim_vs_speed(horses_train):
    print 'Jockey\'s Claim and Speed'

    claims = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            claims.append(r.jockeys_claim)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(claims, speeds))
    print ''

    plt.scatter(claims, speeds, color='blue', s=0.7)
    plt.xlabel('Jockey\'s Claim (pounds)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def place_vs_speed(horses_train):
    print 'Place and Speed'

    places = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            places.append(r.horse_place)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(places, speeds))
    print ''

    plt.scatter(places, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Place')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def comptime_vs_speed(horses_train):
    print 'Comptime and Speed'

    times = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            times.append(r.horse_comptime)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(times, speeds))
    print ''

    plt.scatter(times, speeds, color='blue', s=0.7)
    plt.xlabel('Time Taken to Complete Race (s)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def distance_vs_speed(horses_train):
    print 'Distance and Speed'

    distances = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            distances.append(r.distance)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(distances, speeds))
    print ''

    plt.scatter(distances, speeds, color='blue', s=0.7)
    plt.xlabel('Race Distance (metres)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()


def goings_vs_speed(horses_train):
    # Get the goings in the training set
    goings = set()
    for h in horses_train:
        for r in h.races:
            goings.add(r.going)

    speeds_per_going = Counter()
    for g in goings:
        going_speeds = []
        for h in horses_train:
            for r in h.races:
                if r.going == g:
                    g_speeds.apped(r.horse_speed)
        speeds_per_going[g] = going_speeds

    print speeds_per_going


def main():
    #horse_parser_98 = HorseParserNoHandicaps('./../Data/born98.csv')
    #horse_parser_05 = HorseParserNoHandicaps('./../Data/born05.csv')

    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParserNoHandicaps('./../Data/born98.csv').races
    races05 = RaceParserNoHandicaps('./../Data/born05.csv').races

    horses_train_98, horses_test_98 = split_dataset(horses98)
    horses_train_05, horses_test_05 = split_dataset(horses05)

    print 'HorsesBorn98 Training Set:'
    print 'No. of horses: ' + str(len(horses_train_98))
    
    rating_vs_speed(horses_train_98)
    prize_money_vs_speed(horses_train_98)  
    odds_vs_speed(horses_train_98)
    age_vs_speed(horses_train_98)
    no_of_runners_vs_speed(horses_train_98)
    race_class_vs_speed(horses_train_98)
    weight_vs_speed(horses_train_98)
    jockeys_claim_vs_speed(horses_train_98)
    place_vs_speed(horses_train_98)
    distance_vs_speed(horses_train_98)
    comptime_vs_speed(horses_train_98)

    print ''


    print 'HorsesBorn05 Training Set:'
    print 'No. of horses: ' + str(len(horses_train_05))
    
    rating_vs_speed(horses_train_05)
    prize_money_vs_speed(horses_train_05)  
    odds_vs_speed(horses_train_05)
    age_vs_speed(horses_train_05)
    no_of_runners_vs_speed(horses_train_05)
    race_class_vs_speed(horses_train_05)
    weight_vs_speed(horses_train_98)
    jockeys_claim_vs_speed(horses_train_98)
    place_vs_speed(horses_train_98)
    distance_vs_speed(horses_train_98)
    comptime_vs_speed(horses_train_98)







if __name__ == "__main__":
    main()