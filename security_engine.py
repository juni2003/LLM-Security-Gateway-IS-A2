from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine
import config

# Initialize Engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Customization 1: Custom Recognizer for Internal API Keys
api_key_pattern = Pattern(name="internal_api_key", regex=config.API_KEY_REGEX, score=0.4)

# Customization 2: Context-aware scoring
api_key_recognizer = PatternRecognizer(
    supported_entity="INTERNAL_API_KEY", 
    patterns=[api_key_pattern],
    context=config.API_KEY_CONTEXT_WORDS 
)
analyzer.registry.add_recognizer(api_key_recognizer)

def detect_injection(text):
    """Calculates a risk score based on known injection keywords."""
    score = 0.0
    for kw in config.INJECTION_KEYWORDS:
        if kw in text.lower():
            score += 0.5
    return score

def apply_policy(text, injection_score, analyzer_results):
    """Enforces the Allow/Mask/Block policy based on configurable thresholds."""
    if injection_score >= config.INJECTION_THRESHOLD:
        return "BLOCK", "[BLOCKED] Prompt Injection or Jailbreak attempt detected."
    
    # Customization 3: Confidence calibration
    calibrated_results = [res for res in analyzer_results if res.score >= config.CONFIDENCE_THRESHOLD]
    
    if calibrated_results:
        anonymized_result = anonymizer.anonymize(text=text, analyzer_results=calibrated_results)
        return "MASK", anonymized_result.text
    
    return "ALLOW", text
