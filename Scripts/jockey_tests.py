from horse_parser import HorseParser 
from race_parser import RaceParser 

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    jockeys98 = set()
    for r in races98:
        for h in races98[r].horses:
            jockeys98.add(h.jockey)

    jockeys05 = set()
    for r in races05:
        for h in races05[r].horses:
            jockeys05.add(h.jockey)

    print 'No. of jockeys in 98 dataset: ' + str(len(jockeys98))
    print 'No. of jockeys in 05 dataset: ' + str(len(jockeys05))


if __name__ == "__main__":
    main()