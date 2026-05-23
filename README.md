# Adjective Order Classifier

A Python NLP project for analyzing semantic adjective ordering in English phrases.

## Overview

This project explores adjective ordering patterns in English by identifying consecutive adjective sequences and classifying adjectives into broad semantic categories.

English adjective order often follows a conventional hierarchy such as:

```txt
opinion → size → age → shape → color → origin → material → purpose
```
For example:
```
beautiful small old wooden table
```
The project extracts adjective sequences from text and analyzes the semantic order of modifiers within each phrase.

## Features
* Reads plain text files
* Tokenizes and POS-tags text with NLTK
* Finds consecutive adjective sequences
* Classifies adjectives into semantic categories
* Exports adjective-order analyses

## Semantic Categories
* Opinion
* Size
* Age
* Shape
* Color
* Origin
* Material
* Purpose

## Setup
Install dependences:
```bash
pip install -r requirements.txt
```
Download required NLTK data:
```python
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
```
## How to Run
```bash
python adjective_order_classifier.py
```
You will be prompted for:
1. An input `.txt` file
2. An output filename

### Example Output
```
Phrase: beautiful small old wooden
Order: opinion → size → age → material
```

## Skills Demonstrated
 * Python scripting
 * Natural language processing
 * Corpus linguistics
 * Parts-of-speech tagging
 * Semantic classification
 * Modifier-order analysis

## Limitations
This project uses a manually defined adjective-category lexicon, so classification coverage is limited. Unknown adjectives are labeled as `unknown`.

## Future Improvements
* Expand the adjective-category lexicon
* Use WordNet or embeddings for semantic grouping
* Analyze adjective-order frequency statistically
* Compare adjective-order patterns across authors
* Add CSV export support
* Visualize ordering distributions
