import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("slide_images", exist_ok=True)

# Helper function to create base canvas
def create_canvas(w=900, h=650, bg=(15, 23, 42)):
    img = Image.new('RGB', (w, h), color=bg)
    d = ImageDraw.Draw(img)
    # Card outline
    d.rounded_rectangle([(8, 8), (w-8, h-8)], radius=16, fill=bg, outline=(51, 65, 85), width=2)
    return img, d

# 1. Slide 3: Dual-Hand 21 Keypoint Skeleton Tracking
def make_slide3_img():
    img, d = create_canvas()
    # Title badge
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "MediaPipe 21-Point Landmark Perception", fill=(45, 212, 191))
    
    # Left Hand (Skeleton)
    wrist_l = (220, 420)
    knuckles_l = [(160, 310), (195, 280), (235, 285), (275, 315)]
    fingertips_l = [(120, 230), (170, 160), (225, 145), (280, 170), (330, 230)]
    
    # Palm Centroid
    d.polygon(knuckles_l + [wrist_l], fill=(13, 148, 136, 60), outline=(20, 184, 166))
    centroid_l = (215, 330)
    d.ellipse([(centroid_l[0]-14, centroid_l[1]-14), (centroid_l[0]+14, centroid_l[1]+14)], fill=(6, 182, 212))
    d.text((centroid_l[0]-10, centroid_l[1]-7), "C", fill=(255, 255, 255))
    
    # Wrist Origin #0
    d.ellipse([(wrist_l[0]-14, wrist_l[1]-14), (wrist_l[0]+14, wrist_l[1]+14)], fill=(244, 63, 94))
    d.text((wrist_l[0]-8, wrist_l[1]-7), "0", fill=(255, 255, 255))
    
    # Bones and fingertips
    for k in knuckles_l:
        d.line([wrist_l, k], fill=(45, 212, 191), width=3)
        d.ellipse([(k[0]-7, k[1]-7), (k[0]+7, k[1]+7)], fill=(20, 184, 166))
    for k, f in zip(knuckles_l, fingertips_l[1:]):
        d.line([k, f], fill=(99, 102, 241), width=3)
        d.ellipse([(f[0]-9, f[1]-9), (f[0]+9, f[1]+9)], fill=(250, 204, 21))
    thumb_base = (145, 360)
    d.line([wrist_l, thumb_base], fill=(45, 212, 191), width=3)
    d.line([thumb_base, fingertips_l[0]], fill=(99, 102, 241), width=3)
    d.ellipse([(fingertips_l[0][0]-9, fingertips_l[0][1]-9), (fingertips_l[0][0]+9, fingertips_l[0][1]+9)], fill=(250, 204, 21))

    # Right Hand (Symmetric)
    wrist_r = (680, 420)
    knuckles_r = [(625, 315), (665, 285), (705, 280), (740, 310)]
    fingertips_r = [(570, 230), (620, 170), (675, 145), (730, 160), (780, 230)]
    
    d.polygon(knuckles_r + [wrist_r], fill=(13, 148, 136, 60), outline=(20, 184, 166))
    centroid_r = (685, 330)
    d.ellipse([(centroid_r[0]-14, centroid_r[1]-14), (centroid_r[0]+14, centroid_r[1]+14)], fill=(6, 182, 212))
    d.text((centroid_r[0]-10, centroid_r[1]-7), "C", fill=(255, 255, 255))
    
    d.ellipse([(wrist_r[0]-14, wrist_r[1]-14), (wrist_r[0]+14, wrist_r[1]+14)], fill=(244, 63, 94))
    d.text((wrist_r[0]-8, wrist_r[1]-7), "0", fill=(255, 255, 255))
    for k in knuckles_r:
        d.line([wrist_r, k], fill=(45, 212, 191), width=3)
        d.ellipse([(k[0]-7, k[1]-7), (k[0]+7, k[1]+7)], fill=(20, 184, 166))
    for k, f in zip(knuckles_r, fingertips_r[:-1]):
        d.line([k, f], fill=(99, 102, 241), width=3)
        d.ellipse([(f[0]-9, f[1]-9), (f[0]+9, f[1]+9)], fill=(250, 204, 21))
    thumb_base_r = (755, 360)
    d.line([wrist_r, thumb_base_r], fill=(45, 212, 191), width=3)
    d.line([thumb_base_r, fingertips_r[4]], fill=(99, 102, 241), width=3)
    d.ellipse([(fingertips_r[4][0]-9, fingertips_r[4][1]-9), (fingertips_r[4][0]+9, fingertips_r[4][1]+9)], fill=(250, 204, 21))

    # Center Dual-Hand Coordination Arc
    d.arc([(300, 260), (600, 480)], start=200, end=340, fill=(250, 204, 21), width=3)
    d.rounded_rectangle([(370, 240), (530, 280)], radius=6, fill=(30, 41, 59))
    d.text((385, 252), "Dual-Hand Vector", fill=(250, 204, 21))

    # Legend at bottom
    d.rounded_rectangle([(30, 560), (870, 620)], radius=10, fill=(30, 41, 59))
    d.ellipse([(50, 580), (68, 598)], fill=(244, 63, 94))
    d.text((78, 582), "Wrist Origin (Anchor 0)", fill=(255, 255, 255))
    d.ellipse([(320, 580), (338, 598)], fill=(6, 182, 212))
    d.text((348, 582), "Palm Centroid Normal", fill=(255, 255, 255))
    d.ellipse([(580, 580), (598, 598)], fill=(250, 204, 21))
    d.text((608, 582), "Fingertip Actuators (#4, 8, 12, 16, 20)", fill=(255, 255, 255))

    img.save("slide_images/slide3.png")

