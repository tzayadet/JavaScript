#!/usr/bin/env python3
"""Validate local references and inline JavaScript in the static experiments."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = set()
        self.inline_scripts = []
        self.current_script = None
        self.current_script_type = ""

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])

        attribute = "src" if tag in {"img", "script", "audio", "video", "source"} else "href"
        if values.get(attribute):
            self.references.append(values[attribute])

        if tag == "script":
            script_type = values.get("type", "").lower()
            if "src" not in values and script_type in {"", "text/javascript", "application/javascript", "module"}:
                self.current_script = []
            else:
                self.current_script = None

    def handle_data(self, data):
        if self.current_script is not None:
            self.current_script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.current_script is not None:
            self.inline_scripts.append("".join(self.current_script))
            self.current_script = None


def main():
    html_files = sorted(ROOT.glob("*.html"))
    if not html_files:
        raise SystemExit("No HTML pages were found.")

    parsers = {}
    errors = []
    all_scripts = []

    for page in html_files:
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        parsers[page.name] = parser
        all_scripts.extend((page.name, script) for script in parser.inline_scripts)

        for reference in parser.references:
            parsed = urlsplit(reference)
            if parsed.scheme or reference.startswith("#") or not parsed.path:
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                errors.append(f"{page.name}: missing local reference {reference}")

    if errors:
        raise SystemExit("\n".join(errors))

    node = shutil.which("node")
    if all_scripts and not node:
        raise SystemExit("Node.js is required to syntax-check inline JavaScript.")

    with tempfile.TemporaryDirectory() as temp_dir:
        for index, (page_name, source) in enumerate(all_scripts, start=1):
            if not source.strip():
                continue
            js_file = Path(temp_dir) / f"inline-{index}.js"
            js_file.write_text(source, encoding="utf-8")
            try:
                subprocess.run([node, "--check", str(js_file)], check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as exc:
                raise SystemExit(
                    f"JavaScript syntax error in {page_name}:\n{exc.stderr or exc.stdout}"
                ) from exc

    print(f"Validated {len(html_files)} HTML pages, {len(all_scripts)} inline script(s), and all local references.")


if __name__ == "__main__":
    main()
