# OTT Rating Analysis using Python

## 1. Project Overview
OTT Rating Analysis is a beginner-friendly data analysis project that studies ratings of movies and shows available on Over-The-Top (OTT) streaming platforms. It uses **Python, Pandas, and NumPy** to clean, organize, summarize, and analyze the dataset.

The project is intentionally **text-based**. It does not use Matplotlib, Seaborn, Plotly, charts, or graphs. Results are displayed as readable console summaries and tables.

> **Dataset note:** `data/ott_ratings.csv` is a small illustrative sample dataset created for demonstrating the project workflow. Its values are not official platform ratings. Replace it with a properly sourced dataset for real-world conclusions.

## 2. Objectives
- Understand the structure and quality of an OTT ratings dataset.
- Clean missing, invalid, and duplicate records.
- Calculate overall rating statistics.
- Compare platforms by average rating, title count, and votes.
- Identify highly rated and low-rated titles.
- Compare ratings across genres, release years, and countries.
- Use NumPy for numerical summaries such as standard deviation and percentiles.

## 3. Tools and Technologies
- **Python 3.9 or newer**
- **Pandas** — data loading, cleaning, grouping, and tabular summaries.
- **NumPy** — numerical calculations and statistical measures.

## 4. Project Structure
```text
ott_rating_analysis/
├── data/
│   └── ott_ratings.csv
├── src/
│   └── analysis.py
├── README.md
└── requirements.txt
```

## 5. Dataset Description
The sample CSV contains these columns:

| Column | Description |
|---|---|
| `title` | Name of the movie or show |
| `platform` | OTT service name |
| `genre` | Main genre |
| `release_year` | Year of release |
| `rating` | Rating on a 0–10 scale |
| `votes` | Number of user votes |
| `country` | Country associated with the title |

## 6. Analysis Performed
1. **Data loading and validation:** checks required columns and reports a clear error if any are missing.
2. **Data cleaning:** trims text fields, converts numeric columns, removes incomplete or invalid rows, and removes duplicate title/platform entries.
3. **Dataset overview:** reports the number of titles, platforms, genres, countries, year range, average rating, median rating, and average votes.
4. **Top-rated titles:** lists up to ten titles ranked by rating, using votes as a tie-breaker.
5. **Platform analysis:** compares title counts, average and median ratings, and vote totals.
6. **Genre analysis:** summarizes title counts, average ratings, and total votes by genre.
7. **Year analysis:** compares title counts and average ratings by release year.
8. **Country analysis:** summarizes title counts and average ratings by country.
9. **NumPy statistics:** calculates rating standard deviation, quartiles, and counts above or below the overall average.
10. **Lowest-rated titles:** lists up to five titles with the lowest ratings.

## 7. Installation
Open a terminal in the project folder and run:

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 8. How to Run
From the project root directory:

```bash
python src/analysis.py
```

To analyze a different CSV file:

```bash
python src/analysis.py --data path/to/your_dataset.csv
```

The analysis report will appear in the terminal. No visualization window or chart files are generated.

## 9. Expected Output
The program prints:
- Dataset overview and overall rating statistics.
- Top-rated titles.
- Platform-wise performance table.
- Genre-wise performance table.
- Release-year and country summaries.
- NumPy statistical insights.
- Lowest-rated titles.

Exact values depend on the CSV dataset supplied.

## 10. Possible Future Improvements
- Add more OTT platforms and a larger, reliably sourced dataset.
- Include separate analysis for movies and television series.
- Add language, runtime, and content-type columns.
- Export the text summaries to a report file.
- Add automated tests for data-cleaning rules.

## 11. Limitations
- The included dataset is small and illustrative, so it should not be used to claim that one real OTT platform is better than another.
- Ratings can vary by source, collection date, and audience.
- Average ratings alone do not capture every aspect of popularity or quality; vote counts should also be considered.

## 12. Conclusion
This project demonstrates an end-to-end introductory data analysis workflow using Pandas and NumPy. It cleans OTT data and extracts useful rating insights through statistical summaries and text tables, without relying on charts or graphs.
