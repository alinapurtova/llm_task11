import pytest
from helpers.test_utils import safe_assert, create_test_case
from helpers.llm_factory import get_llm
from helpers.metrics_factory import faithfulness

llm = get_llm()
metric = faithfulness(llm)

CASES = [
    {"question": "What is the capital of France?", "expected": "Paris", "context": ["France is a country in Europe. Paris is the capital of France."]},
    {"question": "Who developed the theory of relativity?", "expected": "Albert Einstein", "context": ["Albert Einstein developed the theory of relativity."]},
    {"question": "What is the largest planet in our solar system?", "expected": "Jupiter", "context": ["Jupiter is the largest planet in the solar system."]}
]

@pytest.mark.parametrize("case", CASES)
def test_accuracy_correctness(case):
    test_case = create_test_case(
        input=case["question"],
        actual_output=llm.generate(case["question"]),
        expected_output=case["expected"],
        retrieval_context=case["context"]
    )
    safe_assert(test_case=test_case, metrics=[metric])
