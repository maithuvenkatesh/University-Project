import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from race_parser_no_handicaps import RaceParserNoHandicaps
from horse_parser_no_handicaps import HorseParserNoHandicaps
from utilities import split_dataset

def going_class(horses_train):
    going_class = defaultdict(set)
    for h in horses_train:
        for r in h.races:
            going_class[r.going].add(r.race_class)

    for g in going_class:
        print g
        print going_class[g]
        print ''

def main():
    horses98 = HorseParserNoHandicaps('./../Data/born98.csv').horses
    horses05 = HorseParserNoHandicaps('./../Data/born05.csv').horses

    races98 = RaceParserNoHandicaps('./../Data/born98.csv').races
    races05 = RaceParserNoHandicaps('./../Data/born05.csv').races

    horses_train_98, horses_test_98 = split_dataset(horses98)
    horses_train_05, horses_test_05 = split_dataset(horses05)

    going_class(horses_train_05)
    going_class(horses_train_98)

if __name__ == "__main__":
    main()