from deepeval.metrics import (
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    HallucinationMetric,
    ToxicityMetric,
    BiasMetric,
    GEval,
)
from deepeval.test_case import LLMTestCaseParams

def faithfulness(llm, threshold=0.8):
    return FaithfulnessMetric(threshold=threshold, model=llm)

def relevancy(llm, threshold=0.6):
    return AnswerRelevancyMetric(threshold=threshold, model=llm)

def hallucination(llm, threshold=0.8):
    return HallucinationMetric(threshold=threshold, model=llm)

def toxicity(llm, threshold=0.8):
    return ToxicityMetric(threshold=threshold, model=llm)

def bias(llm, threshold=0.7):
    return BiasMetric(threshold=threshold, model=llm)

def geval(llm, *, name, criteria, threshold=0.7):
    return GEval(
        name=name,
        criteria=criteria,
        threshold=threshold,
        model=llm,
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
    )
