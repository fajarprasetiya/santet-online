## misc.py - Useful module of Santet-Online
# -*- coding: utf-8 -*-
##
import os
import sys

__banner__ = """
\033[1;37m          ,       
\033[1;37m      _,-""-._    
\033[1;37m    ,'        '.  
\033[1;37m   / \033[1;31m   ,-,  ,-\033[1;37m \ \033[0m
\033[1;37m  |  \033[1;31m  /   \ | o| \033[0m
\033[1;37m  \  \033[1;31m  `-o-'  `-'                     ( )_        ( )_ 
\033[1;37m   `,   _.--'`'--`\033[1;31m  ___    _ _   ___  | ,_)   __  | ,_)
\033[1;37m     `--`---'  \033[1;31m   /',__) /'_` )/' _ `\| |   /'__`\| |  
\033[1;37m       ,' '    \033[1;31m   \__, \( (_| || ( ) || |_ (  ___/| |_ 
\033[1;37m     ./ ,  `,  \033[1;31m   (____/`\__,_)(_) (_)`\__)`\____)`\__)
\033[1;37m     / /     \  \033[1;37m       Made with \033[1;31m<3\033[0m\033[1;37m by BlackHoleSec\033[0m
\033[1;37m    (_)))_ _," \033[0m
\033[1;37m        ||||       DedSecTL - DjoSec12 - Mr.4NDR00T-DC\033[0m
\033[1;37m       _||||_,    MrTenSwapper07 - Deathdies - ./d3r4y\033[0m
\033[1;37m------(_,-._)))-----------------------------------------\033[0m
"""
backtomenu_banner = """
  99) Return back to main menu
  00) Exit the Santet-Online
"""
netcatrat_menubanner = """
  01) Generate Payload
  02) Start a Listener
"""

def netcatrat_menu():
	print netcatrat_menubanner

def logo():
	print __banner__

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print backtomenu_banner
	backtomenu = raw_input("santet > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print "\nERROR: Wrong input"
		time.sleep(2)
		restart_program()