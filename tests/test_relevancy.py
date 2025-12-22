from helpers.metrics_factory import relevancy
from helpers.test_utils import safe_assert, create_test_case
from helpers.llm_factory import get_llm

llm = get_llm()

DOCS = [
    {
        "input": "What is the return policy of the company?",
        "expected_output": "You can return products within 30 days of purchase.",
        "context": ["Our company allows returns within 30 days if the product is in original condition."]
    },
    {
        "input": "How can I contact customer support?",
        "expected_output": "You can contact customer support via email or phone.",
        "context": ["Customer support is available via email support@company.com and by phone at 123-456-7890."]
    },
    {
        "input": "Where is the company located?",
        "expected_output": "The company is located in New York City.",
        "context": ["Our headquarters are in New York City."]
    },
]

def generate_relevancy_test(doc):
    metric = relevancy(llm, threshold=0.7)
    test_case = create_test_case(
        input=doc["input"],
        actual_output=llm.generate(doc["input"]),
        expected_output=doc["expected_output"],
        context=doc["context"],
        retrieval_context=doc["context"]
    )
    success, message = safe_assert(test_case=test_case, metrics=[metric])
    assert success, message

def test_relevancy_case_1():
    generate_relevancy_test(DOCS[0])

def test_relevancy_case_2():
    generate_relevancy_test(DOCS[1])

def test_relevancy_case_3():
    generate_relevancy_test(DOCS[2])
