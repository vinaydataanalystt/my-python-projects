


def get_details():
    print("=" * 50)
    print("        RESUME BUILDER - Enter your details")
    print("=" * 50)

    data = {}
    data["name"] = input("Full name: ").strip()
    data["email"] = input("Email: ").strip()
    data["phone"] = input("Phone: ").strip()
    data["location"] = input("City / Location: ").strip()
    data["job_role"] = input("Job role you want (e.g. Python Developer): ").strip()
    data["education"] = input("Education (e.g. B.Tech CSE, XYZ College, 2025): ").strip()
    data["skills"] = input("Skills (separate with commas): ").strip()
    data["projects"] = input("Projects (separate with commas): ").strip()
    data["experience"] = input("Experience/Internship (type 'None' if fresher): ").strip()
    data["certifications"] = input("Certifications (or 'None'): ").strip()
    return data


def build_prompt(data):
    return PROMPT_TEMPLATE.format(**data)


def make_bullets(text):
    items = [item.strip() for item in text.split(",") if item.strip()]
    return "\n".join("  - " + item for item in items)


def build_resume(data):
    line = "=" * 50
    resume = f"""{line}
{data['name'].upper()}
{data['email']} | {data['phone']} | {data['location']}
{line}

PROFESSIONAL SUMMARY
Motivated fresher seeking a {data['job_role']} role. Eager to apply
my skills and learn through real-world projects.

SKILLS
{make_bullets(data['skills'])}

PROJECTS
{make_bullets(data['projects'])}

EDUCATION
  {data['education']}

EXPERIENCE
  {data['experience']}

CERTIFICATIONS
{make_bullets(data['certifications'])}
"""
    return resume


def save_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved -> {filename}")


def main():
    data = get_details()

    prompt = build_prompt(data)
    resume = build_resume(data)

    print("\n" + "-" * 50)
    print("YOUR RESUME (basic version):")
    print("-" * 50)
    print(resume)

    save_file("prompt_for_ai.txt", prompt)
    save_file("resume.txt", resume)

    print("\nNext step: open prompt_for_ai.txt, copy it and paste it")
    print("into ChatGPT / Claude / Gemini to get a polished resume.")


if __name__ == "__main__":
    main()