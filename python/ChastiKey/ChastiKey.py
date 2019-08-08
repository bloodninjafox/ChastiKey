import math
import os
import pandas as pd
import random

chastikey_df = None


class ChastiKey():

    def __init__(self):
        """ Initialise ChastiKey() class """

        global chastikey_df
        if chastikey_df is None:
            if os.path.isfile(os.getcwd() + r"\ChastiKeyLocks.dat"):
                print("Loading database.")
                chastikey_df = pd.read_pickle(os.getcwd() + r"\ChastiKeyLocks.dat")
            else:
                print("Creating new database.")
                chastikey_df = pd.DataFrame(columns=["average_minutes_locked", "average_no_of_cards_drawn", 
                                                     "average_no_of_turns", "best_case_minutes_locked", 
                                                     "best_case_no_of_cards_drawn", "best_case_no_of_turns", 
                                                     "lock_level", "maximum_double_ups", "maximum_freezes", 
                                                     "maximum_greens", "maximum_reds", "maximum_resets",
                                                     "maximum_yellows_add", "maximum_yellows_minus", 
                                                     "maximum_yellows_random", "minimum_double_ups", "minimum_freezes", 
                                                     "minimum_greens", "minimum_reds", "minimum_resets", 
                                                     "minimum_yellows_add", "minimum_yellows_minus", "minimum_yellows_random",
                                                     "multiple_greens_required", "regularity", "worst_case_minutes_locked", 
                                                     "worst_case_no_of_cards_drawn", "worst_case_no_of_turns"])
                chastikey_df.to_pickle(os.getcwd() + r"\ChastiKeyLocks.dat")

    def __add_card_to_deck(self, card_name):
        """ (Private) Adds a card to the deck if there's not already too many of that card. """

        if card_name == "DoubleUp":
            if self.no_of_double_ups < 20:
                self.deck.append("DoubleUp")
                self.no_of_double_ups = self.no_of_double_ups + 1
        if card_name == "Freeze":
            if self.no_of_freezes < 20:
                self.deck.append("Freeze")
                self.no_of_freezes = self.no_of_freezes + 1
        if card_name == "Green":
            if self.no_of_greens < 20:
                self.deck.append("Green")
                self.no_of_greens = self.no_of_greens + 1
        if card_name == "Red":
            if self.no_of_reds < 399:
                self.deck.append("Red")
                self.no_of_reds = self.no_of_reds + 1
        if card_name == "Reset":
            if self.no_of_resets < 20:
                self.deck.append("Reset")
                self.no_of_resets = self.no_of_resets + 1
        if card_name == "YellowAdd1":
            if self.no_of_yellows_add_1 < 199:
                self.deck.append("YellowAdd1")
                self.no_of_yellows_add_1 = self.no_of_yellows_add_1 + 1
                self.no_of_yellows = self.no_of_yellows + 1
        if card_name == "YellowAdd2":
            if self.no_of_yellows_add_2 < 199:
                self.deck.append("YellowAdd2")
                self.no_of_yellows_add_2 = self.no_of_yellows_add_2 + 1
                self.no_of_yellows = self.no_of_yellows + 1
        if card_name == "YellowAdd3":
            if self.no_of_yellows_add_3 < 199:
                self.deck.append("YellowAdd3")
                self.no_of_yellows_add_3 = self.no_of_yellows_add_3 + 1
                self.no_of_yellows = self.no_of_yellows + 1
        if card_name == "YellowMinus1":
            if self.no_of_yellows_minus_1 < 199:
                self.deck.append("YellowMinus1")
                self.no_of_yellows_minus_1 = self.no_of_yellows_minus_1 + 1
                self.no_of_yellows = self.no_of_yellows + 1
        if card_name == "YellowMinus2":
            if self.no_of_yellows_minus_2 < 199:
                self.deck.append("YellowMinus2")
                self.no_of_yellows_minus_2 = self.no_of_yellows_minus_2 + 1
                self.no_of_yellows = self.no_of_yellows + 1

    def __create_deck(self):
        """ (Private) Creates a new deck with the required cards. """

        # Reset deck list and card counts.
        self.deck = []
        self.no_of_double_ups = 0
        self.no_of_freezes = 0
        self.no_of_greens = 0
        self.no_of_reds = 0
        self.no_of_resets = 0
        self.no_of_yellows = 0
        self.no_of_yellows_add_1 = 0
        self.no_of_yellows_add_2 = 0
        self.no_of_yellows_add_3 = 0
        self.no_of_yellows_minus_1 = 0
        self.no_of_yellows_minus_2 = 0

        for i in range(1, random.randint(self.minimum_double_ups, self.maximum_double_ups)):
            self.__add_card_to_deck("DoubleUp")
        for i in range(1, random.randint(self.minimum_freezes, self.maximum_freezes)):
            self.__add_card_to_deck("Freeze")
        for i in range(1, random.randint(self.minimum_greens, self.maximum_greens)):
            self.__add_card_to_deck("Green")
        for i in range(1, random.randint(self.minimum_reds, self.maximum_reds)):
            self.__add_card_to_deck("Red")
        for i in range(1, random.randint(self.minimum_resets, self.maximum_resets)):
            self.__add_card_to_deck("Resets")
        for i in range(1, random.randint(self.minimum_yellows_add, self.maximum_yellows_add)):
            random_yellow = random.randint(1, 3)
            if random_yellow == 1:
                self.__add_card_to_deck("YellowAdd1")
            if random_yellow == 2:
                self.__add_card_to_deck("YellowAdd2")
            if random_yellow == 3:
                self.__add_card_to_deck("YellowAdd3")
        for i in range(1, random.randint(self.minimum_yellows_minus, self.maximum_yellows_minus)):
            random_yellow = random.randint(1, 2)
            if random_yellow == 1:
                self.__add_card_to_deck("YellowMinus1")
            if random_yellow == 2:
                self.__add_card_to_deck("YellowMinus2")
        for i in range(1, random.randint(self.minimum_yellows_random, self.maximum_yellows_random)):
            random_yellow = random.randint(1, 5)
            if random_yellow == 1:
                self.__add_card_to_deck("YellowAdd1")
            if random_yellow == 2:
                self.__add_card_to_deck("YellowAdd2")
            if random_yellow == 3:
                self.__add_card_to_deck("YellowAdd3")
            if random_yellow == 4:
                self.__add_card_to_deck("YellowMinus1")
            if random_yellow == 5:
                self.__add_card_to_deck("YellowMinus2")

        # Store the starting card counts in the initial counts. This is required for when the reset card is revealed.
        self.initial_double_ups = self.no_of_double_ups
        self.initial_freezes = self.no_of_freezes
        self.initial_greens = self.no_of_greens
        self.initial_reds = self.no_of_reds
        self.initial_resets = self.no_of_resets
        self.initial_yellows_add_1 = self.no_of_yellows_add_1
        self.initial_yellows_add_2 = self.no_of_yellows_add_2
        self.initial_yellows_add_3 = self.no_of_yellows_add_3
        self.initial_yellows_minus_1 = self.no_of_yellows_minus_1
        self.initial_yellows_minus_2 = self.no_of_yellows_minus_2

    def __initialise_simulation(self, simulations_to_run=10, regularity=24, multiple_greens_required=0, minimum_double_ups=0, maximum_double_ups=0, minimum_freezes=0, maximum_freezes=0, minimum_greens=1, maximum_greens=1, minimum_reds=0, maximum_reds=0, minimum_resets=0, maximum_resets=0, minimum_yellows_add=0, maximum_yellows_add=0, minimum_yellows_minus=0, maximum_yellows_minus=0, minimum_yellows_random=0, maximum_yellows_random=0, print_output=False):
        """ (Private) Initialise simulation """

        # Probably far too many variables, but these are used throughout.
        self.average_case_cards_drawn = 0
        self.average_case_chances = 0
        self.average_case_length = 0
        self.average_minutes_locked = 0
        self.average_no_of_turns = 0
        self.average_no_of_cards_drawn = 0
        self.best_case_cards_drawn = 0
        self.best_case_chances = 0
        self.best_case_length = 0
        self.best_case_minutes_locked = 9999999999
        self.best_case_no_of_turns = 9999999999
        self.best_case_no_of_cards_drawn = 9999999999
        self.deck = []
        self.hide_greens_until = 0
        self.initial_double_ups = 0
        self.initial_freezes = 0
        self.initial_greens = 0
        self.initial_reds = 0
        self.initial_resets = 0
        self.initial_yellows_add_1 = 0
        self.initial_yellows_add_2 = 0
        self.initial_yellows_add_3 = 0
        self.initial_yellows_minus_1 = 0
        self.initial_yellows_minus_2 = 0
        self.maximum_double_ups = max(minimum_double_ups, maximum_double_ups)
        self.maximum_freezes = max(minimum_freezes, maximum_freezes)
        self.maximum_greens = max(minimum_greens, maximum_greens)
        self.maximum_reds = max(minimum_reds, maximum_reds)
        self.maximum_resets = max(minimum_resets, maximum_resets)
        self.maximum_yellows_add = max(minimum_yellows_add, maximum_yellows_add)
        self.maximum_yellows_minus = max(minimum_yellows_minus, maximum_yellows_minus)
        self.maximum_yellows_random = max(minimum_yellows_random, maximum_yellows_random)
        self.minimum_double_ups = min(minimum_double_ups, maximum_double_ups)
        self.minimum_freezes = min(minimum_freezes, maximum_freezes)
        self.minimum_greens = min(minimum_greens, maximum_greens)
        self.minimum_reds = min(minimum_reds, maximum_reds)
        self.minimum_resets = min(minimum_resets, maximum_resets)
        self.minimum_yellows_add = min(minimum_yellows_add, maximum_yellows_add)
        self.minimum_yellows_minus = min(minimum_yellows_minus, maximum_yellows_minus)
        self.minimum_yellows_random = min(minimum_yellows_random, maximum_yellows_random)
        self.minutes_locked = 0
        self.multiple_greens_required = multiple_greens_required
        self.no_of_cards_drawn = 0
        self.no_of_double_ups = 0
        self.no_of_freezes = 0
        self.no_of_greens = 0
        self.no_of_reds = 0
        self.no_of_resets = 0
        self.no_of_turns = 0
        self.no_of_yellows = 0
        self.no_of_yellows_add_1 = 0
        self.no_of_yellows_add_2 = 0
        self.no_of_yellows_add_3 = 0
        self.no_of_yellows_minus_1 = 0
        self.no_of_yellows_minus_2 = 0
        self.regularity = regularity
        self.simulation_count = 0
        self.simulations_to_run = simulations_to_run
        self.worst_case_cards_drawn = 0
        self.worst_case_chances = 0
        self.worst_case_length = 0
        self.worst_case_minutes_locked = 0
        self.worst_case_no_of_turns = 0
        self.worst_case_no_of_cards_drawn = 0

        self.__run_simulations()

    def __remove_card_from_deck(self, card_name):
        """ (Private) Removes a card from the deck. """

        if card_name in self.deck:
            if card_name == "DoubleUp":
                self.no_of_double_ups = self.no_of_double_ups - 1
            if card_name == "Freeze":
                self.no_of_freezes = self.no_of_freezes - 1
            if card_name == "Green":
                self.no_of_greens = self.no_of_greens - 1
            if card_name == "Red":
                self.no_of_reds = self.no_of_reds - 1
            if card_name == "Resets":
                self.no_of_resets = self.no_of_resets - 1
            if card_name == "YellowAdd1":
                self.no_of_yellows_add_1 = self.no_of_yellows_add_1 - 1
                self.no_of_yellows = self.no_of_yellows - 1
            if card_name == "YellowAdd2":
                self.no_of_yellows_add_2 = self.no_of_yellows_add_2 - 1
                self.no_of_yellows = self.no_of_yellows - 1
            if card_name == "YellowAdd3":
                self.no_of_yellows_add_3 = self.no_of_yellows_add_3 - 1
                self.no_of_yellows = self.no_of_yellows - 1
            if card_name == "YellowMinus1":
                self.no_of_yellows_minus_1 = self.no_of_yellows_minus_1 - 1
                self.no_of_yellows = self.no_of_yellows - 1
            if card_name == "YellowMinus2":
                self.no_of_yellows_minus_2 = self.no_of_yellows_minus_2 - 1
                self.no_of_yellows = self.no_of_yellows - 1
            self.deck.remove(card_name)

    def __run_simulations(self):
        """ (Private) Runs simulations """

        # Loop until all x simulations have been run.
        while self.simulation_count < self.simulations_to_run:
            self.minutes_locked = 0
            self.no_of_cards_drawn = 0
            self.no_of_turns = 0
            self.simulation_count = self.simulation_count + 1
            self.__create_deck()
            # The minimum number of reds decides when the green cards can be found.
            if self.maximum_reds == 0:
                self.hide_greens_until = 1
            elif self.minimum_reds != self.maximum_reds:
                self.hide_greens_until = self.minimum_reds
            else:
                self.hide_greens_until = 1
            # Loop until the deck has no cards. The loop can also be exited below once all of the required greens have been found.
            while len(self.deck) > 0:
                # Pick a random card from the deck.
                card_picked = random.choice(self.deck)
                # If green and green found too early, continue and try again.
                if card_picked == "Green" and self.no_of_turns < self.hide_greens_until and self.no_of_double_ups + self.no_of_freezes + self.no_of_reds + self.no_of_resets + self.no_of_yellows > 0:
                    continue
                # If double up, then double the number of reds and yellows in the deck.
                if card_picked == "DoubleUp":
                    self.__remove_card_from_deck("DoubleUp")
                    for i in range(1, self.no_of_reds):
                        self.__add_card_to_deck("Red")
                    for i in range(1, self.no_of_yellows_add_1):
                        self.__add_card_to_deck("YellowAdd1")
                    for i in range(1, self.no_of_yellows_add_2):
                        self.__add_card_to_deck("YellowAdd2")
                    for i in range(1, self.no_of_yellows_add_3):
                        self.__add_card_to_deck("YellowAdd3")
                    for i in range(1, self.no_of_yellows_minus_1):
                        self.__add_card_to_deck("YellowMinus1")
                    for i in range(1, self.no_of_yellows_minus_2):
                        self.__add_card_to_deck("YellowMinus2")
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If freeze, then add 2 to 4 times the regularity to the total lock time.
                if card_picked == "Freeze":
                    self.__remove_card_from_deck("Freeze")
                    minutes_frozen = random.randint(120 * self.regularity, 240 * self.regularity)
                    self.average_minutes_locked = self.average_minutes_locked + minutes_frozen
                    self.minutes_locked = self.minutes_locked + minutes_frozen
                    self.average_no_of_turns = self.average_no_of_turns + 1
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_turns = self.no_of_turns + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If green, unlock if multiple greens not required, or if all greens were found.
                if card_picked == "Green":
                    self.__remove_card_from_deck("Green")
                    if self.multiple_greens_required == 0:
                        self.deck = []
                    elif self.multiple_greens_required == 1 and self.no_of_greens == 0:
                        self.deck = []
                    self.average_no_of__cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If red, then add 60 minutes * the regularity.
                if card_picked == "Red":
                    self.__remove_card_from_deck("Red")
                    self.average_minutes_locked = self.average_minutes_locked + (60 * self.regularity)
                    self.minutes_locked = self.minutes_locked + (60 * self.regularity)
                    self.average_no_of_turns = self.average_no_of_turns + 1
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_turns = self.no_of_turns + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If reset, then reset the deck. Set the number of cards back to the initial counts, except for double up and reset cards.
                if card_picked == "Reset":
                    self.__remove_card_from_deck("Reset")
                    if self.no_of_freezes > self.initial_freezes:
                        for i in range(self.no_of_freezes, self.initial_freezes + 1, -1):
                            self.__remove_card_from_deck("Freeze")
                    elif self.no_of_freezes < self.initial_freezes:
                        for i in range(self.no_of_freezes + 1, self.initial_freezes):
                            self.__add_card_to_deck("Freeze")
                    if self.no_of_greens > self.initial_greens:
                        for i in range(self.no_of_greens, self.initial_greens + 1, -1):
                            self.__remove_card_from_deck("Green")
                    elif self.no_of_greens < self.initial_greens:
                        for i in range(self.no_of_greens + 1, self.initial_greens):
                            self.__add_card_to_deck("Green")
                    if self.no_of_reds > self.initial_reds:
                        for i in range(self.no_of_reds, self.initial_reds + 1, -1):
                            self.__remove_card_from_deck("Red")
                    elif self.no_of_reds < self.initial_reds:
                        for i in range(self.no_of_reds + 1, self.initial_reds):
                            self.__add_card_to_deck("Red")
                    if self.no_of_yellows_add_1 > self.initial_yellows_add_1:
                        for i in range(self.no_of_yellows_add_1, self.initial_yellows_add_1 + 1, -1):
                            self.__remove_card_from_deck("YellowAdd1")
                    elif self.no_of_yellows_add_1 < self.initial_yellows_add_1:
                        for i in range(self.no_of_yellows_add_1 + 1, self.initial_yellows_add_1):
                            self.__add_card_to_deck("YellowAdd1")
                    if self.no_of_yellows_add_2 > self.initial_yellows_add_2:
                        for i in range(self.no_of_yellows_add_2, self.initial_yellows_add_2 + 1, -1):
                            self.__remove_card_from_deck("YellowAdd2")
                    elif self.no_of_yellows_add_2 < self.initial_yellows_add_2:
                        for i in range(self.no_of_yellows_add_2 + 1, self.initial_yellows_add_2):
                            self.__add_card_to_deck("YellowAdd2")
                    if self.no_of_yellows_add_3 > self.initial_yellows_add_3:
                        for i in range(self.no_of_yellows_add_3, self.initial_yellows_add_3 + 1, -1):
                            self.__remove_card_from_deck("YellowAdd3")
                    elif self.no_of_yellows_add_3 < self.initial_yellows_add_3:
                        for i in range(self.no_of_yellows_add_3 + 1, self.initial_yellows_add_3):
                            self.__add_card_to_deck("YellowAdd3")
                    if self.no_of_yellows_minus_1 > self.initial_yellows_minus_1:
                        for i in range(self.no_of_yellows_minus_1, self.initial_yellows_minus_1 + 1, -1):
                            self.__remove_card_from_deck("YellowMinus1")
                    elif self.no_of_yellows_minus_1 < self.initial_yellows_minus_1:
                        for i in range(self.no_of_yellows_minus_1 + 1, self.initial_yellows_minus_1):
                            self.__add_card_to_deck("YellowMinus1")
                    if self.no_of_yellows_minus_2 > self.initial_yellows_minus_2:
                        for i in range(self.no_of_yellows_minus_2, self.initial_yellows_minus_2 + 1, -1):
                            self.__remove_card_from_deck("YellowMinus2")
                    elif self.no_of_yellows_minus_2 < self.initial_yellows_minus_2:
                        for i in range(self.no_of_yellows_minus_2 + 1, self.initial_yellows_minus_2):
                            self.__add_card_to_deck("YellowMinus2")
                    self.average_no_of_turns = self.average_no_of_turns + 1
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_turns = self.no_of_turns + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If yellow add 1, then add 1 red to the deck.
                if card_picked == "YellowAdd1":
                    self.__remove_card_from_deck("YellowAdd1")
                    self.__add_card_to_deck("Red")
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If yellow add 2, then add 2 reds to the deck.
                if card_picked == "YellowAdd2":
                    self.__remove_card_from_deck("YellowAdd2")
                    self.__add_card_to_deck("Red")
                    self.__add_card_to_deck("Red")
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If yellow add 3, then add 3 reds to the deck.
                if card_picked == "YellowAdd3":
                    self.__remove_card_from_deck("YellowAdd3")
                    self.__add_card_to_deck("Red")
                    self.__add_card_to_deck("Red")
                    self.__add_card_to_deck("Red")
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If yellow minus 1, then remove 1 red from the the deck.
                if card_picked == "YellowMinus1":
                    self.__remove_card_from_deck("YellowMinus1")
                    self.__remove_card_from_deck("Red")
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
                # If yellow minus 2, then remove 2 reds from the the deck.
                if card_picked == "YellowMinus2":
                    self.__remove_card_from_deck("YellowMinus2")
                    self.__remove_card_from_deck("Red")
                    self.__remove_card_from_deck("Red")
                    self.average_no_of_cards_drawn = self.average_no_of_cards_drawn + 1
                    self.no_of_cards_drawn = self.no_of_cards_drawn + 1
            # If the time, turns, and cards drawn count are better or worst then the last best or worst values, then store the new values.
            if self.simulation_count <= self.simulations_to_run:
                if self.minutes_locked < self.best_case_minutes_locked:
                    self.best_case_minutes_locked = self.minutes_locked
                if self.no_of_turns < self.best_case_no_of_turns:
                    self.best_case_no_of_turns = self.no_of_turns
                if self.no_of_cards_drawn < self.best_case_no_of_cards_drawn:
                    self.best_case_no_of_cards_drawn = self.no_of_cards_drawn
                if self.minutes_locked > self.worst_case_minutes_locked:
                    self.worst_case_minutes_locked = self.minutes_locked
                if self.no_of_turns > self.worst_case_no_of_turns:
                    self.worst_case_no_of_turns = self.no_of_turns
                if self.no_of_cards_drawn > self.worst_case_no_of_cards_drawn:
                    self.worst_case_no_of_cards_drawn = self.no_of_cards_drawn

    def ClearLocks(self):
        """ Clears all locks from the database """

        global chastikey_df
        print("Clearing all locks from the database.")
        chastikey_df = None
        if os.path.isfile(os.getcwd() + r"\ChastiKeyLocks.dat"):
            os.remove(os.getcwd() + r"\ChastiKeyLocks.dat")
        print("Locks cleared.")
        self.__init__()

    def DisplayStats(self):
        """ Display database stats """

        global chastikey_df
        print(str(chastikey_df.shape[0]) + " lock(s) saved.")

    def GenerateLocks(self, number_of_locks=1, lock_level=None):
        """ Generate random locks """

        args_lock_level = lock_level
        global chastikey_df
        print("Generating " + str(number_of_locks) + " lock(s).")
        for i in range(0, number_of_locks):
            if args_lock_level is None:
                lock_level = round(random.uniform(0.1, 1), 1)
            else:
                lock_level = args_lock_level / 10.0
            self.__initialise_simulation(simulations_to_run=10, regularity=1, multiple_greens_required=random.randint(0, 1), minimum_double_ups=random.randint(0, math.ceil(20 * lock_level)), maximum_double_ups=random.randint(0, math.ceil(20 * lock_level)), minimum_freezes=random.randint(0, math.ceil(20 * lock_level)), maximum_freezes=random.randint(0, math.ceil(20 * lock_level)), minimum_greens=random.randint(1, math.ceil(20 * lock_level)), maximum_greens=random.randint(1, math.ceil(20 * lock_level)), minimum_reds=random.randint(0, math.ceil(399 * lock_level)), maximum_reds=random.randint(0, math.ceil(399 * lock_level)), minimum_resets=random.randint(0, math.ceil(20 * lock_level)), maximum_resets=random.randint(0, math.ceil(20 * lock_level)), minimum_yellows_add=random.randint(0, math.ceil(199 * lock_level)), maximum_yellows_add=random.randint(0, math.ceil(199 * lock_level)), minimum_yellows_minus=random.randint(0, math.ceil(199 * lock_level)), maximum_yellows_minus=random.randint(0, math.ceil(199 * lock_level)), minimum_yellows_random=random.randint(0, math.ceil(199 * lock_level)), maximum_yellows_random=random.randint(0, math.ceil(199 * lock_level)), print_output=False)
            new_lock = {
                "average_minutes_locked": self.average_minutes_locked / self.simulations_to_run, 
                "average_no_of_cards_drawn": self.average_no_of_cards_drawn / self.simulations_to_run, 
                "average_no_of_turns": self.average_no_of_turns / self.simulations_to_run, 
                "best_case_minutes_locked": self.best_case_minutes_locked,
                "best_case_no_of_turns": self.best_case_no_of_turns,
                "best_case_no_of_cards_drawn": self.best_case_no_of_cards_drawn,
                "lock_level": lock_level,
                "maximum_double_ups": self.maximum_double_ups,
                "maximum_freezes": self.maximum_freezes,
                "maximum_greens": self.maximum_greens,
                "maximum_reds": self.maximum_reds,
                "maximum_resets": self.maximum_resets,
                "maximum_yellows_add": self.maximum_yellows_add,
                "maximum_yellows_minus": self.maximum_yellows_minus,
                "maximum_yellows_random": self.maximum_yellows_random,
                "minimum_double_ups": self.minimum_double_ups,
                "minimum_freezes": self.minimum_freezes,
                "minimum_greens": self.minimum_greens,
                "minimum_reds": self.minimum_reds,
                "minimum_resets": self.minimum_resets,
                "minimum_yellows_add": self.minimum_yellows_add,
                "minimum_yellows_minus": self.minimum_yellows_minus,
                "minimum_yellows_random": self.minimum_yellows_random,
                "multiple_greens_required": self.multiple_greens_required,
                "regularity": self.regularity,
                "worst_case_minutes_locked": self.worst_case_minutes_locked,
                "worst_case_no_of_turns": self.worst_case_no_of_turns,
                "worst_case_no_of_cards_drawn": self.worst_case_no_of_cards_drawn
            }
            chastikey_df = chastikey_df.append(new_lock, ignore_index=True)
            chastikey_df.to_pickle(os.getcwd() + r"\ChastiKeyLocks.dat")
        print(str(number_of_locks) + " lock(s) generated and saved to dataframe.")

    def SaveToExcel(self, excel_file=None):
        """ Save locks database to an excel file """

        global chastikey_df
        if excel_file is None:
            excel_file = os.getcwd() + r"\ChastiKeyLocks.xlsx"
        chastikey_df.to_excel(excel_file, index=False)
        print("Excel file created.")
