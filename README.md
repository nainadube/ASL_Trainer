# ASL Trainer 🤟

**ASL Trainer** is an intelligent Sign Language Recognition system designed to recognize and interpret American Sign Language (ASL) gestures using computer vision and deep learning.

---

## 📁 Project Structure

```
ASL_Trainer/
│
├── dataset/            # Raw and processed gesture datasets
├── notebooks/          # Jupyter notebooks for experiments & exploration
│   └── 01_dataset_exploration.ipynb
├── models/             # Trained models, checkpoints, and weights
├── src/                # Core source code and utilities
├── app/                # Application entry points (e.g., Streamlit, FastAPI, or GUI)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/nainadube/ASL_Trainer.git
cd ASL_Trainer
```

### 2. Prerequisites
- Python 3.9+ recommended

### 3. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Notebooks
```bash
jupyter notebook notebooks/01_dataset_exploration.ipynb
```

---

## 📌 Development Roadmap
- [x] **Day 1**: Project structure setup & Dataset Exploration
- [ ] **Day 2**: Data preprocessing & Keypoint Extraction (MediaPipe / OpenCV)
- [ ] **Day 3**: Feature engineering & Model architecture design
- [ ] **Day 4**: Model training & Evaluation
- [ ] **Day 5**: Real-time webcam inference application

