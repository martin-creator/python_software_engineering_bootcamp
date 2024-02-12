# Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not.
#In simple words, testing is executing a system in order to identify any gaps, errors, or missing requirements in contrary to the actual requirements.
# There are different types of testing including:
# Unit testing
## It involves testing individual units or components of a software. The primary goal is to validate that each unit of the software performs as designed.
# Integration testing
## It involves testing the integration of different units or components. The primary goal is to validate that the software components work together as designed.
# Functional testing
## It involves testing the software against the functional requirements/specifications. The primary goal is to validate that the software performs as expected.
# End-to-end testing
## It involves testing the complete software product in a scenario which simulates real-world use, such as interacting with the database, network, hardware, and other applications.
# Load testing
## It involves testing the software under heavy loads, such as testing its ability to handle user and data load.
# Stress testing
## It involves testing the software under extreme conditions, such as testing the software at the peak load capacity.
# Performance testing
## It involves testing the software performance, such as its response time, speed, and reliability.
# Usability testing
## It involves testing the software user interface, such as its ease of use, efficiency, and user satisfaction.
# Regression testing
## It involves testing the software after changes to ensure that the changes have not affected the existing functionality.

# In python we mainly use the pytest which is a testing framework that allows us to write test codes using python. It helps us to write simple and scalable test codes.
# The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.
# The pytest framework is easy to install and use. It is a mature full-featured Python testing tool.
#
# Examples from simple to complex using pytest

# Example 1: Simple test
# The following example shows a simple test using pytest.
# The test function name should start with test_.
# The assert statement is used to check the result.

# test_simple.py
def test_addition():
    assert 1 + 2 == 3

# Run the test using the following command:
# pytest test_pytest_introduction.py
    
# Example 2: Test with setup and teardown
# The following example shows a test with setup and teardown using pytest.
# The setup function name should start with setup_.
# The teardown function name should start with teardown_.(At teardown function helps to clean up the resources after the test)

# test_pytest_introduction.py
import pytest

@pytest.fixture
def setup():
    print("\nSetup")

def test_fixture(setup):
    print("Executing test_fixture")
    assert True

def teardown():
    print("\nTeardown")

# Run the test using the following command:
# pytest test_pytest_introduction.py
    
# Example 3: Test with parameters

# The following example shows a test with parameters using pytest.
# The @pytest.mark.parametrize decorator is used to pass the parameters.
# The test function should take the parameters as input.
    
# test_pytest_introduction.py
import pytest

@pytest.mark.parametrize("input, output", [(1, 2), (3, 4)])
def test_addition(input, output):
    assert input + 1 == output

# Run the test using the following command:
# pytest test_pytest_introduction.py
    
# Example 4: Test with exception

# The following example shows a test with exception using pytest.
# The pytest.raises function is used to check the exception.
    
# test_pytest_introduction.py
import pytest

def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# Run the test using the following command:
# pytest test_pytest_introduction.py
        
# Example 5: Test with fixtures

# The following example shows a test with fixtures using pytest.
# The @pytest.fixture decorator is used to define a fixture.
# The test function takes the fixture as input.
# The fixture function name should start with fixture_.
# A fixture is used to provide a fixed baseline upon which tests can reliably and repeatedly execute.
    
# test_pytest_introduction.py
import pytest

@pytest.fixture
def setup():
    print("\nSetup")
    yield
    print("\nTeardown")

def test_fixture(setup):
    print("Executing test_fixture")
    assert True

# Run the test using the following command:
# pytest test_pytest_introduction.py
# A fixture is commonly used in scenerios where a test requires a database, a network connection, a file, or any other resource.
    
# Example 6: Test with marks
    
# The following example shows a test with marks using pytest.
# The @pytest.mark decorator is used to define a mark.
# The -m option is used to run the tests with the specified mark.
    
# test_pytest_introduction.py
import pytest

@pytest.mark.smoke
def test_one():
    assert True

@pytest.mark.sanity
def test_two():
    assert True

# Run the test using the following command:
# pytest -m smoke test_pytest_introduction.py
    

# Example 7: Test with skip and xfail
    
# The following example shows a test with skip and xfail using pytest.
# The pytest.skip function is used to skip the test.
# The pytest.xfail function is used to mark the test as an expected failure.
    
# test_pytest_introduction.py
import pytest

@pytest.mark.skip(reason="Skipping the test")
def test_skip():
    assert True

@pytest.mark.xfail(reason="Failing the test")
def test_xfail():
    assert False

# Run the test using the following command:
# pytest test_pytest_introduction.py
    
# Example 8: Test with fixtures and marks

# The following example shows a test with fixtures and marks using pytest.
# The test function takes the fixture as input.
# The fixture function name should start with fixture_.
    
# test_pytest_introduction.py
import pytest

@pytest.fixture
def setup():
    print("\nSetup")
    yield
    print("\nTeardown")

@pytest.mark.smoke
def test_fixture(setup):
    print("Executing test_fixture")
    assert True

# Run the test using the following command:
# pytest -m smoke test_pytest_introduction.py
    