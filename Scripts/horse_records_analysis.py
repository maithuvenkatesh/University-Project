import matplotlib.pyplot as plt

from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 
from horse_records_organiser import HorseRecords

''' Returns the races which contain the records of all horses in the dataset '''
def get_full_races(races):
    full_races = {}
    
    for r in races:
        if len(races[r].horses) == races[r].no_of_runners:
            full_races[races[r].race_key] = races[r]

    return full_races

''' Returns the count of horses given a number of races '''
def horses_with_k_races(races, horse_records):
    horses_race_count = Counter()
    seen_horses = set()

    for r in races:
        for h in races[r].horses:
            if h.horse_key not in seen_horses:
                total_races = len(horse_records[h.horse_key].races)
                horses_race_count[total_races] += 1
                seen_horses.add(h.horse_key)
            else:
                continue

    return horses_race_count

def plot_graph(no_of_races, no_of_horses, title):
    xbins = [x for x in range(len(no_of_races))]
    
    plt.hist(no_of_horses, bins=xbins, color='blue  ')
    #plt.bar(no_of_races, no_of_horses, width, color='blue')
    plt.show()


def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    full_races_98 = get_full_races(races98)
    full_races_05 = get_full_races(races05)

    horse_records_98 = HorseRecords(full_races_98).horses
    full_race_horse_data_05 = HorseRecords(full_races_05).horses

    full_horses_race_count_98 = horses_with_k_races(full_races_98, horse_records_98)
    full_horses_race_count_05 = horses_with_k_races(full_races_05, full_race_horse_data_05)

    no_of_races_98 = [n for n in full_horses_race_count_98]
    no_of_races_05 = [n for n in full_horses_race_count_05]

    no_of_horses_98 = [full_horses_race_count_98[x] for x in full_horses_race_count_98]
    no_of_horses_05 = [full_horses_race_count_05[x] for x in full_horses_race_count_05]

    print 'Born98 Dataset Statistics:'
    print 'Race counts of horses for races with all runners: '
    print full_horses_race_count_98
    print 'No. of races:'
    print no_of_races_98
    print 'No. of horses:'
    print no_of_horses_98

    print ''

    print 'Born05 Dataset Statistics:'
    print 'Race counts of horses for races with all runners: '
    print full_horses_race_count_05
    print 'No. of races:'
    print no_of_races_05
    print 'No. of horses:'
    print no_of_horses_05

    plot_graph(no_of_races_98, no_of_horses_98, 'No. of Races per Horse (Born98 Dataset)')
    plot_graph(no_of_races_05, no_of_horses_05, 'No. of Races per Horse (Born05 Dataset)')


if __name__ == "__main__":
    main()