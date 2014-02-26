import re
import matplotlib.pyplot as plt

from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 
from horse_records_organiser import HorseRecords

''' Plots the graph for fractions of handicap races for horses '''
def plot_handicap_graph(handicap_fractions):
    fractions = [n for n in handicap_fractions]
    counts = [handicap_fractions[n] for n in handicap_fractions]

    plt.bar(fractions, counts, 0.015)
    #plt.plot(bins, counts, 'r--')
    plt.show()


''' Returns the races which contain the records of all horses in the dataset '''
def get_full_races(races):
    full_races = {}
    
    for r in races:
        if len(races[r].horses) == races[r].no_of_runners:
            full_races[races[r].race_hash] = races[r]

    return full_races

''' Finds the number and types of the different types of races in the dataset. '''
def race_types(races):
    race_types_counts = Counter()

    for r in races:
        race_name = races[r].name.lower()
        
        if re.search('maiden', race_name) and re.search('stakes', race_name):
            race_types_counts['maiden stakes'] += 1
        
        elif re.search('maiden', race_name) and re.search('handicap', race_name):
            race_types_counts['maiden handicap'] += 1
       
        elif re.search('maiden', race_name):
            race_types_counts['maiden'] += 1

        elif re.search('stakes', race_name):
            race_types_counts['stakes'] += 1

        elif re.search('nursery', race_name):
            race_types_counts['nursery'] += 1
        
        elif re.search('handicap', race_name): 
            race_types_counts['handicap'] += 1

        else:
           race_types_counts['other'] += 1

    return race_types_counts

''' Computes the fraction of handicap races that horses have participated in '''
def handicap_races(horse_records):
    handicap_fractions = Counter()
    total_races = 0

    for h in horse_records:
        handicap_races = 0
        races = horse_records[h].races
        total_races = len(races)
        for r in races:
            race_name = races[r].name.lower()
            if re.search('handicap', race_name) or re.search('nursery', race_name):
                handicap_races += 1

        fraction = float(handicap_races)/total_races
        handicap_fractions[fraction] += 1

    return handicap_fractions

''' Computes the fraction of handicap races that horses have participated in '''
def handicap_race_counter(horse_records):
    handicap_counter = Counter()
    total_races = 0

    for h in horse_records:
        handicap_races = 0
        races = horse_records[h].races
        total_races = len(races)
        for r in races:
            race_name = races[r].name.lower()
            if re.search('handicap', race_name) or re.search('nursery', race_name):
                handicap_races += 1

        fraction = float(handicap_races)/total_races
        if fraction < float(1)/3:
            handicap_fractions[total_races] += 1

    return handicap_fractions


def main():
    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    full_races_98 = get_full_races(races98)
    full_races_05 = get_full_races(races05)

    horse_records_98 = HorseRecords(full_races_98).horses
    horse_records_05 = HorseRecords(full_races_05).horses

    full_race_types_counts_98 = race_types(full_races_98)
    full_race_types_counts_05 = race_types(full_races_05)

    handicap_fractions_98 = handicap_races(horse_records_98)
    handicap_fractions_05 = handicap_races(horse_records_05)

    print 'born98.csv file statistics:'
    print 'No. of full races of different types: '
    print full_race_types_counts_98
    print 'Fraction of handicap races and horse counts'
    print handicap_fractions_98

    print ''

    print 'born05.csv file statistics:'
    print 'No. of full races of different types: '
    print full_race_types_counts_05
    print 'Fraction of handicap races and horse counts'
    print handicap_fractions_05


    plot_handicap_graph(handicap_fractions_98)

if __name__ == "__main__":
    main()