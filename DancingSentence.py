import string

class DancingSentence:
	"""Division 1, Level One
	   Steven Schmatz"""
	def makeDancing(self, sentence):
		letter_list = list(sentence)
		i = 0
		oddCount = 0
		while i < len(letter_list):
			if letter_list[i] != " ":
				if oddCount % 2 == 0:
					letter_list[i] = letter_list[i].upper()
				oddCount += 1
			i += 1
		return ''.join(letter_list)

"""
Test Cases
----------

myClass = DancingSentence()
test_string = "hello world"
print myClass.makeDancing(test_string)"""