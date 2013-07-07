#! /usr/bin/env python

import unittest
import pyganim

"""
Headless testing for pyganim.
"""

class PyganimTests(unittest.TestCase):
    
    def setUp(self):
       self.images = [('testimages/bolt_strike_0001.png', 0.1),
                      ('testimages/bolt_strike_0002.png', 0.1),
                      ('testimages/bolt_strike_0003.png', 0.1),
                      ('testimages/bolt_strike_0004.png', 0.1),
                      ('testimages/bolt_strike_0005.png', 0.1),
                      ('testimages/bolt_strike_0006.png', 0.1),
                      ('testimages/bolt_strike_0007.png', 0.1),
                      ('testimages/bolt_strike_0008.png', 0.1),
                      ('testimages/bolt_strike_0009.png', 0.1),
                      ('testimages/bolt_strike_0010.png', 0.1)]
       self.boltAnim = pyganim.PygAnimation(self.images)

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

    def test_frameNav(self):
        """
        Tests frame-by-frame navigation.
        """
        current_frame = self.boltAnim.currentFrameNum
        offset = current_frame + 1
        self.boltAnim.nextFrame()
        self.assertEqual(offset, self.boltAnim.currentFrameNum)

        current_frame = offset
        jump = 3
        offset = current_frame + jump
        # By here, we are not yet testing the overflow condition.
        self.assertTrue(offset < len(self.images))
        self.boltAnim.nextFrame(jump)
        self.assertEqual(offset, self.boltAnim.currentFrameNum)

        # Loop around! Should still be equal.
        self.boltAnim.nextFrame(len(self.images))
        self.assertEqual(offset, self.boltAnim.currentFrameNum)

if __name__ == "__main__":
    unittest.main()
