# PRODIGY_DS_04
### Sentiment Analysis on Twitter Data

Overview

This project performs sentiment analysis on a Twitter dataset using the VADER (Valence Aware Dictionary and sEntiment Reasoner) model from the NLTK library. The analysis includes:

### Data preprocessing

Sentiment score calculation

Data visualization (sentiment distribution, word clouds, and sentiment trends)

### Requirements

To run this project, install the following dependencies:
```bash
pip install pandas matplotlib seaborn wordcloud nltk
```

Additionally, ensure that NLTK's VADER model is downloaded:
```bash
import nltk
nltk.download('vader_lexicon')
```

## Dataset

The script uses a CSV file containing Twitter data. The dataset must be formatted with the following columns:

ID: Unique identifier for each tweet

Topic: The topic discussed in the tweet

Sentiment: Label indicating sentiment (e.g., Positive, Negative, Neutral)

Tweet: The tweet text

## Usage

Run the script using:
```bash
python taskds04.py
```

This will:

Load and preprocess the dataset

Apply sentiment analysis using VADER

Generate visualizations, including a sentiment distribution chart, word cloud, and sentiment score distribution

## Output

The script produces:

-- Sentiment Distribution
![Ouput](https://github.com/piscongentine/PRODIGY_DS_04/blob/main/Out3.png)

-- Word Cloud for Positive Tweets
![Ouput](https://github.com/piscongentine/PRODIGY_DS_04/blob/main/Out2.png)

--Sentiment Score Distribution
![Ouput](https://github.com/piscongentine/PRODIGY_DS_04/blob/main/Out1.png)

### Notes

Ensure the dataset is correctly formatted and available at the specified path.

Modify the file path in the script (file_path) to point to your dataset.

The script includes textual annotations with the label Piscongentine_man in visualizations.

## Author

Piscongentine_man
