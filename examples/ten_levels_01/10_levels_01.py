# -*- coding: utf-8 -*-

u"""10_levels_01
A simple game economics example
Demonstration with 10 levels
"""

__usage__ = u"""Usage: python3 10_levels_01 [options]
Options:
  -h, --help              show this help
  -d                      show debugging information  
Examples:
  python3 10_levels_01.py
  runs a 10 level game
"""

__author__ = u"Amallyn"
__version__ = u"$Revision: 0.01 $"
__date__ = u"$Date: 2022/11/18 00:06:30 $"
__copyright__ = u"Copyright [" + __author__ + "]"
__license__ = u"Licensed under the Apache License, Version 2.0"

from random import random

"""
Levels difficulty
difficulty is the loss percentage
win ratio = 1 - difficulty/100
"""
levels_difficulty = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 5,
    "5": 7,
    "6": 10,
    "7": 14,
    "8": 20,
    "9": 30,
    "10": 45
}

class Resource:
    pass

class CoinResource(Resource):
    pass

class Upgrade:
    pass

class Player:
    """
    Player
    a player
    """

    def __init__(self, name = "Player Name"):
        """
        Init
        """
        self.name = name
        experience = 0
        cleared_levels = 0

    def reset(self):
        """
        reset the game
        """
        # experience lowers the difficulty of a level
        # win ratio = (1 - difficulty/100) * experience/100
        self.experience = 0
        self.cleared_levels = 0

class GameEngine:
    """
    GameEngine
    runs our game mechanics
    """

    def __init__(self):
        """
        Init
        """
        pass
    def play_level(self, player, level):
        r = random()
        difficulty = float(0.01* levels_difficulty[str(level)])
        win = r >= difficulty
        print("| level {:2d}".format(level), "| difficulty", "{:.2f}".format(difficulty), "| result: ", "{:.3f}".format(r), "| win: ", win, " |")
        return win

class Simulator:
    """
    Simulator
    simulate a player playing x turns
    """
    def __init__(self):
        """
        Init
        """
        pass

    def run(self, player, turns):
        """
        runs a simulation
        """

class Calculator:
    """
    Calculator
    Calculates a player playing x turns
    """
    def __init__(self):
        """
        Init
        """
        pass

    def run(self, player, turns):
        """
        runs a calculation
        """

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    """
    main
    """
    import getopt
    if argv is None:
        argv = sys.argv

    try:
        try:                                
            opts, args = getopt.getopt(argv, "h:d", ["help"])
        except getopt.error as msg:
            raise Usage(msg)            
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(__usage__)                   
                sys.exit()                  
            elif opt == '-d':
                global _debug               
                _debug = 1                  
    except Usage as err:
        print(err.msg, file=sys.stderr)
        print ("for help use --help", file=sys.stderr)
        return 2

    player = Player("player one")
    game_engine = GameEngine()
    print("== ", player.name, " ==")
    for level in range(1, 11):
        game_engine.play_level(player, level)
        
if __name__ == "__main__":
    import sys
    print("\n" + __doc__ + "\n" + __copyright__ + "\n" + __license__ +"\n" )
    main(sys.argv[1:])
