"""Generate the markdown files and nav automatically"""

import mkdocs_gen_files
from pathlib import Path

# define root path
src_root = Path("app")


for path in src_root.glob("**/*.py"):
    print(path)
    doc_path = Path("docs", path).with_suffix(".md")

    with mkdocs_gen_files.open(doc_path, "w") as f:
        script_path = ".".join(path.with_suffix("").parts)
        print(f" {script_path}.py", file=f)
        print("::: " + script_path, file=f)