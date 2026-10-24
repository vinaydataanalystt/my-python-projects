
import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------------
# STEP 1: CREATE THE COURSE DATA (only the first time)
# ---------------------------------------------------------------
# If you have a real dataset, save it as courses.csv with the same
# column names and this step will be skipped.

FILE = "courses.csv"

if not os.path.exists(FILE):
    courses = [
        ("Python for Beginners", "Programming", "Beginner", "python basics variables loops functions coding programming", 4.7, 6),
        ("Advanced Python Programming", "Programming", "Advanced", "python decorators generators oop advanced coding programming", 4.5, 8),
        ("Java Programming Masterclass", "Programming", "Intermediate", "java oop classes objects programming backend coding", 4.6, 10),
        ("C and C++ Fundamentals", "Programming", "Beginner", "c cpp pointers memory programming basics coding", 4.3, 8),
        ("Web Development with HTML and CSS", "Web Development", "Beginner", "html css website design layout responsive frontend", 4.6, 5),
        ("JavaScript Essentials", "Web Development", "Beginner", "javascript dom events web frontend programming browser", 4.6, 6),
        ("React for Frontend Developers", "Web Development", "Intermediate", "react javascript components hooks frontend web", 4.7, 8),
        ("Node.js and Express Backend", "Web Development", "Intermediate", "nodejs express api backend javascript server database", 4.5, 8),
        ("Data Analysis with Pandas", "Data Science", "Beginner", "python pandas numpy data analysis cleaning dataframe", 4.7, 6),
        ("Data Visualization with Power BI", "Data Science", "Beginner", "power bi dashboard charts reports data visualization dax", 4.6, 5),
        ("Statistics for Data Science", "Data Science", "Intermediate", "statistics probability hypothesis testing data analysis mathematics", 4.4, 7),
        ("Machine Learning with Python", "Machine Learning", "Intermediate", "machine learning python scikit-learn regression classification models prediction", 4.8, 10),
        ("Deep Learning with TensorFlow", "Machine Learning", "Advanced", "deep learning neural networks tensorflow keras python models", 4.7, 12),
        ("Natural Language Processing", "Machine Learning", "Advanced", "nlp text python machine learning chatbot tokens sentiment", 4.5, 10),
        ("Computer Vision with OpenCV", "Machine Learning", "Advanced", "opencv images computer vision python detection deep learning", 4.4, 9),
        ("SQL for Beginners", "Databases", "Beginner", "sql queries select join database tables data", 4.6, 4),
        ("MySQL Database Administration", "Databases", "Intermediate", "mysql database admin backup performance sql queries", 4.3, 6),
        ("MongoDB for Developers", "Databases", "Intermediate", "mongodb nosql database documents backend queries", 4.4, 5),
        ("Excel for Data Analysis", "Business", "Beginner", "excel formulas pivot tables charts data analysis spreadsheet", 4.5, 4),
        ("Digital Marketing Fundamentals", "Business", "Beginner", "marketing seo social media ads content brand analytics", 4.3, 5),
        ("Project Management Basics", "Business", "Beginner", "project management planning teams agile scrum leadership", 4.4, 5),
        ("Cloud Computing with AWS", "Cloud", "Intermediate", "aws cloud servers storage deployment computing devops", 4.6, 8),
        ("Docker and Kubernetes", "Cloud", "Advanced", "docker kubernetes containers deployment devops cloud", 4.5, 7),
        ("Cyber Security Essentials", "Security", "Beginner", "security hacking network encryption threats protection", 4.4, 6),
        ("UI UX Design Fundamentals", "Design", "Beginner", "ui ux design figma wireframes prototype user experience", 4.5, 5),
        ("Generative AI and Prompt Engineering", "Machine Learning", "Beginner", "generative ai prompt engineering chatgpt llm text models", 4.6, 4),
    ]
    df_new = pd.DataFrame(courses, columns=["title", "category", "level", "description", "rating", "weeks"])
    df_new.insert(0, "course_id", range(1, len(df_new) + 1))
    df_new.to_csv(FILE, index=False)
    print("Sample data created:", FILE)


