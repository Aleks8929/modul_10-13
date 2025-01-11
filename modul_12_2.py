import runner_and_tournament as rnt
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        people = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {n: rnt.Runner(name=n, speed=s) for n, s in people.items()}

    @classmethod
    def tearDownClass(cls):
        for a, b in cls.all_results.items():
            print(f'{a}: {b}')

    def test_tournament(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_tournament_2(self):
        tour = rnt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_tournament_3(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[3], self.runners['Ник'])

if __name__ == '__main__':
    unittest.main()
