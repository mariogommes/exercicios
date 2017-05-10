import unittest
import find_phone

class Find_Phone_Tests(unittest.TestCase):
	
	def test_char_to_cellphoneNumbers(self):
		inputFileName = 'entradaTeste.txt'
		outputFileName = 'saidaTeste.txt'

		file = open(inputFileName, 'w+')

		file.write('1-home-sweet-home')
		file.seek(0)

		find_phone.char_to_cellphoneNumbers(inputFileName, outputFileName)
		output = open(outputFileName, 'r')
		outputStr = output.readline()

		file.close()
		output.close()

		self.assertEqual(outputStr, '1-4663-79338-4663')

if __name__ == '__main__':
    unittest.main()