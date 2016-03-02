import re

class Converter:

	def jessConverter(self, histoireLine):

		line = "(temps(16h) & loc(magasin) & voir(philippe,christian))"

		matchObj = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if matchObj:
			print ("(" + matchObj.group(1) + " est un " + matchObj.group(2) + ")")

		matchObj = re.match( r'etre\(([NOT,]*),([^,]*),([^,]*)\)', str(histoireLine), re.M | re.I)
		if matchObj:
			print ("")

		matchObj = re.match(r'temps\((.*?)\) & loc\((.*?)\) & voir\(([^,]*),([^,]*)\)', line[1:], re.M | re.I)
		if matchObj:
			print ("(" + matchObj.group(4) + " vu " +   matchObj.group(3) + " au " +  matchObj.group(2) + " a " +  matchObj.group(1)+ ")")
		else:
			print ("gg")
