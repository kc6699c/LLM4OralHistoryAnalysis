from bertopic import BERTopic
import pandas as pd
from collections import Counter
import re

# CONFIG   
FILE_PATH = "FinalDataset_TopicClassification_Sentiment.csv"
TEXT_COLUMN = "Sentence"
SENTIMENT_COLUMN = "Sentiment"
CATEGORY_COLUMN = "Topic_Classification"

# Load Data
df = pd.read_csv(FILE_PATH)
df.dropna(subset=[TEXT_COLUMN], inplace=True)

results = []

# Run BERTopic Per Sentiment 
for sentiment in df[SENTIMENT_COLUMN].unique():
    print(f"\nProcessing sentiment: {sentiment}")
    df_sent = df[df[SENTIMENT_COLUMN] == sentiment]
    docs = df_sent[TEXT_COLUMN].astype(str).tolist()

    # Run BERTopic
    topic_model = BERTopic(language="english", verbose=False)
    topics, _ = topic_model.fit_transform(docs)

    df_sent = df_sent.copy()
    df_sent["BERTopic_Label"] = topics

    # Process each category
    for cat in sorted(df_sent[CATEGORY_COLUMN].unique()):
        df_cat = df_sent[df_sent[CATEGORY_COLUMN] == cat]
        topic_counts = df_cat["BERTopic_Label"].value_counts()

        word_counter = Counter()

        for topic_id, count in topic_counts.items():
            if topic_id == -1:
                continue
            topic_words = topic_model.get_topic(topic_id)
            for word, _ in topic_words[:10]:
                # Count how many times this word appears in this category's sentences
                pattern = re.compile(rf"\b{re.escape(word)}\b", flags=re.IGNORECASE)
                word_freq = sum(df_cat[TEXT_COLUMN].str.count(pattern))
                word_counter[word] += word_freq

        top_entities = word_counter.most_common(10)
        result_row = {
            "Sentiment": sentiment,
            "Category": f"Category {cat}",
        }
        for i, (word, freq) in enumerate(top_entities, 1):
            result_row[f"Top {i}"] = f"{word} ({freq})"
        results.append(result_row)

# Save to CSV   
output_df = pd.DataFrame(results)
output_df.to_csv("bertopic_entity_frequency_by_sentiment.csv", index=False)
print("Entity frequency analysis saved to 'bertopic_entity_frequency_by_sentiment.csv'")
