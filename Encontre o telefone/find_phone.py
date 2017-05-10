import re

def char_to_cellphoneNumbers(inputFileName='entrada.txt', outputFileName='saida.txt'):
	#regex para aceitar apenas A-Z, a-z, 1 , 0 e -
	pattern = re.compile('^[a-zA-Z01-]{1,30}$')

	letter_number_map = {
		"a": "2", "b": "2", "c": "2",
		"d": "3", "e": "3", "f": "3",
		"g": "4", "h": "4", "i": "4",
		"j": "5", "k": "5", "l": "5",
		"m": "6", "n": "6", "o": "6",
		"p": "7", "q": "7", "r": "7",
		"s": "7", "t": "8", "u": "8",
		"v": "8", "w": "9", "x": "9",
		"y": "9", "z": "9",
	}

	#entrada deve ser escrita em um arquivo txt com o nome entrada.txt na mesma página do script
	try:
		file = open(inputFileName, 'r')
	except FileNotFoundError :
		file = open(inputFileName, 'w+')

	lines = file.readlines()

	output = open(outputFileName, 'w')


	for line in lines:
		if pattern.match(line.strip('\n')) != None :
			for char in line :
				output.write(letter_number_map[char.lower()] if char.lower() in letter_number_map else char)

	file.close()
	output.close()

char_to_cellphoneNumbers()
outputs = open('saida.txt', 'r')

for output in outputs.readlines():
	print(output.strip('\n'))

outputs.close()
