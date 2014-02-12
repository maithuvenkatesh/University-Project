from horse_parser import HorseParser 
from race_parser import RaceParser 

def main():
	horses98 = HorseParser('./../Data/born98.csv').horses
	horses05 = HorseParser('./../Data/born05.csv').horses

	races98 = RaceParser('./../Data/born98.csv').races
	races05 = RaceParser('./../Data/born05.csv').races

	print 'born98.csv file statistics:'
	print ''
	print 'No. of horses: ' + str(len(horses98))
	print 'No. of races: ' + str(len(races98))

	all_horses_present = 0

	for r in races98:
		if len(races98[r].horses) == races98[r].no_of_runners:
			all_horses_present += 1

	print 'No. of races for which we have all the horses: ' + str(all_horses_present)
	print 'Fraction of races for which we have all the horses: ' + str(float(all_horses_present)/len(races98))

	winner_present = 0
	for r in races98:
		if races98[r].winner and horses98[races98[r].winner]:
			winner_present += 1

	print 'No. of races for which we have the winner: ' + str(winner_present)
	print 'Fraction of races for which we have the winner: ' + str(float(winner_present)/len(races98))

	average_race_per_horse = 0
	for h in horses98:
		average_race_per_horse += len(horses98[h].races)

	print 'Average no. of races per horse: ' + str(float(average_race_per_horse)/len(horses98))

	print '----------------------------------------------------------------------------------------------'

	print 'born05.csv file statistics:'
	print ''
	print 'No. of horses: ' + str(len(horses05))
	print 'No. of races: ' + str(len(races05))

	all_horses_present = 0

	for r in races05:
		if len(races05[r].horses) == races05[r].no_of_runners:
			all_horses_present += 1

	print 'No. of races for which we have all the horses: ' + str(all_horses_present)
	print 'Fraction of races for which we have all the horses: ' + str(float(all_horses_present)/len(races05))

	winner_present = 0
	for r in races05:
		if races05[r].winner and horses05[races05[r].winner]:
			winner_present += 1

	print 'No. of races for which we have the winner: ' + str(winner_present)
	print 'Fraction of races for which we have the winner: ' + str(float(winner_present)/len(races05))


	average_race_per_horse = 0
	for h in horses05:
		average_race_per_horse += len(horses05[h].races)

	print 'Average no. of races per horse: ' + str(float(average_race_per_horse)/len(horses05))



if __name__ == "__main__":
	main()