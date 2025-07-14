import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from collections import defaultdict, Counter
import re
import torch
print("CUDA Available:", torch.cuda.is_available())
print("CUDA Device Count:", torch.cuda.device_count())
print("Device Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load dataset
df = pd.read_csv("FinalDataset_TopicClassification_Sentiment.csv")

# Map topic codes to readable labels
topic_map = {
    0: "Biographical Info",
    1: "Life Before Incarceration",
    2: "Life During Incarceration",
    3: "Military Service",
    4: "Post-War Return",
    5: "Peace & Justice",
    6: "Unclassified"
}
df["Category"] = df["Topic_Classification"].map(topic_map)

# Load pretrained BERT NER model
model_name = "dslim/bert-base-NER"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name).to(device)
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer,
                        aggregation_strategy="simple", device=0 if torch.cuda.is_available() else -1)

# Domain-specific entities
custom_domain_patterns  = {
    "CAMP": [
        "Manzanar", "Tule Lake", "Poston", "Topaz", "Minidoka", "Gila River", "Heart Mountain",
        "Rohwer", "Jerome", "Amache", "Granada", "Santa Anita", "Tanforan", "Pinedale", "Pomona"
    ],
    "POLICY": [
        "Executive Order 9066", "curfew order", "relocation", "forced removal", "internment",
        "exclusion zone", "mass incarceration", "evacuation", "military exclusion"
    ],
    "ORG": [
        "War Relocation Authority", "WRA", "Department of Justice", "DOJ", "FBI", "ACLU",
        "Japanese American Citizens League", "JACL", "U.S. Army", "War Department"
    ],
    "EVENT": [
        "redress movement", "wartime hysteria", "resettlement", "evacuation", "apology",
        "compensation", "civil rights violation", "petition", "sit-in", "protest"
    ],
    "PROGRAM": [
        "loyalty questionnaire", "registration", "segregation", "enlistment drive",
        "resettlement program", "Nisei soldiers"
    ],
    "LAW": [
        "Civil Liberties Act", "Public Law 100-383", "court case", "legal challenge", "Supreme Court"
    ],
    "TIME_PERIOD": [
        "1942", "1943", "1945", "post-war", "pre-war", "1988", "World War II", "WWII", "wartime"
    ],
    "MOVEMENT": [
        "forced relocation", "train relocation", "bus relocation", "exile", "repatriation"
    ],
    "MILITARY_UNIT": [
        "442nd Regimental Combat Team", "MIS", "Military Intelligence Service", "100th Battalion"
    ],
    "SYMBOLIC_OBJECT": [
        "barbed wire", "guard tower", "watchtower", "fence", "searchlight"
    ],
    "REDRESS": [
        "apology", "reparations", "compensation", "acknowledgment", "official apology"
    ],
    "PROTEST": [
        "petition", "protest", "sit-in", "court appeal", "march", "advocacy"
    ],
    "GOV_AGENCY": [
        "Department of Justice", "War Department", "U.S. Army", "WRA", "FBI"
    ],
    "LOCATION": [
        "California", "Wapato", "Fresno", "Salem", "Seattle", "Los Angeles", "Hawaii", "Japan", "Washington"
    ]
}

# Convert to lowercase matcher set
custom_lookup = {k: set(map(str.lower, v)) for k, v in custom_domain_patterns.items()}

# Initialize frequency counter
entity_freq = defaultdict(Counter)

# Process sentences
for _, row in df.iterrows():
    sentence = row["Sentence"]
    category = row["Category"]
    sentiment = row["Sentiment"]

    # BERT-based standard NER extraction
    bert_entities = ner_pipeline(sentence)
    for ent in bert_entities:
        entity_text = ent['word'].strip()
        entity_type = ent['entity_group']
        if len(entity_text) >= 3:
            entity_freq[(category, sentiment, entity_type)][entity_text] += 1

    # Rule-based domain NER (you will fill in the values above)
    for label, terms in custom_lookup.items():
        for match in terms:
            if re.search(rf"\b{re.escape(match)}\b", sentence, re.IGNORECASE):
                entity_freq[(category, sentiment, label)][match] += 1

# Convert frequency results to DataFrame
rows = []
for (cat, sent, etype), counter in entity_freq.items():
    for ent_text, freq in counter.items():
        rows.append({
            "Category": cat,
            "Sentiment": sent,
            "Entity_Type": etype,
            "Entity": ent_text,
            "Frequency": freq
        })

df_freq = pd.DataFrame(rows)

# Save both files
df_freq.to_csv("Entity_Frequencies_All.csv", index=False)

print("All entities saved to: Entity_Frequencies_All.csv")
