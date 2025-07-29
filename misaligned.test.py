import unittest
from misaligned import get_color_map, print_color_map

def fake_print(line):
    captured_lines.append(line)

class MisalignedTest(unittest.TestCase):
    generated_manual = []
    
    def fake_print_fn(line):
        generated_manual.append(line)
    
    # Call with fake print function
    count = print_color_map(fake_print_fn)
    
    # Prepare actual expected output
    expected_manual = [
        f'{index} | {major} | {minor}'
        for index, major, minor in get_color_map()
    ]
    
    self.assertEqual(count, len(expected_manual))
    self.assertEqual(generated_manual, expected_manual)

if __name__ == '__main__':
  unittest.main()
