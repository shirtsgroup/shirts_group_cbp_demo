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

# Test get_look_and_say_sequence
@pytest.mark.parametrize('input,expected',
                         [(1, [1,11,21,1211,111221]),
                          (2, [2,12,1112,3112,132112]),
                          (3, [3,13,1113,3113,132113]),
                          (4, [4,14,1114,3114,132114])]
    )
def test_get_look_and_say_sequence(input, expected):
    # Multiple look and say sequences
    out = shirts_group_cbp_demo.get_look_and_say_sequence(input)
    assert out == expected

def test_get_look_and_say_sequence_types():
    out = shirts_group_cbp_demo.get_look_and_say_sequence(1)
    assert isinstance(out, list)

