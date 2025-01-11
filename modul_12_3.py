import unittest
import suite_12_3


my_test = unittest.TestSuite()

my_test.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))
my_test.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(my_test)