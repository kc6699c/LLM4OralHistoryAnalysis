# LLM4OralHistoryAnalysis
**Evaluating Large Language Models for Understanding Oral History Through Text Classification and Sentiment Analysis**



## Historical Context
The Japanese attack on Pearl Harbor on December 7, 1941, marked the United States’ entry into World War II and triggered widespread suspicion, fear, and discriminatory actions against Japanese Americans. On February 19, 1942, President Franklin D. Roosevelt signed Executive Order 9066, authorizing the U.S. military to create exclusion zones and forcibly remove individuals deemed security risks. This led to the mass incarceration of approximately 120,000 people of Japanese ancestry, the majority of whom were U.S. citizens. Japanese Americans were removed from their homes in California, Oregon, Washington, and Arizona. Initially confined in temporary “assembly centers”—often repurposed racetracks or fairgrounds—they were later transferred to ten more permanent and remote “relocation centers” across the interior U.S. These included Tule Lake and Manzanar (California); Gila River and Poston (Arizona); Jerome and Rohwer (Arkansas); Minidoka (Idaho); Topaz (Utah); Heart Mountain (Wyoming); and Granada (Colorado).

Families were given only days to pack, often losing their homes, farms, and businesses. Living conditions in the camps were harsh, with poorly insulated barracks and limited resources. Nearly 70,000 of those incarcerated were American citizens, yet no charges of disloyalty were filed, and no legal mechanism existed to challenge their detention. In the post-war years, public narratives began to shift. While early portrayals emphasized patriotism—especially through the heroism of the 442nd Regimental Combat Team, the most decorated unit in U.S. military history—the 1970s and 1980s witnessed a growing movement demanding redress. This culminated in the Civil Liberties Act of 1988, which issued a formal government apology and provided financial reparations to surviving victims.

One of the most significant preservation efforts is the [Densho Project](https://densho.org), founded in 1995. “Densho,” meaning “to pass on to the next generation,” curates an extensive digital archive of over 900 oral history interviews, ensuring that the voices and experiences of those unjustly incarcerated are preserved and made accessible for future generations.

## Research Design Overview
<p align="center"> <img src="images/pipeline_overview.png" alt="Annotation and Evaluation Pipeline Overview" width="600"/> </p>
The figure above illustrates our complete annotation and evaluation pipeline for analyzing Japanese-American incarceration oral histories using large language models (LLMs). This repository provides access to the annotated dataset, prompt templates, model outputs, and evaluation scripts used in our large-scale sentence-level classification and sentiment analysis experiments.
