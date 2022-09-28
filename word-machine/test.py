import unittest
from word_machine import WordMachine

word_machine = WordMachine()
class WordMachineTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(word_machine.get_result('3'),[3])
        self.assertEqual(word_machine.get_result('3 3 2'),[3,3,2])

    def test_sum(self):
        self.assertEqual(word_machine.get_result('2 2 +'),[4])
        self.assertEqual(word_machine.get_result('2 -2 +'),[0])
        self.assertEqual(word_machine.get_result('-3 -2 +'),[-5])

    def test_sub(self):
        self.assertEqual(word_machine.get_result('3 2 -'),[1])
        self.assertEqual(word_machine.get_result('3 3 -'),[0])
        self.assertEqual(word_machine.get_result('3 5 -'),[-2])
        self.assertEqual(word_machine.get_result('3 -5 -'),[8])
    
    def test_dup(self):
        self.assertEqual(word_machine.get_result('3 DUP'),[3,3])
        self.assertEqual(word_machine.get_result("2 3 4 DUP"),[2,3,4,4])
    
    def test_pop(self):
        self.assertEqual(word_machine.get_result("3 POP"),[])
        self.assertEqual(word_machine.get_result("3 POP 4 3 POP"),[4]) 
    
if __name__ == '__main__':
    unittest.main()
