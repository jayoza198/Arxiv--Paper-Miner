import streamlit as st
import pandas as pd
import feedparser
import urllib.parse
import requests
from datetime import datetime

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(page_title="Advanced arXiv Paper Miner", layout="wide")

st.title("📚 Advanced arXiv Research Paper Miner")
st.caption("Category filtering • Date filtering • Citation counts • Auto-tagging")

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------
st.sidebar.header("🔍 Search Filters")

query = st.sidebar.text_input(
    "Search Query",
    placeholder="e.g. deep reinforcement learning portfolio optimization"
)

categories = st.sidebar.multiselect(
    "arXiv Categories",
    [
        "cs.AI", "cs.LG", "cs.CL",
        "q-fin.EC", "q-fin.TR", "q-fin.ST",
        "stat.ML", "math.OC", "econ.TH"
    ],
    default=[]
)

start_date = st.sidebar.date_input("Start Date", value=datetime(2018, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime.today())

max_results = st.sidebar.number_input(
    "Max Papers",
    min_value=1,
    max_value=2000,
    value=30,
    step=5
)

run_search = st.sidebar.button("🚀 Run Miner")

# -------------------------------------------------
# Semantic Scholar Citation Fetch
# -------------------------------------------------
def fetch_citation_count(arxiv_id):
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=citationCount"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json().get("citationCount", 0)
    except:
        pass
    return 0

# -------------------------------------------------
# Auto-Tagging Logic (Rule-Based, Fast)
# -------------------------------------------------
def auto_tag_paper(text):
    tags = []

    tag_map = {
        "reinforcement learning": "Reinforcement Learning",
        "deep learning": "Deep Learning",
        "portfolio": "Quant Finance",
        "trading": "Algorithmic Trading",
        "option": "Derivatives",
        "llm": "Large Language Models",
        "transformer": "Transformers",
        "time series": "Time Series",
        "volatility": "Risk Modeling"
    }

    text_lower = text.lower()

    for keyword, tag in tag_map.items():
        if keyword in text_lower:
            tags.append(tag)

    return ", ".join(set(tags)) if tags else "General Research"

# -------------------------------------------------
# arXiv Fetch Function
# -------------------------------------------------
def fetch_arxiv_papers(query, categories, max_results):
    base_url = "http://export.arxiv.org/api/query?"
    encoded_query = urllib.parse.quote(query)

    category_filter = ""
    if categories:
        category_filter = "+AND+(" + " OR ".join([f"cat:{c}" for c in categories]) + ")"

    query_url = (
        f"{base_url}"
        f"search_query=all:{encoded_query}{category_filter}"
        f"&start=0"
        f"&max_results={max_results}"
        f"&sortBy=submittedDate"
        f"&sortOrder=descending"
    )

    feed = feedparser.parse(query_url)
    papers = []

    for entry in feed.entries:
        published_date = datetime.strptime(entry.published[:10], "%Y-%m-%d").date()

        if not (start_date <= published_date <= end_date):
            continue

        arxiv_id = entry.id.split("/abs/")[-1]

        citation_count = fetch_citation_count(arxiv_id)

        combined_text = entry.title + " " + entry.summary
        tags = auto_tag_paper(combined_text)

        papers.append({
            "title": entry.title.replace("\n", " ").strip(),
            "abstract": entry.summary.replace("\n", " ").strip(),
            "published_date": published_date,
            "arxiv_id": arxiv_id,
            "paper_url": entry.link,
            "citation_count": citation_count,
            "auto_tags": tags,
            "categories": ", ".join(entry.tags[i]["term"] for i in range(len(entry.tags)))
        })

    return papers

# -------------------------------------------------
# Run Search
# -------------------------------------------------
if run_search:
    if not query.strip():
        st.warning("Please enter a search query.")
    else:
        with st.spinner("Mining arXiv and enriching metadata..."):
            results = fetch_arxiv_papers(query, categories, max_results)

        if not results:
            st.error("No papers found with the selected filters.")
        else:
            df = pd.DataFrame(results)
            df = df.sort_values("citation_count", ascending=False)

            st.success(f"Found {len(df)} papers")

            st.dataframe(df, use_container_width=True, height=500)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇️ Download CSV",
                csv,
                "arxiv_research_papers_enriched.csv",
                "text/csv"
            )

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("---")
st.caption("arXiv API • Semantic Scholar API • Built for Research Automation")
