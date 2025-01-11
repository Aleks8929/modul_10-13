import unittest
import inspect
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = Runner('Таня')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = Runner('Коля')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker2 = Runner('Катя')
        run2 = Runner('Олег')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        people = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {n: rnt.Runner(name=n, speed=s) for n, s in people.items()}

    @classmethod
    def tearDownClass(cls):
        for a, b in cls.all_results.items():
            print(f'{a}: {b}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tour = rnt.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tour = rnt.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[3], self.runners['Ник'])


if __name__ == '__main__':
    unittest.main()
