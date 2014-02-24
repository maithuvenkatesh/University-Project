from collections import Counter
from horse_parser import HorseParser 
from race_parser import RaceParser 

class Race:
    def __init__(self, race_hash, race_track, race_date, race_time, race_name, race_prize, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight_carried, jockey_name, jockeys_claim, trainer, horse_odds, horse_speed, winning_horse):
        self.race_hash = race_hash
        self.track = race_track
        self.date = race_date
        self.time = race_time
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
        self.horse_speed = horse_speed
        self.race_winner = winning_horse

class Horse:
    def __init__(self, horse_name, horse_hash):
        self.name = horse_name
        self.horse_hash = horse_hash
        self.races = {}

''' Returns the races which contain the records of all horses in the dataset '''
def get_full_races(races):
    full_races = {}
    
    for r in races:
        if len(races[r].horses) == races[r].no_of_runners:
            full_races[races[r].race_hash] = races[r]

    return full_races

def get_all_horses_from_full_races(full_races):
    horses = {}

    for r in full_races:
        for h in full_races[r].horses:
            race_hash = full_races[r].race_hash
            race_track = full_races[r].track
            race_date = full_races[r].date
            race_time = full_races[r].time
            race_name = full_races[r].name
            prize_money = full_races[r].prize
            race_restrictions = full_races[r].restrictions
            no_of_runners = full_races[r].no_of_runners
            going = full_races[r].going
            race_class = full_races[r].race_class
            race_distance = full_races[r].distance
            winning_horse = full_races[r].winner

            horse_name = h.name
            horse_hash = h.horse_hash
            horse_place = h.place
            horse_age = h.age
            weight_carried = h.weight_carried
            jockey_name = h.jockey
            jockeys_claim = h.jockeys_claim
            trainer = h.trainer
            odds = h.odds
            horse_speed = h.speed

            race = Race(race_hash, race_track, race_date, race_time, race_name, prize_money, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight_carried, jockey_name, jockeys_claim, trainer, odds, horse_speed, winning_horse)
            horse = Horse(horse_name, horse_hash)

            try:       
                horses[horse_hash].races[race_hash] = race
            except KeyError:
                horses[horse_hash] = horse
                horses[horse_hash].races[race_hash] = race

    return horses

def horses_with_k_races(full_races, full_race_horses_data):
    horses_race_count = Counter()
    seen_horses = set()

    for r in full_races:
        for h in full_races[r].horses:
            if h.horse_hash not in seen_horses:
                total_races = len(full_race_horses_data[h.horse_hash].races)
                horses_race_count[total_races] += 1

    return horses_race_count

def main():
    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    full_races_98 = get_full_races(races98)
    full_races_05 = get_full_races(races05)

    full_race_horse_data_98 = get_all_horses_from_full_races(full_races_98)
    full_race_horse_data_05 = get_all_horses_from_full_races(full_races_05)

    horses_race_count_98 = horses_with_k_races(full_races_98, full_race_horse_data_98)
    horses_race_count_98 = horses_with_k_races(full_races_98, full_race_horse_data_98)

    print horses_race_count_98


if __name__ == "__main__":
    main()