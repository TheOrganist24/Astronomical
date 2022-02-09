import unittest
from astronomical import __version__


class TestMainModule(unittest.TestCase):
    def test_version(self):
        assert __version__ == "0.4.1"
