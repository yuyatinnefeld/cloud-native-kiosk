"""Generate the markdown files and nav automatically"""
from pathlib import Path
import mkdocs_gen_files


src_root = Path("app")
for path in src_root.glob("**/*.py"):
    doc_path = Path("docs", path.relative_to(src_root)).with_suffix(".md")

    with mkdocs_gen_files.open(doc_path, "w") as f:
        script_path = ".".join(path.with_suffix("").parts)
        print(f"# {script_path}.py", file=f)
        print("::: " + script_path, file=f)
