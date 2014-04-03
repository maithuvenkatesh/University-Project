import numpy as np
from collections import defaultdict
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset

''' Correlation Coefficients '''

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

def stall_vs_speed(horses_train):
    print 'Stall No. and Speed'

    stalls = []
    speeds = []
    for h in horses_train:
        for r in h.races:
            stalls.append(r.stall_no)
            speeds.append(r.horse_speed)

    print 'CC: ' + str(np.corrcoef(stalls, speeds))
    print ''

def goings_vs_speed(horses_train):
    print 'Going and Speed'

    goings_and_speeds = defaultdict(list)

    for h in horses_train:
        for r in h.races:
            goings_and_speeds[r.going].append(r.horse_speed)


def rating_vs_odds(horses_train):
    print 'Rating and Odds'
    odds = []
    ratings = []
    for h in horses_train:
        for r in h.races:
            odds.append(r.horse_odds)
            ratings.append(r.horse_rating)

    print np.corrcoef(odds,ratings)
    print ''

def jockeys_claim_test(horses):
    c_set = set()
    claims = []
    weights = []

    for h in horses:
        for r in h.races:
            c_set.add(r.jockeys_claim)
            claims.append(r.jockeys_claim)
            weights.append(r.weight_carried)

    print 'Claims and Weight'
    print np.corrcoef(claims, weights)
    print ''

    print c_set
    

def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

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
    stall_vs_speed(horses_train_98)
    rating_vs_odds(horses_train_98)
    #goings_vs_speed(horses_train_98)

    print ''

    print 'HorsesBorn05 Training Set:'
    print 'No. of horses: ' + str(len(horses_train_05))
    
    rating_vs_speed(horses_train_05)
    prize_money_vs_speed(horses_train_05)  
    odds_vs_speed(horses_train_05)
    age_vs_speed(horses_train_05)
    no_of_runners_vs_speed(horses_train_05)
    race_class_vs_speed(horses_train_05)
    weight_vs_speed(horses_train_05)
    jockeys_claim_vs_speed(horses_train_05)
    place_vs_speed(horses_train_05)
    distance_vs_speed(horses_train_05)
    comptime_vs_speed(horses_train_05)
    stall_vs_speed(horses_train_05)
    rating_vs_odds(horses_train_05)

if __name__ == "__main__":
    main()