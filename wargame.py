"""
Author: Ken Lambert
Edited By:  Leigh Stauffer
File: wargame.py
Project 9

Module for playing the game of War
"""

from cards import Deck

class WarGame(object):
    """Plays the game of War."""

    def __init__(self):
        """Sets up the two players, the war pile, the deck, and the
        game state."""
        self._player1 = Player()
        self._player2 = Player()
        self._warPile = []
        self._gameState = ""
        self._deck = Deck()
        self._deck.shuffle()

    def __str__(self):
        """Returns the game state."""
        return self._gameState

    def deal(self):
        """Deals 26 cards to each player."""
        while not self._deck.isEmpty():
            self._player1.addToUnplayedPile(self._deck.deal())
            self._player2.addToUnplayedPile(self._deck.deal())

    def step(self):
        """Makes one move in the game, and returns the two cards
        played."""
        card1 = self._player1.getCard()
        card2 = self._player2.getCard()
        self._warPile.append(card1)
        self._warPile.append(card2)
        self._gameState = "Player 1: " + str(card1) + "\n" +\
                          "Player 2: " + str(card2)
        if card1.rank == card2.rank:
            self._gameState += "\nCards added to War pile\n"
        elif card1.rank > card2.rank:
            self._transferCards(self._player1)
            self._gameState += "\nCards go to Player 1"
        else:
            self._transferCards(self._player2)
            self._gameState += "\nCards go to Player 2"
        return (card1, card2)

    def _transferCards(self, player):
        """Transfers cards from the war pile to the player's
        winnings pile."""
        while len(self._warPile) > 0:
            player.addToWinningsPile(self._warPile.pop())

    def winner(self):
        """Returns None if there is no winner yet.  Otherwise,
        returns a string indicating the player who won with each
        player's number of cards, or a tie."""
        if self._player1.isDone() or self._player2.isDone():
            count1 = self._player1.winningsCount()
            count2 = self._player2.winningsCount()
            if count1 > count2:
                return "Player 1 wins, " + str(count1) + " to " +\
                       str(count2) +"!"
            elif count2 > count1:
                return "Player 2 wins, " + str(count2) + " to " +\
                       str(count1) +"!"
            else:
                return "The game ends in a tie!\n"
        else:
            return None

class Player(object):
    """Represents a War game player."""

    def __init__(self):
        """Sets up the player's unplayed and winnings piles."""
        self._unplayedPile = []
        self._winningsPile = []
        pass

    def __str__(self):
        """Returns a description of the player's winnings pile."""
        result = ", ".join(map(str, self._winningsPile))
        return result

    def addToUnplayedPile(self, card):
        """Adds card to the player's unplayed pile."""
        self._unplayedPile.append(card)

    def addToWinningsPile(self, card):
        """Adds card to the player's winnings pile."""
        self._winningsPile.append(card)

    def getCard(self):
        """Removes and returns a card from the player's unplayed pile."""
        return self._unplayedPile.pop(0)
        

    def isDone(self):
        """Returns True if the player's unplayed pile is empty,
        or False otherwise."""
        if len(self._unplayedPile) > 0:
            return False
        return True

    def winningsCount(self):
        """Returns the number of cards in the player's winnings pile."""
        return len(self._winningsPile)
        

        
