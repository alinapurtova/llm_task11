from helpers.llm_factory import get_llm
from helpers.metrics_factory import hallucination
from helpers.test_utils import safe_assert, create_test_case

llm = get_llm()


def test_hallucination():
    question = "My friend said that the Moon is made of cheese. Is this true?"

    metric = hallucination(llm, threshold=0.85)

    context = [
        "The Moon is Earth's natural satellite.",
        "Scientific studies confirm that the Moon is composed mainly of rock and metal, not cheese."
    ]

    test_case = create_test_case(
        input=question,
        actual_output=llm.generate(question),
        expected_output="No",
        context=context,
        retrieval_context=context
    )

    safe_assert(test_case=test_case, metrics=[metric])
