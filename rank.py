import json
import csv
# Load Candidates
file_path = "candidates.jsonl"

candidates = []

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            candidates.append(json.loads(line))

print("Total Candidates:", len(candidates))

# Show First Candidate
print("\nCandidate ID:", candidates[0]["candidate_id"])
print("Name:", candidates[0]["profile"]["anonymized_name"])
print("Current Title:", candidates[0]["profile"]["current_title"])
print("Experience:", candidates[0]["profile"]["years_of_experience"])

print("\nSkills:")
for skill in candidates[0]["skills"]:
    print("-", skill["name"])


# ----------------------------
# Score Function
# ----------------------------

def calculate_score(candidate):

    score = 0

    # Experience
    exp = candidate["profile"]["years_of_experience"]

    if 5 <= exp <= 9:
        score += 20

    # Current Title
    title = candidate["profile"]["current_title"].lower()

    if "ai" in title:
        score += 20
    elif "ml" in title:
        score += 20
    elif "machine learning" in title:
        score += 20

        # Skills
    skills = [skill["name"].lower() for skill in candidate["skills"]]

    important_skills = [
        "python",
        "nlp",
        "milvus",
        "lora",
        "fine-tuning llms",
        "embeddings",
        "faiss",
        "pinecone",
        "weaviate",
        "qdrant",
        "elasticsearch",
        "opensearch"
    ]

    for skill in important_skills:
        if skill in skills:
            score += 5

    # Career History Keywords
    career_text = ""

    for job in candidate["career_history"]:
        career_text += job["title"].lower() + " "
        career_text += job["description"].lower() + " "

    important_keywords = [
        "rag",
        "llm",
        "transformer",
        "embedding",
        "vector",
        "retrieval",
        "langchain",
        "fine-tuning"
    ]

    matched_keywords = 0

    for word in important_keywords:
        if word in career_text:
            matched_keywords += 1

    score += min(matched_keywords * 3, 18)

    # Company Preference
    company = candidate["profile"]["current_company"].lower()

    service_companies = [
        "tcs",
        "infosys",
        "wipro",
        "accenture",
        "cognizant",
        "capgemini",
        "mindtree",
        "ltimindtree",
        "hcl"
    ]

    if company not in service_companies:
        score += 10

    # Open to Work
    if candidate["redrob_signals"]["open_to_work_flag"]:
        score += 10

    # Notice Period
    notice = candidate["redrob_signals"]["notice_period_days"]

    if notice <= 30:
        score += 10
    elif notice <= 60:
        score += 5

    return score

def generate_reason(candidate):

    reasons = []

    exp = candidate["profile"]["years_of_experience"]

    if exp >= 5:
        reasons.append("Strong experience")

    skills = [s["name"].lower() for s in candidate["skills"]]

    ai_skills = []

    for s in ["python","nlp","milvus","lora","faiss","pinecone","rag","langchain"]:
        if s in skills:
            ai_skills.append(s.upper())

    if ai_skills:
        reasons.append("Skills: " + ", ".join(ai_skills))

    if candidate["redrob_signals"]["open_to_work_flag"]:
        reasons.append("Open to Work")

    notice = candidate["redrob_signals"]["notice_period_days"]

    if notice <= 30:
        reasons.append("Immediate Joiner")

    return " | ".join(reasons)
print("\nScore:", calculate_score(candidates[0]))

# ----------------------------
# Score All Candidates
# ----------------------------

ranked_candidates = []

for candidate in candidates:
    score = calculate_score(candidate)

    ranked_candidates.append({
        "candidate_id": candidate["candidate_id"],
        "score": score
    })

print("\nTotal Ranked Candidates:", len(ranked_candidates))
print(ranked_candidates[:5])

# ----------------------------
# Sort Candidates
# ----------------------------

ranked_candidates.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTop 10 Candidates:")

for c in ranked_candidates[:10]:
    print(c)
    # ----------------------------
# Top 100 Candidates
# ----------------------------

top100 = ranked_candidates[:100]

print("\nTop 100 Selected:", len(top100))

# ----------------------------
# Create Submission CSV
# ----------------------------

with open("submission.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["candidate_id", "rank", "score", "reasoning"])

    rank = 1

    for candidate in top100:

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            generate_reason(
    next(
        c for c in candidates
        if c["candidate_id"] == candidate["candidate_id"]
    )
)
        ])

        rank += 1

print("\nSubmission CSV Created Successfully!")


