
---

# Vertical Federated Learning (VFL)

**Privacy-Preserving Machine Learning for Collaborative Intelligence**

---

###  Overview

This project demonstrates an implementation of **Vertical Federated Learning (VFL)** — a privacy-preserving machine learning technique that allows **multiple organizations or entities to collaboratively train a shared model without exchanging raw data**.

Unlike traditional centralized training, where all data must be aggregated, VFL enables **feature-partitioned datasets** (different parties hold different attributes about the same users) to contribute to model learning securely and efficiently.

The project focuses on **ethical AI, data governance, and regulatory compliance (GDPR)** while ensuring model performance through secure communication and joint gradient computation.

---

### Concept

In **Vertical Federated Learning**, data is distributed *vertically* across institutions — meaning:

* Each participant owns **different features** for the **same set of entities**.
* A **common ID** field is shared to align records across datasets.
* Parties train a shared model by exchanging **encrypted intermediate gradients**, never exposing raw features or labels.

This project simulates such collaboration between **two parties (Party A and Party B)** using synthetic data.

---

###  Project Structure

```
vertifcal-federated-learning/
│
├── vfl/
│   ├── vfl-1.ipynb          # Simulates Party A (holds partial features)
│   ├── vfl-2.ipynb          # Simulates Party B (holds complementary features)
│
├── output/
│   ├── dataset1.csv         # Dataset for Party A
│   ├── dataset2.csv         # Dataset for Party B
│
├── generate.py              # Script for synthetic data generation
├── cyber-lab-dtc.ipynb      # Decision tree classifier experiment
└── README.md
```

---

### Dataset Description

#### **dataset1.csv** – *(Party A)*

| Column    | Description                                               |
| :-------- | :-------------------------------------------------------- |
| `dr`      | Derived risk or behavioral metric                         |
| `id`      | Common identifier across datasets                         |
| `x0`–`x9` | Local feature columns representing user/system attributes |

#### **dataset2.csv** – *(Party B)*

| Column | Description                                      |
| :----- | :----------------------------------------------- |
| `ar`   | Activity rate (auxiliary feature)                |
| `id`   | Common identifier (shared with dataset1)         |
| `fr`   | Fraud label (1 = Fraudulent, 0 = Non-fraudulent) |

These datasets represent **different data holders** collaborating on a **shared fraud detection model**.

---

---

### How to Run

#### 1. Generate Synthetic Datasets

```bash
python generate.py --size 1000 --output-dir output
```

This creates:

* `dataset1.csv` (Party A data)
* `dataset2.csv` (Party B data)

#### 2. Train and Simulate Federated Learning

* Open `vfl/vfl-1.ipynb` and `vfl/vfl-2.ipynb` in Jupyter.
* Run both notebooks separately to simulate the collaboration between two institutions.
* The shared gradients emulate the **secure learning pipeline** of VFL.

---

### Sample Output

```
Generated first dataset with 1000 records: output/dataset1.csv
Generated second dataset with 1000 records: output/dataset2.csv

Dataset statistics:
Total records: 1000
Fraudulent records: 287 (28.70%)
Non-fraudulent records: 713 (71.30%)
```

---


### Applications

This approach supports **cross-institutional collaboration** where direct data sharing is restricted, such as:

* **Finance** – Joint fraud detection across banks
* **Healthcare** – Shared diagnostics between hospitals
* **Cybersecurity** – Distributed anomaly detection
* **Education** – Federated student performance analysis

It embodies the future of **trustworthy and ethically governed AI**.

---

### Research Relevance

Vertical Federated Learning advances **AI governance**, **data ethics**, and **compliance-aware AI systems**.
The model respects **privacy-by-design** principles while enabling data-driven innovation — a foundation for trustworthy AI ecosystems under the **EU AI Act** and **GDPR**.

---

### Future Enhancements

* Integration with **Homomorphic Encryption** for secure gradient computation
* Extension to **multi-party VFL** beyond two nodes
* Incorporation of **Explainable AI (XAI)** for interpretability
* Real-world federated datasets for validation

---





