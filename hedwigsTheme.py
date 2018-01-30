#hedwigsTheme.py
#
# Author:     Jasmine Mai
# Email:      maijd@g.cofc.edu
# Class:      CSCI 180:01
# Assignment: Homework #1
# Due Date:   26 January 2018
#
# Purpose: To play the melody of Hedwig's Theme using Python.
#
# https://www.youtube.com/watch?v=d4Ndy1qMTAM - I wrote down the music notes and 
# deciphered each note duration.
#
# Input:   None.
#
# Output:  The melody, Hedwig's Theme, played by the computer.

from music import *

#The collection of various pitches and durations contained within the theme
pitch1    = [B5, E6, G6, FS6, E6, B6, A6, FS6]
duration1 = [HN, HN, QN, QN,  HN, HN, HN, HN]
pitch2    = [E6, G6, FS6, D6, F6, B5]
duration2 = [HN, QN, QN,  HN, HN, HN]
pitch3    = [B5, E6, G6, FS6, E6, B6, D7, CS7, C7]
duration3 = [HN, HN, QN, QN,  HN, HN, HN, HN, WN]
pitch4    = [GS5, C6, B6, AS6, AS5, G5, E5]
duration4 = [QN,  QN, QN, QN,  HN,  QN, WN]
pitch5    = [REST, G6, B6, G6, B6]
duration5 = [EN,   QN, HN, QN, HN]
pitch6    = [G6, C7, B6, BF6, FS6, G6, AS5, B5, B6]
duration6 = [QN, HN, QN, QN,  QN,  HN, HN,  QN, WN]
pitch7    = [G6, D6, CS6, C6, GS5, C6, B6, AS6, AS5, G5, E5]
duration7 = [QN, HN, QN,  HN, QN,  HN, QN, HN,  HN,  HN, WN]

#The phrase that is contained within the theme
theme = Phrase()
theme.addNoteList(pitch1, duration1)
theme.addNoteList(pitch2, duration2)
theme.addNoteList(pitch3, duration3)
theme.addNoteList(pitch4, duration4)
theme.addNoteList(pitch5, duration5)
theme.addNoteList(pitch6, duration6)
theme.addNoteList(pitch5, duration5)
theme.addNoteList(pitch7, duration7)

#Setting the tempo and the different instrument instead of the default
theme.setTempo(160)
theme.setInstrument(PICCOLO)

#Let's play!
Play.midi(theme)
