from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 

def get_goings(races):

    ''' Returns a set of goings for race data '''

    going = set()

    for r in races:
        going.add(races[r].going)

    return going

def get_race_counts(races, going_set):

    ''' Returns counts for the number of races for each going type '''

    race_counts = Counter()
    for g in going_set:
        for r in races:
            if races[r].going == g:
                race_counts[g] += 1

    return race_counts

def find_missing_going(going_set1, going_set2):
    if len(going_set1) != len(going_set2):
        return going_set2 - going_set1
            

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    goings98 = get_goings(races98)
    goings05 = get_goings(races05)

    print 'Test 1: No. of different types of going in 98 dataset: ' + str(len(goings98))
    print goings98

    print ''

    print 'No. of different types of going in 05 dataset: ' + str(len(goings05))
    print goings05

    missing_goings = find_missing_going(goings05, goings98)
    print 'Missing going: ' + str(missing_goings)



    going_race_counts_98 = get_race_counts(races98, goings98)
    going_race_counts_05 = get_race_counts(races05, goings05)




if __name__ == "__main__":
    main()