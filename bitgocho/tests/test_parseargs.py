import unittest

from bitgocho.application.parseargs import parse_args


class ParseArgsTest(unittest.TestCase):
    def test_parseargs(self):
        self.assertEqual(
            parse_args(
                ("d", "--a", "pq", "e", "--b", "3", "--c", "4.5", "f"),
                (("a", "x", ""), ("b", 1, ""), ("c", 2.3, "")),
            ),
            ({"a": "pq", "b": 3, "c": 4.5}, ["d", "e", "f"]),
        )
        self.assertEqual(parse_args([], [("a", "x", "")]), ({"a": "x"}, []))
        self.assertEqual(
            parse_args(["--a", "x", "--a", "y"], [("a", "", "")]), ({"a": "y"}, [])
        )
        self.assertEqual(parse_args(["x"], [], 1, 2), ({}, ["x"]))
        self.assertEqual(parse_args(["x", "y"], [], 1, 2), ({}, ["x", "y"]))
        self.assertRaises(ValueError, parse_args, ["--a", "x"], [])
        self.assertRaises(ValueError, parse_args, ["--a"], [("a", "x", "")])
        self.assertRaises(ValueError, parse_args, [], [], 1, 2)
        self.assertRaises(ValueError, parse_args, ["x", "y", "z"], [], 1, 2)
        self.assertRaises(ValueError, parse_args, ["--a", "2.0"], [("a", 3, "")])
        self.assertRaises(ValueError, parse_args, ["--a", "z"], [("a", 2.1, "")])


if __name__ == "__main__":
    unittest.main()
