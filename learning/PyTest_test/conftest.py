import pytest
import time


def pytest_addoption(parser):
    parser.addoption("--additional_value", action="store", default=0, type=int, help='Add value')


@pytest.fixture(scope='session')
def additional_value(request):
    return request.config.getoption("additional_value")


@pytest.fixture(scope='class', autouse=True)
def suite_data():
    print('\n  > Suite setup')
    yield
    print('   > Suite teardown')


@pytest.fixture(scope='function')
def case_data():
    print('   > Case setup')
    yield time.time()
    print('   > Case teardown')
