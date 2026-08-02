import pypdf

r = pypdf.PdfReader(open("study_guides.pdf", "rb"))
print(f"Pages: {len(r.pages)}")

# Try to get text from first few pages to understand structure
for i in range(min(5, len(r.pages))):
    text = r.pages[i].extract_text()
    print(f"\n--- Page {i+1} ---")
    print(text[:500] if text else "No text extracted")
