import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        from allure import attach
        attach(f"Test {item.name}: {result.outcome}", name="Test Outcome")
