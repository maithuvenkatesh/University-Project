class Race:
    def __init__(self, race_key, race_track, race_date, race_time, race_name, race_prize, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight_carried, jockey_name, jockeys_claim, trainer, horse_odds, horse_speed, winning_horse):
        self.race_key = race_key
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
    def __init__(self, horse_name, horse_key):
        self.name = horse_name
        self.horse_key = horse_key
        self.races = {}

class HorseRecords:
    def __init__(self, full_races):
        self.horses = {}

        for r in full_races:
            for h in full_races[r].horses:
                race_key = full_races[r].race_key
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
                horse_key = h.horse_key
                horse_place = h.place
                horse_age = h.age
                weight_carried = h.weight_carried
                jockey_name = h.jockey
                jockeys_claim = h.jockeys_claim
                trainer = h.trainer
                odds = h.odds
                horse_speed = h.speed

                race = Race(race_key, race_track, race_date, race_time, race_name, prize_money, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight_carried, jockey_name, jockeys_claim, trainer, odds, horse_speed, winning_horse)
                horse = Horse(horse_name, horse_key)

                try:       
                    self.horses[horse_key].races[race_key] = race
                except KeyError:
                    self.horses[horse_key] = horse
                    self.horses[horse_key].races[race_key] = race