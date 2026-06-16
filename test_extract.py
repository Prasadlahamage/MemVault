from ai.extractor import extract_facts

result = extract_facts(
    """
    Today I walked 8000 steps.
    My weight is 73kg.
    Had chicken biryani.
    """
)

print(result)