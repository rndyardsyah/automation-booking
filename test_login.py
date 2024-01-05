def login(i):
    return i+1

class TestCases:

    def test_1(self):
      assert login(2) == 3

    def test_2(self):
       assert login(2) == 4

    def test_3(self):
     assert login(2) == 3