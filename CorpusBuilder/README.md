# CorpusBuilder

A tiny corpus builder for preparing text datasets.

## Structure

```text
CorpusBuilder/
├── builder.py
├── config.py
└── README.md
```

## Features

- Load all `.txt` files from `RAW_DIR`
- Clean whitespace and line breaks
- Remove duplicate documents
- Save one merged dataset

## Usage

1. Put text files in the input folder.
2. Set paths in `config.py`.
3. Run:

```bash
python builder.py
```

The output dataset is saved to `OUTPUT_DIR / OUTPUT_FILE`.

## Pipeline

```text
Load files
    ↓
Clean text
    ↓
Remove duplicates
    ↓
Save dataset
```

## Note

This project stays intentionally small. Everything lives in `builder.py` to keep it easy to read and edit.