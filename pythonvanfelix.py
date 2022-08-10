import pandas as pd
abc = pd.read_csv("Pokemon.csv")

def zoekPokemon(zoekterm):
	for voortuin in abc["Name"]:
		#print(voortuin)
		if zoekterm == voortuin:
			return True
	return False

zpok = input("Welke pokemon zoek je? ")

if zoekPokemon(zpok):
	print("yes")
else:
	print("No")
