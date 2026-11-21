import pptx

prs = pptx.Presentation(r"C:\Users\shrey\.gemini\antigravity\brain\c9fd9f2a-5cf9-42f3-8858-f7cd683583c8\.user_uploaded\media_1795175890463_53d2a1ea.pptx")

for idx in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]:
    slide = prs.slides[idx]
    print(f"=== SLIDE {idx+1} ===")
    for s_idx, shape in enumerate(slide.shapes):
        if shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE and shape.name != "Picture 24" and shape.name != "Picture 51":
            print(f"  Shape {s_idx}: name='{shape.name}', left={shape.left}, top={shape.top}, w={shape.width}, h={shape.height}")

