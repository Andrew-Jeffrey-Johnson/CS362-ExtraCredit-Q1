import unittest
import question1

class testQ1(unittest.TestCase):
	# Successful test
	def test_add(self):
		self.assertEqual(question1.reverseSentence("Hello, World"), "World Hello,")

	if __name__ == '__main__':
		unittest.main()
