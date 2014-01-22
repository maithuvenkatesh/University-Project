from collections import defaultdict

class Horse:
	def __init__(self, horse_name):
		self.name = horse_name
		self.races = []

	def add_race(self, race_name, horse_age):
		self.races.append((race_name, horse_age))


def main():
	horses = {}
	with open('../Data/born98.csv', 'r') as f:
		attributes = f.readline().strip().split()

		race_idx = attributes.index('race_name')
		horse_idx = attributes.index('horse_name')
		age_idx = attributes.index('horse_age')

		for line in f:
			data = line.strip().split('\t')		
			horse_name = data[horse_idx][1:-1].strip()
			race_name = data[race_idx][1:-1].strip()
			horse_age = data[age_idx][1:-1].strip()

			try:
				horses[horse_name].add_race(race_name, horse_age)
			except KeyError:
				horses[horse_name] = Horse(horse_name)
				horses[horse_name].add_race(race_name, horse_age)  

		for h in sorted(horses)[:50]:
			horse = horses[h]
			print horse.name

			for r in horse.races:
				print r

			print ''		



if __name__ == "__main__":
    main()