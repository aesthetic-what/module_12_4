import unittest
import logging
import rt_with_exceptions as rt

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            piple1 = rt.Runner("Timur", -5)
            for _ in range(10):
                piple1.walk()
            self.assertEqual(piple1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            piple1 = rt.Runner(12, 9)
            for _ in range(10):
                piple1.run()
            self.assertEqual(piple1.distance, 100)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверный тип данных для Runner", exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()
    logging.shutdown()