import unittest
from misaligned import get_color_map, print_color_map, format_color_map_line

class MisalignedTest(unittest.TestCase):
    captured_output = []
    
    def fake_print_fn(line):
        captured_output.append(line)
    
    # Call with fake print function
    count = print_color_map(fake_print_fn)
    
    # Prepare actual expected output
    expected_output = [
        format_color_map_line(entry)
        for entry in get_color_map()
    ]

    count = print_color_map(fake_print_fn)
    self.assertEqual(captured_output, expected_output)
    self.assertEqual(count, len(expected_output))

if __name__ == '__main__':
  unittest.main()
