"""
Unit and regression test for the shirts_group_cbp_demo package.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import numpy as np
import shirts_group_cbp_demo


def test_shirts_group_cbp_demo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "shirts_group_cbp_demo" in sys.modules

# Testing get_odds function

def test_get_odds_typing():
    """Test typing output from get_odds with different input lists"""
    # python list
    out = shirts_group_cbp_demo.get_odds([1,2,3,4,5,6,7,8,9])
    assert type(out) == list

    # python set
    out = shirts_group_cbp_demo.get_odds((1,2,3,4,5,6,7,8,9))
    assert type(out) == list

    # numpy array
    out = shirts_group_cbp_demo.get_odds(np.array([1,2,3,4,5,6,7,8,9]))
    assert type(out) == list

def test_get_odds_funct():
    # Identifies odd numbers
    out = shirts_group_cbp_demo.get_odds([1,2,3,4,5,6,7,8,9])
    assert out == [1,3,5,7,9]

    # List of all even numbers
    out = shirts_group_cbp_demo.get_odds([2,2,4,8,6,2,12])
    assert out == []

    # Negative numbers
    out = shirts_group_cbp_demo.get_odds([-5,-4,-3,-2,-1])
    assert out == [-5,-3,-1]

    # Zero
    out = shirts_group_cbp_demo.get_odds([-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5])
    assert out == [-5,-3,-1,1,3,5]

def test_get_odds_errors():
    # string
    with pytest.raises(TypeError):
        out = shirts_group_cbp_demo.get_odds([1,2,3,"4"])

    #float
    with pytest.raises(TypeError):
        out = shirts_group_cbp_demo.get_odds([1,2,3,4.564])

# Testing get_evens function

def test_get_evens_typing():
    """Test typing output from get_evens with different input lists"""
    # python list
    out = shirts_group_cbp_demo.get_evens([1,2,3,4,5,6,7,8,9])
    assert type(out) == list

    # python set
    out = shirts_group_cbp_demo.get_evens((1,2,3,4,5,6,7,8,9))
    assert type(out) == list

    # numpy array
    out = shirts_group_cbp_demo.get_evens(np.array([1,2,3,4,5,6,7,8,9]))
    assert type(out) == list

def test_get_evens_funct():
    # Identifies even numbers
    out = shirts_group_cbp_demo.get_evens([1,2,3,4,5,6,7,8,9])
    assert out == [2,4,6,8]

    # List of all odd numbers
    out = shirts_group_cbp_demo.get_evens([1,1,3,9,7,3,21])
    assert out == []

    # Negative numbers
    out = shirts_group_cbp_demo.get_evens([-5,-4,-3,-2,-1])
    assert out == [-4,-2]

    # Zero
    out = shirts_group_cbp_demo.get_evens([-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5])
    assert out == [-4, -2, 0, 2, 4]

def test_get_evens_errors():
    # string
    with pytest.raises(TypeError):
        out = shirts_group_cbp_demo.get_evens([1,2,3,"4"])

    #float
    with pytest.raises(TypeError):
        out = shirts_group_cbp_demo.get_evens([1,2,3,4.564])

def test_check_prime():
    numbers_1 = [1, 2, 3, 4, 5]
    bool_lst_1 = [shirts_group_cbp_demo.check_prime(i) for i in numbers_1]
    assert bool_lst_1 == [False, True, True, False, True]
    
    numbers_2 = range(1, 101)
    bool_lst_2 = [shirts_group_cbp_demo.check_prime(i) for i in numbers_2]
    assert sum(bool_lst_2) == 25

    with pytest.raises(TypeError):
        out_1 = shirts_group_cbp_demo.check_prime(1.5)
        out_2 = shirts_group_cbp_demo.check_prime(-1)

# Test look_and_say

