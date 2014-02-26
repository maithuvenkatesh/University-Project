from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 

def find_all_jockeys(races):
    jockeys = set()
    for r in races:
        for h in races[r].horses:
            jockeys.add(h.jockey)
    return jockeys

def find_no_of_sits(races, jockey_set):
    no_of_sits_by_jockeys = Counter()
    
    for r in races:
        for h in races[r].horses:
            no_of_sits_by_jockeys[h.jockey]

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    jockeys98 = find_all_jockeys(races98)
    jockeys05 = find_all_jockeys(races05)

    print 'No. of jockeys in 98 dataset: ' + str(len(jockeys98))
    print 'No. of jockeys in 05 dataset: ' + str(len(jockeys05))




if __name__ == "__main__":
    main()