# AI Resume Ranking Challenge

## Project Overview

This project was developed for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

The system reads 100,000 candidate profiles from the provided dataset, calculates a score for each candidate based on multiple job-relevant factors, ranks all candidates, and generates the Top 100 candidates in the required submission format.

---

## Features

- Load 100,000 candidate profiles
- Score every candidate automatically
- Rank candidates based on job relevance
- Generate Top 100 candidates
- Export results to submission.csv
- Validation passed successfully

---

## Scoring Criteria

The scoring algorithm considers the following factors:

- Years of Experience
- Current Job Title
- AI/ML Skills
- Career History Keywords
- Company Preference
- Open to Work Status
- Notice Period

Each candidate receives a final score based on these parameters.

---

## Technologies Used

- Python
- JSON
- CSV

---

## Project Structure

AI-Resume-Challenge/

- rank.py
- candidates.jsonl
- submission.csv
- README.md
- requirements.txt
- validate_submission.py

---

## How to Run

Open terminal inside the project folder and run:

```bash
python rank.py
```

---

## Output

The program generates:

```
submission.csv
```

containing the Top 100 ranked candidates.

---

## Validation

The generated submission was validated successfully using:

```bash
python validate_submission.py submission.csv
```

Output:

```
Submission is valid.
```

---

## Author

**Renu**