# 2. Slide 4: Communication Gap & Wearable Gloves Bottleneck
def make_slide4_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "The Communication Divide & Limitations", fill=(244, 63, 94))

    # Left: Deaf Signer
    d.rounded_rectangle([(50, 110), (380, 480)], radius=14, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    d.rounded_rectangle([(70, 130), (360, 170)], radius=8, fill=(244, 63, 94))
    d.text((105, 142), "Traditional Dilemma: Wearables", fill=(255, 255, 255))
    
    # Glove drawing
    d.rounded_rectangle([(140, 210), (290, 370)], radius=20, fill=(51, 65, 85), outline=(239, 68, 68), width=3)
    d.text((165, 280), "SENSOR GLOVE", fill=(248, 113, 113))
    d.text((70, 400), "• Exorbitant Cost ($500 - $1,500)", fill=(226, 232, 240))
    d.text((70, 425), "• Fragile Flex-Sensors & Wiring", fill=(226, 232, 240))
    d.text((70, 450), "• Unnatural & Fatiguing in Public", fill=(226, 232, 240))

    # VS Center Icon
    d.ellipse([(415, 260), (485, 330)], fill=(244, 63, 94))
    d.text((435, 285), "VS", fill=(255, 255, 255))

    # Right: TheHomoSapiens Camera Vision
    d.rounded_rectangle([(520, 110), (850, 480)], radius=14, fill=(30, 41, 59), outline=(13, 148, 136), width=2)
    d.rounded_rectangle([(540, 130), (830, 170)], radius=8, fill=(13, 148, 136))
    d.text((580, 142), "TheHomoSapiens Solution", fill=(255, 255, 255))

    # Laptop / Camera icon
    d.rounded_rectangle([(610, 210), (760, 310)], radius=10, fill=(2, 6, 23), outline=(45, 212, 191), width=2)
    d.ellipse([(675, 230), (695, 250)], fill=(45, 212, 191))
    d.text((635, 270), "STANDARD WEBCAM", fill=(45, 212, 191))
    d.line([(580, 320), (790, 320)], fill=(71, 85, 105), width=6)

    d.text((540, 400), "• Zero Cost ($0) — 100% Free FOSS", fill=(45, 212, 191))
    d.text((540, 425), "• No Wearables — Bare-Hand Signing", fill=(45, 212, 191))
    d.text((540, 450), "• Instant Real-Time Voice Broadcast", fill=(45, 212, 191))

    # Bottom summary pill
    d.rounded_rectangle([(50, 520), (850, 600)], radius=10, fill=(2, 6, 23), outline=(20, 184, 166), width=2)
    d.text((70, 545), "Democratizing Accessibility: Transforming Any Camera into an ISL Interpreter", fill=(255, 255, 255))

    img.save("slide_images/slide4.png")

# 3. Slide 5: SMART Objectives Grid
def make_slide5_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (380, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "SMART Performance Benchmark Goals", fill=(250, 204, 21))

    cards = [
        ("30+ FPS", "Real-Time Tracking", "Dual-hand 21 keypoint extraction at full camera frame rate", (13, 148, 136), 50, 105),
        ("< 50 ms", "Sub-50ms Latency", "Instant in-browser spatial geometry & temporal sequence inference", (99, 102, 241), 470, 105),
        ("> 95 %", "Classification Accuracy", "High-precision recognition on core ISL phrases & alphabet signs", (244, 63, 94), 50, 320),
        ("2-Way", "Speech & Text Audio", "Vocalized dialogue via Web Speech API & dynamic sentence builder", (16, 185, 129), 470, 320),
    ]

    for val, title, desc, col, x, y in cards:
        d.rounded_rectangle([(x, y), (x+380, y+180)], radius=12, fill=(30, 41, 59), outline=col, width=2)
        d.rounded_rectangle([(x+15, y+15), (x+140, y+65)], radius=8, fill=col)
        d.text((x+30, y+27), val, fill=(255, 255, 255))
        d.text((x+155, y+27), title, fill=(255, 255, 255))
        d.text((x+20, y+95), desc[:40], fill=(203, 213, 225))
        d.text((x+20, y+125), desc[40:], fill=(203, 213, 225))

    d.rounded_rectangle([(50, 535), (850, 605)], radius=10, fill=(30, 41, 59))
    d.text((70, 560), "All targets measured and verified across diverse lighting & distance conditions", fill=(45, 212, 191))
    img.save("slide_images/slide5.png")

# 4. Slide 6: Technical Scope Boundaries
def make_slide6_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (380, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "System Technical Scope Boundaries", fill=(45, 212, 191))

    # In-Scope Box (Green/Teal)
    d.rounded_rectangle([(40, 100), (430, 580)], radius=14, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    d.rounded_rectangle([(60, 115), (410, 160)], radius=8, fill=(16, 185, 129))
    d.text((150, 128), "IN-SCOPE DOMAIN", fill=(255, 255, 255))

    in_items = [
        "✔ Dual-Hand 21-point tracking",
        "✔ RGB webcams & phone cameras",
        "✔ Anchor-point coordinate normalization",
        "✔ 30-Frame sequence pooling (MLP)",
        "✔ Core ISL vocabulary (50+ actions)",
        "✔ Fingerspelled A-Z alphabets",
        "✔ Speech synthesis (TTS audio)",
        "✔ Sentence builder queuing engine",
        "✔ Native Android APK compilation",
        "✔ SuperAdmin audit trails & analytics"
    ]
    for i, it in enumerate(in_items):
        d.text((60, 180 + i * 38), it, fill=(226, 232, 240))

    # Out-of-Scope Box (Red/Rose)
    d.rounded_rectangle([(470, 100), (860, 580)], radius=14, fill=(30, 41, 59), outline=(244, 63, 94), width=2)
    d.rounded_rectangle([(490, 115), (840, 160)], radius=8, fill=(244, 63, 94))
    d.text((560, 128), "OUT-OF-SCOPE DOMAIN", fill=(255, 255, 255))

    out_items = [
        "✖ Wearable sensory hardware gloves",
        "✖ Specialized LiDAR / Depth cameras",
        "✖ Multi-speaker overlapped signing",
        "✖ Complex sign poetry & theatrical ISL",
        "✖ Non-standard regional dialects",
        "✖ Sub-second full sentence translation",
        "✖ Facial emotion micromovement parsing",
        "✖ Offline edge TPU / FPGA co-processors",
        "✖ Continuous un-segmented paragraphs"
    ]
    for i, it in enumerate(out_items):
        d.text((490, 185 + i * 42), it, fill=(203, 213, 225))

    img.save("slide_images/slide6.png")

# 5. Slide 7: Literature Survey Evolution
def make_slide7_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (400, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "Sign Language ML Research Evolution", fill=(129, 140, 248))

    milestones = [
        ("1998", "Starner et al. (MIT)", "Hidden Markov Models (HMM) with colored gloves", (71, 85, 105)),
        ("2020", "Zhang et al. (Google)", "MediaPipe Hands: On-device 21-point 2.5D landmarks", (13, 148, 136)),
        ("2021", "Rastgoo et al.", "Multi-modal LSTM & 3D-CNNs (Heavy server requirement)", (99, 102, 241)),
        ("2023", "Sharma et al. (IEEE)", "Graph Neural Networks for ISL topology", (168, 85, 247)),
        ("2026", "TheHomoSapiens (Proposed)", "Anchor-Point Kinematics + In-Browser Speech (Zero-Lag)", (20, 184, 166))
    ]

    for i, (yr, auth, desc, col) in enumerate(milestones):
        y = 100 + i * 105
        # Year bubble
        d.rounded_rectangle([(50, y), (150, y+75)], radius=10, fill=col)
        d.text((70, y+25), yr, fill=(255, 255, 255))
        # Arrow / Line
        if i < 4:
            d.line([(100, y+75), (100, y+105)], fill=(148, 163, 184), width=3)
        # Content card
        d.rounded_rectangle([(175, y), (850, y+75)], radius=10, fill=(30, 41, 59), outline=col, width=2)
        d.text((200, y+15), auth, fill=(255, 255, 255))
        d.text((200, y+45), desc, fill=(203, 213, 225))

    img.save("slide_images/slide7.png")

# 6. Slide 8: 5-Stage Methodology Flowchart
def make_slide8_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "TheHomoSapiens 5-Stage System Pipeline", fill=(45, 212, 191))

    stages = [
        ("STAGE 1", "Live Video Ingestion", "30 FPS Webcam Stream / Camera2 API", (13, 148, 136)),
        ("STAGE 2", "MediaPipe Perception", "42 Coordinate 3D Landmarks Extraction", (99, 102, 241)),
        ("STAGE 3", "Anchor Normalization", "Wrist #0 Origin & Knuckle Centroid Deltas", (6, 182, 212)),
        ("STAGE 4", "Temporal ML Classifier", "30-Frame Kinematic Feature Pooling (MLP)", (244, 63, 94)),
        ("STAGE 5", "Speech & Sentence Queue", "Web Speech TTS Audio Broadcast", (16, 185, 129))
    ]

    for i, (stg, tit, sub, col) in enumerate(stages):
        y = 95 + i * 105
        d.rounded_rectangle([(60, y), (840, y+80)], radius=12, fill=(30, 41, 59), outline=col, width=2)
        d.rounded_rectangle([(80, y+15), (200, y+65)], radius=8, fill=col)
        d.text((100, y+27), stg, fill=(255, 255, 255))
        d.text((230, y+18), tit, fill=(255, 255, 255))
        d.text((230, y+48), sub, fill=(148, 163, 184))
        if i < 4:
            d.line([(450, y+80), (450, y+105)], fill=(45, 212, 191), width=4)

    img.save("slide_images/slide8.png")

# 7. Slide 9: Tech Stack Grid
def make_slide9_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "Core Technology & Library Ecosystem", fill=(45, 212, 191))

    techs = [
        ("MediaPipe Tasks 1.0", "Vision Perception", "21-point dual-hand 3D tracking", (13, 148, 136), 50, 95),
        ("Scikit-Learn (MLP)", "Machine Learning", "Temporal sequence neural classifier", (99, 102, 241), 470, 95),
        ("FastAPI & Uvicorn", "Backend Engine", "High-performance async REST endpoints", (244, 63, 94), 50, 255),
        ("Motor / MongoDB", "Database Driver", "Asynchronous logging & audit trail", (16, 185, 129), 470, 255),
        ("HTML5 Canvas & TTS", "Frontend HUD", "Sub-50ms render loop & voice synthesis", (250, 204, 21), 50, 415),
        ("Android Studio (Java)", "Mobile Compilation", "Native mobile APK with Camera2 bridge", (168, 85, 247), 470, 415)
    ]

    for name, cat, desc, col, x, y in techs:
        d.rounded_rectangle([(x, y), (x+380, y+135)], radius=12, fill=(30, 41, 59), outline=col, width=2)
        d.rounded_rectangle([(x+15, y+12), (x+160, y+45)], radius=6, fill=col)
        d.text((x+25, y+18), cat, fill=(255, 255, 255))
        d.text((x+20, y+60), name, fill=(255, 255, 255))
        d.text((x+20, y+95), desc, fill=(148, 163, 184))

    d.rounded_rectangle([(50, 575), (850, 625)], radius=8, fill=(30, 41, 59))
    d.text((70, 590), "100% Free & Open-Source Stack — Zero Cloud API Subscription Overhead", fill=(45, 212, 191))
    img.save("slide_images/slide9.png")

