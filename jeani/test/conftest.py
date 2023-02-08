import json
import pytest
from pathlib import Path


CURRENT_DIR = Path(__file__).parent
DATA_DIR = CURRENT_DIR / 'data'
TEST_DATA_PATH = DATA_DIR / 'test_data.json'
TEST_VER_DATA_PATH = DATA_DIR / 'verification_data.json'

with (
    open(TEST_DATA_PATH) as fp1,
    open(TEST_VER_DATA_PATH) as fp2
):
    data_json = json.load(fp1)
    verification_json = json.load(fp2)


def pytest_configure():
    pytest.test_data = data_json
    pytest.verification_data = verification_json
