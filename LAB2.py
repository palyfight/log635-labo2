# -*- coding: utf-8 -*-
import codecs
import nltk
from nltk import *
from converter import Converter
from jessWriter import JessWriter

with codecs.open("histoire.txt","r", encoding='UTF-8') as histoire:
	histoireText = histoire.read().replace('\n', '').replace(',', '').replace('\'', ' ').lower().split('.')

with codecs.open ("grammar.cfg", "r", encoding='UTF-8') as grammaire:
    grammaireText=grammaire.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = parse.FeatureEarleyChartParser(grammar)

converter = Converter()
jessWriter = JessWriter()
fileContent = ""

for phrase in histoireText:
	
	tokens = phrase.split()
	trees = parser.parse(tokens)
	
	for tree in trees:
	    print(tree)
	    fileContent += "\t" + converter.jessConverter(tree.label()['SEM']) + "\n"
	    #nltk.draw.tree.draw_trees(tree)
	    print(tree.label()['SEM'])

	jessWriter.writeFile(fileContent)