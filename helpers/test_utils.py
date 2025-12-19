from deepeval import assert_test as original_assert_test
from deepeval.test_case import LLMTestCase


def create_test_case(
        *,
        input: str,
        actual_output: str,
        expected_output: str | None = None,
        context: list[str] | None = None,
        retrieval_context: list[str] | None = None,
):
    return LLMTestCase(
        input=input,
        actual_output=actual_output,
        expected_output=expected_output,
        context=context,
        retrieval_context=retrieval_context,
    )


def safe_assert(test_case, metrics):
    try:
        original_assert_test(test_case=test_case, metrics=metrics)
        return True
    except AssertionError as e:
        return False
    except Exception as e:
        return False