# ---------------------------------------------------------------
# STEP 2: LOAD THE DATA
# ---------------------------------------------------------------
df = pd.read_csv(FILE)
df = df.dropna().reset_index(drop=True)

# One text for each course: title + category + description
df["text"] = df["title"] + " " + df["category"] + " " + df["description"]


# ---------------------------------------------------------------
# STEP 3: TURN TEXT INTO NUMBERS AND FIND SIMILARITY
# ---------------------------------------------------------------
def clean_words(text):
    # Make small letters, split into words, remove common words like "the",
    # and cut a plural 's' so that "websites" matches "website"
    words = re.findall("[a-z0-9]+", text.lower())
    result = []
    for w in words:
        if w in ENGLISH_STOP_WORDS:
            continue
        if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        result.append(w)
    return result


vectorizer = TfidfVectorizer(tokenizer=clean_words, token_pattern=None)
course_matrix = vectorizer.fit_transform(df["text"])

# similarity[i][j] = how similar course i is to course j (0 to 1)
similarity = cosine_similarity(course_matrix)


# ---------------------------------------------------------------
# STEP 4: FUNCTIONS TO RECOMMEND COURSES
# ---------------------------------------------------------------

def show_courses(rows, scores=None):
    # Print courses neatly
    for number, (i, row) in enumerate(rows.iterrows(), 1):
        line = str(number) + ". " + row["title"] + " | " + row["level"] + " | Rating " + str(row["rating"]) + " | " + str(row["weeks"]) + " weeks"
        if scores is not None:
            line = line + " | Match " + str(round(scores[i] * 100)) + "%"
        print(line)


def recommend_similar(course_name, top=5):
    # Find the course the user typed
    found = df[df["title"].str.lower().str.contains(course_name.lower())]
    if len(found) == 0:
        print("Course not found. Choose option 3 to see all courses.")
        return
    index = found.index[0]
    print("\nBecause you liked:", df.loc[index, "title"])
    print("You may also like:\n")

    scores = similarity[index].copy()
    scores[index] = -1                       # do not recommend the same course
    best = scores.argsort()[::-1][:top]      # positions of the highest scores
    show_courses(df.iloc[best], scores)


def recommend_by_interest(interest, level="", top=5):
    # Compare the user's interest text with every course
    interest_vector = vectorizer.transform([interest])
    scores = cosine_similarity(interest_vector, course_matrix)[0]

    if max(scores) == 0:
        print("Sorry, nothing matches that. Try words like python, data, web, cloud.")
        return

    result = df.copy()
    if level != "":
        result = result[result["level"].str.lower() == level.lower()]
        if len(result) == 0:
            print("No courses found for that level.")
            return

    best = scores[result.index].argsort()[::-1][:top]
    chosen = result.iloc[best]
    chosen = chosen[[scores[i] > 0 for i in chosen.index]]

    print("\nCourses for your interest:", interest, "\n")
    show_courses(chosen, scores)


# ---------------------------------------------------------------
# STEP 5: MENU
# ---------------------------------------------------------------
print("\n===== COURSE RECOMMENDATION SYSTEM =====")
print("Total courses available:", len(df))

while True:
    print("\n1. Recommend courses similar to one I liked")
    print("2. Recommend courses for my interest")
    print("3. Show all courses")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter a course name (example: python): ")
        recommend_similar(name)

    elif choice == "2":
        interest = input("What do you want to learn? (example: data analysis with python): ")
        level = input("Level - Beginner / Intermediate / Advanced (press Enter for any): ")
        recommend_by_interest(interest, level)

    elif choice == "3":
        print()
        print(df[["course_id", "title", "category", "level", "rating"]].to_string(index=False))

    elif choice == "4":
        print("Thank you! Happy learning.")
        break

    else:
        print("Please enter a number from 1 to 4.")
