#!/usr/bin/env python3
"""
make_poly_jpg.py
Usage:
  python3 make_poly_jpg.py input.jpg -m "Hello from alert" -o result.jpg

This writes a VALID JPEG file (actual image bytes) then appends an HTML page
(after a newline). Browsers normally ignore trailing HTML for direct file-open,
so use the server below to force it to be parsed as text/html.
"""
import argparse
import os
import json

HTML_PAYLOAD_TEMPLATE = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>{title}</title></head>
<body>
  <h1>{title}</h1>
  <p>Polyglot JPG demo — HTML appended after JPEG bytes.</p>
  <img src="{embedded}" alt="embedded image" style="max-width:50%;">
  <script>
    (function() {{
      alert({msg});
    }})();
  </script>
</body>
</html>
"""

def build_html(message, embedded_path):
    # Use a safe JSON string literal for the JS alert message
    msg = json.dumps(message)
    # If you want the image displayed via data URI, you'd base64-embed; keep simple here
    embedded = embedded_path
    return HTML_PAYLOAD_TEMPLATE.format(title="Polyglot JPG", embedded=embedded, msg=msg)

def write_polyglot(jpg_in, out, message):
    if not os.path.isfile(jpg_in):
        raise SystemExit(f"Input not found: {jpg_in}")
    html = build_html(message, os.path.basename(jpg_in))
    # Read the real image bytes
    with open(jpg_in, "rb") as f:
        img_bytes = f.read()
    # Write real JPEG bytes, then newline + HTML text
    with open(out, "wb") as f:
        f.write(img_bytes)
        f.write(b"\n")
        f.write(html.encode("utf-8"))
    print(f"Wrote polyglot JPG: {out}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="Input image (jpg/png/gif)")
    p.add_argument("-m", "--message", default="Hello from polyglot alert", help="Alert message")
    p.add_argument("-o", "--output", default=None, help="Output .jpg filename")
    args = p.parse_args()

    out = args.output or (os.path.splitext(args.input)[0] + "_poly.jpg")
    if not out.lower().endswith(".jpg"):
        out += ".jpg"

    write_polyglot(args.input, out, args.message)

if __name__ == "__main__":
    main()
