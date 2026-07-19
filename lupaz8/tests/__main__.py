if __name__ == '__main__':
    import sys
    import unittest
    from . import suite
    result = unittest.TextTestRunner(verbosity=2).run(suite()).failures
    print("NOTE - currently 9 failures and 40 errors due to z8lua differences, not going to bother updating or ignoring the tests, not unless I decide to unittest the stuff I added")
    sys.exit(1 if result else 0)
