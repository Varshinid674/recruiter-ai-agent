import random
job_description = "Looking for Python developer with ML skills"
resumes = [
    {
        "name": "A",
        "skills": ["Python", "ML"],
        "experience": 2,
        "gender": "Female",
        "education": "B.Tech",
        "college_tier": 1,
        "salary_expectation": 6,
        "notice_period": 30,
        "location": "Bangalore",
        "relocate": True
    },
    {
        "name": "B",
        "skills": ["Java"],
        "experience": 1,
        "gender": "Male",
        "education": "B.Tech",
        "college_tier": 2,
        "salary_expectation": 4,
        "notice_period": 60,
        "location": "Chennai",
        "relocate": False
    }
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
        skill_score = len(set(c["skills"]) & set(skills))
        
        education_score = 2 if c["education"] == "B.Tech" else 1
        
        tier_score = 3 if c["college_tier"] == 1 else 1
        
        c["score"] = skill_score + c["experience"] + education_score + tier_score + c["test_score"] * 0.1

    return candidates
def filter_candidates(candidates):
    filtered = []
    
    for c in candidates:
        if (c["location"] == "Bangalore" or c["relocate"]) and c["salary_expectation"] <= 8 and c["notice_period"] <= 60:
            filtered.append(c)
    
    return filtered
def assess_candidates(candidates):
    for c in candidates:
        c["test_score"] = random.randint(60, 100)
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

filtered = filter_candidates(candidates)

screened = screen_candidates(filtered, skills)

assessed = assess_candidates(screened)

matched = match_candidates(assessed, skills)

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