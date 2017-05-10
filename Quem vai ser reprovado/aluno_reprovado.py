import re

def loadInstances():
	#entrada deve ser escrita em um arquivo txt com o nome entrada.txt na mesma página do script
	try:
		file = open('entrada.txt', 'r')
	except FileNotFoundError :
		file = open('entrada.txt', 'w+')

	instance_list = []
	lines = file.readlines()
	file.seek(0)

	pattern = re.compile('^[a-z]{1,20}\s([0-9]{1}|10)$')
	first_instance_line_pattern = re.compile('^([0-9]{1,2}|100)$')

	for i in range(0, len(lines)):
		line = file.readline()
		instance = {}
		if first_instance_line_pattern.match(line.strip('\n')) != None:
			for i in range(0, int(line)):
				line = file.readline()
				if pattern.match(line.strip('\n')) != None:
					instance[line.split(' ')[0]] = line.split(' ')[1].strip('\n')

			instance_list.append(instance)

	file.close()
	return instance_list

def write_output(instance, instance_number):
	output = open('saida.txt', 'a')
	minor = 11
	draw_list = []

	for line in instance:
		minor = int(instance[line]) if int(instance[line]) < minor else minor

	for student in instance:
		if int(instance[student]) == minor:
			draw_list.append(student)

	draw_list.sort()
	instance_number_str = str(instance_number)

	output.write("Instancia " + instance_number_str + '\n')
	print("Instancia " + instance_number_str)
	output.write(draw_list[-1] + '\n\n')
	print(draw_list[-1] + '\n')

	output.close()


instance_list = loadInstances()
instance_number = 0

output = open('saida.txt', 'w')
output.close()

for instance in instance_list:
	instance_number += 1
	write_output(instance, instance_number)
