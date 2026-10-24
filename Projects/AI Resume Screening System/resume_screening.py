from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample resumes (name and skills)
names = ["Ravi", "Priya", "Arun", "Meena"]
resumes = [
    "python pandas machine learning data analysis sql",
    "html css javascript react web development",
    "python sql power bi data visualization excel",
    "java spring boot backend development mysql",
]

print("AI Resume Screening System")
job = input("Enter job description or skills needed: ")

# Turn the text into numbers and compare
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform([job] + resumes)
scores = cosine_similarity(matrix[0:1], matrix[1:])[0]

# Show the result for each candidate
print("\nResults:")
for i in range(len(names)):
    percent = round(scores[i] * 100, 1)
    if percent >= 30:
        print(names[i], "-", percent, "% match - Shortlisted")
    else:
        print(names[i], "-", percent, "% match - Rejected")