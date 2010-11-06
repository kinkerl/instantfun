#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python-pygame
import pygame.mixer as mixer
import appindicator
import gtk
import gobject
import os

def play(widget = None):
	filename = os.environ["HOME"] +'/.instantfun/' + widget.get_children()[0].get_label() + '.mp3'
	mixer.init(44100)
	mixer.music.load(filename)
	mixer.music.play()


menu = gtk.Menu()


for filename in os.listdir(os.environ["HOME"] +'/.instantfun/'):
	filename = filename[:-4]
	menuItemStatus = gtk.MenuItem(filename)
	menuItemStatus.set_sensitive(True)
	menuItemStatus.connect('activate',play)
	menuItemStatus.show()
	menu.append(menuItemStatus)

indicator = appindicator.Indicator ("instantfun", 'instantfun', appindicator.CATEGORY_APPLICATION_STATUS)
indicator.set_status (appindicator.STATUS_ACTIVE)
indicator.set_menu(menu)

gtk.main()
