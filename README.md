### ukrainian_readability project

## 💡 Description of the Problem

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


## 📚 Data Source

The dataset used in this project is based on the Ukrainian Textbook Readability Dataset by
[Sergii Prykhodchenko](https://github.com/prykhodchenkosd/ukrtb).  
The original dataset includes linguistic statistics extracted from Ukrainian school textbooks
(Grades 1–9). It was used here under an open-source academic license for educational purposes.

All preprocessing, labeling, and level assignments (elementary → academic) were performed by me.


## 🧹 Data Preparation and Cleaning

Briefly:

* Combined and cleaned datasets from Grades 1–9
* Added difficulty level labels: Beginner → Academic
* Handled missing values in AvgWord in Syl using mean imputation
* Saved cleaned dataset as combined_clean.csv


## 📈 Exploratory Data Analysis (EDA)


Include combined image:

![Feature Distributions](images/feature_distributions.png)

### Pairplot Analysis


![Pairplot](images/pairplot.png)


## 🌡️ Correlation Heatmap Description

To identify relationships between features, I plotted a correlation heatmap of all numeric variables.
The analysis revealed strong positive correlations between features such as Words, Letters, and Sentences, which all reflect text length.
At the same time, AvgWord in Syl and AvgWord in Letters showed weaker correlations with other variables, indicating they capture distinct linguistic properties.

This confirmed that word-level features contribute unique information about text complexity, justifying their inclusion in the final model.

![Correlation Heatmap](images/correlation_heatmap.png)


## 🤖 Model Training and Results



## 🧩 Feature Importance Analysis



![Feature Importance](images/feature_importance.png)



## 🧮 Confusion Matrix and Evaluation



![Confusion Matrix](images/confusion_matrix.png)


## 🧰 Project Structure



```

midterm_project/
│
├── data/
│   ├── res1-5.xlsx
│   ├── res2_1-5.xlsx
│   ├── combined_clean.csv
│   └── README_data.md
│
├── EDA/
│   └── readability_EDA.ipynb
│
├── model/
│   └── ukrainian_readability_model.pkl
│
├── app/
│   ├── train.py
│   ├── predict.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── images/
│   ├── feature_distributions.png
│   ├── pairplot.png
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│
└── README.md

```



## 🐳 Docker Usage



## 🚀 Deployment

* Optional: URL or note that the service runs locally via Docker (127.0.0.1:8000)
* Add short explanation how to run it with docker run or uvicorn.


## 🙏 Acknowledgments

Dataset by [Sergii Prykhodchenko](https://github.com/prykhodchenkosd/ukrtb)
ML Zoomcamp by Alexey Grigorev
Special thanks for open educational resources and Ukrainian NLP community inspiration.


