from pathlib import Path

from config import RAW_DIR, OUTPUT_DIR, OUTPUT_FILE


def load_files():
    """Load all .txt files from RAW_DIR."""
    pass


def clean_text(text):
    """Normalize text."""
    pass


def remove_duplicates(texts):
    """Remove duplicate entries."""
    pass


def save_dataset(text):
    """Save dataset to OUTPUT_DIR."""
    pass


def main():
    print("CorpusBuilder")

    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    texts = load_files()
    texts = [clean_text(t) for t in texts]
    texts = remove_duplicates(texts)

    save_dataset("\n".join(texts))

    print("Done.")


if __name__ == "__main__":
    main()
