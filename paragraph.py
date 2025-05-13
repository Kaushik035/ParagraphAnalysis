import argparse
from collections import Counter
import re
import sys

def analyze_text(text: str) -> tuple:
    """
    Analyze a text paragraph and return word statistics.
    
    Args:
        text (str): The input text to analyze
        
    Returns:
        tuple: (total_words, unique_words, most_common_word, frequency)
    """
    if not text.strip():
        print("Error: Empty text provided")
        sys.exit(1)
        
    # Converting text to lowercase and extract words using regex
    words = re.findall(r'\b\w+\b', text.lower()) 
    
    if not words:
        print("Error: No valid words found in the text")
        sys.exit(1)
        
    total_words = len(words)
    unique_words = len(set(words))
    most_common_word, frequency = Counter(words).most_common(1)[0]

    return total_words, unique_words, most_common_word, frequency

def main():
    """
    Main function to handle command-line arguments and display results.
    """
    parser = argparse.ArgumentParser(
        description="Analyze a paragraph of text and provide word statistics.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python paragraph.py "Hello world! Hello again!"
        """
    )
    parser.add_argument(
        "paragraph",
        type=str,
        help="Text paragraph to analyze. Enclose in quotes if it contains spaces."
    )
    
    try:
        args = parser.parse_args()
        total, unique, common, freq = analyze_text(args.paragraph)
        
        print("\nText Analysis Results:")
        print("-" * 20)
        print(f"Total words: {total}")
        print(f"Unique words: {unique}")
        print(f"Most frequent word: '{common}' (appears {freq} times)")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
