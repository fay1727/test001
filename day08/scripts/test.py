import  pytest
class Test:
    @pytest.mark.parametrize("a",[1,2,3])
    def test01(self,a):
        assert a !=2