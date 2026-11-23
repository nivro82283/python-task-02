"""Behavioral tests for all eleven required exercises."""
import datetime
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def load_module(filename):
    """Load exercise files whose required names contain dots and digits."""
    spec = importlib.util.spec_from_file_location(
        filename.replace('.', '_'), ROOT / 'src' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Task02Tests(unittest.TestCase):
    """Check examples, boundary cases and externally observable behavior."""

    def test_directory_filter(self):
        """Include only matching files, without descending into directories."""
        module = load_module('5.1.thats_the_way.py')
        with tempfile.TemporaryDirectory() as folder:
            for name in ['deep.txt', 'deeper.svg', 'Deep.txt', 'other.txt']:
                (Path(folder) / name).touch()
            (Path(folder) / 'deep_folder').mkdir()
            self.assertEqual(set(module.thats_the_way(folder)), {'deep.txt', 'deeper.svg'})

    def test_date_endpoints(self):
        """The inclusive range can return both endpoints, including leap day."""
        module = load_module('5.1.no_vinnigret.py')
        for offset, expected in [(0, '2024-02-28'), (2, '2024-03-01')]:
            with patch.object(module.random, 'randint', return_value=offset):
                result = module.no_vinnigret('2024-02-28', '2024-03-01')
                self.assertEqual(result, datetime.date.fromisoformat(expected))
        self.assertEqual(module.no_vinnigret('2024-02-29', '2024-02-29'),
                         datetime.date(2024, 2, 29))

    def test_invalid_dates(self):
        """Reject impossible dates and reversed intervals."""
        module = load_module('5.1.no_vinnigret.py')
        for start, end in [('2026-02-30', '2026-03-01'), ('2026-03-02', '2026-03-01')]:
            with self.assertRaises(ValueError):
                module.no_vinnigret(start, end)

    def test_monday_message(self):
        """Print the required message for Monday."""
        module = load_module('5.1.no_vinnigret.py')
        with patch('builtins.input', side_effect=['2026-11-16'] * 2):
            with patch('builtins.print') as printer:
                module.main()
        printer.assert_any_call('אין לי ויניגרט!')

    def test_join_examples(self):
        """Check custom/default separators, one list and no lists."""
        module = load_module('5.2.cup_of_join.py')
        self.assertEqual(module.join([1, 2], [8], [9, 5, 6], sep='@'),
                         [1, 2, '@', 8, '@', 9, 5, 6])
        self.assertEqual(module.join([1], [2]), [1, '-', 2])
        self.assertEqual(module.join([1]), [1])
        self.assertIsNone(module.join())

    def test_join_empty_lists_and_mutation(self):
        """Keep separators around empty lists, and leave input lists unchanged."""
        module = load_module('5.2.cup_of_join.py')
        values = [1]
        separator = ['x']
        self.assertEqual(module.join([], values, [], sep=separator),
                         [separator, 1, separator])
        self.assertEqual(values, [1])

    def test_recipe_examples(self):
        """Calculate weighted prices and omit optional ingredients."""
        module = load_module('5.2.piece_of_cake.py')
        prices = {'chocolate': 18, 'milk': 8}
        self.assertEqual(module.get_recipe_price(prices, chocolate=200, milk=100), 44)
        self.assertEqual(module.get_recipe_price(
            prices, optionals=['milk'], chocolate=300), 54)
        self.assertEqual(module.get_recipe_price({}), 0)
        self.assertEqual(module.get_recipe_price({'flour': 3}, flour=50), 1.5)

    def test_binary_messages(self):
        """Handle short runs, invalid bytes, adjacent messages and missing !."""
        module = load_module('5.3.parsle_tongue.py')
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / 'messages.bin'
            file.write_bytes(b'\xffabcd!abcde!hello!\x00UPPER!world!unfinished')
            self.assertEqual(list(module.parsle_tongue(file)),
                             ['abcde!', 'hello!', 'world!'])

    def test_interleaving(self):
        """Both implementations match the notebook example."""
        module = load_module('5.4.interleaves.py')
        expected = ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
        self.assertEqual(module.interleave('abc', [1, 2, 3], ('!', '@', '#')), expected)
        self.assertEqual(list(module.generator_interleaves(
            iter('abc'), iter([1, 2, 3]), iter(('!', '@', '#')))), expected)
        self.assertEqual(module.interleaves('ab', [1]), ['a', 1])
        self.assertEqual(module.interleaves(), [])
        self.assertEqual(module.interleaves([], [1]), [])

    def test_generator_is_lazy(self):
        """No input values are consumed until iteration starts."""
        module = load_module('5.4.interleaves.py')
        values = iter([1, 2])
        result = module.generator_interleaves(values)
        self.assertEqual(next(values), 1)
        self.assertEqual(list(result), [2])

    def test_timer(self):
        """Forward positional and keyword arguments once and measure elapsed time."""
        module = load_module('6.2.running_2000.py')
        function = Mock(return_value=12)
        with patch.object(module.time, 'perf_counter', side_effect=[10.0, 10.25]):
            elapsed = module.timer(function, 3, name='Bug')
        self.assertEqual(elapsed, 0.25)
        function.assert_called_once_with(3, name='Bug')

    def test_timer_propagates_exception(self):
        """The timer must not conceal errors from the supplied callable."""
        module = load_module('6.2.running_2000.py')
        with self.assertRaises(ValueError):
            module.timer(Mock(side_effect=ValueError('failure')))

    def test_word_lengths(self):
        """Normalize repeated words and remove punctuation/digits."""
        module = load_module('6.3.long_cat_is_long.py')
        self.assertEqual(module.count_words('Cat, CAT! long\ncat. 123'),
                         {'cat': 3, 'long': 4})
        self.assertEqual(module.count_words('... 123'), {})
        self.assertEqual(module.count_words("can't"), {'cant': 4})

    def test_pixel_message(self):
        """Decode a small independently encoded grayscale image."""
        module = load_module('6.4.remember_remember.py')
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'encoded.png'
            image = Image.new('L', (3, 256), 255)
            for column, char in enumerate('Hi!'):
                image.putpixel((column, ord(char)), 1)
            image.save(path)
            self.assertEqual(module.remember_remember(path), 'Hi!')
            image.putpixel((0, 1), 0)
            image.save(path)
            with self.assertRaises(ValueError):
                module.remember_remember(path)

    def test_grouping(self):
        """Preserve duplicates and group order for a one-shot iterable."""
        module = load_module('6.5.group_by.py')
        self.assertEqual(module.group_by(len, iter(['hi', 'bye', 'yo', 'try', 'hi'])),
                         {2: ['hi', 'yo', 'hi'], 3: ['bye', 'try']})
        self.assertEqual(module.group_by(len, []), {})

    def test_mail_reading(self):
        """Urgent mail comes first and read messages never appear a second time."""
        office = load_module('7.2.sent_turtle.py').PostOffice(['a', 'b'])
        first = office.send_message('a', 'b', 'normal')
        urgent = office.send_message('a', 'b', 'urgent', True)
        self.assertEqual(office.read_inbox('b', 0), [])
        self.assertEqual([msg['id'] for msg in office.read_inbox('b', 1)], [urgent])
        self.assertEqual([msg['id'] for msg in office.read_inbox('b', 50)], [first])
        self.assertEqual(office.read_inbox('b'), [])
        self.assertTrue(all(msg['read'] for msg in office.boxes['b']))

    def test_mail_search(self):
        """Search title and body including read messages, without marking reads."""
        office = load_module('7.2.sent_turtle.py').PostOffice(['a', 'b'])
        office.send_message('a', 'b', 'body', title='needle')
        office.send_message('a', 'b', 'needle in body')
        self.assertEqual(len(office.search_inbox('b', 'needle')), 2)
        self.assertEqual(len(office.read_inbox('b')), 2)
        self.assertEqual(len(office.search_inbox('b', 'needle')), 2)
        self.assertEqual(office.search_inbox('b', 'missing'), [])

    def test_mail_errors(self):
        """Reject missing recipients and invalid read counts."""
        office = load_module('7.2.sent_turtle.py').PostOffice(['a'])
        with self.assertRaises(KeyError):
            office.send_message('a', 'missing', 'hello')
        self.assertEqual(office.message_id, 0)
        with self.assertRaises(ValueError):
            office.read_inbox('a', -1)
        with self.assertRaises(TypeError):
            office.read_inbox('a', 1.5)


if __name__ == '__main__':
    unittest.main()
