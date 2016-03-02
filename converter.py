import re

class Converter:

	def jessConverter(self, histoireLine):

		matchObj = re.match( r'etre\(([^,]*),([^,]*)\)', str(histoireLine), re.M|re.I)
		if matchObj:
		  return ("(" + matchObj.group(1) + " est un " + matchObj.group(2) + ")")

		matchObj = re.match( r'etre\(([NOT,]*),([^,]*),([^,]*)\)', str(histoireLine), re.M|re.I)
		if matchObj:
		  return ""

		matchObj = re.match( r'etre\(([NOT,]*),([^,]*),([^,]*)\)', str(histoireLine), re.M|re.I)
		if matchObj:
		  return ""