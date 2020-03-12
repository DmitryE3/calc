class TestSuite():
    def test_case_1(self, case_data, additional_value):
        time = int(case_data)
       # print('   > time = {}'.format(int))
        parametr = additional_value
       # assert (time % 2 == 0)
        assert(parametr == 1)

