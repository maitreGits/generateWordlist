#!/usr/bin/env python
# Run the program and follow the instructions, 
import sys

specialChars = ["@","\"","\'", "(",")","$","*","&","?","_","-","!"]
years = []
wordlist =[]

def main() :
    years = generateYears()
    words = raw_input("Give me words in order to create wordlist (separate with space):")
    words = words.split(" ")
    for word in words :    
        words.index(word)
        #On ajoute le mot simple
        wordlist.append(word)
        #  + annee
        addThings(years,wordlist,word)
        #On ajoute le mot simple avec la premiere lettre en majuscule
        wordlist.append(word.title())
        addThings(years,wordlist,word.title())
        #juxtaposer les autres mots rentres
        for word2 in words :
            if words.index(word2) != words.index(word) :
                manageWord(years,wordlist,word+word2)
                manageWord(years,wordlist,word.title()+word2.title())
                manageWord(years,wordlist,word.title()+word2)
                manageWord(years,wordlist,word+word2.title())
                
    for word in wordlist :
        print word
        

def manageWord(years,wl,word) :
    wordlist.append(word)
    addThings(years,wl,word)

# ajouter annee, charactere speciaux etc ...
def addThings(years, wl,word) :
    for year in years :
        wl.append(word+str(year))
        wl.append(str(year)+word)
    for sc in specialChars :
        wl.append(sc+word)
        wl.append(word+sc)
    for year in years :
        for sc in specialChars:
            wl.append(word+str(year)+sc)
            wl.append(word+sc+str(year))
            wl.append(str(year)+word+sc)
            wl.append(str(year)+sc+word)
            wl.append(sc+str(year)+word)
            wl.append(sc+str(year)+word)
        

def generateYears():
    res = []
    for i in range (1955,2031) :
        res.append(i)
    return res

if __name__ == "__main__" :
    main()