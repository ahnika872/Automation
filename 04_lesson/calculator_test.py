import pytest
from calculator import Calculator

calculator = Calculator()
# ++
# --
# -+
# ..
# n 0

# @pytest.mark.skip(reason="починить тест позже") 
# @pytest.mark.xfail (strict=True) #если тест упадет ожидаемо 
# @pytest.mark.positive_test #маркер придуманнный отметка
@pytest.mark.positive_test
@pytest.mark.parametrize( 'num1, num2, result', [
    (4,5,9), 
    (-6, -10, -16), 
    (-6,6,0),
    (5.61, 4.29, 9.9), 
    (10,0,10),
    (-10.5, 1234, 1223.5)
    ])
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result

def test_div_positive_nums():
    calculator = Calculator()
    res = calculator.div(10,2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

@pytest.mark.parametrize( 'nums, result', [([], 0), ([1,2,3,4,5,6,7,8,9,5],5)])
def test_avg_empty_list(nums, result):
    calculator = Calculator()
    numbers = []
    res = calculator.avg(nums)
    assert res == result
