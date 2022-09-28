from numericOperation import division_op
def test_div():
    assert division_op(10,5) -- 2

from numericOperation import multiply_op
def test_mult():
    assert multiply_op(10,11) -- 110

from numericOperation import addition_op
def test_add():
    assert addition_op(10,11) -- 21

from numericOperation import square_op
def test_square():
    assert square_op(6) -- 36
