from clint.textui import colored
import brands as br
import enableMultilib as eM
import programs as pr
import os, sys
def disElec(situation):
	while True:
		try:
			print(colored.green("\n[1] Ubuntu / Linux Mint / Any Ubuntu-based distro\n[2] Arch / Manjaro / Any arch derivatives\n[3] Debian / Antix / Any full Debian-based distro\n[4] Go back"))
			distro = int(input("Select an option -> "))
			
			# Ubuntu / Ubuntu-based installer
			
			if distro == 1:
				if situation == "drivers":
					br.brandSelUbuntu()
				elif situation == "programs":
					print(colored.green("\n[1] WINE (Essential)\n[2] Lutris\n[3] GOverlay with MangoHUD\n[4] Steam\n[5] Back"))
					prgm = int(input("Select an option -> "))
					if prgm == 1:
						pr.WINE("ubuntu")
					elif prgm == 2:
						pr.Lutris("ubuntu")
					elif prgm == 3:
						pr.GOverlwMango("ubuntu")
					elif prgm == 4:
						pr.Steam("ubuntu")
					elif prgm == 5:
						break
			
			# Arch / Arch derivatives installer
			
			elif distro == 2:
				if situation == "drivers":
					print(colored.red('''
						The script will edit the /etc/pacman.conf file, for enable multilib, you can know more about multlib here:
						https://www.linuxsecrets.com/archlinux-wiki/wiki.archlinux.org/index.php/Multilib.html

						'''))
					op = input("Do you want to continue? [Y/N] -> ")
					if op == 'Y' or op == 'y':
						eM.pacmanConf("drivers")
				elif situation == "programs":
					print(colored.green("\n[1] WINE (Essential)\n[2] Lutris\n[3] GOverlay with MangoHUD\n[4] Steam\n[5] Back"))
					prgm = int(input("Select an option -> "))
					if prgm == 1:
						eM.pacmanConf("program")
						pr.WINE("arch")
					elif prgm == 2:
						pr.Lutris("arch")
					elif prgm == 3:
						pr.GOverlwMango("arch")
					elif prgm == 4:
						pr.Steam("arch")
					elif prgm == 5:
						break

			# Debian / full-debian based installer

			elif distro == 3:
				if situation == "drivers":
					print(colored.red("FIXME: Add drivers installer for Debian"))

				elif situation == "programs":
					print(colored.green("\n[1] WINE (Essential)\n[2] Lutris\n[3] GOverlay with MangoHUD\n[4] Steam\n[5] Back"))
					prgm = int(input("Select an option -> "))
					if prgm == 1:
						pr.WINE("debian")
					elif prgm == 2:
						pr.Lutris("lutris")
					elif prgm == 3:
						pr.GOverlwMango("debian")
					elif prgm == 4:
						pr.Steam("ubuntu")
					elif prgm == 5:
						break
					
			elif distro == 4:
				break
			else:
				print("Wrong option, you must choose one number")
		except PermissionError:
			print(colored.red("Run the script as root, using: sudo GamingSetup.py"))
			sys.exit(1)
		except ValueError:
			print(colored.red("Invalid entered value"))