# 8. Slide 10: Hardware & Software Requirements
def make_slide10_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "System Deployment & Runtime Environment", fill=(250, 204, 21))

    # Hardware Card
    d.rounded_rectangle([(50, 100), (430, 520)], radius=14, fill=(30, 41, 59), outline=(13, 148, 136), width=2)
    d.rounded_rectangle([(70, 120), (410, 165)], radius=8, fill=(13, 148, 136))
    d.text((120, 133), "HARDWARE ENVIRONMENT", fill=(255, 255, 255))
    hw_lines = [
        "• Processor: Intel Core i3/i5 / AMD Ryzen",
        "• RAM: 8 GB Recommended (4 GB Minimum)",
        "• Camera: Standard 720p / 1080p Webcam",
        "• GPU: Integrated Intel HD / Radeon Graphics",
        "• Mobile: Android Smartphone (Android 8+)",
        "• Storage: 200 MB Free Space",
        "• Zero Sensor Hardware Requirements!"
    ]
    for i, l in enumerate(hw_lines):
        d.text((70, 200 + i * 44), l, fill=(226, 232, 240))

    # Software Card
    d.rounded_rectangle([(470, 100), (850, 520)], radius=14, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    d.rounded_rectangle([(490, 120), (830, 165)], radius=8, fill=(99, 102, 241))
    d.text((540, 133), "SOFTWARE ENVIRONMENT", fill=(255, 255, 255))
    sw_lines = [
        "• Operating System: Windows 10/11 or Ubuntu",
        "• Python Runtime: Python 3.10+",
        "• Vision Suite: MediaPipe Tasks 1.0+",
        "• ML Framework: Scikit-learn & NumPy",
        "• Backend Server: FastAPI + Uvicorn ASGI",
        "• Browser: Chrome / Edge / Firefox (WebGL)",
        "• IDE: VS Code / Android Studio"
    ]
    for i, l in enumerate(sw_lines):
        d.text((490, 200 + i * 44), l, fill=(226, 232, 240))

    d.rounded_rectangle([(50, 550), (850, 615)], radius=10, fill=(2, 6, 23), outline=(20, 184, 166), width=2)
    d.text((75, 572), "Accessible To Anyone: No Dedicated GPU or Costly Sensor Hardware Needed", fill=(45, 212, 191))
    img.save("slide_images/slide10.png")

# 9. Slide 11: Expected Outcomes Showcase
def make_slide11_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "Key Tangible Deliverables Matrix", fill=(16, 185, 129))

    outcomes = [
        ("Web Assistive Portal", "Live browser camera HUD tracking dual hands at 30+ FPS with instantaneous voice readout.", (13, 148, 136)),
        ("Anchor-Point HUD", "21-point skeletal mesh highlighting wrist origin, palm normal, and fingertip actuators.", (99, 102, 241)),
        ("Sentence Builder", "Intelligent queuing buffer assembling separate signs into cohesive vocalized sentences.", (244, 63, 94)),
        ("Native Android APK", "Portable mobile translation application enabling on-the-go communication anywhere.", (16, 185, 129)),
        ("SuperAdmin Console", "Administrative analytics, audit trails, and dynamic vocabulary manager.", (250, 204, 21))
    ]

    for i, (tit, desc, col) in enumerate(outcomes):
        y = 90 + i * 105
        d.rounded_rectangle([(50, y), (850, y+85)], radius=12, fill=(30, 41, 59), outline=col, width=2)
        d.rounded_rectangle([(65, y+15), (260, y+70)], radius=8, fill=col)
        d.text((80, y+30), tit, fill=(255, 255, 255))
        d.text((280, y+20), desc[:48], fill=(255, 255, 255))
        d.text((280, y+50), desc[48:], fill=(148, 163, 184))

    img.save("slide_images/slide11.png")

