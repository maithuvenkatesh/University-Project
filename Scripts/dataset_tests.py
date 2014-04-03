import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from horse_parser_no_handicaps import HorseParserNoHandicaps
from race_parser_no_handicaps import RaceParserNoHandicaps

''' Methods which plot correlations between input variables and horse speed '''

def rating_vs_speed(horses):
    print 'Rating and Speed'

    ratings = []
    speeds = []
    for h in horses:
        for r in h.races:
            ratings.append(r.horse_rating)
            speeds.append(r.horse_speed)

    plt.scatter(ratings, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Rating')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def age_vs_speed(horses):
    print 'Age and Speed'

    ages = []
    speeds = []
    for h in horses:
        for r in horses[h].races:
            ages.append(r.horse_age)
            speeds.append(r.horse_speed)

    plt.scatter(ages, speeds, color='blue',s=0.7)
    plt.xlabel('Horse Age')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def odds_vs_speed(horses):
    print 'Odds and Speed'

    odds = []
    speeds = []
    for h in horses:
        for r in h.races:
            odds.append(r.horse_odds)
            speeds.append(r.horse_speed)


    plt.scatter(odds, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Odds')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def no_of_runners_vs_speed(horses):
    print 'No. of runners and Speed'

    runners = []
    speeds = []
    for h in horses:
        for r in h.races:
            runners.append(r.no_of_runners)
            speeds.append(r.horse_speed)


    plt.scatter(runners, speeds, color='blue', s=0.7)
    plt.xlabel('No. of Runners per Race')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def prize_money_vs_speed(horses):
    print 'Prize Money and Speed'

    prize_money = []
    speeds = []
    for h in horses:
        for r in h.races:
            prize_money.append(r.prize)
            speeds.append(r.horse_speed)

    plt.scatter(prize_money, speeds, color='blue', s=0.7)
    plt.xlabel('Prize Money per Race (Pound Sterling)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def race_class_vs_speed(horses):
    print 'Race Class and Speed'

    race_class = []
    speeds = []
    for h in horses:
        for r in h.races:
            race_class.append(r.race_class)
            speeds.append(r.horse_speed)

    plt.scatter(race_class, speeds, color='blue', s=0.7)
    plt.xlabel('Race Class')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

''' Computes the average horse speed in each race class '''
def class_average_speeds(races1, races2):
    race_class1 = defaultdict(list)
    averages1 = defaultdict()

    for r in races:
        for h in races[r].horses:
            race_class[races[r].race_class].append(h.speed)

    for rc in race_class:
        total_speed = sum([x for x in race_class[rc]])
        number = len(race_class[rc])
        averages[rc] = float(total_speed)/number
        total_speed = 0.0
        number = 0

def runners(races1, races2):
    runners



def weight_vs_speed(horses):
    print 'Weight and Speed'

    weights_carried = []
    speeds = []
    for h in horses:
        for r in h.races:
            weights_carried.append(r.weight_carried)
            speeds.append(r.horse_speed)

    plt.scatter(weights_carried, speeds, color='blue', s=0.7)
    plt.xlabel('Weight Carried by Horse (pounds)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def jockeys_claim_vs_speed(horses1, horses2):
    print 'Jockey\'s Claim and Speed'

    claims = []
    speeds = []
    for h in horses:
        for r in h.races:
            claims.append(r.jockeys_claim)
            speeds.append(r.horse_speed)

    plt.scatter(claims, speeds, color='blue', s=0.7)
    plt.xlabel('Jockey\'s Claim (pounds)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def place_vs_speed(horses):
    print 'Place and Speed'

    places = []
    speeds = []
    for h in horses:
        for r in h.races:
            places.append(r.horse_place)
            speeds.append(r.horse_speed)

    plt.scatter(places, speeds, color='blue', s=0.7)
    plt.xlabel('Horse Place')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def comptime_vs_speed(horses):
    print 'Comptime and Speed'

    times = []
    speeds = []
    for h in horses:
        for r in h.races:
            times.append(r.horse_comptime)
            speeds.append(r.horse_speed)

    plt.scatter(times, speeds, color='blue', s=0.7)
    plt.xlabel('Time Taken to Complete Race (s)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def distance_vs_speed(horses):
    print 'Distance and Speed'

    distances = []
    speeds = []
    for h in horses:
        for r in h.races:
            distances.append(r.distance)
            speeds.append(r.horse_speed)

    plt.scatter(distances, speeds, color='blue', s=0.7)
    plt.xlabel('Race Distance (metres)')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def stall_vs_speed(horses):
    print 'Stall No. and Speed'

    stalls = []
    speeds = []
    for h in horses:
        for r in h.races:
            stalls.append(r.stall_no)
            speeds.append(r.horse_speed)

    plt.scatter(stalls, speeds, color='blue', s=0.7)
    plt.xlabel('Stall No.')
    plt.ylabel('Horse Speed (metres/sec)')
    plt.show()

def goings_vs_speed(horses):
    print 'Going and Speed'

    goings_and_speeds = defaultdict(list)

    for h in horses:
        for r in h.races:
            goings_and_speeds[r.going].append(r.horse_speed)

''' Plots the average race speeds '''
def average_race_speeds(races1, races2):
    average_speeds1 = []
    for r in races1:
        total_speed = 0.0
        no_of_horses = len(races1[r].horses)
        for h in races1[r].horses:
            total_speed += h.speed
        average_speeds1.append(total_speed/no_of_horses)

    average_speeds2 = []
    for r in races2:
        total_speed = 0.0
        no_of_horses = len(races2[r].horses)
        for h in races2[r].horses:
            total_speed += h.speed
        average_speeds2.append(total_speed/no_of_horses)

    plt.hist([average_speeds1, average_speeds2], 40, histtype='bar', color=['blue','green'], label=['HorsesBorn1998','HorsesBorn2005'])
    plt.ylabel('No. of Races')
    plt.xlabel('Average Race Speed (metres/second)')
    plt.legend()
    plt.show()

''' Plots the average horse speeds '''
def average_horse_speeds(horses1, horses2):
    average_speeds1 = []
    for h in horses1:
        total_speed = 0.0
        no_of_races = len(horses1[h].races)
        for r in horses1[h].races:
            total_speed += r.horse_speed
        average_speeds1.append(total_speed/no_of_races)
    
    average_speeds2 = []
    for h in horses2:
        total_speed = 0.0
        no_of_races = len(horses2[h].races)
        for r in horses2[h].races:
            total_speed += r.horse_speed
        average_speeds2.append(total_speed/no_of_races)

    plt.hist([average_speeds1, average_speeds2], 40, histtype='bar', color=['blue','green'], label=['HorsesBorn1998','HorsesBorn2005'])
    plt.ylabel('No. of Horses')
    plt.xlabel('Average Horse Speed (metres/second)')
    plt.legend()
    plt.show()

''' Plots the number of records for each age'''
def horses_age_record_no(horses1,horses2):
    ages1 = []
    for h in horses1:
        for r in horses1[h].races:
            ages1.append(r.horse_age)

    ages2 = []
    for h in horses2:
        for r in horses2[h].races:
            ages2.append(r.horse_age)

    plt.hist([ages1,ages2], 40, histtype='bar', color=['blue','green'], label=['HorsesBorn1998','HorsesBorn2005'])
    plt.ylabel('No. of Race Records per Age')
    plt.xlabel('Age of Horses')
    plt.legend()
    plt.show()

def race_distances(races1, races2):
    distances1 = []
    for r in races1:
        distances1.append(races1[r].distance)

    distances2 = []
    for r in races2:
        distances2.append(races2[r].distance)

    plt.hist([distances1,distances2], 40, histtype='bar', color=['blue','green'], label=['HorsesBorn1998','HorsesBorn2005'])
    plt.ylabel('No. of Race Records per Race Distance')
    plt.xlabel('Distance of Races (metres)')
    plt.legend()
    plt.show()

def race_records_per_horse(horses1, horses2):
    records1 = []
    for h in horses1:
        records1.append(len(horses1[h].races))

    records2 = []
    for h in horses2:
        records2.append(len(horses2[h].races))

    plt.hist([records1,records2], 40, histtype='bar', color=['blue','green'], label=['HorsesBorn1998','HorsesBorn2005'])
    plt.ylabel('Frequency')
    plt.xlabel('No. of Race Records per Horse')
    plt.legend()
    plt.show()

def race_class_records(races1, races2):
    records1 = []
    for r in races1:
        records1.append(races1[r].race_class)

    records2 = []
    for r in races2:
        records2.append(races2[r].race_class)

    plt.hist([records1,records2], 40, histtype='bar', color=['blue','green'], label=['HorsesBorn1998','HorsesBorn2005'])
    plt.ylabel('No. of Race Records per Race Class')
    plt.xlabel('Race Class')
    plt.legend()
    plt.show()

def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParserNoHandicaps('./../Data/born98.csv').races
    races05 = RaceParserNoHandicaps('./../Data/born05.csv').races


    print 'HorsesBorn98 Training Set:'
    print 'No. of horses: ' + str(len(horses98))
    print 'No. of races: ' + str(len(races98))

    print 'HorsesBorn05 Training Set:'
    print 'No. of horses: ' + str(len(horses05))
    print 'No. of races: ' + str(len(races05))

    #average_race_speeds(races98, races05)
    #average_horse_speeds(horses98, horses05)
    #horses_age_record_no(horses98, horses05)
    #race_distances(races98, races05)
    #race_records_per_horse(horses98, horses05)
    race_class_records(races98, races05)

    '''
    rating_vs_speed(horses98)
    prize_money_vs_speed(horses98)  
    odds_vs_speed(horses98)
    age_vs_speed(horses98)
    no_of_runners_vs_speed(horses98)
    race_class_vs_speed(horses98)
    weight_vs_speed(horses98)
    jockeys_claim_vs_speed(horses98)
    place_vs_speed(horses98)
    distance_vs_speed(horses98)
    comptime_vs_speed(horses98)
    stall_vs_speed(horses98)
    #goings_vs_speed(horses98)
    '''
    print ''



    #average_race_speeds(races05)
    #average_horse_speeds(horses05)
    '''
    rating_vs_speed(horses05)
    prize_money_vs_speed(horses05)  
    odds_vs_speed(horses05)
    age_vs_speed(horses05)
    no_of_runners_vs_speed(horses05)
    race_class_vs_speed(horses05)
    weight_vs_speed(horses05)
    jockeys_claim_vs_speed(horses05)
    place_vs_speed(horses05)
    distance_vs_speed(horses05)
    comptime_vs_speed(horses05)
    stall_vs_speed(horses05)
    '''

if __name__ == "__main__":
    main()