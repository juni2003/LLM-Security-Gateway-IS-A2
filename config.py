# Configuration settings for the LLM Security Gateway

# Threat Detection Keywords
INJECTION_KEYWORDS = [
    "ignore previous", 
    "system prompt", 
    "jailbreak", 
    "bypass", 
    "you are now"
]

# Configurable Thresholds
INJECTION_THRESHOLD = 0.8
CONFIDENCE_THRESHOLD = 0.6

# Presidio Customization Settings
API_KEY_REGEX = r"AKIA[0-9A-Z]{16}"
API_KEY_CONTEXT_WORDS = ["api", "key", "secret", "token", "credential"]
