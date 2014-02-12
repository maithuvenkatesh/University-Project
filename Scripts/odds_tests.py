import matplotlib.pyplot as plt
from horse_parser import HorseParser 
from race_parser import RaceParser 

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    odds = []
    for r in races98:
        total_odds = 0
        
        for h in races98[r].horses:
            total_odds += 1/h.odds
        
        odds.append(total_odds)

        if total_odds > 10:
            print races98[r].name + ' ' + str(total_odds)
            print races98[r].date
            print races98[r].track
            print races98[r].time
            print races98[r].no_of_runners
            for h in races98[r].horses:
                print h.name + ' : ' + str(h.odds)

            print ''


    plt.plot(odds)
    plt.xlabel('Race')
    plt.ylabel('Total Odds for Each Race')
    plt.show()
    

if __name__ == "__main__":
    main()