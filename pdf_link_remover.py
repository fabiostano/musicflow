from pathlib import Path
import fitz  # PyMuPDF

src_dir = Path("_static/papers")
out_root = Path("_static/papers_img")
out_root.mkdir(parents=True, exist_ok=True)

zoom = 2.0  # ~144 DPI; use 2.5-3.0 for higher quality
mat = fitz.Matrix(zoom, zoom)

for pdf_path in sorted(src_dir.glob("*.pdf")):
    doc = fitz.open(pdf_path)
    paper_name = pdf_path.stem
    out_dir = out_root / paper_name
    out_dir.mkdir(parents=True, exist_ok=True)

    # clean old images in target folder
    for old in out_dir.glob("page_*.png"):
        old.unlink()

    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        out_file = out_dir / f"page_{i:03d}.png"
        pix.save(out_file)

    print(f"{pdf_path.name}: {len(doc)} pages -> {out_dir}")

print("Done.")