# 10. Slide 14: Feasibility Pillars
def make_slide14_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "Three Pillars of Project Feasibility", fill=(250, 204, 21))

    pillars = [
        ("Technical Feasibility", [
            "• MediaPipe runs in-browser via WASM/WebGL",
            "• Lightweight MLP runs in sub-10ms latency",
            "• Standard consumer webcams supply 30 FPS",
            "• Distance invariant coordinate normalization"
        ], (13, 148, 136), 50),
        ("Economic Feasibility", [
            "• 100% Free & Open-Source (FOSS) software",
            "• Zero cloud inference cost (runs on-device)",
            "• No hardware glove costs ($500+ saved)",
            "• Minimal server requirements (FastAPI/Mongo)"
        ], (99, 102, 241), 320),
        ("Operational Feasibility", [
            "• Zero learning curve — sign into camera",
            "• Instantaneous speech for hearing listeners",
            "• Deployable in schools, clinics, and offices",
            "• Responsive UI with dark/light themes"
        ], (16, 185, 129), 590)
    ]

    for title, points, col, x in pillars:
        d.rounded_rectangle([(x, 100), (x+260, 520)], radius=14, fill=(30, 41, 59), outline=col, width=2)
        d.rounded_rectangle([(x+15, 120), (x+245, 170)], radius=8, fill=col)
        d.text((x+25, 135), title, fill=(255, 255, 255))
        for j, p in enumerate(points):
            d.text((x+15, 200 + j * 75), p[:22], fill=(226, 232, 240))
            d.text((x+15, 230 + j * 75), p[22:], fill=(148, 163, 184))

    d.rounded_rectangle([(50, 550), (850, 615)], radius=10, fill=(2, 6, 23), outline=(20, 184, 166), width=2)
    d.text((80, 572), "Conclusion: Technically Sound, Economically Viable, and Socially Impactful", fill=(45, 212, 191))
    img.save("slide_images/slide14.png")

