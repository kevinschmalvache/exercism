import string
import re

vowels = "aeiou"
ambigiuos = "xyq"
ending = "ay"
def translate(text):
    return " ".join(translate_word(w) for w in text.split(" "))

def translate_word(word):
    if sum([1 for i in word if i not in string.ascii_letters])>0:
        raise ValueError(text+" is invald word")
    else:
        run = True
        while run:
            if word[0] not in vowels:
                if word[0] not in ambigiuos:
                    word = word[1:]+word[0]
                else:
                    for letter in ambigiuos:
                       match = re.search(r""+letter+"["+vowels+"]",word)
                       if match != None:
                           if match.group()=="qu":
                               word = word[2:]+word[:2]
                           else:
                               word = word[1:]+word[0]
                       else:
                           run = False
        
            else:
                run = False
    return word.lower()+ending

if __name__=="__main__":
    print(translate("yellow"))