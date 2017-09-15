import unittest
from main.filter_system import FilterSystem


class TestFilterSystem(unittest.TestCase):

    def setUp(self):
        self.filter_system = FilterSystem()

    def tearDown(self):
        pass

    def test_init_PlugIns(self):
        self.assertGreater(len(self.filter_system.filter_plugins.keys()), 0, 'no plugin found')
        for plugin in self.filter_system.filter_plugins:
            self.assertTrue(callable(self.filter_system.filter_plugins[plugin]), 'filter is not callable')
