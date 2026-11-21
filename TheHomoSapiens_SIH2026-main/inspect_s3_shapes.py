import pptx

prs = pptx.Presentation(r"C:\Users\shrey\.gemini\antigravity\brain\c9fd9f2a-5cf9-42f3-8858-f7cd683583c8\.user_uploaded\media_1795175890463_53d2a1ea.pptx")
s3 = prs.slides[2]

for i, s in enumerate(s3.shapes):
    print(f"Shape {i}: name='{s.name}', type={s.shape_type}, left={s.left}, top={s.top}, w={s.width}, h={s.height}")

