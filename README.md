
# 🏥 Medical Insurance Charges Prediction – Flask Web App

A complete Flask-based web application that predicts **medical insurance charges** using a Machine Learning model.
The application includes:

✔ User Registration
✔ User Login (JWT Authentication)
✔ Dynamic Prediction Form (Categorical dropdowns populated via APIs)
✔ ML Model Prediction (Age, BMI, Gender, Smoker, Region, Children)
✔ Secure API Endpoints
✔ Frontend UI (HTML + CSS)
✔ Background Images for Visualization

---

## 📂 Project Structure

```
project/
│
├── artifacts/
│   ├── label_encoded_data.json
│   └── Linear_reg_model.pkl
│
├── src/
│   ├── database.py
│   └── utils.py
│
├── static/
│   └── images/
│        └── medical_ins1.webp
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── prediction.html
│
├── config.py
├── main.py
└── README.md
```

---

# 🚀 Features

### 🔐 Authentication

* User registration
* User login with **JWT-based authentication**
* Token stored securely in browser `localStorage`

### 📊 Prediction

* Predicts **medical insurance charges**
* Inputs:

  * Age
  * BMI
  * Gender (fetched dynamically)
  * Smoker status (fetched dynamically)
  * Region (fetched dynamically)
  * Number of children

### 🌐 Frontend (UI)

* Clean, centered form UI
* Background medical-themed image
* Dynamic dropdowns and radio buttons
* Same-page prediction output

### 🧠 Machine Learning

* Linear Regression model
* Preprocessed & label-encoded data stored in artifacts

---

# ⚙️ Tech Stack

| Component  | Technology                  |
| ---------- | --------------------------- |
| Backend    | Flask                       |
| Auth       | Flask-JWT-Extended          |
| Frontend   | HTML + CSS + JS             |
| ML         | Scikit-Learn                |
| Database   | MongoDB (via `database.py`) |
| Deployment | Local server / Cloud-ready  |

---

# 🛠️ Installation & Setup

### ✔ 1. Clone the Repository

```bash
git clone <your_repo_link>
cd project
```

---

### ✔ 2. Create & Activate Virtual Environment

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ✔ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, use:

```bash
pip install flask flask-jwt-extended pymongo scikit-learn
```

---

### ✔ 4. Configure `config.py`

Example:

```python
FLASK_PORT_NUMBER = 5000
MONGO_CONNECTION = "mongodb://localhost:27017"
DATABASE_NAME = "medical_insurance"
COLLECTION_NAME = "users"
```

Adjust as per your environment.

---

### ✔ 5. Start the App

```bash
python main.py
```

The app will run at:

```
http://127.0.0.1:5000/
```

---

# 🔗 Application Flow

### 🏁 1. Login Page

```
/
```

Users can log in or navigate to the registration page.

---

### 📝 2. Registration Page

```
/register_page
```

After successful registration, user can return to login.

---

### 🎯 3. Prediction Page

```
/prediction
```

Automatically loads **Gender**, **Smoker**, and **Region** options using JWT-authenticated APIs.

User enters details → prediction result shown on same page.

---

# 📡 API Endpoints

### 🔍 Authentication APIs

#### **POST /register**

Registers a new user
**Body:**

* user_name
* password
* email_id
* contact_number
* dob

---

#### **POST /login**

Returns JWT token
**Body:**

* user_name
* password

---

### 🔧 Utility APIs (JWT Required)

#### **GET /gender_options**

Returns available gender options from stored JSON.

#### **GET /smoker_options**

Returns smoker options.

#### **GET /region_options**

Returns region names derived from model features.

---

### ⚙️ Prediction API

#### **POST /prediction_api**

Requires Authorization: `Bearer <token>`

**Body (FormData):**

| Field    | Type   | Description         |
| -------- | ------ | ------------------- |
| age      | number | Person's age        |
| bmi      | number | Body Mass Index     |
| gender   | string | male/female         |
| smoker   | string | yes/no              |
| region   | string | 4 region categories |
| children | number | 0–6                 |

**Response:**

```json
{
  "result": "Predicted Medical insurance charges is: 15342.50"
}
```

---

# 🖼 UI Enhancements

All pages include a medical-themed background:

```css
background: url('/static/images/medical_ins1.webp') no-repeat center center fixed;
background-size: cover;
```

Forms have:

* Glass effect (blur)
* Centered layout
* Smooth border-radius
* Shadow

---

# 📘 How Machine Learning Works

### Model:

* A **Linear Regression model** trained on medical insurance dataset
* Stored in:

  ```
  artifacts/Linear_reg_model.pkl
  ```
* Features engineered and label-encoded using:

  ```
  artifacts/label_encoded_data.json
  ```

### Prediction Pipeline:

1. Receive form values
2. Load JSON mapping
3. Convert categorical → numerical
4. Load saved ML model
5. Predict insurance charges
6. Return formatted result

---

# 🧪 Testing Steps

1. Register a user
2. Login → receive JWT
3. Access `/prediction`
4. Check API calls in browser DevTools → Network
5. Test prediction with multiple inputs
6. If model loads successfully → prediction works

---

# 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first to discuss what you’d like to improve.

---

# 📜 License

This project is open-source and free to use.
