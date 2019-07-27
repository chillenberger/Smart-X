import random
import string

#library used to make qr code
import pyqrcode


#
# def codeCreator():
#     # code39 table
#     #should have used a dictonary, change this in the future
#     zero	=	"101001101101"	;	B	=	"101101001011"	;	M	=	"110110101001"	;	X	    =	"100101101011"
#     one	    =	"110100101011"	;	C	=	"110110100101"	;	N	=	"101011010011"	;	Y	    =	"110010110101"
#     two	    =	"101100101011"	;	D	=	"101011001011"	;	O	=	"110101101001"	;	Z	    =	"100110110101"
#     three	=	"110110010101"	;	E	=	"110101100101"	;	P	=	"101101101001"	;	dash	=	"100101011011"
#     four	=	"101001101011"	;	F	=	"101101100101"	;	Q	=	"101010110011"	;	dot	    =	"110010101101"
#     five	=	"110100110101"	;	G	=	"101010011011"	;	R	=	"110101011001"	;	space	=	"100110101101"
#     six	    =	"101100110101"	;	H	=	"110101001101"	;	S	=	"101101011001"	;	dollor	=	"100100100101"
#     seven	=	"101001011011"	;	I	=	"101101001101"	;	T	=	"101011011001"	;	fslash	=	"100100101001"
#     eight	=	"110100101101"	;	J	=	"101011001101"	;	U	=	"110010101011"	;	plus	=	"100101001001"
#     nine	=	"101100101101"	;	K	=	"110101010011"	;	V	=	"100110101011"	;	percent	=	"101001001001"
#     A	    =	"110101001011"	;	L	=	"101101010011"	;	W	=	"110011010101"	;	star	=	"100101101101"
#
#     numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
#     letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#
#     #star is opening variable for code39
#     newCode = star
#     readableCode = ''
#     pinCode = ''
#
#     for x in range(2):
#         item = random.choice(letters)
#         readableCode = readableCode + item
#         newCode = newCode + eval(item)
#
#     newCode = newCode + dash
#     readableCode = readableCode + "-"
#
#     for x in range(4):
#         item = random.choice(numbers)
#         readableCode = readableCode + convertNumber(item)
#         newCode = newCode + eval(item)
#
#     for x in range(4):
#         pinCode = pinCode + str(random.choice(range(10)))
#
#     #star is closing character for code39
#     newCode = newCode + star
#     print(readableCode)
#
#     #translate binary into dash unicode
#     barCode = code39Translator(newCode)
#     print(barCode)
#
#     #put values in dictionary for easy return
#     fullCode = {'barCode':barCode, 'readableCode':readableCode, 'pinCode':pinCode}
#     return(fullCode)
#
#
#
#
# def code39Translator(newCode):
#     translatedCode = ""
#
#     print("new code length = " + str(len(newCode)))
#
#     for x in range(0,len(newCode),2):
#         if newCode[x] == '1':
#             if newCode[x+1] == '1':
#                 translatedCode = translatedCode + "\u2588"
#             else:
#                 translatedCode = translatedCode + "\u258c"
#         else:
#             if newCode[x+1] == '1':
#                 translatedCode = translatedCode + "\u2590"
#             else:
#                 translatedCode = translatedCode + "\u2591"
#
#
#     print("translateCode length = " + str(len(translatedCode)))
#     return(translatedCode)
#
#
# def convertNumber(number):
#     if number == "zero":
#         return("0")
#     if number == "one":
#         return("1")
#     if number == "two":
#         return("2")
#     if number == "three":
#         return("3")
#     if number == "four":
#         return("4")
#     if number == "five":
#         return("5")
#     if number == "six":
#         return("6")
#     if number == "seven":
#         return("7")
#     if number == "eight":
#         return("8")
#     else:
#         return("9")


class codeCreator():
    def __init__(self):
        self.codeItems = {
            '0'	:	"101001101101"	,	'B'	:	"101101001011"	,	'M'	:	"110110101001"	,	'X'	:	"100101101011" ,
            '1'	:	"110100101011"	,	'C'	:	"110110100101"	,	'N'	:	"101011010011"	,	'Y'	:	"110010110101" ,
            '2'	:	"101100101011"	,	'D'	:	"101011001011"	,	'O'	:	"110101101001"	,	'Z'	:	"100110110101" ,
            '3'	:	"110110010101"	,	'E'	:	"110101100101"	,	'P'	:	"101101101001"	,	'-'	:	"100101011011" ,
            '4'	:	"101001101011"	,	'F'	:	"101101100101"	,	'Q'	:	"101010110011"	,	'.'	:	"110010101101" ,
            '5'	:	"110100110101"	,	'G'	:	"101010011011"	,	'R'	:	"110101011001"	,	' '	:	"100110101101" ,
            '6'	:	"101100110101"	,	'H'	:	"110101001101"	,	'S'	:	"101101011001"	,	'$'	:	"100100100101" ,
            '7'	:	"101001011011"	,	'I'	:	"101101001101"	,	'T'	:	"101011011001"	,	'/'	:	"100100101001" ,
            '8'	:	"110100101101"	,	'J'	:	"101011001101"	,	'U'	:	"110010101011"	,	'+'	:	"100101001001" ,
            '9'	:	"101100101101"	,	'K'	:	"110101010011"	,	'V'	:	"100110101011"	,	'%'	:	"101001001001" ,
            'A'	:	"110101001011"	,	'L'	:	"101101010011"	,	'W'	:	"110011010101"	,	'*'	:	"100101101101" ,}
        code = self.barCode()
        self.barCode = code['unicode']
        self.readableCode = code['readable']
        self.pinCode = self.pinCode()


    def barCode(self):
        letters = {'unicode':'', 'readable':''}
        numbers = {'unicode':'', 'readable':''}
        code    = {'unicode':'', 'readable':''}

        for x in range(2):
            y = random.choice(string.ascii_uppercase)
            letters['readable'] = letters['readable'] + y
            letters['unicode'] = letters['unicode'] + self.codeItems[y]

        for x in range(4):
            y = str(random.randint(0,9))
            numbers['readable'] = numbers['readable'] + y
            numbers['unicode'] = numbers['unicode'] + self.codeItems[y]

        code['unicode'] = self.code39Translator(self.codeItems['*'] + \
            letters['unicode'] + self.codeItems['-'] + numbers['unicode'] + \
            self.codeItems['*'])

        code['readable'] = letters['readable'] + '-' + numbers['readable']
        return(code)


    def pinCode(self):
        pinCode = ''
        for x in range(4):
            pinCode = pinCode + str(random.choice(range(10)))
        return(pinCode)


    def code39Translator(self, newCode):
        translatedCode = ""

        for x in range(0,len(newCode),2):
            if newCode[x] == '1':
                if newCode[x+1] == '1':
                    translatedCode = translatedCode + "\u2588"
                else:
                    translatedCode = translatedCode + "\u258c"
            else:
                if newCode[x+1] == '1':
                    translatedCode = translatedCode + "\u2590"
                else:
                    translatedCode = translatedCode + "\u2591"

        return(translatedCode)



def codGenerator(letters, numbers):
    code = ''
    for x in range(letters):
        code = code + random.choice(string.ascii_uppercase)

    code = code + '-'

    for x in range(numbers):
        code = code + str(random.choice(range(10)))

    return(code)
