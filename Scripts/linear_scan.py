'''
This script tests for duplicates
'''

import re, string

class Race:
	def __init__(self, race_track, race_date, race_time, race_name, race_prize, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight_carried, jockey_name, jockeys_claim, trainer, horse_odds):
		self.track = race_track
		self.date = race_date
		self.name = race_name
		self.prize = race_prize
		self.restrictions = race_restrictions
		self.no_of_runners = no_of_runners
		self.going = going
		self.race_class = race_class
		self.distance = race_distance
		self.horse_place = horse_place
		self.horse_age = horse_age
		self.weight_carried = weight_carried
		self.horse_jockey = jockey_name
		self.jockeys_claim = jockeys_claim
		self.horse_trainer = trainer
		self.horse_odds = horse_odds


class Horse:
	def __init__(self, horse_name, name_hash):
		self.name = horse_name
		self.name_hash = name_hash
		self.races = []

	def add_race(self, race):
		self.races.append(race)


def main():
	horses = {}
	with open('../Data/born98.csv') as f:
		attributes = f.readline().strip().split()

		race_date_idx = attributes.index('race_date')
		race_time_idx = attributes.index('race_time')
		race_track_idx = attributes.index('track')
		race_name_idx = attributes.index('race_name')
		restrictions_idx = attributes.index('race_restrictions_age')
		race_class_idx = attributes.index('race_class')
		major_idx = attributes.index('major')
		race_dist_idx = attributes.index('race_distance')
		prize_idx = attributes.index('prize_money')
		going_idx = attributes.index('going_description')
		runners_idx = attributes.index('number_of_runners')
		distbt_idx = attributes.index('distbt') 

		horse_name_idx = attributes.index('horse_name')
		horse_place_idx = attributes.index('place')
		stall_idx = attributes.index('stall')
		trainer_idx = attributes.index('trainer')
		horse_age_idx = attributes.index('horse_age')
		jockey_name_idx = attributes.index('jockey_name')
		jockeys_claim_idx = attributes.index('jockeys_claim')
		weight_pounds_idx = attributes.index('pounds')
		odds_idx = attributes.index('odds')
		fav_idx = attributes.index('fav')
		rating_idx = attributes.index('official_rating')
		comptime_idx = attributes.index('comptime')
		total_dstbt_idx = attributes.index('TotalDstBt')
		
		for line in f:
			data = line.strip().split('\t')

			if len(data) == 25:
				race_date = data[race_date_idx][1:-1].strip()
				race_time = data[race_time_idx][1:-1].strip()
				race_track = data[race_track_idx][1:-1].strip()
				race_name = data[race_name_idx][1:-1].strip()
				race_distance = data[race_dist_idx][1:-1].strip()
				race_restrictions = data[restrictions_idx][1:-1].strip()
				race_class = data[race_class_idx][1:-1].strip()
				prize_money = float(data[prize_idx][1:-1])
				going = data[going_idx][1:-1].strip()
				no_of_runners = int(data[runners_idx][1:-1])

				horse_name = data[horse_name_idx][1:-1].strip()
				exclude = set(string.punctuation)
				name_hash = horse_name.lower() # Used for the key of the hashtable
				name_hash = ''.join(c for c in name_hash if c not in exclude)
				name_hash = name_hash.replace(' ', '')

				horse_age = int(data[horse_age_idx][1:-1])
				
				horse_place = data[horse_place_idx][1:-1].strip()
				horse_place = [int(s) for s in horse_place if s.isdigit()]
				horse_place = int(''.join(map(str, horse_place)))

				weight = data[weight_pounds_idx][1:-1].strip()
				odds = data[odds_idx][1:-1].strip()
				comptime = data[comptime_idx][1:-1].strip()
				trainer = data[trainer_idx][1:-1].strip()
				jockey_name = data[jockey_name_idx][1:-1].strip()
				jockeys_claim = data[jockeys_claim_idx][1:-1].strip()
				rating = data[rating_idx][1:-1].strip()

				race = Race(race_track, race_date, race_time, race_name, prize_money, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight, jockey_name, jockeys_claim, trainer, odds)
				horse = Horse(horse_name, name_hash) 

				try:       
					horses[name_hash].add_race(race)
				except KeyError:
					horses[name_hash] = horse
					horses[name_hash].add_race(race)

	'''
	Checking for duplicate horse names
	'''
	hash_names = []
	h_names = set()

	for h in horses:
		hash_names.append(horses[h].name_hash)
		h_names.add(horses[h].name_hash)

	if len(h_names) == len(hash_names):
		print 'No duplicates'
	else:
		print 'Duplicates exist'


if __name__ == "__main__":
	main()
