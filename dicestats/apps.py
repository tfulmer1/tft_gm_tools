from __future__ import unicode_literals
from random import randint
import itertools
from django.apps import AppConfig


class DicestatsConfig(AppConfig):
    name = 'dicestats'


def parse_input(input_string):
    input_string = input_string.lower()
    dice, sides = input_string.split('d')
    return int(dice), int(sides)


def roll_dice(dice, sides, modifier=0):
    total = 0
    for x in range(0,dice):
        total += randint(1,sides)
    total += modifier
    return total


def value_range(dice, sides):
    floor = 1 * dice
    ceiling = dice * sides
    return floor, ceiling


def build_outcomes(min, max):
    outcomes = [x for x in range(min,max)]
    outcomes.append(max)
    return outcomes


def build_lookup_table(dice, sides):
    faces = [x for x in range(1,sides+1)]
    table = [row for row in itertools.product(faces, repeat=dice)]
    return table


def find_probability(outcome, dice, sides):
    table = build_lookup_table(dice,sides)
    combos = 0
    for combo in table:
        if sum(combo) == outcome:
            combos += 1
    probability = float(combos) / float(len(table))
    return probability


def compute_raw_probabilities(dice, sides):
    min, max = value_range(dice, sides)
    outcomes = build_outcomes(min, max)
    probabilities = {}
    for outcome in outcomes:
        probabilities[str(outcome)] = find_probability(outcome, dice, sides)
    return probabilities


def compute_value_or_below(prob_table, target_value):
    odds = 0
    for key, value in prob_table.iteritems():
        if int(key) <= int(target_value):
            odds += float(value)
    return odds


def compute_value_or_above(prob_table, target_value):
    odds = 0
    for key, value in prob_table.iteritems():
        if int(key) >= int(target_value):
            odds += float(value)
    return odds

if __name__ == '__main__':
    dice,sides = parse_input(raw_input("Input dice in 3d6 notation: "))
    probs = compute_raw_probabilities(dice,sides)
    for x in range(dice,(dice*sides)+1):
        print "Odds of {0} or less: {1:.2f}".format(x, 100*compute_value_or_below(probs,x))
