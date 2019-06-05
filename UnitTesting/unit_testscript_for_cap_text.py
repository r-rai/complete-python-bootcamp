'''
function for unit testind cap_text() function
'''

import unittest
import cap_text

class TestCap(unittest.TestCase):

	#test case to test only one world
	def test_one_word(self):
		text = "python"
		result = cap_text.cap_text(text)
		self.assertEqual(result,"Python")
	
	#test case to test multiple word	
	def test_multiple_word(self):
		text = "mera wala word"
		result = cap_text.cap_text(text)
		self.assertEqual(result,"Mera Wala Word")
		
if __name__ == "__main__":
	unittest.main()
	