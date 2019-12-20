
# Given a set of rolls [k1, k2, k3, k4, ..., kN], calculates the maximum possible "upper section" Yahtzee score.
# DailyProgrammer 11/11/2019 single-line solution
YahtzeeMax = lambda rolls : max([rolls.count(k)*k for k in rolls])
