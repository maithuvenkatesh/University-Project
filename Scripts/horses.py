import re

class Race:
	def __init__(self, race_track, race_date, race_time, race_name, race_prize, race_restrictions, no_of_runners, going, race_class, race_distance):
		self.track = race_track
		self.date = race_date
		self.name = race_name
		self.prize = race_prize
		self.restrictions = race_restrictions
		self.no_of_runners = no_of_runners
		self.going = going
		self.race_class = race_class
		self.distance = race_distance

class Horse:
	def __init__(self, horse_name, horse_age, horse_place, weight_carried, jockey_name, jockeys_claim, trainer, horse_odds):
		self.name = horse_name
		self.age = horse_age
		self.place = horse_place
		self.weight_carried = weight_carried
		self.jockey = jockey_name
		self.jockeys_claim = jockeys_claim
		self.trainer = trainer
		self.odds = horse_odds
		self.races = {}

		def add_race(self, Race):
			self.races += Race


def main():
	races = {}
	horses = {}
	with open('Data/born98.csv') as f:
		attributes = f.readline().strip().split()

		race_date_idx = attributes.index('race_date')
		race_time_idx = attributes.index('race_time')
		race_track_idx = attributes.index('track')
		race_name_idx = attributes.index('race_name')
		restrictions_idx = attributes.index('race_restrictions_age')
		race_class_idx = attributes.index('race_class')
		major_idx = attributes.index('major')	# May be missing
		race_dist_idx = attributes.index('race_distance')
		prize_idx = attributes.index('prize_money')
		going_idx = attributes.index('going_description')
		runners_idx = attributes.index('number_of_runners')
		distbt_idx = attributes.index('distbt') # Not added yet

		horse_name_idx = attributes.index('horse_name')
		horse_place_idx = attributes.index('place')
		stall_idx = attributes.index('stall')
		trainer_idx = attributes.index('trainer')
		horse_age_idx = attributes.index('horse_age')
		jockey_name_idx = attributes.index('jockey_name')
		jockeys_claim_idx = attributes.index('jockeys_claim')
		weight_pounds_idx = attributes.index('pounds')
		odds_idx = attributes.index('odds')
		fav_idx = attributes.index('fav')	# May be mising
		rating_idx = attributes.index('official_rating')
		comptime_idx = attributes.index('comptime')
		total_dstbt_idx = attributes.index('TotalDstBt')

		print attributes
		
		for line in f:
			data = line.strip().split('\s')
			print len(data)

			if len(data) == 25:
				race_name = data[race_name_idx][1:-1].strip()
				race_date = data[race_date_idx][1:-1]
				race_track = data[race_track_idx][1:-1]
				race_time = data[race_time_idx][1:-1]
				race_distance = data[race_dist_idx][1:-1]
				race_restrictions = data[restrictions_idx][1:-1]
				race_class = data[race_class_idx][1:-1]
				prize_money = data[prize_idx][1:-1]
				going = data[going_idx][1:-1]
				no_of_runners = int(data[runners_idx][1:-1])

				horse_name = data[horse_name_idx][1:-1]
				horse_age = int(data[horse_age_idx][1:-1])
				horse_place = data[horse_place_idx][1:-1]
				weight = data[weight_pounds_idx][1:-1]
				odds = data[odds_idx][1:-1]
				comptime = data[comptime_idx][1:-1]
				trainer = data[trainer_idx][1:-1]
				jockey_name = data[jockey_name_idx][1:-1]
				jockeys_claim = data[jockeys_claim_idx][1:-1]
				rating = data[rating_idx][1:-1]

				race = Race(race_track, race_date, race_time, race_name, prize_money, race_restrictions, no_of_runners, going, race_class, race_distance)
				horse = Horse(horse_name, horse_age, horse_place, weight, jockey_name, jockeys_claim, trainer, odds) 
					
				try:                    
					races[race_name].add_horse(horse)
				except KeyError:
					races[race_name] = race
					races[race_name].add_horse(horse)

			elif len(data) < 25 or len(data) > 25:
				print 'Error'

				'''
			elif len(data) is 24:
				print 'Error'
				
				race_name = data[race_name_idx][1:-1].strip()
				race_date = data[race_date_idx][1:-1]
				race_track = data[race_track_idx][1:-1]
				race_time = data[race_time_idx][1:-1]
				race_distance = data[race_dist_idx - 1][1:-1]
				race_restrictions = data[restrictions_idx][1:-1]
				race_class = data[race_class_idx][1:-1]
				prize_money = data[prize_idx - 1][1:-1]
				going = data[going_idx - 1][1:-1]
				no_of_runners = int(data[runners_idx - 1][1:-1])

				horse_name = data[horse_name_idx - 1][1:-1]
				horse_age = int(data[horse_age_idx - 1][1:-1])
				horse_place = data[horse_place_idx - 1][1:-1]
				weight = data[weight_pounds_idx][1:-1]
				odds = data[odds_idx - 1][1:-1]
				comptime = data[comptime_idx - 1][1:-1]
				trainer = data[trainer_idx - 1][1:-1]
				jockey_name = data[jockey_name_idx - 1][1:-1]
				jockeys_claim = data[jockeys_claim_idx - 1][1:-1]
				rating = data[rating_idx - 1][1:-1]
				'''


				''''
		for r in races:
			print len(races)
			print ''

			print races[r].name
			print races[r].horses
			print ''
			'''

if __name__ == "__main__":
	main()
