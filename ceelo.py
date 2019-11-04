'''
File: ceelo.py

Author: Amit

Date: 9/15/19

Program pops up a window that allows the user to roll the dice
and play Cee Lo. If player rolls 4-5-6, player automatically wins.
If player rolls 3 of the same number, point value is that number. If
player rolls 1-2-3, player automatically loses. If player rolls a pair, 
point value is value of the 3rd die.
'''

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from die import Die


class DiceDemo(EasyFrame):

	def __init__(self):
		''' Creates the dice, and sets up the Images and labels for the three dice to 
		be displayed, the state label, and the two command buttons '''
		EasyFrame.__init__(self, title = "Cee Lo Dice", height = 350, width = 550, background = 'medium orchid')
		self.die1 = Die()
		self.die2 = Die()
		self.die3 = Die()
		self.dieLabel1 = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW", background = 'medium orchid')
		self.dieLabel2 = self.addLabel(text = "", row = 0, column = 1, sticky = "NSEW", background = 'medium orchid')
		self.dieLabel3 = self.addLabel(text = "", row = 0, column = 2, sticky = "NSEW", background = 'medium orchid')
		self.stateLabel = self.addLabel(text = "", row = 1, column = 0, sticky = "NSEW", columnspan = 2, background = 'medium orchid', font = ('Verdana', 14, 'bold'))
		
		self.value = self.addLabel(text = "Point Value", row = 2, column = 0, sticky = "NSEW", background = 'medium orchid')
		self.number = self.addIntegerField(value = 0, row = 2, column = 1)
		self.total = self.addLabel(text = "Total Points", row = 2, column = 2, sticky = "NSEW", background = 'medium orchid')
		self.total2 = self.addIntegerField(value = 0, row = 2, column = 3)
		
		self.button = self.addButton(text = "Roll", row = 3, column = 0, columnspan = 2, command = self.nextRoll)
		self.button2 = self.addButton(text = "New Game", row = 3, column = 2, columnspan = 2, command = self.newGame)
		self.addLabel(text = "", row = 4, column = 1, columnspan = 3, background = 'medium orchid')

		self.button["background"] = 'green yellow'
		self.button["font"] = "Arial+Bold"
		self.button2["background"] = 'green yellow'
		self.button2["font"] = "Arial+Bold"

		self.refreshImages()

	def nextRoll(self):
		''' Rolls the dice and updates the view with the results '''
		a = self.die1
		b = self.die2
		c = self.die3

		values = []
		
		a.roll()
		b.roll()
		c.roll()

		#total = self.die1.getValue() + self.die2.getValue() + self.die3.getValue()
		#self.stateLabel["text"] = "Total = " + str(total)
		val1 = a.getValue()
		val2 = b.getValue()
		val3 = c.getValue()

		values.append(val1)
		values.append(val2)
		values.append(val3)
	
		points = 0

		if 4 in values:
			if 5 in values:
				if 6 in values:
					self.result = self.addLabel(text = "You WIN!", row = 4, column = 1, columnspan = 3, background = 'red')
		elif 1 in values:
			if 2 in values:
				if 3 in values:
					self.result = self.addLabel(text = "You LOSE!", row = 4, column = 1, columnspan = 3, background = 'red')	
		elif val1 == val2 == val3:
			self.number.setValue(val1)
			self.total2.getValue()
			points += val1
			self.total2.setValue(points)
			self.result = self.addLabel(text = "You rolled Trips!", row = 4, column = 1, columnspan = 3, background = 'red')				
		elif val1 == val2 == val3 == 6:
			self.result = self.addLabel(text = "You Lose!", row = 4, column = 1, columnspan = 3, background = 'red')
		elif val1 == val2:
			self.number.setValue(val3)
			self.total2.getValue()
			points += val3
			self.total2.setValue(points)
			self.result = self.addLabel(text = "Roll again ", row = 4, column = 1, columnspan = 3, background = 'red')
		elif val2 == val3:
			self.number.setValue(val1)
			self.total2.getValue()
			points += val1
			self.total2.setValue(points)
			self.result = self.addLabel(text = " Roll Again", row = 4, column = 1, columnspan = 3, background = 'red')
		elif val1 == val3:
			self.number.setValue(val2)
			self.total2.getValue()
			points += val2
			self.total2.setValue(points)
			self.result = self.addLabel(text = "Roll Again ", row = 4, column = 1, columnspan = 3, background = 'red')
		else:
			self.result = self.addLabel(text = " ", row = 4, column = 1, columnspan = 3, background = 'red')

		self.refreshImages()

	def newGame(self):
		''' Create new dice and updates the view '''
		self.die1 = Die()
		self.die2 = Die()
		self.die3 = Die()
		self.stateLabel["text"] = ""
		self.refreshImages()

	def refreshImages(self):
		''' Updates the images in the window '''
		fileName1 = "dice" + str(self.die1) + ".gif"
		fileName2 = "dice" + str(self.die2) + ".gif"
		fileName3 = "dice" + str(self.die3) + ".gif"
		self.image1 = PhotoImage(file = fileName1)
		self.dieLabel1["image"] = self.image1
		self.image2 = PhotoImage(file = fileName2)
		self.dieLabel2["image"] = self.image2
		self.image3 = PhotoImage(file = fileName3)
		self.dieLabel3["image"] = self.image3


def main():
	''' Instantiates and pops up the window '''
	DiceDemo().mainloop()

main()
