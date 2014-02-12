from horse_parser import HorseParser 
from race_parser import RaceParser 

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    going98 = set()
    going05 = set()

    for r in races98:
        going98.add(races98[r].going)

    for r in races05:
        going05.add(races05[r].going)

    print 'No. of different types of going in 98 dataset: ' + str(len(going98))
    print going98

    print ''

    print 'No. of different types of going in 05 dataset: ' + str(len(going05))
    print going05

if __name__ == "__main__":
    main()