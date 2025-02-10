import os

def generate_summary():
    summary_path = "SUMMARY.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("# Summary\n\n")
        for root, _, files in os.walk("."):
            for file in sorted(files):
                if file.endswith(".md") and file not in ["README.md", "SUMMARY.md"]:
                    rel_path = os.path.relpath(os.path.join(root, file), ".")
                    title = file.replace(".md", "").replace("-", " ").title()
                    f.write(f"- [{title}]({rel_path})\n")

generate_summary()