import allure
import  pytest

class Test_haha:
    @allure.step(title="测试名字1")
    @pytest.mark.parametrize("a",[1,2,3])
    def test01(self,a):
        allure.attach("描述","测试步骤描述")
        assert a !=2

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试名字2")
    @pytest.mark.parametrize("a", [1, 3, 4])
    def test02(self, a):
        assert a != 2