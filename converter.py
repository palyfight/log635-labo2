import re

class Converter:

	def getSubject(self,subject):
		pronom = ["il", "elle", "on"]
		if (subject in pronom):
			return self.lastSubject
		else:
			self.lastSubject = subject
			return subject

	def jessConverter(self, histoireLine):

	
		lastSubject = ""

		regexLine = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(1))
			return ("(" + lastSubject + " est " + regexLine.group(2) + ")")

		regexLine = re.match( r'etre\(([^,]*),([NOT,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " " + regexLine.group(2) + " " + regexLine.group(1) + ")")

		regexLine = re.match(r'temps\((.*?)\) & loc\((.*?)\) & voir\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " vu " +   regexLine.group(3) + " au " +  regexLine.group(2) + " a " +  regexLine.group(1) + ")")


		regexLine = re.match(r'but\(devenir\((.*?)\)\) & prendre\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(2))
			return ("(" + lastSubject + " prend " + regexLine.group(3) + " de " + regexLine.group(1) + ")")


		regexLine = re.match(r'avant_temps\((.*?)\) & loc\((.*?)\) & doit\(etre\((.*?)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " doit etre a " + regexLine.group(2) + " avant " + regexLine.group(1) + ")")


		regexLine = re.match(r'until\(arrivee\((.*?)\)\) & loc\((.*?)\) & doit\(rester\((.*?)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " attend " + regexLine.group(1) + " a " + regexLine.group(2) + ")")


		regexLine = re.match(r'voir\(\(with\((.*?)\) & (.*)\),facher\((.*?)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " facher de voir " +  regexLine.group(1) + " avec "+  regexLine.group(2) + ")")


		regexLine = re.match(r'avant\(quitter\(loc\((.*?)\)\)\) & manger\(([^,]*),([^,]*)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(2))
			return ("(" + lastSubject + " mange des " +  regexLine.group(3) + " a la " +  regexLine.group(1) + ")")


		regexLine = re.match(r'manger\(([^,]*),([^,]*)\) & (.*)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(1))
			return ("(" + lastSubject + " mange des " +  regexLine.group(2) + " " +  regexLine.group(3) + ")")


		regexLine = re.match(r'jouer\(\(with\(([^,]*)\) & ([^,]*)\),(.*)\)', str(histoireLine), re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(La " + lastSubject + " joue au " +  regexLine.group(2) + " avec " +  regexLine.group(1) + ")")

		regexLine = re.match(r'etre\((.*),\(with\((.*?)\) & loc\((.*?)\)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(1))
			return ("(" + lastSubject + " est au " +  regexLine.group(3) + " avec " +  regexLine.group(2) + ")")

		regexLine = re.match(r'doit\(jouer\(\(with\((.*?)\) & (.*)\)\),(.*)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " doit jouer au " +  regexLine.group(2) + " avec " +  regexLine.group(1) + ")")

		regexLine = re.match(r'marcher\(([^,]*),([^,]*),([^,]*)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(3))
			return ("(" + lastSubject + " marche " + regexLine.group(2) + " " + regexLine.group(1) + ")" )

		regexLine = re.match(r'aime\(([^,]*),prendre\(\(with\(([^,]*)\) & ([^,]*)\)\)\)\)', str(histoireLine)[1:-1], re.M | re.I)
		if regexLine:
			lastSubject = self.getSubject(regexLine.group(1))
			return ("(" + lastSubject + " aime prendre " +  regexLine.group(3) + " avec " +  regexLine.group(2) + ")" )

		return "Regex parsing error"



			
