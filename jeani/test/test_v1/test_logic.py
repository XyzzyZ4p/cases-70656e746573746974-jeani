import pytest
from jeani.src.state import State
from jeani.src.v1.logic import parse


def test_logic_correctness():
    test_data = pytest.test_data
    verification_data = pytest.verification_data
    state = State([])
    parse(test_data, state)
    assert state == verification_data


def test_logic_with_1_element():
    test_data = [1]
    verification_data = [1]
    state = State([])
    parse(test_data, state)
    assert state == verification_data


def test_logic_with_no_elements():
    test_data = {}
    verification_data = []
    state = State([])
    parse(test_data, state)
    assert state == verification_data


def test_logic_with_incorrect_element():
    test_data = 42
    verification_data = [42]
    state = State([])
    parse(test_data, state)
    assert state == verification_data
