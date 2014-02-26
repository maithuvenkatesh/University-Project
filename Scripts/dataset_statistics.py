from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 

''' Computes the number of races in the dataset for which the dataset contains the records of all participating horses '''
def no_of_races_with_all_horses(races):
    total_races = 0
    
    for r in races:
        if len(races[r].horses) == races[r].no_of_runners:
            total_races += 1
    
    return total_races

''' Computes the number of races in the dataset for which the dataset contains the record of the winning horse '''
def no_of_races_with_winner(races, horses):
    total_races = 0
    
    for r in races:
        if races[r].winner and horses[races[r].winner]:
            total_races += 1

    return total_races

''' Computes the average number of races per horse within the dataset '''
def average_no_of_races_per_horse(horses):
    total_races = 0

    for h in horses:
        total_races += len(horses[h].races)

    average_races = float(total_races)/len(horses)
    return average_races


''' Returns the races which contain the records of all horses in the dataset '''
def get_full_races(races):
    full_races = {}
    
    for r in races:
        if len(races[r].horses) == races[r].no_of_runners:
            full_races[races[r].race_hash] = races[r]

    return full_races


''' Computes the ages of horses in races where all horse records are present in the dataset '''
def get_ages(full_races):
    ages = set()

    for r in full_races:
        for h in full_races[r].horses:
            ages.add(h.age)

    return ages

''' Computes the number of races for horses at each age. Only takes into account those races which have all runners '''
def races_at_each_age(full_races, ages_set):
    no_of_races_per_age = Counter()
    
    for a in ages_set:
        total_races = 0
        for r in full_races:
            ages = [h.age for h in full_races[r].horses]
            if max(ages) == a:
                total_races += 1
        no_of_races_per_age[a] = total_races

    return no_of_races_per_age

''' Computes the number of races with k missing horses in the dataset  '''
def races_with_k_missing_runners(races):
    races_with_missing_horses = Counter()

    for r in races:
        missing_runners = races[r].no_of_runners - len(races[r].horses)
        races_with_missing_horses[missing_runners] += 1

    return races_with_missing_horses

''' Computes the frequency of races with k horses participating '''
def races_with_k_runners(races):
    races_with_k_horses = Counter()

    for r in races:
        races_with_k_horses[races[r].no_of_runners] += 1
    
    return races_with_k_horses

#''' Computes the number of races which contain the information for the winning horse '''
'''
def races_with_winning_horse(races):
    races_with_winner = 0

    for r in races:
        for h in races[r].horses:
            if races[r].winner == h.horse_hash:
                races_with_winner += 1

    return races_with_winner
'''

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    full_races_98 = get_full_races(races98)
    full_races_05 = get_full_races(races05)

    total_races_with_all_horses_98 = no_of_races_with_all_horses(races98)
    total_races_with_winners_98 = no_of_races_with_winner(races98, horses98)

    total_races_with_all_horses_05 = no_of_races_with_all_horses(races05)
    total_races_with_winners_05 = no_of_races_with_winner(races05, horses05)

    average_races_per_horse_98 = average_no_of_races_per_horse(horses98)
    average_races_per_horse_05 = average_no_of_races_per_horse(horses05)

    ages98 = get_ages(full_races_98)
    ages05 = get_ages(full_races_05)

    no_of_races_per_age_98 = races_at_each_age(full_races_98, ages98)
    no_of_races_per_age_05 = races_at_each_age(full_races_05, ages05)

    races_with_k_missing_horses_98 = races_with_k_missing_runners(races98)
    races_with_k_missing_horses_05 = races_with_k_missing_runners(races05)

    print 'born98.csv file statistics:'
    print 'No. of horses: ' + str(len(horses98))
    print 'No. of races: ' + str(len(races98))
    print 'No. of races for which we have all the horses: ' + str(total_races_with_all_horses_98)
    print 'No. of races for which we have the winner: ' + str(total_races_with_winners_98)
    print 'Fraction of races for which we have all the horses: ' + str(float(total_races_with_all_horses_98)/len(races98))
    print 'Fraction of races for which we have the winner: ' + str(float(total_races_with_winners_98)/len(races98))
    print 'Average no. of races per horse: ' + str(average_races_per_horse_98)
    print 'No. of races for horses at each age: ' + str(no_of_races_per_age_98)
    print 'No. of races with k-missing horse records: ' + str(races_with_k_missing_horses_98)

    print ''

    print 'born05.csv file statistics:'
    print 'No. of horses: ' + str(len(horses05))
    print 'No. of races: ' + str(len(races05))
    print 'No. of races for which we have all the horses: ' + str(total_races_with_all_horses_05)
    print 'No. of races for which we have the winner: ' + str(total_races_with_winners_05)
    print 'Fraction of races for which we have all the horses: ' + str(float(total_races_with_all_horses_05)/len(races05))
    print 'Fraction of races for which we have the winner: ' + str(float(total_races_with_winners_05)/len(races05))
    print 'Average no. of races per horse: ' + str(average_races_per_horse_05)
    print 'No. of races for horses at each age: ' + str(no_of_races_per_age_05)
    print 'No. of races with k-missing horse records: ' + str(races_with_k_missing_horses_05)
    

if __name__ == "__main__":
	main()