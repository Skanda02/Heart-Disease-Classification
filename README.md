# Heart-Disease-Classification
Predicting heart disease using machine learning

*This notebook contains the information I learned from the course:*  
[Course Link](https://www.udemy.com/share/102vAM3@Is9tP5bT9ywhTr2HBL2CgBmp9AXdZ3teTMchBf_cXAw38OEv12XISZv7TcAU9YWGrQ==/)

---
** Project Structure**

```
Heart-Disease-Classification/
│
├── App/
│   ├── app.py                      # Main application (UI / API / interface)
│   └── connecter.py                # Handles database or model connections
│
├── Dataset/
│   └── heart-disease.csv           # Main dataset file
│
├── Model/
│   └── logistic_regression_model.pkl  # Saved trained model
│
├── Notebook/
│   └── Heart-Disease-Classification.ipynb  # Jupyter notebook for analysis
│
├── README.md                       # Project overview and usage instructions
└── requirements.txt                 # Dependencies list

```

## The Approach we will be following :

|-- 1. Problem definition <br>
|-- 2. Data <br>
|-- 3. Evaluation <br>
|-- 4. Features <br>
|-- 5. Modelling <br>
|-- 6. Experimentation <br>

---

## 1. Problem Definition
"Given clinical parameters about a patient, can we predict whether or not they have heart disease?"

---

## 2. Data
The original data came from the **Cleveland dataset** from the UCI Machine Learning Repository.  
[UCI Repository Link](https://archive.ics.uci.edu/ml/datasets/heart+Disease)  

There is also a version of it available on **Kaggle**:  
[Kaggle Dataset Link](https://www.kaggle.com/datasets/sumaiyatasmeem/heart-disease-classification-dataset)

---

## 3. Evaluation
Since this is related to the **health sector**, we need **high accuracy**.  
If we achieve **95% accuracy**, we will consider the effort worth it (maybe or maybe not).

---

## 4. Features
1. **age** - age in years  

2. **sex** - (1 = male; 0 = female)  

3. **cp** - chest pain type  
   - 0: Typical angina → chest pain related to decreased blood supply to the heart  
   - 1: Atypical angina → chest pain not related to the heart  
   - 2: Non-anginal pain → typically esophageal spasms (non-heart related)  
   - 3: Asymptomatic → chest pain not showing signs of disease  

4. **trestbps** - resting blood pressure (in mm Hg on admission to the hospital)  
   - Anything above 130–140 is typically cause for concern  

5. **chol** - serum cholesterol in mg/dl  
   - serum = LDL + HDL + 0.2 * triglycerides  
   - Above 200 is cause for concern  

6. **fbs** - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)  
   - '>126' mg/dL signals diabetes  

7. **restecg** - resting electrocardiographic results  
   - 0: Nothing to note  
   - 1: ST-T Wave abnormality  
     - Can range from mild symptoms to severe problems  
     - Signals non-normal heartbeat  
   - 2: Possible or definite left ventricular hypertrophy  
     - Enlarged heart's main pumping chamber  

8. **thalach** - maximum heart rate achieved  

9. **exang** - exercise induced angina (1 = yes; 0 = no)  

10. **oldpeak** - ST depression induced by exercise relative to rest  
    - Looks at stress of heart during exercise  
    - Unhealthy heart will stress more  

11. **slope** - the slope of the peak exercise ST segment  
    - 0: Upsloping → better heart rate with exercise (uncommon)  
    - 1: Flatsloping → minimal change (typical healthy heart)  
    - 2: Downsloping → signs of unhealthy heart  

12. **ca** - number of major vessels (0–3) colored by fluoroscopy  
    - Colored vessel means the doctor can see the blood passing through  
    - The more blood movement, the better (no clots)  

13. **thal** - thalium stress result  
    - 1, 3: Normal  
    - 6: Fixed defect → used to be defect but okay now  
    - 7: Reversible defect → no proper blood movement when exercising  

14. **target** - whether the patient has disease or not  
    - 1 = Yes  
    - 0 = No  
    - *(Predicted attribute)*  
---
##  How to Use the App

### Step 1: Clone the Repository
- Run the following command in your terminal 
```bash
git clone https://github.com/Skanda02/Heart-Disease-Classification.git
```

---
### Step 2: Create a Virtual Environment
- On macOS / Linux:

```bash
python3 -m venv .venv
```
- On Windows:

```bash
python -m venv .venv
```
---
### Step 3: Activate the Virtual Environment and Install Dependencies
Activate the environment:

- macOS / Linux:
```bash
source .venv/bin/activate
```
- Windows:
```bash
.venv\Scripts\activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```
---
### Step 4: Run the App

Start the application by running:
- macOS / Linux
```bash
python3 app.py
```
- Windows
```bash
python app.py
```
---
