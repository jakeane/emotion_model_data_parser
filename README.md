# Emotion Model Data Parser

## Data Files

- `/data`: Raw data from empathetic dialogues

- `/output16`: Data and emotion file for 16-emotion model

  - Necessary files
    - `train.tsv` `test.tsv`, and `dev.tsv` for general Data
    - `emotions.txt` for mapping emotions to id numbers
    - `sentiment_dict.json` to map emotions to positive/neutral/negative

- `/output32`: Data and emotion file for 32-emotion model
  - Necessary files
    - `train.tsv` `test.tsv`, and `dev.tsv` for general Data
    - `emotions.txt` for mapping emotions to id numbers
    - `sentiment_dict.json` to map emotions to positive/neutral/negative

## Data Formatting

- `train.tsv` `test.tsv`, and `dev.tsv`
  - Three columns, separated by tabs, with no headers
    - text: what the user says
    - emotion: number representing emotion of text
    - id: arbitrary id, does not really matter

## Running parser

In the terminal, run: `python3 tsv_parser.py -i <inputdir> -o <outputdir>`

`inputdir` will likely be `/data` unless additional data is found, and `outputdir` is where `*.tsv` and `emotions.txt` will be outputted. `sentiment_dict.json` will have to be done manually at this point.
