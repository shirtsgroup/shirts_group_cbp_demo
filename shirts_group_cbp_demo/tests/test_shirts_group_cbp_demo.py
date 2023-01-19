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







