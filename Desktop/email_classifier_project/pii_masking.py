import re
import spacy

# Load SpaCy NER (en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

# PII regex patterns
patterns = {
    "email": r"[a-zA-Z0-9+._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone_number": r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b",
    "aadhar_num": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3,4}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2})\b",
    "dob": r"\b(?:\d{1,2}[-/th|st|rd|nd\s]*)?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[-/\s]*\d{2,4}\b"
}

# Mapping SpaCy labels to PII types
spacy_label_map = {
    "PERSON": "full_name",
    "DATE": "dob"
}

def mask_text(text):
    masked_text = text
    entities = []

    # Regex masking
    for entity_type, pattern in patterns.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.span()
            original = match.group()
            entities.append({
                "position": [start, end],
                "classification": entity_type,
                "entity": original
            })
            masked_text = masked_text.replace(original, f"[{entity_type}]", 1)

    # SpaCy NER masking
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in spacy_label_map:
            mapped_type = spacy_label_map[ent.label_]
            original = ent.text
            start = text.find(original)
            end = start + len(original)
            if original not in masked_text:
                entities.append({
                    "position": [start, end],
                    "classification": mapped_type,
                    "entity": original
                })
                masked_text = masked_text.replace(original, f"[{mapped_type}]", 1)

    return masked_text, entities
