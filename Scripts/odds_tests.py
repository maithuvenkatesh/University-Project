import matplotlib.pyplot as plt
from horse_parser import HorseParser 
from race_parser import RaceParser 
from utility_functions import get_full_races

''' Calculates the total odds for the races with all horses present '''
def calculate_total_odds(full_races):
    odds = []
    for r in races:
        total_odds = 0
        for h in races[r].horses:
            total_odds += 1/h.odds
        odds.append(total_odds)

    return odds

def all_horses_have_odds(races):
        


def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    full_races_98 = get_full_races(races98)
    full_races_05 = get_full_races(races05)

    odds98 = calculate_total_odds(races98)
    odds05 = calculate_total_odds(races05)

    print 'Maximum in born98 dataset: ' + str(max(odds98))
    print 'Minimum in born98 dataset: ' + str(min(odds98))

    print 'Maximum in born05 dataset: ' + str(max(odds05))
    print 'Minimum in born05 dataset: ' + str(min(odds05))

    plt.plot(odds98)
    plt.xlabel('Race')
    plt.ylabel('Total Odds for Race')
    plt.show()
    
    plt.plot(odds05)
    plt.xlabel('Race')
    plt.ylabel('Total Odds for Race')
    plt.show()

if __name__ == "__main__":
    main()