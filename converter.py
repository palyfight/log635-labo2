import re

class Converter:

	def jessConverter(self, histoireLine):

		regexLine = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(1) + " est " + regexLine.group(2) + ")")

		regexLine = re.match( r'etre\(([NOT,]*),([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			return ("")

		regexLine = re.match(r'temps\((.*?)\) & loc\((.*?)\) & voir\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(4) + " vu " +   regexLine.group(3) + " au " +  regexLine.group(2) + " a " +  regexLine.group(1) + ")")


		regexLine = re.match(r'but\(devenir\((.*?)\)\) & prendre\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(2) + " prend " + regexLine.group(1) + " de " + regexLine.group(1) + ")")


		regexLine = re.match(r'avant_temps\((.*?)\) & loc\((.*?)\) & doit\(etre\((.*?)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(3) + " doit etre a " + regexLine.group(2) + " avant " + regexLine.group(1) + ")")


		regexLine = re.match(r'until\(arrivee\((.*?)\)\) & loc\((.*?)\) & doit\(rester\((.*?)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(3) + " attend " + regexLine.group(1) + " a " + regexLine.group(2) + ")")


		regexLine = re.match(r'voir\(\(with\((.*?)\) & (.*)\),facher\((.*?)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(3) + " facher de voir " +  regexLine.group(1) + " avec "+  regexLine.group(2) + ")")


		regexLine = re.match(r'avant\(quitter\(loc\((.*?)\)\)\) & manger\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(2) + " mange des " +  regexLine.group(3) + " a la " +  regexLine.group(1) + ")")


		regexLine = re.match(r'manger\(([^,]*),([^,]*)\) & (.*)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			return ("(" + regexLine.group(1) + " mange des " +  regexLine.group(2) + " " +  regexLine.group(3) + ")")


		regexLine = re.match(r'jouer\(\(with\(([^,]*)\) & ([^,]*)\),(.*)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			return ("(La " + regexLine.group(3) + " joue au " +  regexLine.group(2) + " avec " +  regexLine.group(1) + ")")

		regexLine = re.match(r'terme\(etre\((.*),\(with\((.*?)\) & loc\((.*?)\)\)\)\) & terme\(doit\(jouer\(\(with\((.*?)\) & (.*)\)\),(.*)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			fisrtFact = "(" + regexLine.group(6) + " doit jouer au " +  regexLine.group(5) + " avec " +  regexLine.group(1) + ")" + "\n\t"
			secondFact = "(" + regexLine.group(4) + " est au " +  regexLine.group(3) + " avec " +  regexLine.group(2) + ")"
			return (fisrtFact + secondFact)
