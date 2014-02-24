import re, string

class Race:
    def __init__(self, race_hash, race_track, race_date, race_time, race_name, race_prize, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight_carried, jockey_name, jockeys_claim, trainer, horse_odds, horse_speed):
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

class Horse:
    def __init__(self, horse_name, horse_hash):
        self.name = horse_name
        self.horse_hash = horse_hash
        self.races = {}

    def add_race(self, race):
        #self.races.append(race)
        self.races[race.race_hash] = race

class HorseParser:
    def __init__(self, filepath):
        self.horses = {}

        with open(filepath) as f:
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

                race_date = data[race_date_idx][1:-1].strip()
                race_time = data[race_time_idx][1:-1].strip()
                race_track = data[race_track_idx][1:-1].strip()
                race_name = data[race_name_idx][1:-1].strip()

                race_hash = race_name + race_date + race_time + race_track

                # Convert distance to meters per second
                FURLONGS_TO_METERS = 201.1680
                MILES_TO_METERS = 1609.344

                try:
                    race_distance = data[race_dist_idx][1:-1].strip()
                except IndexError:
                    print len(data)
                    print data
                    print race_dist_idx
                    print race_date
                    print race_time
                    print race_track

                if len(race_distance) == 2:
                   
                    if race_distance[1] is 'f':
                        race_distance = float(race_distance[0]) * FURLONGS_TO_METERS
                    elif race_distance[1] is 'm':
                        race_distance = float(race_distance[0]) * MILES_TO_METERS
               
                elif len(race_distance) == 3:
                    race_distance = (float(race_distance[0]) + 0.5) * FURLONGS_TO_METERS
                
                elif len(race_distance) == 4:
                    miles_to_meters = float(race_distance[0]) * MILES_TO_METERS
                    
                    furlongs_to_meters = 0.0
                    try:
                        furlongs_to_meters = float(race_distance[2]) * FURLONGS_TO_METERS
                    except ValueError:
                        furlongs_to_meters = 0.5 * FURLONGS_TO_METERS
                    
                    race_distance = miles_to_meters + furlongs_to_meters
                
                elif len(race_distance) == 5:
                    miles_to_meters = float(race_distance[0]) * MILES_TO_METERS
                    furlongs_to_meters_1 = float(race_distance[2]) * FURLONGS_TO_METERS

                    furlongs_to_meters_2 = 0.0
                    try:
                        furlongs_to_meters_2 = float(race_distance[3]) * FURLONGS_TO_METERS
                    except ValueError:
                        furlongs_to_meters_2 = 0.5 * FURLONGS_TO_METERS

                    race_distance = miles_to_meters + furlongs_to_meters_1 + furlongs_to_meters_2

                race_restrictions = data[restrictions_idx][1:-1].strip()
                
                race_class = data[race_class_idx][1:-1].strip().split()[-1]
                race_grade = 0
                
                if race_class == 'Irish':
                    race_class = 8
                elif race_class == 1:
                    race_grade = int(data[major_idx][1:-1].strip().split()[-1])
                else:
                    race_class = int(race_class)

                prize_money = float(data[prize_idx][1:-1])
                going = data[going_idx][1:-1].strip()
                no_of_runners = int(data[runners_idx][1:-1])

                horse_name = data[horse_name_idx][1:-1].strip()
                exclude = set(string.punctuation)
                horse_hash = horse_name.lower() # Used for the key of the hashtable
                horse_hash = ''.join(c for c in horse_hash if c not in exclude)
                horse_hash = horse_hash.replace(' ', '')

                horse_age = int(data[horse_age_idx][1:-1])

                # TODO - check horse placing codes
                horse_place = data[horse_place_idx][1:-1].strip()
                match = re.search(re.compile('\d'), horse_place)
                if match:
                    horse_place = [int(s) for s in horse_place if s.isdigit()]
                    if len(horse_place) == 0:
                        horse_place = 0
                    else:
                        horse_place = int(''.join(map(str, horse_place)))
                else:
                    horse_place = 0

                winner = ''
                if horse_place == 1:
                    winner = horse_hash

                weight = float(data[weight_pounds_idx][1:-1].strip())
                odds = float(data[odds_idx][1:-1].strip())

                # Converts comptime to seconds
                comptime = data[comptime_idx][1:-1].strip()
                comptime = comptime.split()
                comptime = 60 * float(comptime[0]) + float(comptime[2][:-1])

                if comptime == 0.0:
                    continue
                
                trainer = data[trainer_idx][1:-1].strip()
                jockey_name = data[jockey_name_idx][1:-1].strip()
                jockeys_claim = float(data[jockeys_claim_idx][1:-1].strip())
                rating = float(data[rating_idx][1:-1].strip())

                horse_speed = float(race_distance)/float(comptime)

                race = Race(race_hash, race_track, race_date, race_time, race_name, prize_money, race_restrictions, no_of_runners, going, race_class, race_distance, horse_place, horse_age, weight, jockey_name, jockeys_claim, trainer, odds, horse_speed)
                horse = Horse(horse_name, horse_hash) 

                try:       
                    self.horses[horse_hash].add_race(race)
                except KeyError:
                    self.horses[horse_hash] = horse
                    self.horses[horse_hash].add_race(race)

'''
def main():
    horses = HorseParser('./../Data/born98.csv').horses


if __name__ == "__main__":
    main()
'''