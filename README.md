# Customer Shopping Sales Prediction Web App 🚀📊

An interactive Streamlit web dashboard designed to forecast shopping sales, display key performance indicators (KPIs), and process customer order inputs in real-time.

---

## 🖥️ Dashboard Features & UI Layout

* **Key Performance Indicators (KPI Cards)**:
  * **Total Customers**: Live customer count overview.
  * **Total Revenue**: Comprehensive revenue tracking in local currency ($\text{₹}$).
  * **Total Expense**: Calculated operational expenses.
  * **Total Profit**: Real-time gross profit metrics with distinct color coding.
* **Interactive Prediction Form**: Input parameters across multiple input fields to estimate sales revenue:
  * `Product Name`
  * `How much Quantity needed?`
  * `Cost per unit`
  * `Department`
  * `City`
  * `Mode of Payment`

---

## 📁 Project Structure

```text
customer_shopping_prediction_web/
│
├── app.py                            # Streamlit web application entry script
├── Customer_Shopping_Prediction.ipynb# Notebook containing EDA and model development
├── sales_prediction_rf_model.pkl    # Serialized Machine Learning model (Random Forest / DT)
├── requirements.txt                  # Python package dependencies
└── README.md                         # Project documentation
```

---

## 🛠️ Tech Stack & Prerequisites

* **Frontend/Dashboard**: [Streamlit](https://streamlit.io/)
* **Data Processing**: `pandas`, `numpy`, `openpyxl`
* **Machine Learning & Modeling**: `scikit-learn`
* **Styling**: Custom CSS injection (`st.markdown`) for card metrics and header padding adjustments

---

## 🚀 Local Installation & Setup

Follow these steps to set up and execute the Streamlit application locally:

### 1. Set Up Virtual Environment

```bash
# Clone the repository
git clone https://github.com/csathishit89/customer_shopping_prediction_web.git
cd customer_shopping_prediction_web

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell / CMD):
venv\Scripts\activate

# macOS / Linux:
source venv/bin/activate
```

### 2. Install Required Dependencies

```bash
pip install streamlit pandas numpy openpyxl scikit-learn
```

### 3. Launch the Application

```bash
streamlit run app.py
```

Once executed, open your web browser and navigate to `http://localhost:8501`.

---

## 👤 Author

* **Sathish Chandrasekar**
  * GitHub: [@csathishit89](https://github.com/csathishit89)