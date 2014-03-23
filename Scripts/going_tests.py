import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from horse_parser import HorseParser 
from race_parser import RaceParser 

def get_goings(races):
    going = set()
    for r in races:
        going.add(races[r].going)

    return going

def get_race_counts(races, going_set):
    race_counts = Counter()
    for g in going_set:
        for r in races:
            if races[r].going == g:
                race_counts[g] += 1

    return race_counts

def going_class(horses):
    going_class = defaultdict(set)
    for h in horses:
        for r in h.races:
            going_class[r.going].add(r.race_class)

    for g in going_class:
        print g
        print going_class[g]
        print ''

def plot_going_race_count(going_race_counts_1, going_race_counts_2, graph_title):
    going_types_1, race_count_1 = zip(*going_race_counts_1.items())
    going_types_2, race_count_2 = zip(*going_race_counts_2.items())

    locs = range(0, len(race_count_1))
    
    plt.bar(locs, race_count_1)
    #plt.bar(locs, race_count_2)
    plt.xticks(rotation=70)
    plt.xticks(locs, going_types_1)

    plt.tight_layout()
    plt.show()

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    goings98 = get_goings(races98)
    goings05 = get_goings(races05)

    print 'No. of different types of going in 98 dataset: ' + str(len(goings98))
    print goings98

    print ''

    print 'No. of different types of going in 05 dataset: ' + str(len(goings05))
    print goings05

    print ''

    '''
    # Find the missing going and add it to the other dataset
    if len(goings98) > len(goings05):
        missing_going = goings98 - goings05
        for g in missing_going:
            goings05.add(g)    

    going_race_counts_98 = get_race_counts(races98, goings98)
    going_race_counts_05 = get_race_counts(races05, goings05)

    plot_going_race_count(going_race_counts_98, going_race_counts_05, 'hhdghdg')
    '''




if __name__ == "__main__":
    main()