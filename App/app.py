import sys
import json
import pickle
import os
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout, QGridLayout,
    QLabel, QSpinBox, QComboBox, QDoubleSpinBox, QCheckBox, QPushButton,
    QDialog, QMessageBox
)

# --- 1. Import your new connecter file ---
import connecter 

class AnalysisDialog(QDialog):
    # ... (code for the dialog is unchanged) ...
    def __init__(self, result_text, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Analysis Result")
        self.setGeometry(300, 300, 300, 150) # x, y, w, h
        
        layout = QVBoxLayout()
        
        # --- Message Label ---
        self.message_label = QLabel(result_text)
        self.message_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.message_label.setWordWrap(True)
        
        # --- OK Button ---
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept) # .accept() closes the dialog
        
        # --- Assemble Layout ---
        layout.addWidget(self.message_label)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)


class FeatureTabApp(QWidget):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.setWindowTitle('Heart Disease Predictor')
        self.setGeometry(200, 200, 600, 450) # (x, y, width, height)
        
        # --- 2. Load the model using the connecter ---
        self.model = self.load_model()

        # ... (rest of your UI setup code is unchanged) ...
        # --- Create Main Layout and Tab Widget ---
        self.main_layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        
        # --- Create the "Patient Data" Tab ---
        # This 'tab' is just a blank QWidget that we'll add a layout to
        self.patient_tab = QWidget()
        self.tabs.addTab(self.patient_tab, "Patient Data Input")

        # Create a grid layout for the form
        grid_layout = QGridLayout()
        grid_layout.setSpacing(15) # Spacing between widgets
        
        # --- Column 1: Features 1-7 ---

        # 1. Age
        grid_layout.addWidget(QLabel("1. Age (years):"), 0, 0)
        self.age_input = QSpinBox()
        self.age_input.setRange(1, 120)
        self.age_input.setValue(50)
        grid_layout.addWidget(self.age_input, 0, 1)

        # 2. Sex
        grid_layout.addWidget(QLabel("2. Sex (1=male, 0=female):"), 1, 0)
        self.sex_input = QComboBox()
        self.sex_input.addItem("Female", 0) # (Display Text, data)
        self.sex_input.addItem("Male", 1)
        grid_layout.addWidget(self.sex_input, 1, 1)

        # 3. Chest Pain (cp)
        grid_layout.addWidget(QLabel("3. Chest Pain Type (cp):"), 2, 0)
        self.cp_input = QComboBox()
        self.cp_input.addItem("0: Typical angina", 0)
        self.cp_input.addItem("1: Atypical angina", 1)
        self.cp_input.addItem("2: Non-anginal pain", 2)
        self.cp_input.addItem("3: Asymptomatic", 3)
        grid_layout.addWidget(self.cp_input, 2, 1)

        # 4. Resting Blood Pressure (trestbps)
        grid_layout.addWidget(QLabel("4. Resting Blood Pressure (trestbps, mm Hg):"), 3, 0)
        self.trestbps_input = QSpinBox()
        self.trestbps_input.setRange(80, 220)
        self.trestbps_input.setValue(120)
        grid_layout.addWidget(self.trestbps_input, 3, 1)

        # 5. Cholesterol (chol)
        grid_layout.addWidget(QLabel("5. Serum Cholesterol (chol, mg/dl):"), 4, 0)
        self.chol_input = QSpinBox()
        self.chol_input.setRange(100, 600)
        self.chol_input.setValue(200)
        grid_layout.addWidget(self.chol_input, 4, 1)

        # 6. Fasting Blood Sugar (fbs)
        grid_layout.addWidget(QLabel("6. Fasting Blood Sugar > 120 (fbs, 1=T, 0=F):"), 5, 0)
        self.fbs_input = QCheckBox() # CheckBox is perfect for True/False
        grid_layout.addWidget(self.fbs_input, 5, 1)

        # 7. Resting ECG (restecg)
        grid_layout.addWidget(QLabel("7. Resting ECG Results (restecg):"), 6, 0)
        self.restecg_input = QComboBox()
        self.restecg_input.addItem("0: Nothing to note", 0)
        self.restecg_input.addItem("1: ST-T Wave abnormality", 1)
        self.restecg_input.addItem("2: Left ventricular hypertrophy", 2)
        grid_layout.addWidget(self.restecg_input, 6, 1)


        # --- Column 2: Features 8-13 ---
        # We'll put these in columns 2 (labels) and 3 (widgets)
        # We add a little minimum width to column 2 to create a gap
        grid_layout.setColumnMinimumWidth(2, 30)

        # 8. Max Heart Rate (thalach)
        grid_layout.addWidget(QLabel("8. Max Heart Rate Achieved (thalach):"), 0, 2)
        self.thalach_input = QSpinBox()
        self.thalach_input.setRange(70, 220)
        self.thalach_input.setValue(150)
        grid_layout.addWidget(self.thalach_input, 0, 3)

        # 9. Exercise Angina (exang)
        grid_layout.addWidget(QLabel("9. Exercise Induced Angina (exang, 1=Y, 0=N):"), 1, 2)
        self.exang_input = QCheckBox() # 0 = No (Unchecked), 1 = Yes (Checked)
        grid_layout.addWidget(self.exang_input, 1, 3)

        # 10. ST Depression (oldpeak)
        grid_layout.addWidget(QLabel("10. ST Depression (oldpeak):"), 2, 2)
        self.oldpeak_input = QDoubleSpinBox() # Use Double for floats
        self.oldpeak_input.setRange(0.0, 6.5)
        self.oldpeak_input.setSingleStep(0.1)
        grid_layout.addWidget(self.oldpeak_input, 2, 3)

        # 11. Slope
        grid_layout.addWidget(QLabel("11. Slope of Peak Exercise ST (slope):"), 3, 2)
        self.slope_input = QComboBox()
        self.slope_input.addItem("0: Upsloping", 0)
        self.slope_input.addItem("1: Flatsloping", 1)
        self.slope_input.addItem("2: Downsloping", 2)
        grid_layout.addWidget(self.slope_input, 3, 3)

        # 12. Major Vessels (ca)
        grid_layout.addWidget(QLabel("12. Major Vessels (ca, 0-3):"), 4, 2)
        self.ca_input = QSpinBox()
        self.ca_input.setRange(0, 3)
        grid_layout.addWidget(self.ca_input, 4, 3)

        # 13. Thalium Stress Test (thal)
        grid_layout.addWidget(QLabel("13. Thalium Stress Result (thal):"), 5, 2)
        self.thal_input = QComboBox()
        # Using the values you provided
        self.thal_input.addItem("1: Normal", 1)
        self.thal_input.addItem("3: Normal", 3)
        self.thal_input.addItem("6: Fixed defect", 6)
        self.thal_input.addItem("7: Reversible defect", 7)
        grid_layout.addWidget(self.thal_input, 5, 3)
        
        # --- Set the tab's layout ---
        self.patient_tab.setLayout(grid_layout)
        
        # --- Add a Submit Button (outside the tab) ---
        self.submit_button = QPushButton("Run Analysis")
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745; color: white;
                font-size: 14px; font-weight: bold;
                padding: 10px; border-radius: 5px;
            }
            QPushButton:hover { background-color: #218838; }
        """)
        
        # --- Finalize Main Layout ---
        self.main_layout.addWidget(self.tabs)
        self.main_layout.addWidget(self.submit_button)
        
        # --- Connect Signals ---
        self.submit_button.clicked.connect(self.run_prediction)
        
    def load_model(self):
        """
        Calls the connecter to get the model.
        """
        # --- 3. This is the "connection" ---
        model = connecter.get_model() 
        
        if model is None:
            # Show an error message if the model couldn't be loaded
            QMessageBox.critical(self, "Error", 
                                 "Could not load the model file.\n" \
                                 "Please check the console for details.")
            return None
        
        return model

    def collect_data(self):
        """
        Gathers all the data from the form fields
        and returns it as a dictionary.
        """
        data = {
            'age': self.age_input.value(),
            'sex': self.sex_input.currentData(), # .currentData() gets the (0, 1)
            'cp': self.cp_input.currentData(),
            'trestbps': self.trestbps_input.value(),
            'chol': self.chol_input.value(),
            'fbs': 1 if self.fbs_input.isChecked() else 0,
            'restecg': self.restecg_input.currentData(),
            'thalach': self.thalach_input.value(),
            'exang': 1 if self.exang_input.isChecked() else 0,
            'oldpeak': self.oldpeak_input.value(),
            'slope': self.slope_input.currentData(),
            'ca': self.ca_input.value(),
            'thal': self.thal_input.currentData()
        }
        
        # Print the collected data to the console in a clean format
        print("--- Patient Data Collected ---")
        print(json.dumps(data, indent=2))
        print("-------------------------------")
        return data

    def run_prediction(self):
        """
        Gathers all data, formats it for the model,
        and runs the prediction.
        """
        if self.model is None:
            print("Model is not loaded. Aborting prediction.")
            QMessageBox.warning(self, "Error", "Model is not loaded. Cannot run analysis.")
            return

        # 1. Get data from the form
        data_dict = self.collect_data()
        
        # 2. Format data for the model
        # The model expects a 2D array in the *exact* feature order.
        # list(data_dict.values()) works because we defined the
        # dictionary in the correct 1-13 order.
        try:
            feature_values = list(data_dict.values())
            input_data = np.array(feature_values).reshape(1, -1) # (1, 13)
        
            # 3. Make prediction
            prediction = self.model.predict(input_data)
            result = prediction[0] # Get the first (and only) prediction

            # 4. Create result text
            # (Assuming 1 = Heart Disease, 0 = No Heart Disease)
            if result == 1:
                result_text = "Analysis Result: High Risk of Heart Disease."
            else:
                result_text = "Analysis Result: Low Risk of Heart Disease."
        
        except Exception as e:
            print(f"Error during prediction: {e}")
            result_text = f"Error: Could not make a prediction.\n{e}"

        # 5. Show result dialog
        dialog = AnalysisDialog(result_text, self)
        dialog.exec_() # .exec_() shows the dialog as a modal window

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion') # Use a clean, modern style
    
    window = FeatureTabApp()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

