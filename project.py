job_description = "Looking for Python developer with ML skills"

resumes = [
    {"name": "A", "skills": ["Python", "ML"], "experience": 2, "gender": "Female"},
    {"name": "B", "skills": ["Java"], "experience": 1, "gender": "Male"},
    {"name": "C", "skills": ["Python", "Data Science"], "experience": 3, "gender": "Female"},
    {"name": "D", "skills": ["ML", "Python"], "experience": 4, "gender": "Male"}
]
def extract_skills(job):
    return ["Python", "ML"]
def source_candidates():
    return resumes
def screen_candidates(candidates, skills):
    selected = []
    for c in candidates:
        if any(skill in c["skills"] for skill in skills):
            selected.append(c)
    return selected
def match_candidates(candidates, skills):
    for c in candidates:
        c["score"] = len(set(c["skills"]) & set(skills)) + c["experience"]
    return candidates
def rank_candidates(candidates):
    return sorted(candidates, key=lambda x: x["score"], reverse=True)
def schedule(candidates):
    for c in candidates:
        c["interview"] = "Tomorrow 10 AM"
    return candidates
def track(candidates):
    for c in candidates:
        c["stage"] = "Interview Scheduled"
    return candidates
def diversity(candidates):
    genders = [c["gender"] for c in candidates]

    return {
        "total_candidates": len(candidates),
        "female_count": genders.count("Female"),
        "male_count": genders.count("Male")
    }
skills = extract_skills(job_description)

candidates = source_candidates()

screened = screen_candidates(candidates, skills)

matched = match_candidates(screened, skills)

ranked = rank_candidates(matched)

scheduled = schedule(ranked)

tracked = track(scheduled)

report = diversity(tracked)

print(tracked)
print(report)
print("\nFinal Selected Candidates:\n")

for c in tracked:
    print(f"Name: {c['name']}")
    print(f"Skills: {c['skills']}")
    print(f"Score: {c['score']}")
    print(f"Interview: {c['interview']}")
    print(f"Stage: {c['stage']}")
    print("------")

print("\nDiversity Report:")
print(report)