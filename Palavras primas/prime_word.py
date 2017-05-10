import re

def isPrime(number):
	div = 0

	for i in range(1, number+1):
		if number %	i == 0 :
			div += 1

	return True if div == 2 else False  

def countWordNumbers(word):
	chars = {}
	minor_a_ascii = 97
	greater_a_ascii = 65
	alphabet_len = 26
	word_numbers_sum = 0

	#preenchendo um dicionário com os números correspondentes a cada letra do alfabeto
	for a in range(minor_a_ascii, minor_a_ascii+alphabet_len):
		chars[chr(a)] = a - (minor_a_ascii - 1)

	for a in range(greater_a_ascii, greater_a_ascii+alphabet_len):
		chars[chr(a)] = a - (greater_a_ascii - (alphabet_len + 1))

	for char in word:
		word_numbers_sum += chars[char]

	return word_numbers_sum

#regex para aceitar apenas A-Z, a-z com tamanho 20
pattern = re.compile('^[a-zA-Z]{1,20}$')

#entrada deve ser escrita em um arquivo txt com o nome entrada.txt na mesma página do script
try:
	file = open('entrada.txt', 'r')
except FileNotFoundError :
	file = open('entrada.txt', 'w+')

lines = file.readlines()
output = open('saida.txt', 'w')

for line in lines:
	if pattern.match(line.strip('\n')) != None and isPrime(countWordNumbers(line.strip('\n'))) :
		print('It is a prime word')
		output.write('It is a prime word\n')

	else :
		print('It is not a prime word')
		output.write('It is not a prime word\n')

file.close()
output.close()