# 11. Slide 15: SDG Alignment Badges
def make_slide15_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "UN Sustainable Development Goals (SDGs)", fill=(45, 212, 191))

    sdgs = [
        ("SDG 3", "GOOD HEALTH & WELL-BEING", "Enables effective doctor-patient dialogue for deaf individuals in emergency clinics and medical consultations.", (76, 159, 56)),
        ("SDG 4", "QUALITY EDUCATION", "Ensures inclusive classroom participation for hearing-impaired students in mainstream colleges and universities.", (197, 25, 45)),
        ("SDG 10", "REDUCED INEQUALITIES", "Breaks systemic communication barriers, empowering deaf citizens with equal employment and legal access.", (221, 19, 103))
    ]

    for i, (num, tit, desc, col) in enumerate(sdgs):
        y = 100 + i * 155
        d.rounded_rectangle([(50, y), (850, y+135)], radius=14, fill=(30, 41, 59), outline=col, width=2)
        # SDG Badge Box
        d.rounded_rectangle([(70, y+20), (190, y+115)], radius=10, fill=col)
        d.text((95, y+50), num, fill=(255, 255, 255))
        
        d.text((220, y+30), tit, fill=(255, 255, 255))
        d.text((220, y+65), desc[:60], fill=(203, 213, 225))
        d.text((220, y+95), desc[60:], fill=(148, 163, 184))

    d.rounded_rectangle([(50, 580), (850, 625)], radius=8, fill=(30, 41, 59))
    d.text((70, 595), "Empowering 63M+ Deaf Indians Toward Social, Educational & Economic Inclusion", fill=(250, 204, 21))
    img.save("slide_images/slide15.png")

