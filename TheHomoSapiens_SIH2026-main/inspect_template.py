import pptx
from pptx.enum.dml import MSO_COLOR_TYPE

prs = pptx.Presentation(r"C:\Users\shrey\.gemini\antigravity\brain\c9fd9f2a-5cf9-42f3-8858-f7cd683583c8\.user_uploaded\media_1795175890463_53d2a1ea.pptx")
s3 = prs.slides[2]

for s_idx in [8, 9, 12, 15]:
    shape = s3.shapes[s_idx]
    print(f"=== Shape {s_idx} ({shape.name}) ===")
    for p_idx, p in enumerate(shape.text_frame.paragraphs):
        print(f"  P{p_idx}: text='{p.text[:40]}' font_size={p.font.size}")
        for r_idx, r in enumerate(p.runs):
            col = "None"
            if r.font.color:
                try:
                    col = str(r.font.color.rgb)
                except Exception:
                    col = f"theme:{r.font.color.theme_color}"
            print(f"    R{r_idx}: '{r.text[:30]}' size={r.font.size} bold={r.font.bold} col={col}")

