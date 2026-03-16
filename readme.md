# Presidio-Based LLM Security Mini-Gateway

A modular security gateway for Large Language Models (LLMs) that detects prompt injections and anonymizes Personally Identifiable Information (PII) using customized Microsoft Presidio.

## Modular Architecture
- `config.py`: Contains configurable thresholds and detection keywords.
- `security_engine.py`: Contains the Presidio analyzer customizations and the policy decision logic.
- `main.py`: The entry point that executes the end-to-end pipeline.

## Installation & Setup Environment
1. Clone this repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install the required dependencies: `pip install -r requirements.txt`

## Running the Application
Execute the main script to run the security pipeline against the predefined test scenarios:
`python main.py`

## Customizations Implemented
1. **Custom Recognizer**: Added regex pattern matching for internal AWS-style API keys.
2. **Context-Aware Scoring**: Boosts the recognition score of API keys if context words are present.
3. **Confidence Calibration**: Policy Engine only masks entities if the analyzer's confidence score exceeds a strict threshold (0.6).
