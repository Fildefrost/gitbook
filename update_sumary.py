import os

def generate_summary(root_dir="."):
    summary_path = os.path.join(root_dir, "SUMMARY.md")

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("# Summary\n\n")

        for dirpath, _, filenames in os.walk(root_dir):
            # Filtrar archivos .md y excluir README.md y SUMMARY.md
            md_files = sorted([file for file in filenames if file.endswith(".md") and file not in ["README.md", "SUMMARY.md"]])
            
            # Generar estructura de navegación
            if md_files:
                rel_path = os.path.relpath(dirpath, root_dir)
                if rel_path != ".":
                    f.write(f"\n## {rel_path.replace('/', ' › ').title()}\n\n")

                for md_file in md_files:
                    file_path = os.path.join(rel_path, md_file) if rel_path != "." else md_file
                    title = md_file.replace(".md", "").replace("-", " ").title()
                    f.write(f"- [{title}]({file_path})\n")

    print("✅ `SUMMARY.md` actualizado correctamente.")

generate_summary()
