# LLM Testing Project with DeepEval

## Summary
This repository contains **automated tests** for **LLM models** (OpenAI GPT) using the **DeepEval framework**.  
The tests cover multiple aspects of LLM behavior, including **accuracy, relevancy, hallucination detection, toxicity, and bias detection**.  
All tests are written in **Python** and structured to allow modular execution of individual test cases.

---

## Requirements  

Before running the tests, make sure you have the following installed:

- **Python 3.11+**
- **pipenv**
- **Git**
- **Allure CLI** (for generating HTML reports)
- **OpenAI API key** stored in `.env` file as `OPENAI_API_KEY`

---

## Installation Steps  

**Clone the repository:**
```bash
git clone https://github.com/alinapurtova/llm_task11.git
cd llm_task11
```

**Install dependencies:**
```bash
pip install pipenv
pipenv install --dev
```

**REMEMBER to set your OpenAI API key in .env:**
OPENAI_API_KEY=your_openai_api_key_here

## Running Tests

**Run all tests:**
```bash
pipenv run tests

```
or with report:
```bash
pipenv run tests-report
```

**Run specific test files:**
```bash
pipenv run test-accuracy
pipenv run test-bias
pipenv run test-hallucination
pipenv run test-relevancy
pipenv run test-toxicity
pipenv run test-geval
```
You can find all these scripts in **Pipfile**.

## Generate Allure Report

**Generate report:**
```bash
pipenv run allure-generate
```

**Open report locally:**
```bash
pipenv run allure-open
```

## Test Coverage

| Test Area                   | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| **Accuracy / Faithfulness** | Checks factual correctness of answers                    |
| **Answer Relevancy**        | Ensures the model response addresses the question        |
| **Hallucination**           | Detects false or misleading information                  |
| **Toxicity**                | Checks for safe and appropriate output                   |
| **Bias Detection**          | Evaluates potential unfair or biased responses           |
| **GEval**                   | Custom evaluation for clarity and correctness of answers |


## CI/CD 
Tests are executed automatically via GitHub Actions with results reported to the branch reports and uploaded to Pages.
Pipeline uses GitHub Secrets with OpenAI API key.
