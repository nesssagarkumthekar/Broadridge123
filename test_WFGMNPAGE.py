from unittest import TestCase

from WFGMNPAGE import root

class Test(TestCase):
    def test_start(self):
        root.mainloop()
        self.fail()