# 12. Slide 16: References & Standards Badge
def make_slide16_img():
    img, d = create_canvas()
    d.rounded_rectangle([(30, 25), (420, 65)], radius=8, fill=(30, 41, 59))
    d.text((45, 38), "Standards & Literature Endorsement", fill=(250, 204, 21))

    refs = [
        ("IEEE ACCESS & TPAMI", "Standard Bibliographic Citations (Zhang 2020, Rastgoo 2021, Starner 1998)", (13, 148, 136)),
        ("ISLRTC CORPUS", "Indian Sign Language Research and Training Centre Official Vocabulary Standards", (99, 102, 241)),
        ("GOOGLE RESEARCH", "MediaPipe Vision 21-Keypoint 3D Anatomical Spatial Coordinate Framework", (244, 63, 94)),
        ("W3C WEB SPEECH API", "Open Web Accessibility Standards for In-Browser Text-to-Speech Synthesis", (16, 185, 129))
    ]

    for i, (tit, desc, col) in enumerate(refs):
        y = 100 + i * 125
        d.rounded_rectangle([(50, y), (850, y+105)], radius=12, fill=(30, 41, 59), outline=col, width=2)
        d.rounded_rectangle([(70, y+20), (280, y+85)], radius=8, fill=col)
        d.text((85, y+42), tit, fill=(255, 255, 255))
        d.text((305, y+30), desc[:48], fill=(255, 255, 255))
        d.text((305, y+60), desc[48:], fill=(148, 163, 184))

    img.save("slide_images/slide16.png")

if __name__ == "__main__":
    make_slide3_img()
    make_slide4_img()
    make_slide5_img()
    make_slide6_img()
    make_slide7_img()
    make_slide8_img()
    make_slide9_img()
    make_slide10_img()
    make_slide11_img()
    make_slide14_img()
    make_slide15_img()
    make_slide16_img()
    print("All custom slide images generated successfully!")

