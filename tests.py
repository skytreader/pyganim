#! /usr/bin/env python

import unittest
import pyganim

"""
Headless testing for pyganim.
"""

class PyganimTests(unittest.TestCase):
    
    def setUp(self):
       self. boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 0.1),
                                             ('testimages/bolt_strike_0002.png', 0.1),
                                             ('testimages/bolt_strike_0003.png', 0.1),
                                             ('testimages/bolt_strike_0004.png', 0.1),
                                             ('testimages/bolt_strike_0005.png', 0.1),
                                             ('testimages/bolt_strike_0006.png', 0.1),
                                             ('testimages/bolt_strike_0007.png', 0.1),
                                             ('testimages/bolt_strike_0008.png', 0.1),
                                             ('testimages/bolt_strike_0009.png', 0.1),
                                             ('testimages/bolt_strike_0010.png', 0.1)])

    def test_state(self):
        """
        Test the state transitions.
        """
        self.boltAnim.play()
        self.assertEqual(self.boltAnim.state, pyganim.PLAYING)

        self.boltAnim.stop()
        self.assertEqual(self.boltAnim.state, pyganim.STOPPED)

        self.boltAnim.pause()
        self.assertEqual(self.boltAnim.state, pyganim.PAUSED)

if __name__ == "__main__":
    unittest.main()
