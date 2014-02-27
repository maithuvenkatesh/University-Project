import random, datetime, operator, re
from race_parser import RaceParser
from horse_parser_no_handicaps import HorseParser

def split_dataset(horses):
    keys = sorted(horses.keys())
    random.seed(1)
    random.shuffle(keys)

    l = len(keys)
    horses_train = [horses[k] for k in keys[l/2:]]
    horses_test = [horses[k] for k in keys[:l/2]]

    return horses_train, horses_test

def main():
    horses98 = HorseParser('./../Data/born98.csv').horses
    horses05 = HorseParser('./../Data/born05.csv').horses

    races98 = RaceParser('./../Data/born98.csv').races
    races05 = RaceParser('./../Data/born05.csv').races

    horses_train_98, horses_test_98 = split_dataset(horses98)

    horses_train_98 = [h for h in horses_train_98 if len(h.races) > 4]

    



        
        
                
        




if __name__ == "__main__":
    main()