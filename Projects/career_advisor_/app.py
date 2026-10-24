# AI Career Advisor - Streamlit App
# Run locally:  streamlit run app.py
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Career Advisor", page_icon="🎯")
st.title("🎯 AI Career Advisor")
st.write("Select your skills and interests. The AI will suggest the best careers for you.")

# ---- 1. Load career data ----
careers = pd.read_csv("careers.csv")

# Make a list of all skills for the dropdown
all_skills = set()
for skills in careers["Skills"]:
    all_skills.update(skills.split(";"))
all_skills = sorted(all_skills)

# ---- 2. User input ----
selected_skills = st.multiselect("Your skills", all_skills)
interests = st.text_input("Your interests (example: building apps, working with data)")

# ---- 3. Recommend careers ----
if st.button("Suggest Careers"):
    if not selected_skills and not interests:
        st.warning("Please select at least one skill or write your interests.")
    else:
        # Convert text to numbers using TF-IDF
        user_text = " ".join(selected_skills) + " " + interests
        career_text = careers["Skills"].str.replace(";", " ") + " " + careers["Description"]

        vectorizer = TfidfVectorizer(stop_words="english")
        career_vectors = vectorizer.fit_transform(career_text)
        user_vector = vectorizer.transform([user_text])

        # Find how similar the user is to each career
        careers["Match"] = cosine_similarity(user_vector, career_vectors)[0] * 100
        top3 = careers.sort_values("Match", ascending=False).head(3)

        st.subheader("Top career matches for you")
        for _, row in top3.iterrows():
            st.markdown(f"### {row['Career']} - {row['Match']:.0f}% match")
            st.write(row["Description"])
            st.progress(min(int(row["Match"]), 100))

            career_skills = row["Skills"].split(";")
            have = [s for s in career_skills if s in selected_skills]
            missing = [s for s in career_skills if s not in selected_skills]
            st.write("✅ Skills you have:", ", ".join(have) if have else "None yet")
            st.write("📚 Skills to learn:", ", ".join(missing) if missing else "None")

            with st.expander("Learning roadmap"):
                for number, step in enumerate(row["Roadmap"].split(";"), start=1):
                    st.write(f"{number}. {step}")
            st.divider()
