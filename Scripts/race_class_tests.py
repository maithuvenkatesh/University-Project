from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 


def average_speed(races, race_class):
    total_average_speed = 0.0
    no_of_races = 0
    
    for r in races:
        if races[r].race_class == race_class:
            no_of_races += 1
            total_average_speed += races[r].calculate_average_speed()

    try:
        return no_of_races, total_average_speed/no_of_races
    except ZeroDivisionError:
        print no_of_races
        print total_average_speed



def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    race_classes = [1,2,3,4,5,6,7,8]

    for c in race_classes:
        print c
        no_of_races, av_speed = average_speed(races98, c)
        print 'Race class: ' + str(c)
        print 'No. of races: ' + str(no_of_races)
        print 'Average speed of a horse running in this race class: ' + str(av_speed)



if __name__ == "__main__":
    main()