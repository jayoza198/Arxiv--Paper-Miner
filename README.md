
# 📚 Advanced arXiv Research Paper Miner

A **Streamlit-based research automation tool** that mines academic papers from **arXiv**, enriches them with **citations from Semantic Scholar**, applies **category & date filters**, performs **auto-topic tagging**, and exports results in **CSV format**.

Built for **researchers, PhD students, quants, and AI engineers** who want a fast, structured way to perform literature reviews.

---

## 🚀 Features

- 🔍 **Keyword-based paper search**
- 🗂 **arXiv category filtering**
  - `cs.AI`, `cs.LG`, `stat.ML`
  - `q-fin.EC`, `q-fin.TR`, `q-fin.ST`
- 📅 **Date range filtering**
- 📈 **Citation count via Semantic Scholar API**
- 🏷 **Automatic topic tagging**
- 📄 **Title, abstract, metadata extraction**
- ⬇️ **One-click CSV export**
- ⚡ **No API key required for arXiv**

---

## 🖥 Demo (Local)

streamlit run main.py


---

## 🏗 Project Structure


.
├── main.py                  # Streamlit application
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```



## 📦 Installation

### 1️⃣ Clone the Repository


git clone https://github.com/your-username/arxiv-paper-miner.git
cd arxiv-paper-miner


### 2️⃣ Create Environment (Recommended)


python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run main.py
```

---

## 🧪 Dependencies

```txt
streamlit
pandas
feedparser
requests
```

---

## 📊 Output CSV Columns

| Column           | Description                |
| ---------------- | -------------------------- |
| `title`          | Paper title                |
| `abstract`       | Paper abstract             |
| `published_date` | arXiv publication date     |
| `arxiv_id`       | arXiv identifier           |
| `paper_url`      | Direct arXiv link          |
| `citation_count` | Semantic Scholar citations |
| `auto_tags`      | Auto-generated topic tags  |
| `categories`     | arXiv categories           |

---

## 🔌 Data Sources

* **arXiv API** – [https://arxiv.org/help/api](https://arxiv.org/help/api)
* **Semantic Scholar API** – [https://api.semanticscholar.org](https://api.semanticscholar.org)

---

## 🧠 Auto-Tagging Logic

Auto-tags are generated using **keyword-based topic detection** across titles and abstracts.

Example:

* `reinforcement learning` → Reinforcement Learning
* `portfolio` → Quantitative Finance
* `llm`, `transformer` → Large Language Models

> Can be upgraded to **LLM-based tagging or embeddings**.

---

## ⚠️ Known Limitations

* Citation counts depend on Semantic Scholar availability
* arXiv API rate limits large batch requests
* Auto-tagging is rule-based (not semantic)

---

## 🛠 Roadmap

* [ ] Semantic search with embeddings
* [ ] BERTopic / topic modeling
* [ ] PDF auto-download
* [ ] Weekly scheduled literature mining
* [ ] FastAPI backend
* [ ] Docker support
* [ ] Multi-query batch mode

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

* arXiv.org
* Semantic Scholar
* Streamlit

---

## 👤 Author

**Jay Oza**
AI Research • Quantitative Finance • Automation Systems

---

> If you find this useful, please ⭐ the repository!

```

---

### 🔥 Optional Next
If you want, I can:
- Add **badges** (Python, Streamlit, License)
- Write a **paper-style README** (for arXiv / research repos)
- Create a **Docker-ready README**
- Make a **SaaS landing README**

Just tell me how public you want this repo to be.
```
