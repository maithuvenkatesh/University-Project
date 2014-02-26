import re
from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 

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

''' Computes the fraction of handicap races that each horse has participated in '''
def handicap_races(horse_records):



''' Computes the different race classes that exist in the races in the dataset '''
def get_classes(races):
    race_classes = set()
    for r in races:
        race_classes.add(races[r].race_class)

    return race_classes


def main():
    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    full_races_98 = get_full_races(races98)
    full_races_05 = get_full_races(races05)

    full_race_types_counts_98 = race_types(full_races_98)
    full_race_types_counts_05 = race_types(full_races_05)

    #race_types_counts_98 = race_types(races98)
    #race_types_counts_05 = race_types(races05)

    race_classes_98 = get_classes(full_races_98)
    race_classes_05 = get_classes(full_races_05)

    print 'born98.csv file statistics:'
    print 'No. of full races of different types: '
    print full_race_types_counts_98
    #print 'No. of races of different types:'
    #print race_types_counts_98
    print 'Race classes:'
    print race_classes_98

    print ''

    print 'born05.csv file statistics:'
    print 'No. of full races of different types: '
    print full_race_types_counts_05
    #print 'No. of races of different types:'
    #print race_types_counts_05
    print 'Race classes:'
    print race_classes_05


if __name__ == "__main__":
    main()