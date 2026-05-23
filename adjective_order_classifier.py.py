"""
Author: Eliana Mugar
Date: 2/10/2021 

Analyze semantic adjective ordering in English phrases.

This script classifies adjectives into broad semantic categories
(opinion, size, age, color, origin, material, etc.) and analyzes
their ordering patterns within adjective sequences.
"""

from pathlib import Path

import nltk


ADJECTIVE_CATEGORIES = {
    "opinion": {
        "beautiful", "ugly", "nice", "lovely", "wonderful",
        "terrible", "excellent", "horrible", "strange"
    },
    "size": {
        "big", "small", "large", "tiny", "huge", "little"
    },
    "age": {
        "old", "young", "new", "ancient", "modern"
    },
    "shape": {
        "round", "square", "flat", "thin", "wide"
    },
    "color": {
        "red", "blue", "green", "black", "white", "yellow"
    },
    "origin": {
        "american", "french", "italian", "japanese", "british"
    },
    "material": {
        "wooden", "metal", "plastic", "silk", "cotton"
    },
    "purpose": {
        "sleeping", "cooking", "dining", "running"
    },
}

ADJECTIVE_TAGS = {"JJ", "JJR", "JJS"}


def classify_adjective(word):
    """Return the semantic category for an adjective."""
    lower_word = word.lower()

    for category, words in ADJECTIVE_CATEGORIES.items():
        if lower_word in words:
            return category

    return "unknown"


def extract_adjective_sequences(text):
    """Extract consecutive adjective sequences from text."""
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    sequences = []
    current_sequence = []

    for word, tag in tagged_tokens:
        if tag in ADJECTIVE_TAGS:
            current_sequence.append(word)
        else:
            if len(current_sequence) >= 2:
                sequences.append(current_sequence)

            current_sequence = []

    if len(current_sequence) >= 2:
        sequences.append(current_sequence)

    return sequences


def analyze_sequence(sequence):
    """Analyze semantic ordering within an adjective sequence."""
    return [
        {
            "word": adjective,
            "category": classify_adjective(adjective),
        }
        for adjective in sequence
    ]


def format_analysis(sequence_analysis):
    """Format one adjective-order analysis."""
    words = [item["word"] for item in sequence_analysis]
    categories = [item["category"] for item in sequence_analysis]

    return (
        f"Phrase: {' '.join(words)}\n"
        f"Order: {' → '.join(categories)}"
    )


def main():
    """Run the adjective-order analyzer."""
    input_path = Path(input("Enter input .txt file path: ").strip())
    output_path = Path(
        input("Enter output filename, e.g. adjective_order_results.txt: ").strip()
    )

    if not input_path.exists():
        print("Error: input file does not exist.")
        return

    text = input_path.read_text(encoding="utf-8")

    sequences = extract_adjective_sequences(text)

    analyses = [
        analyze_sequence(sequence)
        for sequence in sequences
    ]

    formatted_results = "\n\n".join(
        format_analysis(analysis)
        for analysis in analyses
    )

    output_path.write_text(formatted_results, encoding="utf-8")

    print(f"Found {len(analyses)} adjective sequences.")
    print(f"Saved results to {output_path}")


if __name__ == "__main__":
    main()

