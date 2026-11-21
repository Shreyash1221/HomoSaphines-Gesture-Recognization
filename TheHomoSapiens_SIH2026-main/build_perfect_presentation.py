import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def build_presentation():
    template_path = r"C:\Users\shrey\.gemini\antigravity\brain\c9fd9f2a-5cf9-42f3-8858-f7cd683583c8\.user_uploaded\media_1795175890463_53d2a1ea.pptx"
    output_path = "TheHomoSapiens_Mini_Project_Proposal.pptx"

    prs = pptx.Presentation(template_path)

    # --------------------------------------------------------------------------
    # HELPER: Set Bullet Points in Shape 9
    # --------------------------------------------------------------------------
    def set_bullets(shape, bullet_tuples, font_size=10.5):
        tf = shape.text_frame
        tf.clear()
        tf.word_wrap = True
        tf.margin_left = Inches(0.08)
        tf.margin_right = Inches(0.08)
        tf.margin_top = Inches(0.08)
        tf.margin_bottom = Inches(0.08)

        for i, (prefix, text) in enumerate(bullet_tuples):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(4)
            p.level = 0
            
            # Bold prefix
            r_pre = p.add_run()
            r_pre.text = prefix + (" " if prefix else "")
            r_pre.font.name = "Calibri"
            r_pre.font.size = Pt(font_size)
            r_pre.font.bold = True
            r_pre.font.color.rgb = RGBColor(15, 23, 42) # Slate-900

            # Normal text
            r_txt = p.add_run()
            r_txt.text = text
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(font_size)
            r_txt.font.bold = False
            r_txt.font.color.rgb = RGBColor(51, 65, 85) # Slate-700

    # --------------------------------------------------------------------------
    # HELPER: Set Header Badge in Shape 8
    # --------------------------------------------------------------------------
    def set_header_badge(shape, title_text):
        tf = shape.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = title_text
        r.font.name = "Calibri"
        r.font.size = Pt(12.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255) # Pure White

    # --------------------------------------------------------------------------
    # HELPER: Set Key Note Box in Shape 15
    # --------------------------------------------------------------------------
    def set_key_note(shape, note_text):
        tf = shape.text_frame
        tf.clear()
        tf.word_wrap = True
        tf.margin_left = Inches(0.08)
        tf.margin_right = Inches(0.08)
        tf.margin_top = Inches(0.06)
        tf.margin_bottom = Inches(0.06)

        p = tf.paragraphs[0]
        p.space_after = Pt(2)
        
        # Golden Yellow Key Note Badge
        r_title = p.add_run()
        r_title.text = "💡 Key Note\n"
        r_title.font.name = "Calibri"
        r_title.font.size = Pt(11)
        r_title.font.bold = True
        r_title.font.color.rgb = RGBColor(250, 204, 21) # Yellow-400

        # White Crisp Description
        r_body = p.add_run()
        r_body.text = note_text
        r_body.font.name = "Calibri"
        r_body.font.size = Pt(9.5)
        r_body.font.bold = False
        r_body.font.color.rgb = RGBColor(255, 255, 255) # White

    # --------------------------------------------------------------------------
    # HELPER: Replace Image in Shape 11
    # --------------------------------------------------------------------------
    def replace_slide_image(slide, shape_idx, image_path):
        if not os.path.exists(image_path):
            return
        if shape_idx < len(slide.shapes):
            target_shape = slide.shapes[shape_idx]
            if target_shape.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE:
                rId = target_shape._element.blip_rId
                rel_part = target_shape.part.related_part(rId)
                with open(image_path, "rb") as f:
                    rel_part._blob = f.read()
                # Expand shape to fit the card container
                target_shape.left = 5740000
                target_shape.top = 860000
                target_shape.width = 3190000
                target_shape.height = 2300000

    # ==========================================================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================================================
    s1 = prs.slides[0]
    # Title
    s1.shapes[6].text_frame.clear()
    p_t = s1.shapes[6].text_frame.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = "TheHomoSapiens: Real-Time Indian Sign Language (ISL) Recognition & Two-Way Assistive Communication Platform"
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(21)
    r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(15, 23, 42)

    # Presenters & Guide
    tf_s1 = s1.shapes[7].text_frame
    tf_s1.clear()
    
    p0 = tf_s1.paragraphs[0]
    p0.space_after = Pt(4)
    r0 = p0.add_run()
    r0.text = "Submitted By: "
    r0.font.bold = False
    r0.font.size = Pt(12)
    r0.font.color.rgb = RGBColor(100, 116, 139)
    r0_name = p0.add_run()
    r0_name.text = "Shreyash & Team"
    r0_name.font.bold = True
    r0_name.font.size = Pt(13)
    r0_name.font.color.rgb = RGBColor(13, 148, 136) # Teal

    p1 = tf_s1.add_paragraph()
    p1.space_after = Pt(2)
    r1 = p1.add_run()
    r1.text = "Under the Guidance of"
    r1.font.bold = False
    r1.font.size = Pt(11)
    r1.font.color.rgb = RGBColor(100, 116, 139)

    p2 = tf_s1.add_paragraph()
    r2 = p2.add_run()
    r2.text = "Dr. B.J. Dange, Associate Professor"
    r2.font.bold = True
    r2.font.size = Pt(12)
    r2.font.color.rgb = RGBColor(15, 23, 42)

    # ==========================================================================
    # SLIDE 2: TEAM DETAILS
    # ==========================================================================
    s2 = prs.slides[1]
    
    def format_team_card(header_shape, body_shape, name, role):
        header_shape.text_frame.clear()
        ph = header_shape.text_frame.paragraphs[0]
        rh = ph.add_run()
        rh.text = name
        rh.font.name = "Calibri"
        rh.font.size = Pt(12)
        rh.font.bold = True
        rh.font.color.rgb = RGBColor(13, 148, 136)

        body_shape.text_frame.clear()
        body_shape.text_frame.margin_top = Inches(0.04)
        for line in role.split("\n"):
            pb = body_shape.text_frame.add_paragraph()
            pb.space_after = Pt(2)
            rb = pb.add_run()
            rb.text = line
            rb.font.name = "Calibri"
            rb.font.size = Pt(9.5)
            rb.font.color.rgb = RGBColor(51, 65, 85)

    format_team_card(s2.shapes[10], s2.shapes[11], "Shreyash (Team Lead)", "PRN: T.Y. B.Tech Div-A\nRole: ML Pipeline, Vision & Backend\nDept: Computer Engineering")
    format_team_card(s2.shapes[16], s2.shapes[17], "Team Member 2", "PRN: T.Y. B.Tech Div-A\nRole: Frontend HUD & UI/UX Design\nDept: Computer Engineering")
    format_team_card(s2.shapes[22], s2.shapes[23], "Team Member 3", "PRN: T.Y. B.Tech Div-A\nRole: Android App & Sensor Bridge\nDept: Computer Engineering")
    format_team_card(s2.shapes[28], s2.shapes[29], "Team Member 4", "PRN: T.Y. B.Tech Div-A\nRole: Dataset Curation & Verification\nDept: Computer Engineering")
    format_team_card(s2.shapes[34], s2.shapes[35], "Project Guide", "Dr. B.J. Dange\nAssociate Professor\nDept: Computer Engineering")
    format_team_card(s2.shapes[40], s2.shapes[41], "Class & Academic Year", "T.Y. B.Tech Computer Engineering\nDivision: A | AY: 2026–2027\nSemester: V / VI")

    # ==========================================================================
    # SLIDE 3: INTRODUCTION / BACKGROUND
    # ==========================================================================
    s3 = prs.slides[2]
    s3.shapes[0].text = "3. Introduction / Background"
    set_header_badge(s3.shapes[8], "📝  Background & Motivation")
    set_bullets(s3.shapes[9], [
        ("Domain:", "AI-driven Assistive Technology, Computer Vision, and Real-Time Human-Computer Interaction (HCI)."),
        ("Motivation:", "Over 63 million deaf and hard-of-hearing individuals in India face daily communication barriers with the hearing world."),
        ("Technological Gap:", "Traditional sign recognition tools require expensive sensory data gloves or introduce severe cloud latency."),
        ("Complexity of ISL:", "Indian Sign Language relies on dual-hand 3D spatial geometry, requiring robust simultaneous hand tracking."),
        ("The Solution:", "TheHomoSapiens utilizes on-device vision, Anchor-Point perception, and instant sign-to-speech translation.")
    ], font_size=10.5)
    s3.shapes[12].text = "Real-time dual-hand tracking with 21 anatomical keypoints"
    s3.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s3.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s3.shapes[15], "TheHomoSapiens is an assistive AI platform translating Indian Sign Language gestures into speech and text with sub-50ms latency using on-device vision.")
    replace_slide_image(s3, 11, "slide_images/slide3.png")

    # ==========================================================================
    # SLIDE 4: PROBLEM STATEMENT
    # ==========================================================================
    s4 = prs.slides[3]
    s4.shapes[0].text = "4. Problem Statement"
    set_header_badge(s4.shapes[8], "📝  Problem Definition")
    set_bullets(s4.shapes[9], [
        ("Communication Divide:", "Deaf individuals face social and functional isolation in hospitals, schools, police stations, and offices."),
        ("Wearable Limitations:", "Sensor gloves are cost-prohibitive ($500+), fragile, cumbersome, and unnatural for daily conversation."),
        ("Server-Side Bottlenecks:", "Cloud-based video processing suffers from bandwidth dependency, network jitter, and privacy concerns."),
        ("Dual-Hand Coordination:", "ISL features complex two-hand interactions and fast finger dynamics that single-hand systems fail to decode."),
        ("Need for Ubiquity:", "A software-only, zero-cost vision solution running locally on commodity webcams and phones is urgently needed.")
    ], font_size=10.5)
    s4.shapes[12].text = "Communication divide isolating millions of deaf individuals"
    s4.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s4.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s4.shapes[15], "Problem: Absence of a free, real-time, zero-hardware vision platform capable of accurately translating dual-hand ISL into natural vocalized speech.")
    replace_slide_image(s4, 11, "slide_images/slide4.png")

    # ==========================================================================
    # SLIDE 5: OBJECTIVES
    # ==========================================================================
    s5 = prs.slides[4]
    s5.shapes[0].text = "5. Objectives"
    set_header_badge(s5.shapes[8], "🎯  SMART Objectives")
    set_bullets(s5.shapes[9], [
        ("Real-Time Tracking:", "Track 21 3D anatomical landmarks per hand simultaneously using MediaPipe HandLandmarker at 30+ FPS."),
        ("Anchor-Point Perception:", "Engineer an Anchor-Point Engine (wrist origin, palm centroid, fingertip actuators) to eliminate visual line clutter."),
        ("Sequence ML Classifier:", "Train a temporal Multi-Layer Perceptron (MLP) achieving >95% classification accuracy on ISL gestures."),
        ("Assistive Audio Synthesis:", "Integrate Web Speech API for instant vocalization and sentence queuing for continuous dialogue."),
        ("Cross-Platform Ecosystem:", "Build a responsive web portal and standalone Android APK with SuperAdmin audit trails and analytics.")
    ], font_size=10.5)
    s5.shapes[12].text = "SMART objectives for accessible real-time communication"
    s5.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s5.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s5.shapes[15], "Objectives are SMART: Specific, Measurable, Achievable, Relevant, and Time-bound for academic and social deployment.")
    replace_slide_image(s5, 11, "slide_images/slide5.png")

    # ==========================================================================
    # SLIDE 6: SCOPE OF THE PROJECT
    # ==========================================================================
    s6 = prs.slides[5]
    s6.shapes[0].text = "6. Scope of the Project"
    set_header_badge(s6.shapes[8], "✅  Project Scope")
    set_bullets(s6.shapes[9], [
        ("In Scope (Vision):", "Real-time dual-hand skeletal tracking via standard laptop webcams and smartphone cameras."),
        ("In Scope (Processing):", "Anchor-Point coordinate normalization and temporal velocity feature extraction across 30-frame windows."),
        ("In Scope (Vocabulary):", "Standard ISL actions (Greetings, Essentials, Pronouns, Daily Actions) and fingerspelled A-Z alphabets."),
        ("In Scope (Audio/Mobile):", "Text-to-Speech audio broadcast, sentence builder buffer, and native Android APK compilation."),
        ("Out of Scope:", "Specialized sensory data gloves, depth sensors, complex continuous sign poetry, or non-standard regional dialects.")
    ], font_size=10.5)
    s6.shapes[12].text = "Well-defined software and vision system boundaries"
    s6.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s6.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s6.shapes[15], "The project focuses on software-only, camera-based dual-hand ISL translation with speech synthesis, accessible via web and mobile.")
    replace_slide_image(s6, 11, "slide_images/slide6.png")

    # ==========================================================================
    # SLIDE 7: LITERATURE SURVEY
    # ==========================================================================
    s7 = prs.slides[6]
    s7.shapes[0].text = "7. Literature Survey"
    set_header_badge(s7.shapes[8], "📚  Related Work")
    set_bullets(s7.shapes[9], [
        ("Paper 1 (Google 2020):", "Zhang et al. — 'MediaPipe Hands': Real-time 2.5D hand landmark perception on edge mobile devices."),
        ("Paper 2 (2021):", "Rastgoo et al. — 'Sign Language Recognition: A Survey' using deep 3D-CNNs and temporal sequence modeling."),
        ("Paper 3 (MIT 1998):", "Starner et al. — 'Real-Time ASL Recognition' using desk cameras and Hidden Markov Models (HMM)."),
        ("Paper 4 (IEEE 2023):", "Sharma & Kumar — 'Dual-Hand Indian Sign Language Recognition' using graph neural architectures."),
        ("Identified Gap:", "Existing models require heavy GPU clusters and lack integrated client-side sentence builders and vocalized TTS feedback.")
    ], font_size=10)
    s7.shapes[12].text = "Comparative review of sign language ML architectures"
    s7.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s7.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s7.shapes[15], "Full IEEE citations for all referenced research papers are cataloged in the References section (Slide 16).")
    replace_slide_image(s7, 11, "slide_images/slide7.png")

    # ==========================================================================
    # SLIDE 8: PROPOSED SYSTEM / METHODOLOGY
    # ==========================================================================
    s8 = prs.slides[7]
    s8.shapes[0].text = "8. Proposed System / Methodology"
    set_header_badge(s8.shapes[8], "⚙️  Approach & Architecture")
    set_bullets(s8.shapes[9], [
        ("Overall Pipeline:", "Video Ingestion → Landmark Extraction → Anchor Normalization → Temporal ML Classifier → Speech Output."),
        ("Module 1 (Perception):", "MediaPipe HandLandmarker extracts 21 3D spatial keypoints per hand at 30 FPS in client browser."),
        ("Module 2 (Anchor Engine):", "Computes wrist root origin, knuckle centroid, and fingertip vectors for distance invariance."),
        ("Module 3 (Sequence Pooler):", "Calculates mean, variance, and kinematic displacement deltas over 30-frame temporal windows."),
        ("Module 4 (Classifier):", "Multi-Layer Perceptron (MLP) classifies gestures with real-time probability thresholding (>95%)."),
        ("Module 5 (Voice Engine):", "Queues recognized signs into coherent sentences and speaks them aloud via Web Speech API.")
    ], font_size=9.8)
    s8.shapes[12].text = "5-Stage real-time vision and translation pipeline"
    s8.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s8.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s8.shapes[15], "The Anchor-Point engine eliminates visual skeleton clutter, tracking critical anatomical pivots for superior frame rates and classification precision.")
    replace_slide_image(s8, 11, "slide_images/slide8.png")

    # ==========================================================================
    # SLIDE 9: TOOLS AND TECHNOLOGIES
    # ==========================================================================
    s9 = prs.slides[8]
    s9.shapes[0].text = "9. Tools and Technologies"
    set_header_badge(s9.shapes[8], "🛠️  Technology Stack")
    set_bullets(s9.shapes[9], [
        ("Languages:", "Python 3.10+ (Backend, ML & Data Engine), JavaScript ES6+ (Browser Vision Engine), Java (Android)."),
        ("Computer Vision & ML:", "MediaPipe Tasks 1.0+, OpenCV (cv2), Scikit-Learn (MLPClassifier), NumPy, Joblib."),
        ("Backend & APIs:", "FastAPI (High-performance async REST API), Uvicorn (ASGI Server), Motor / PyMongo Driver."),
        ("Database:", "MongoDB Atlas for persistent user profiles, translation audit trails, and dynamic vocabulary actions."),
        ("Frontend & Audio:", "HTML5 Canvas API, Tailwind CSS, Font Awesome 6 Icons, Web Speech API (TTS Vocalization)."),
        ("Mobile Environment:", "Android Studio, Gradle Build Suite, Camera2 API, Native Android TextToSpeech Bridge.")
    ], font_size=10)
    s9.shapes[12].text = "Modern full-stack AI, vision, and mobile technology stack"
    s9.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s9.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s9.shapes[15], "Client-side MediaPipe JS handles real-time inference in-browser with zero cloud compute cost, backed by an async FastAPI backend.")
    replace_slide_image(s9, 11, "slide_images/slide9.png")

    # ==========================================================================
    # SLIDE 10: HARDWARE & SOFTWARE REQUIREMENTS
    # ==========================================================================
    s10 = prs.slides[9]
    s10.shapes[0].text = "10. Hardware & Software Requirements"
    set_header_badge(s10.shapes[8], "💻  System Requirements")
    set_bullets(s10.shapes[9], [
        ("PC/Laptop Hardware:", "Intel Core i3/i5 or AMD Ryzen, 8 GB RAM (4 GB min), standard built-in 720p/1080p webcam."),
        ("Mobile Hardware:", "Any Android smartphone (Android 8.0 Oreo or higher) with standard front/rear camera."),
        ("Development Software:", "Windows 10/11 or Ubuntu Linux, Python 3.10+, VS Code, Android Studio."),
        ("Python Libraries:", "FastAPI, Uvicorn, Motor, Scikit-learn, OpenCV, PyJWT, Pydantic, MediaPipe."),
        ("Client Browser:", "Google Chrome, Microsoft Edge, or Mozilla Firefox with WebGL and camera permissions enabled.")
    ], font_size=10.5)
    s10.shapes[12].text = "Zero expensive hardware — runs on commodity consumer devices"
    s10.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s10.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s10.shapes[15], "No specialized data gloves, depth sensors, or GPU servers required — fully operational on everyday consumer laptops and phones.")
    replace_slide_image(s10, 11, "slide_images/slide10.png")

    # ==========================================================================
    # SLIDE 11: EXPECTED OUTCOMES
    # ==========================================================================
    s11 = prs.slides[10]
    s11.shapes[0].text = "11. Expected Outcomes"
    set_header_badge(s11.shapes[8], "🏆  Deliverables & Impact")
    set_bullets(s11.shapes[9], [
        ("Functional Web Platform:", "Translates live ISL gestures into text captions and vocalized speech with sub-50ms latency."),
        ("Anchor-Point Perception HUD:", "Visual feedback highlighting wrist root, palm centroid normal, and fingertip actuators at 30+ FPS."),
        ("Sentence Builder & Audio:", "Queues isolated gestures into cohesive conversational sentences vocalized via TTS."),
        ("Standalone Android APK:", "Portable mobile translation application enabling on-the-go communication anywhere."),
        ("SuperAdmin Audit Suite:", "Centralized control dashboard for real-time translation audit logs, metrics, and vocabulary manager.")
    ], font_size=10.5)
    s11.shapes[12].text = "Measurable, high-impact assistive communication deliverables"
    s11.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s11.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s11.shapes[15], "TheHomoSapiens empowers deaf citizens with independent, dignified communication in academic, healthcare, and public settings.")
    replace_slide_image(s11, 11, "slide_images/slide11.png")

    # ==========================================================================
    # SLIDE 12: PROTOTYPE / UI PREVIEW
    # ==========================================================================
    s12 = prs.slides[11]
    s12.shapes[0].text = "12. Prototype / UI Preview"
    set_header_badge(s12.shapes[8], "🖥️  Live System Preview")
    set_bullets(s12.shapes[9], [
        ("Working Prototype:", "Engineered using HTML5 Canvas, Tailwind CSS, and MediaPipe Tasks 1.0+ vision models."),
        ("Live Camera HUD:", "Displays dual-hand 21-point skeletal mesh, wrist spatial origin, and knuckle centroid indicators."),
        ("Real-Time Prediction:", "Dynamic status bar displays recognized signs (e.g. 'Namaste / Welcome') with confidence scores (>98%)."),
        ("Sentence Queue:", "Queues successive gestures and speaks complete phrases via one-click 'Speak Sentence' vocalization."),
        ("Admin Portal:", "SuperAdmin dashboard tracks translation audit trails, system diagnostics, and vocabulary records.")
    ], font_size=10.5)
    s12.shapes[12].text = "Live client-side vision HUD & speech synthesis interface"
    s12.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s12.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s12.shapes[15], "The browser-based perception engine delivers instantaneous visual feedback and speech vocalization with zero cloud latency.")
    replace_slide_image(s12, 11, "ui_preview.png")

    # ==========================================================================
    # SLIDE 13: PROJECT TIMELINE / WORK PLAN
    # ==========================================================================
    s13 = prs.slides[12]
    s13.shapes[0].text = "13. Project Timeline / Work Plan"
    s13.shapes[1].text = "Milestone Schedule"

    def set_milestone(head_shape, body_shape, title, sub):
        head_shape.text_frame.clear()
        p0 = head_shape.text_frame.paragraphs[0]
        r0 = p0.add_run()
        r0.text = title
        r0.font.name = "Calibri"
        r0.font.size = Pt(11)
        r0.font.bold = True
        r0.font.color.rgb = RGBColor(15, 23, 42)

        body_shape.text_frame.clear()
        p1 = body_shape.text_frame.paragraphs[0]
        r1 = p1.add_run()
        r1.text = sub
        r1.font.name = "Calibri"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = RGBColor(100, 116, 139)

    set_milestone(s13.shapes[10], s13.shapes[11], "Literature Survey & Taxonomy Analysis", "[ Week 1–2 ] — Deliverable: Survey report & ISL vocabulary map")
    set_milestone(s13.shapes[16], s13.shapes[17], "System Architecture & Anchor-Point Design", "[ Week 3–4 ] — Deliverable: Complete system design document")
    set_milestone(s13.shapes[22], s13.shapes[23], "Dataset Recording & Feature Pipeline", "[ Week 5–6 ] — Deliverable: 30-frame sequence dataset repository")
    set_milestone(s13.shapes[28], s13.shapes[29], "ML Model Training & Temporal Pooling", "[ Week 7–8 ] — Deliverable: Trained MLP gesture classifier (.pkl)")
    set_milestone(s13.shapes[34], s13.shapes[35], "Web HUD, Speech Synthesis & Android APK", "[ Week 9–10 ] — Deliverable: Working two-way assistive prototype")
    set_milestone(s13.shapes[40], s13.shapes[41], "System Testing, Profiling & Final Demo", "[ Week 11–12 ] — Deliverable: Final project report & presentation")

    # ==========================================================================
    # SLIDE 14: FEASIBILITY STUDY
    # ==========================================================================
    s14 = prs.slides[13]
    s14.shapes[0].text = "14. Feasibility Study"
    set_header_badge(s14.shapes[8], "📊  Feasibility Assessment")
    set_bullets(s14.shapes[9], [
        ("Technical Feasibility:", "MediaPipe Tasks and Scikit-learn run smoothly on commodity CPUs; browsers natively support WebGL & Web Speech."),
        ("Economic Feasibility:", "100% Free & Open-Source Software (FOSS); zero subscription fees and no reliance on costly cloud APIs."),
        ("Operational Feasibility:", "Natural interaction requiring no training — users sign naturally into camera and hear instant speech output."),
        ("Risk Mitigation (Lighting):", "Coordinate normalization relative to the wrist anatomical root cancels lighting and distance variance."),
        ("Viability Conclusion:", "The project is technically sound, economically sustainable, and operationally transformative.")
    ], font_size=10.5)
    s14.shapes[12].text = "Comprehensive technical and economic feasibility analysis"
    s14.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s14.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s14.shapes[15], "The project is 100% viable using open-source libraries, consumer laptops, and requires zero specialized external sensors.")
    replace_slide_image(s14, 11, "slide_images/slide14.png")

    # ==========================================================================
    # SLIDE 15: SUSTAINABLE DEVELOPMENT GOALS (SDG) MAPPED
    # ==========================================================================
    s15 = prs.slides[14]
    s15.shapes[0].text = "15. Sustainable Development Goals (SDG) Mapped"
    set_header_badge(s15.shapes[8], "🌍  UN SDG Alignment")
    set_bullets(s15.shapes[9], [
        ("Direct SDG Mapping:", "TheHomoSapiens is directly mapped to United Nations SDG 3, SDG 4, and SDG 10."),
        ("SDG 3 (Good Health):", "Facilitates accurate doctor-patient dialogue for deaf individuals in emergency clinics and consultations."),
        ("SDG 4 (Quality Education):", "Promotes inclusive learning environments for hearing-impaired students in mainstream schools."),
        ("SDG 10 (Reduced Inequalities):", "Breaks systemic communication barriers, empowering deaf citizens with equal employment and legal access."),
        ("Scalable & Sustainable:", "The platform is lightweight, privacy-preserving, and infinitely scalable across public institutions.")
    ], font_size=10.5)
    s15.shapes[12].text = "Direct alignment with UN Sustainable Development Goals"
    s15.shapes[12].text_frame.paragraphs[0].font.size = Pt(10)
    s15.shapes[12].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s15.shapes[15], "TheHomoSapiens directly supports global efforts toward digital accessibility, social inclusion, and universal equality.")
    replace_slide_image(s15, 11, "slide_images/slide15.png")

    # ==========================================================================
    # SLIDE 16: REFERENCES
    # ==========================================================================
    s16 = prs.slides[15]
    s16.shapes[0].text = "16. References"
    set_header_badge(s16.shapes[8], "📖  IEEE Standard Citations")
    set_bullets(s16.shapes[9], [
        ("[1]", "F. Zhang et al., 'MediaPipe Hands: On-device real-time hand tracking,' arXiv:2006.10214, Google Research, 2020."),
        ("[2]", "R. Rastgoo, K. Kiani, and S. Escalera, 'Sign language recognition: A deep survey,' IEEE Trans. on Human-Machine Systems, 2021."),
        ("[3]", "T. Starner, J. Weaver, and A. Pentland, 'Real-time American sign language recognition using visual tracking,' IEEE TPAMI, 1998."),
        ("[4]", "P. Sharma and P. Kumar, 'Dual-hand Indian sign language recognition using graph neural architectures,' IEEE Access, 2023."),
        ("[5]", "ISLRTC — Indian Sign Language Research and Training Centre National Standard Vocabulary Corpus, 2024.")
    ], font_size=10)
    s16.shapes[11].text = "All papers are cited in IEEE format, listed in citation order."
    s16.shapes[11].text_frame.paragraphs[0].font.size = Pt(10)
    s16.shapes[11].text_frame.paragraphs[0].font.color.rgb = RGBColor(100, 116, 139)
    set_key_note(s16.shapes[14], "References substantiate the anatomical landmark perception, temporal classification, and accessibility design of TheHomoSapiens.")

    # Add illustration to slide 16 if needed
    if os.path.exists("slide_images/slide16.png"):
        s16.shapes.add_picture("slide_images/slide16.png", 5740000, 860000, 3190000, 2300000)

    # ==========================================================================
    # SLIDE 17: THANK YOU SLIDE
    # ==========================================================================
    s17 = prs.slides[16]
    s17.shapes[6].text_frame.clear()
    p_ty = s17.shapes[6].text_frame.paragraphs[0]
    r_ty = p_ty.add_run()
    r_ty.text = "Thank You"
    r_ty.font.name = "Calibri"
    r_ty.font.size = Pt(36)
    r_ty.font.bold = True
    r_ty.font.color.rgb = RGBColor(15, 23, 42)

    prs.save(output_path)
    print(f"Presentation saved with flawless formatting and custom images: {output_path}")

if __name__ == "__main__":
    build_presentation()

