### ukrainian_readability project

## Description of the problem

Although readability formulas such as *Flesch Reading Ease* and *Flesch-Kincaid Grade Level* exist for English and some other languages, Ukrainian currently lacks any established computational model to automatically assess text difficulty.
This creates challenges for Ukrainian language learners, teachers, and educational material developers, who have no objective way to evaluate whether a text is appropriate for a given proficiency level.

To address this gap, I used the Ukrainian Textbook Readability Dataset created by Sergii Prykhodchenko et al., which contains linguistic statistics extracted from Ukrainian school textbooks (Grades 1–9).
The original researchers focused on comparing various readability formulas, but their raw dataset also provides detailed structural features (word counts, sentence lengths, syllable counts, etc.).

In this project, I:

* Focused only on the raw linguistic features rather than the Flesch-style readability indices.
* Reorganized the data into five aggregated difficulty levels (Beginner → Academic).
* Performed feature analysis and model training using Random Forest and XGBoost classifiers.
* Achieved 95% accuracy in predicting the difficulty level of a given text passage.

This model can later be used to estimate the difficulty of Ukrainian texts for language learners, helping educators and developers automatically classify materials by reading level.


## Data Source

The dataset used in this project is based on the Ukrainian Textbook Readability Dataset by
[Sergii Prykhodchenko](https://github.com/prykhodchenkosd/ukrtb).  
The original dataset includes linguistic statistics extracted from Ukrainian school textbooks
(Grades 1–9). It was used here under an open-source academic license for educational purposes.

All preprocessing, labeling, and level assignments (elementary → academic) were performed by me.
