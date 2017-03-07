import sys
import string
from collections import namedtuple


def main():

    #if sys.argv[1] == "-createLexic":
    if 0 == 0:
        print "Creating lexic..."

        CreateLexic()


        print "The Lexic have been created successfully and stored in lexic.txt"
    else:
        print "Invalid argument. Please execute the command: 'python main.py -createLexic' to create the file lexic.txt"

    #if sys.argv[1] == "-test":
    if 0 == 0:
        print "Creating test..."

        Test()

        print "The test have been created successfully and stored in o1.txt"
    else:
        print "Invalid argument. Please execute the command: 'python main.py -test' to create the file o1.txt"


def CreateLexic():

    corpus = open("corpus.txt","r")
    lexid = {}
    lexic = open("lexic.txt", "w")



    for linec in corpus:
        linec = linec.decode("latin_1").encode("UTF-8")

        linec = linec.replace("\r\n","")
        linec = linec.replace('\n', '')
        wordsc = linec.split("\t")
        #print words
        wordsc[0] = wordsc[0].lower()
        if wordsc[0] in lexid:
            if wordsc[1] in lexid[wordsc[0]]:
                lexid[wordsc[0]][wordsc[1]] += 1
            else:
                lexid[wordsc[0]] = {wordsc[1]: 1}
        else:
            lexid[wordsc[0]] = {wordsc[1]: 1}

    #print lexid
    lexid
    for key1 in lexid:
        for key2 in lexid[key1]:
            lexic.write(key1 + "\t" + key2 + "\t" + str(lexid[key1][key2]) + "\n")

    for key1 in lexid:
        palabra = key1
        valor = 0

        for key2 in lexid[key1]:
            if valor < lexid[key1][key2]: # nomes escric els valors mes alts
                palabra = key2

            #lexic.write(key1 + "\t" + key2 + "\t" + str(lexid[key1][key2]) + "\n")

        lexic.write(key1 + "\t" + palabra + "\t" + str(valor) + "\n")


    lexic.close()
def Test():
    test1 = open("test_1.txt", "r")
    test2 = open("test_2.txt", "r")
    o1 = open("o1.txt", "w")
    o2 = open("o2.txt", "w")
    #lexic = open("lexic.txt", "r")
    count = 0
    for linet in test1:
        found = False
        lexic = open("lexic.txt", "r")
        count += 1
        linet = linet.decode("latin_1").encode("UTF-8")

        linet = linet.replace("\r\n", "")
        linet = linet.replace('\n', '')
        wordst = linet.split("\t")
        wordst[0] = wordst[0].lower()
        #print wordst
        for linel in lexic and not found: #hace falta if con booleano por si no la encuentra poner algo rabdom
            linel = linel.decode("latin_1").encode("UTF-8")

            linel = linel.replace("\r\n", "")
            linel = linel.replace('\n', '')
            wordsl = linel.split("\t")
            wordsl[0] = wordsl[0].lower()
            #if count > 1:
            #    print wordst[0]
            #    print wordsl[0]
            if wordst[0] == wordsl[0]:
                o1.write(wordst[0] + "\t" + wordsl[1] + "\n")
                found = True
        lexic.close()





if __name__ == "__main__":
    main()