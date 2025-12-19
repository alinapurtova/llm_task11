from helpers.test_utils import safe_assert, create_test_case
from helpers.llm_factory import get_llm
from helpers.metrics_factory import geval

llm = get_llm()


def test_geval():
    question = "Explain what an API is with example."

    metric = geval(
        llm,
        name="Clarity and correctness",
        criteria="The answer should be clear, concise, and factually correct."
    )

    test_case = create_test_case(
        input=question,
        actual_output=llm.generate(question),
    )

    safe_assert(test_case=test_case, metrics=[metric])
