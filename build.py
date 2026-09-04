#!/usr/bin/env python3
"""
Generates the eight HTML pages plus per-room css/js stubs.
Run:  python3 build.py

SOURCES
-------
Prose comes from Yeonhoo's filled-in content workbook, kept in his own voice and
only tightened for the page. Factual detail (apparatus, essay questions, course
topics, award wording) is drawn from the supplied PDFs. General context that
claims nothing personal — what a von Mises truss is, how ABRSM grades work — is
mine. Nothing is invented.
"""

import os

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

NAME = "Yeonhoo Kim"
EMAIL = "ykim2027@chadwickschool.org"
RESUME = "assets/resume/Yeonhoo-Kim-Resume.pdf"
INSTAGRAM = "https://www.instagram.com/yeonhoo__09/"

IMG = "assets/images/"
DOC = "assets/docs/"
MED = "assets/media/"

ROOMS = [
    # ══════════════════════════════════════════════════ ROOM 01
    {
        "slug": "physics-research",
        "num": "01", "title": "Physics &amp; Research", "plain": "Physics & Research",
        "years": "2025—2026", "count_word": "Four entries", "count_short": "4 entries",
        "tile": {"src": IMG + "room-physics-tile.jpg", "ratio": "ratio-16-9",
                 "alt": "Yeonhoo in the lab at Jeonbuk University, in front of a whiteboard showing bi-stable and mono-stable switch working"},
        "wide": True,
        "tile_caption": ("Nonlinear vibration with a university advisor, an Extended Essay in "
                         "revision, and two Stanford courses still open."),
        "intro": ("The first and most valuable room. Understanding the world through physics: "
                  "studying, researching, and experimenting."),
        "stats": [("1", "Paper submitted"), ("1", "In revision"), ("1", "Conference poster")],
        "entries": [
            {
                "n": "1.1",
                "short": "Asymmetric Monostable Behavior of an Elastic von Mises Truss",
                "title": "Asymmetric Monostable Behavior of an Elastic von Mises Truss Under Base Excitation",
                "year": "2025—",
                "meta": ["April 2025 — present &middot; Advisor, Professor P. Kim, Jeonbuk University",
                         "Poster accepted, GCIMM 2026 &middot; Submitted, Journal of Emerging Investigators 2026"],
                "label": ("Research paper. Simulation built in MATLAB. Advised at Jeonbuk "
                          "University. Poster accepted for presentation at GCIMM 2026; submitted "
                          "to the Journal of Emerging Investigators, 2026."),
                "image": {"src": IMG + "truss-whiteboard.jpg", "kind": "photo",
                          "alt": "Whiteboard at the Jeonbuk University lab showing bi-stable and mono-stable switch derivations",
                          "caption": "Working through the bi-stable and mono-stable cases at the lab."},
                "thumbs": [
                    {"src": IMG + "truss-diagram.jpg", "kind": "document",
                     "alt": "Free-body diagram of the von Mises truss under base excitation"},
                    {"src": IMG + "truss-bifurcation.jpg", "kind": "document",
                     "alt": "MATLAB amplitude sweep showing the bifurcation at G = 0.2"},
                    {"src": IMG + "truss-matlab.jpg", "kind": "photo",
                     "alt": "MATLAB simulation code on a laptop"},
                ],
                "paras": [
                    "A von Mises truss is about as simple as a structure gets: two straight bars, "
                    "pinned at their outer ends, meeting at a shallow peak in the middle. Press "
                    "down on that peak hard enough and the whole thing snaps through and inverts. "
                    "Whether it springs back on its own or stays inverted is the difference "
                    "between monostable and bistable behaviour, and it is why these trusses turn "
                    "up in energy harvesters, vibration isolators and mechanical switches.",
                    "I became interested in the project while I was studying mechanical vibration. "
                    "Reading through papers on bistable systems and forced vibration, I came "
                    "across the paper by Ghoshal et al., which raised questions in me about "
                    "testing conditions similar to theirs.",
                    "I was able to contact Professor P. Kim through a personal connection &mdash; he "
                    "was a friend of my parents from the same university, and I got a chance to "
                    "talk with him. After that first conversation I reached out on my own about "
                    "studying nonlinear vibration. He gave me recorded lectures and homework so I "
                    "could build up what I needed, starting from engineering mathematics like "
                    "second-order ordinary differential equations and moving to nonlinear "
                    "vibration itself, damping included.",
                    "The study is a simulation, built in MATLAB. <strong>The result was that a "
                    "large enough constant biasing force transforms the symmetric bistable system "
                    "&mdash; one OFF and two ON states &mdash; into an asymmetric monostable "
                    "system with one OFF and one ON state</strong>, depending on both the "
                    "amplitude and the frequency of the base excitation.",
                    "Most of the difficulty was MATLAB itself, which was new to me; I worked "
                    "through tutorials until I could generate the results I wanted. There were "
                    "also moments when unexpected results came out &mdash; large interwell "
                    "motions where I had expected small oscillations &mdash; which pushed me to "
                    "analyse the system more deeply.",
                ],
                "links": [("Read the paper, PDF &#8595;", DOC + "von-mises-truss-paper.pdf", True)],
            },
            {
                "n": "1.2",
                "short": "Effect of Temperature Parameter on a Vibrating Cantilever System",
                "title": "Investigation on the Effect of Temperature Parameter on a Vibrating Cantilever System",
                "year": "2025—",
                "meta": ["Grade 11 — present &middot; IB Extended Essay, carried on as an individual investigation"],
                "label": ("Extended Essay in physics, still in revision. Research question: how "
                          "does temperature affect the natural frequency of a stainless steel "
                          "cantilever beam at a fixed length?"),
                "image": {"src": IMG + "ee-apparatus.jpg", "kind": "photo",
                          "alt": "The cantilever rig inside the oven: a steel ruler clamped between wooden blocks with a G-clamp, sensor cable taped to a post",
                          "caption": "The rig inside the oven."},
                "thumbs": [
                    {"src": IMG + "ee-sensor-trace.jpg", "kind": "document",
                     "alt": "Hall-effect sensor trace showing the decaying oscillation of the cantilever"},
                ],
                "paras": [
                    "A cantilever is a beam clamped at one end and free at the other &mdash; a "
                    "diving board. Displace the free end and it oscillates at a natural frequency "
                    "set by its geometry and its stiffness. Stiffness is not a fixed property: "
                    "heat a metal beam and its Young&rsquo;s modulus falls, so the frequency it "
                    "wants to ring at drifts with temperature.",
                    "The apparatus is deliberately cheap. A stainless steel ruler is clamped "
                    "between two wooden blocks with G-clamps at the 15 cm mark, magnets are fixed "
                    "at the free end, and a Hall-effect sensor reads the oscillation. The whole "
                    "assembly goes into an oven, and readings run from room temperature up to "
                    "140&nbsp;&deg;C.",
                    "Two effects compete as the steel heats. The falling Young&rsquo;s modulus "
                    "lowers the frequency, and thermal expansion lengthens the beam slightly, "
                    "which lowers it too &mdash; but across this range the expansion term is "
                    "roughly eight times smaller, so the modulus dominates.",
                    "This began as my Extended Essay, but I have taken it past what the essay "
                    "required and am still revising it as an individual investigation.",
                ],
                "links": [],
            },
            {
                "n": "1.3",
                "short": "Gravitation to Levitation",
                "title": "Gravitation to Levitation: Physics from Supernova to Superconductor",
                "year": "2026",
                "meta": ["July 2026 &middot; University of Chicago, summer course &middot; Grade: A"],
                "label": ("Three-week summer session at the University of Chicago, taught in the "
                          "Kersten Physics Teaching Center. College credit, grade A."),
                "image": {"src": IMG + "uchicago-library.jpg", "kind": "photo",
                          "alt": "Yeonhoo working through problems in a University of Chicago library, campus lanyard on the desk",
                          "caption": "Working through the problem sets, Regenstein."},
                "thumbs": [
                    {"src": IMG + "uchicago-sign.jpg", "kind": "photo",
                     "alt": "Yeonhoo beside the University of Chicago sign on campus"},
                    {"src": IMG + "uchicago-class.jpg", "kind": "photo",
                     "alt": "The summer session class in the Kersten Physics Teaching Center"},
                ],
                "paras": [
                    "The three weeks were a magnificent experience &mdash; a chance to keep "
                    "discovering physics beyond the high school level, in a discussion setting, "
                    "with people who are interested in the subject as much as I am &mdash; three weeks of discussion-based, university-style lectures. It confirmed "
                    "my interest in physics and made me even more attracted to it.",
                    "The course ran the length of its own title, gravitation at one end and "
                    "levitation at the other. Alongside the lectures we worked in groups on two "
                    "presentations. The first was on the Hubble tension &mdash; the disagreement "
                    "between two ways of measuring how fast the universe is expanding, one built "
                    "from the cosmic distance ladder and one from the cosmic microwave "
                    "background. The second was on blackbody radiation, starting from the "
                    "question of where starlight actually comes from.",
                    "There were guest lectures too. The one I keep returning to was a graduate "
                    "student&rsquo;s lecture on dark matter and X-ray telescopes.",
                ],
                "links": [("Hubble tension slides &#8595;", DOC + "uchicago-hubble-tension.pdf", True),
                          ("Blackbody radiation slides &#8595;", DOC + "uchicago-blackbody-radiation.pdf", False)],
            },
            {
                "n": "1.4",
                "short": "Two Stanford courses in progress",
                "title": "Special Relativity and Quantum Mechanics",
                "year": "2026—",
                "meta": ["2026 — present &middot; Stanford University via Coursera &middot; Stanford Online via edX &middot; Both in progress"],
                "label": ("Understanding Einstein: The Special Theory of Relativity. Quantum "
                          "Mechanics for Scientists and Engineers 1. Taken alongside IB Year 2."),
                "paras": [
                    "I came back from the three weeks in Chicago wanting more of that level, so I "
                    "signed up for two college-level courses and have been working through them "
                    "alongside IB Year 2.",
                    "Special relativity begins from two assumptions &mdash; that the laws of "
                    "physics look identical to anyone moving at constant velocity, and that light "
                    "travels at the same speed no matter who measures it &mdash; then follows "
                    "them without flinching, until time dilation, length contraction and the "
                    "mass&ndash;energy relation arrive as consequences rather than as separate "
                    "discoveries.",
                    "The quantum mechanics course is the first half of a two-part sequence: "
                    "wavefunctions, the Schr&ouml;dinger equation, particles in wells and against "
                    "barriers. It is the machinery that has to be in place before any application "
                    "makes sense.",
                ],
                "links": [],
            },
        ],
    },

    # ══════════════════════════════════════════════════ ROOM 02
    {
        "slug": "competitions-programs",
        "num": "02", "title": "Competitions &amp; Programs", "plain": "Competitions & Programs",
        "years": "2023—2026", "count_word": "Nine entries", "count_short": "9 entries",
        "tile": {"src": IMG + "room-competitions-tile.jpg", "ratio": "ratio-4-5",
                 "alt": "Yeonhoo working through mathematics problems by hand at a desk"},
        "wide": False,
        "tile_caption": "Ten recognitions in physics and mathematics — and the problems behind them.",
        "intro": ("Room for displaying my efforts to understand the world and myself. This room is "
                  "not simply a medal wall, but a glimpse into what made those possible."),
        "stats": [("10", "Recognitions"), ("4", "Years competing"), ("9", "Entries")],
        "entries": [
            {
                "n": "2.1", "short": "Physics Bowl, Division II", "title": "Physics Bowl, Division II",
                "year": "2025", "meta": ["Grade 11 &middot; Bronze Award"],
                "label": "American Association of Physics Teachers. Bronze Award, Division II.",
                "paras": [
                    "Forty multiple-choice physics questions in forty-five minutes.",
                    "I wanted to challenge myself beyond the classroom. A friend and I stumbled "
                    "on this competition and went together to our physics teacher to ask him to "
                    "host it. He accepted the proposal and was happy to help us prepare.",
                    "Division II targets second-year physics students. I wanted to be more "
                    "challenged, so I entered it as a first-year student. That meant studying the "
                    "second-year IB physics material on my own. It was extra work, but I enjoyed "
                    "connecting the new concepts to the old ones and building a better "
                    "understanding of both.",
                ],
                "links": [("Certificate &#8595;", DOC + "physicsbowl-certificate.pdf", True),
                          ("Contest page &#8599;", "https://www.aapt.org/Programs/PhysicsBowl/index.cfm", False)],
            },
            {
                "n": "2.2", "short": "Sir Isaac Newton Exam", "title": "Sir Isaac Newton Exam",
                "year": "2025", "meta": ["Grade 11 &middot; 1st in School, 3rd in Korea"],
                "label": "University of Waterloo. First in school, third in Korea.",
                "paras": [
                    "Waterloo&rsquo;s physics contest for secondary students. The questions "
                    "reward physical reasoning over recall &mdash; they rarely resemble anything "
                    "sitting at the end of a textbook chapter.",
                    "I found out about the exam while searching for extra work I could do to "
                    "deepen my understanding of physics. The questions were quite different from "
                    "the ones in class: they combined physics with fun, and that resonated with "
                    "me. So I asked my physics teacher to host the exam at our school, which he "
                    "thankfully accepted.",
                    "Afterwards, the students who volunteered to take it played 3v3 basketball "
                    "with our physics teacher. That is one of the most memorable experiences I "
                    "have had recently.",
                ],
                "facts": [("1st", "In school"), ("3rd", "In Korea")],
                "links": [("Contest page &#8599;", "https://uwaterloo.ca/centre-advanced-science-education/science-contests/sir-isaac-newton-exam", False)],
            },
            {
                "n": "2.3", "short": "Waterloo Mathematics Contests",
                "title": "Waterloo Mathematics Contests: Pascal, Cayley, Fermat", "year": "2023—25",
                "meta": ["Grades 9, 10 and 11 &middot; Distinction in all three"],
                "label": ("University of Waterloo, CEMC. Pascal in Grade 9, Cayley in Grade 10, "
                          "Fermat in Grade 11. Distinction in all three."),
                "paras": [
                    "I enjoy mathematics for the same reason I enjoy physics: it is the most "
                    "elegant way I know of saying something exactly.",
                    "Waterloo sets one contest per year group, so these three are the same ladder "
                    "climbed three years running, each rung harder than the last. As three "
                    "separate lines on a r&eacute;sum&eacute; the progression disappears.",
                    "Fermat, in Grade 11, was optional. I took it anyway, in the middle of "
                    "everything else that year.",
                ],
                "facts": [("3", "Contests"), ("3", "Distinctions")],
                "links": [("Certificates &#8595;", DOC + "waterloo-contest-certificates.pdf", True),
                          ("CEMC page &#8599;", "https://cemc.uwaterloo.ca/contests/pcf", False)],
            },
            {
                "n": "2.4", "short": "AMC 12", "title": "AMC 12", "year": "2025",
                "meta": ["Grade 11 &middot; Top 25%"],
                "label": "Mathematical Association of America. AMC 12A, November 2025. Top 25%.",
                "image": {"src": IMG + "working-problems.jpg", "kind": "photo",
                          "alt": "Working through mathematics problems by hand at a desk, loose sheets stacked beside a laptop"},
                "paras": [
                    "Twenty-five questions in seventy-five minutes, scored so that leaving a "
                    "question blank beats guessing it.",
                    "This was one of the most challenging experiences I have had in mathematics. "
                    "I had a lot of difficulty preparing, especially in geometry, which I am weak "
                    "at. I did not achieve the highest result here, but it taught me mathematics "
                    "and how to act when I am confronted with a problem I cannot immediately "
                    "solve.",
                ],
                "links": [("Score report &#8595;", DOC + "amc12-result.pdf", True),
                          ("Contest page &#8599;", "https://maa.org/student-programs/amc/", False)],
            },
            {
                "n": "2.5", "short": "World Mathematics Team Competition",
                "title": "World Mathematics Team Competition", "year": "2024",
                "meta": ["Grade 10 &middot; Bronze, Individual round"],
                "label": "Held in Incheon. Individual, relay and team rounds. Bronze in the individual round.",
                "paras": [
                    "A team-based mathematics competition with individual, relay and team rounds. "
                    "Students interested in mathematics were invited from our grade, and I was "
                    "lucky enough to join the team with my friends.",
                    "It taught me that problem solving does not have to happen alone, and that it "
                    "benefits everyone involved. That realisation shaped how I approached "
                    "mathematics and physics afterwards &mdash; looking for and forming "
                    "communities of people interested in the same things.",
                ],
                "links": [("Contest page &#8599;", "https://wmtc.international/", False)],
            },
            {
                "n": "2.6", "short": "Math League", "title": "Math League", "year": "2024",
                "meta": ["Grade 10 &middot; International Round Qualifier &middot; 7th nationally"],
                "label": "Qualified for the International Round. Seventh place nationally.",
                "image": {"src": IMG + "math-league-team.jpg", "kind": "photo",
                          "alt": "The Math League team with their medals, schools listed on the screen behind",
                          "caption": "The team, with the qualifying schools listed behind."},
                "paras": [
                    "Only the individual round counted towards moving on, but the competition "
                    "also had group rounds. With a different group of friends from the team I "
                    "went to WMTC with, I met new people and worked alongside them.",
                    "Solving problems together let me think from perspectives I would not have "
                    "reached alone, which is an experience I would like more of in other areas "
                    "too.",
                ],
                "links": [("Result &#8595;", DOC + "math-league-certificate.pdf", True),
                          ("Contest page &#8599;", "https://www.mathleague.org/", False)],
            },
            {
                "n": "2.7", "short": "Chadwick International Mathematics Competition",
                "title": "Chadwick International Mathematics Competition", "year": "2023—",
                "meta": ["Grade 9 — present &middot; Second place in Grade 9, organising member since"],
                "label": "Chadwick International. Silver Award, March 2024. Now writes problems and supervises exams.",
                "image": {"src": IMG + "cimc-supervising.jpg", "kind": "photo",
                          "alt": "Yeonhoo supervising a student during the Chadwick International Mathematics Competition",
                          "caption": "Supervising the exam I used to sit."},
                "paras": [
                    "The competition was led by a sophomore I knew from junior varsity volleyball "
                    "when I was a freshman. I applied as a student who liked mathematics, and I "
                    "placed second in the high school division.",
                    "The leader then asked if I wanted to be an organising member and write "
                    "problems for the semi-annual middle and high school competition, and I "
                    "accepted. I now create original problems and supervise the exams.",
                    "Making problems instead of solving them made me think more deeply and "
                    "understand how a problem actually works, which helped my creative thinking "
                    "and my problem solving.",
                ],
                "links": [("Certificate &#8595;", DOC + "cimc-certificate.pdf", True),
                          ("Competition page &#8599;", "https://www.instagram.com/ci_mathcompetition/", False)],
            },
            {
                "n": "2.8", "short": "Korea Science &amp; Engineering Fair",
                "title": "Korea Science &amp; Engineering Fair", "year": "2024",
                "meta": ["Grade 10 &middot; Recognition Award"],
                "label": "KSEF. Korea's national science fair. Recognition Award.",
                "image": {"src": IMG + "ksef-team.jpg", "kind": "photo",
                          "alt": "The project team at the KSEF 2024 entrance banner",
                          "caption": "KSEF 2024."},
                "paras": [
                    "I was not sure which career I would pursue at this point, though I knew I "
                    "liked physics from the bottom of my heart.",
                    "My friends invited me onto a coding project that used artificial "
                    "intelligence to detect drunk driving from the motion of the car and the "
                    "movement of the driver&rsquo;s head.",
                ],
                "links": [("Certificate &#8595;", DOC + "ksef-certificate.pdf", True)],
            },
            {
                "n": "2.9", "short": "Business Black Box",
                "title": "Business Black Box, Wharton Korea Undergraduate Business Society",
                "year": "2023", "meta": ["Grade 9 &middot; Participant"],
                "label": "Wharton Korea Undergraduate Business Society. Participant.",
                "image": {"src": IMG + "business-black-box.jpg", "kind": "photo",
                          "alt": "The Business Black Box team after the final presentation"},
                "paras": [
                    "My friends who are interested in economics and business invited me onto "
                    "their team. Along with my friend from the mathematics team, we were assigned "
                    "the calculations behind the team&rsquo;s ideas.",
                    "It was interesting to come together with a single goal when everyone had a "
                    "different background &mdash; business, psychology, physics.",
                    "The programme ran under Wharton and UPenn undergraduate mentors. We worked "
                    "real corporate cases &mdash; market entry, consumer engagement &mdash; under "
                    "time pressure, synthesising raw data into pitch decks and using frameworks "
                    "like SWOT, PESTEL and the 4Ps.",
                ],
                "links": [("Program page &#8599;", "https://www.bizblackbox.com/ko/home", False)],
            },
        ],
    },

    # ══════════════════════════════════════════════════ ROOM 03
    {
        "slug": "writing",
        "num": "03", "title": "Writing", "plain": "Writing",
        "years": "2023—2026", "count_word": "Four entries", "count_short": "4 entries",
        "tile": {"src": IMG + "room-writing-tile.jpg", "ratio": "ratio-4-5",
                 "alt": "Yeonhoo at the John Locke Institute award ceremony at the Sheldonian Theatre, Oxford"},
        "wide": False,
        "tile_caption": "Three John Locke commendations, a Scholastic Silver Key, and a blog.",
        "intro": "Room for expressing myself through language. Understanding through language.",
        "stats": [("4", "Awards"), ("7", "Essays"), ("3", "Years")],
        "entries": [
            {
                "n": "3.1", "short": "John Locke Essay Competition",
                "title": "John Locke Essay Competition", "year": "2023—24",
                "meta": ["Grades 9 and 10 &middot; Three commendations",
                         "Presented at the Sheldonian Theatre, Oxford"],
                "label": ("John Locke Institute. Commendation in the Junior category and in "
                          "Psychology, 2023. Commendation in History, 2024. All three essays "
                          "below in full."),
                "image": {"src": IMG + "john-locke-oxford.jpg", "kind": "photo",
                          "alt": "Yeonhoo at the John Locke Institute ceremony in Oxford",
                          "caption": "The Sheldonian Theatre, Oxford."},
                "paras": [
                    "The John Locke Institute sets open questions across subjects and asks for "
                    "short essays answering them. The questions are broad on purpose, so most of "
                    "the work is narrowing one down to something you can actually argue.",
                    "Three commendations across three papers. In the Junior category I argued "
                    "about whether safety matters more than fun, working from the flight response "
                    "and how differently people draw the line on risk. In Psychology I asked "
                    "whether beliefs are voluntary, splitting belief into what we hold about "
                    "ourselves, about others, and about the world. In History I wrote on how "
                    "civilisations fall, starting from Will Durant&rsquo;s line that civilisation "
                    "begins with order, grows with liberty and dies with chaos.",
                ],
                "facts": [("3", "Commendations"), ("2", "Years")],
                "links": [("History essay &#8595;", DOC + "john-locke-history-essay.pdf", True),
                          ("Psychology essay &#8595;", DOC + "john-locke-psychology-essay.pdf", False),
                          ("Junior essay &#8595;", DOC + "john-locke-junior-essay.pdf", False),
                          ("Competition page &#8599;", "https://www.johnlockeinstitute.com/essay-competition", False)],
            },
            {
                "n": "3.2", "short": "Scholastic Art &amp; Writing Awards",
                "title": "Scholastic Art &amp; Writing Awards", "year": "2026",
                "meta": ["Silver Key, Short Story &middot; Alliance for Young Artists &amp; Writers"],
                "label": ("Silver Key for &ldquo;The Starr&rdquo;, 2026. The oldest recognition "
                          "programme for secondary-school creative work in the United States; "
                          "entries are judged blind."),
                "paras": [
                    "&ldquo;The Starr&rdquo; is a short story set in a world where social "
                    "standing is literal. Followers decide which floor of the tower you live on, "
                    "and a notification promoting you to the Bronze floor is enough to make you "
                    "pack everything you own into one light bag and get on the tram.",
                    "It is the piece I am most willing to have read.",
                ],
                "links": [("Read &ldquo;The Starr&rdquo; &#8595;", DOC + "the-starr-short-story.pdf", True),
                          ("Certificate &#8595;", DOC + "scholastic-silver-key-certificate.pdf", False),
                          ("Awards page &#8599;", "https://www.artandwriting.org/", False)],
            },
            {
                "n": "3.3", "short": "Essays and research programmes",
                "title": "Essays and Research Programmes", "year": "2024—25",
                "meta": ["Grades 10 and 11 &middot; Entered, not placed"],
                "label": ("Cambridge Centre for International Research; Harvard Crimson Global "
                          "Essay Competition; Global Research and Consulting; Minds Underground; "
                          "John Locke, Psychology, 2025."),
                "paras": [
                    "Alongside the competitions above I have written for several programmes "
                    "without placing in them. They are here because the writing happened, and "
                    "because the range is the point.",
                    "For Global Research and Consulting I wrote on what it means to harness "
                    "technology for the social good, arguing through the Socratic method that we "
                    "rarely define the &ldquo;good&rdquo; we claim to be building towards. For "
                    "Minds Underground I wrote on whether physics discovers reality or constructs "
                    "models of it, and argued that the question only arises from a "
                    "misconception. I entered John Locke again in Grade 11, in Psychology, on "
                    "Eleanor Roosevelt&rsquo;s claim that no one can make you feel inferior "
                    "without your consent. I also took part in the Cambridge Centre for "
                    "International Research in Grade 11 and the Harvard Crimson Global Essay "
                    "Competition in Grade 10.",
                    "Several of these exist only as drafts, so I have not posted the texts.",
                ],
                "links": [("CCIR certificate &#8595;", DOC + "ccir-certificate.pdf", False),
                          ("HCGEC certificate &#8595;", DOC + "hcgec-certificate.pdf", False)],
            },
            {
                "n": "3.4", "short": "Blog", "title": "Blog", "year": "2025—",
                "meta": ["Grade 11 — present"],
                "label": "Ongoing since Grade 11.",
                "paras": ["Blog entries for the things I am interested in &mdash; self-initiated, "
                          "and deliberately wide: STEM, culture, literary arts, music and society, "
                          "along with reflections and interpretations that connect back to what I "
                          "am studying."],
                "links": [("Read the blog &#8599;", "https://kimyeonhoo.blogspot.com", True)],
            },
        ],
    },

    # ══════════════════════════════════════════════════ ROOM 04
    {
        "slug": "service-community",
        "num": "04", "title": "Service &amp; Community", "plain": "Service & Community",
        "years": "2023—2026", "count_word": "Seven entries", "count_short": "7 entries",
        "tile": {"src": IMG + "room-service-tile.jpg", "ratio": "ratio-16-9",
                 "alt": "Culture Protectors volunteers outside the Wongaksa free meal centre"},
        "wide": True,
        "tile_caption": ("Four leadership roles, one organisation founded in Grade 9, and a national "
                         "volunteer award."),
        "intro": ("Understanding the community around me and creating positive changes. Four "
                  "leadership roles, one organisation I started in Grade 9 and still run, and a "
                  "Silver Award at the National Youth Volunteer Awards."),
        "stats": [("1", "Founded"), ("4", "Leadership roles"), ("7", "Entries")],
        "entries": [
            {
                "n": "4.1", "short": "Chadwick International Culture Protectors",
                "title": "Chadwick International Culture Protectors", "year": "2024—",
                "meta": ["Grade 10 — present &middot; Member in Grade 10, Leader from Grade 11",
                         "National Youth Volunteer Awards, Silver Award &middot; Grade 11"],
                "label": ("A club dedicated to protecting, promoting and sharing the rich culture "
                          "and history of the Republic of Korea."),
                "image": {"src": IMG + "cic-volunteer-award.jpg", "kind": "photo",
                          "alt": "Receiving the Silver Award on stage at the National Youth Volunteer Awards",
                          "caption": "National Youth Volunteer Awards."},
                "thumbs": [
                    {"src": IMG + "cic-serving.jpg", "kind": "photo",
                     "alt": "Serving meals in apron and gloves at the Wongaksa free meal centre"},
                    {"src": IMG + "cic-soup-kitchen.jpg", "kind": "photo",
                     "alt": "Culture Protectors volunteers outside the Wongaksa free meal centre"},
                ],
                "paras": [
                    "We organise monthly volunteer work at the Wongaksa soup kitchen and plogging "
                    "in Tapgol Park.",
                    "We have also collaborated with the Korea Heritage Service on events aimed at "
                    "foreigners inside and outside the school community &mdash; creating posters, "
                    "running sessions introducing Nakseonjae, and similar work to promote Korean "
                    "heritage.",
                    "In October 2025 I served as an English docent at the 11th Palace Culture "
                    "Festival, <em>Nakseonjae: 100 Years of Time and Scenery</em>, and was given a "
                    "letter of appreciation by the Korean Imperial Family Culture Institute for "
                    "the role.",
                    "The Silver Award at the National Youth Volunteer Awards in Grade 11 came out "
                    "of this work.",
                ],
                "links": [("Silver Award &#8595;", DOC + "national-youth-volunteer-silver.pdf", True),
                          ("Nakseonjae appreciation &#8595;", DOC + "cic-nakseonjae-appreciation.pdf", False),
                          ("Instagram &#8599;", "https://www.instagram.com/cic_chadwick/", False)],
            },
            {
                "n": "4.2", "short": "Taste of Songdo", "title": "Taste of Songdo", "year": "2023—",
                "meta": ["Grade 9 — present &middot; Founder and Leader"],
                "label": "Founded in Grade 9 and still running. Using food as a language for culture.",
                "image": {"src": IMG + "kimchi-making.jpg", "kind": "photo",
                          "alt": "The annual kimchi-making event, students in aprons and hairnets around long tables",
                          "caption": "The annual kimchi-making event."},
                "thumbs": [
                    {"src": IMG + "songdo-cooking.jpg", "kind": "photo",
                     "alt": "A cooking session for teachers, dishes laid out on the table"},
                    {"src": IMG + "songdo-event.jpg", "kind": "photo",
                     "alt": "An outdoor Taste of Songdo event"},
                    {"src": IMG + "songdo-presentation.jpg", "kind": "photo",
                     "alt": "Presenting during a Taste of Songdo session"},
                ],
                "paras": [
                    "I started Taste of Songdo to use food as a language for culture.",
                    "It runs an annual kimchi-making event for ninth graders, which has become a "
                    "tradition, and experimental cooking sessions over the summer break for "
                    "newly arriving foreign teachers and returning teachers at our school. We "
                    "also run a cooking session for students coming on exchange from "
                    "Chadwick&rsquo;s Palos Verdes campus.",
                    "Alongside the events I manage an Instagram page introducing local "
                    "restaurants and food stories for foreigners living in the Songdo area of Incheon.",
                ],
                "facts": [("9th", "Grade founded"), ("4", "Years running")],
                "links": [("Instagram &#8599;", "https://www.instagram.com/taste_of_songdo/", True)],
            },
            {
                "n": "4.3", "short": "US Pushcart Library", "title": "US Pushcart Library",
                "year": "2023—",
                "meta": ["Grade 9 — present &middot; Member in Grades 9 to 11, Co-Leader in Grade 12"],
                "label": "Teaching sessions and events for village schoolers.",
                "image": {"src": IMG + "pushcart-teaching.jpg", "kind": "photo",
                          "alt": "A teaching session with village schoolers around a craft table",
                          "caption": "A teaching session."},
                "thumbs": [
                    {"src": IMG + "pushcart-audiobook.jpg", "kind": "photo",
                     "alt": "Grade 3 students holding up their audiobook project sheets"},
                ],
                "paras": [
                    "We organise teaching sessions for more than twenty high school students, and "
                    "events for village schoolers aimed at encouraging fun learning and a "
                    "supportive environment.",
                    "The project I liked most was collaborating with twenty-five Grade 3 students "
                    "to create audiobooks for the blind.",
                ],
                "links": [],
            },
            {
                "n": "4.4", "short": "Beyond the Border", "title": "Beyond the Border", "year": "2023—",
                "meta": ["Grade 9 — present &middot; Member in Grades 9 and 10, Leader from Grade 11"],
                "label": "Support for vulnerable communities in Korea, with the Sun Blanket Foundation.",
                "image": {"src": IMG + "beyond-the-border.jpg", "kind": "photo",
                          "alt": "Beyond the Border members at an exhibition of work by young artists"},
                "paras": [
                    "We collaborate with the Sun Blanket Foundation to provide support for "
                    "vulnerable communities within Korea, among them talented young artists who "
                    "are orphans.",
                    "We have raised over $2,000 in donations, in two months.",
                ],
                "links": [("Website &#8599;", "https://www.beyondtheborder1.com/", True)],
            },
            {
                "n": "4.5", "short": "Core Value Council", "title": "Core Value Council",
                "year": "2024—25", "meta": ["Grades 10 and 11 &middot; Member"],
                "label": "Member role, ended after Grade 11.",
                "image": {"src": IMG + "core-value-event.jpg", "kind": "photo",
                          "alt": "The annual core values event, village schoolers and student organisers in a classroom"},
                "paras": [
                    "The council organises an annual event for village schoolers to learn and "
                    "embrace the school&rsquo;s core values: responsibility, respect, compassion, "
                    "honesty, and fairness.",
                ],
                "links": [],
            },
            {
                "n": "4.6", "short": "Bali Coral Restoration Trip",
                "title": "Bali Coral Restoration Trip", "year": "2023—24",
                "meta": ["Grades 9 and 10 &middot; Head Member"],
                "label": "An annual trip to the Padang Bai area of Bali.",
                "image": {"src": IMG + "bali-coral-planting.jpg", "kind": "photo",
                          "alt": "Divers working on a coral nursery frame on the sea floor at Padang Bai",
                          "caption": "Planting on the nursery frames, Padang Bai."},
                "thumbs": [
                    {"src": IMG + "bali-nursery-frame.jpg", "kind": "photo",
                     "alt": "Holding a coral nursery frame before the dive"},
                    {"src": IMG + "bali-underwater.jpg", "kind": "photo",
                     "alt": "A diver carrying a basket of coral fragments underwater"},
                    {"src": IMG + "bali-diver.jpg", "kind": "photo",
                     "alt": "Yeonhoo in dive mask and regulator at the surface"},
                ],
                "paras": [
                    "An annual trip to Bali to restore coral for positive marine environmental "
                    "impact. We planted coral reefs and cleaned the ocean floor in the Padang Bai "
                    "area.",
                    "As head member I helped run the programme, working with local operators and "
                    "public safety officials to get each trip in the water.",
                    "I certified as a CMAS One Star diver before the first trip, in Grade 9, with "
                    "two friends who came along &mdash; that certification is in Room 06.",
                ],
                "links": [],
            },
            {
                "n": "4.7", "short": "Hwarang Youth Foundation", "title": "Hwarang Youth Foundation",
                "year": "2023", "meta": ["Grade 9 &middot; City of Los Angeles Recognition for Service"],
                "label": "A service club. Recognised by the City of Los Angeles.",
                "image": {"src": IMG + "hwarang-pens.jpg", "kind": "photo",
                          "alt": "Assembling ball point pens during a Hwarang Youth Foundation session",
                          "caption": "Making pens at a Hwarang session."},
                "thumbs": [
                    {"src": IMG + "hwarang-session.jpg", "kind": "photo",
                     "alt": "A tutoring session in progress, seen from behind"},
                ],
                "paras": [
                    "We made ball point pens alongside elderly people in economically poor areas, "
                    "taught basic school subjects to multicultural children, and taught "
                    "instruments &mdash; piano and drums &mdash; to children supervised by public "
                    "schools after school hours.",
                ],
                "links": [("Recognition &#8595;", DOC + "hwarang-la-recognition.pdf", True)],
            },
        ],
    },

    # ══════════════════════════════════════════════════ ROOM 05
    {
        "slug": "music",
        "num": "05", "title": "Music", "plain": "Music",
        "years": "2023—2026", "count_word": "Three entries", "count_short": "3 entries",
        "tile": {"src": IMG + "room-music-tile.jpg", "ratio": "ratio-1-1",
                 "alt": "Yeonhoo behind the drum kit"},
        "wide": False,
        "tile_caption": "Drums, percussion and piano. Three years in a national honour ensemble.",
        "intro": "Room for expressing myself through artistic sound waves. Understanding myself.",
        "stats": [("2", "KIMEA awards"), ("3", "Years at National Honor Festival"), ("3", "Recordings")],
        "entries": [
            {
                "n": "5.1", "short": "J&rsquo;Blue Jazz Band", "title": "J&rsquo;Blue Jazz Band",
                "year": "2024—",
                "meta": ["Grade 10 — present &middot; Drums",
                         "Gold and Platinum Award &middot; KIMEA Solo &amp; Ensemble"],
                "label": ("Gold Award for &ldquo;All the Things You Are&rdquo;, arranged by Mark "
                          "Taylor. Platinum Award for &ldquo;Billie&rsquo;s Bounce&rdquo;, "
                          "arranged by John Wasson."),
                "variant": "wide",
                "lead": {"src": IMG + "jblue-drums.jpg", "ratio": "ratio-16-9",
                         "alt": "Yeonhoo behind the drum kit during a J'Blue Jazz Band performance"},
                "paras": [
                    "I play drums in the band. The drummer sets tempo and dynamics for everyone "
                    "in the room and cannot stop mid-piece to talk about it, which is a "
                    "particular kind of responsibility even when you are not the one in charge.",
                    "I also help organise the occasions we play &mdash; graduation, the bazaar "
                    "fair, and school concerts.",
                    "At the KIMEA Solo &amp; Ensemble competition we took a Gold Award for "
                    "&ldquo;All the Things You Are&rdquo;, arranged by Mark Taylor, and a "
                    "Platinum Award for &ldquo;Billie&rsquo;s Bounce&rdquo;, arranged by John "
                    "Wasson.",
                ],
                "media_below": {
                    "heading": "Recordings",
                    "videos": [
                        {"src": MED + "billies-bounce.mp4", "poster": MED + "billies-bounce-poster.jpg",
                         "title": "Billie&rsquo;s Bounce", "note": "Arranged by John Wasson. Platinum Award."},
                        {"src": MED + "all-of-me.mp4", "poster": MED + "all-of-me-poster.jpg",
                         "title": "All of Me", "note": "J&rsquo;Blue Jazz Band."},
                        {"src": MED + "isnt-she-lovely.mp4", "poster": MED + "isnt-she-lovely-poster.jpg",
                         "title": "Isn&rsquo;t She Lovely", "note": "J&rsquo;Blue Jazz Band."},
                    ],
                },
                "links": [],
            },
            {
                "n": "5.2", "short": "National Honor Festival", "title": "National Honor Festival, KIMEA",
                "year": "2023—25", "meta": ["Grades 9 to 11 &middot; Percussion &middot; Selected by audition"],
                "label": ("Korea International Music Educators Association. An honour ensemble "
                          "drawn from international schools across Korea, three consecutive years."),
                "image": {"src": IMG + "kimea-honor-festival.jpg", "kind": "photo",
                          "alt": "The National Honor Festival ensemble assembled in front of the festival banner"},
                "paras": [
                    "Selection is by annual audition, which meant fitting audition preparation in "
                    "between schoolwork. I led the student group section as a percussionist.",
                    "Orchestral percussion is quite different from playing kit in a jazz band. "
                    "The music is rigid &mdash; I follow the conductor and have to be subtle with "
                    "expression, especially dynamics. I met a lot of different people during the "
                    "KIMEA sessions, which was a great experience.",
                ],
                "media_below": {
                    "heading": "Performances",
                    "links": [
                        {"href": "https://www.youtube.com/watch?v=_jCHejba5Es",
                         "title": "National Honor Festival, 2026", "note": "Watch on YouTube &#8599;"},
                        {"href": "https://drive.google.com/file/d/1hgpxVFWaGgOnvhwuUSmDa599_uKltY0O/view?usp=sharing",
                         "title": "National Honor Festival, 2025", "note": "Watch on Google Drive &#8599;"},
                    ],
                },
                "links": [("Festival page &#8599;", "https://www.kimeaonline.org/", False)],
            },
            {
                "n": "5.3", "short": "Piano", "title": "Piano", "year": "—",
                "meta": ["ABRSM Grade 4"],
                "label": "ABRSM Grade 4. Grades run 1 to 8; each exam covers prepared pieces, scales, sight-reading and aural tests.",
                "paras": [
                    "I have played piano since I was very young, and it is one of the reasons I "
                    "developed a natural affinity for music. I do not play very much now, but I "
                    "still play for my own entertainment from time to time.",
                ],
                "links": [],
            },
        ],
    },

    # ══════════════════════════════════════════════════ ROOM 06
    {
        "slug": "sport-discipline",
        "num": "06", "title": "Sport &amp; Discipline", "plain": "Sport & Discipline",
        "years": "2022—2026", "count_word": "Three entries", "count_short": "3 entries",
        "tile": {"src": IMG + "room-sport-tile.jpg", "ratio": "ratio-1-1",
                 "alt": "Junior varsity volleyball team lined up in uniform"},
        "wide": False,
        "tile_caption": "A Kukkiwon black belt, two years as volleyball captain, and a dive certification.",
        "intro": ("Room for activity. Three things that took years rather than terms &mdash; and "
                  "that the r&eacute;sum&eacute; gives a single line each."),
        "stats": [("4th", "Kukkiwon grade"), ("2", "Years as captain"), ("3", "Entries")],
        "entries": [
            {
                "n": "6.1", "short": "Junior Varsity Volleyball", "title": "Junior Varsity Volleyball",
                "year": "2023—25",
                "meta": ["Grades 9 to 11 &middot; Player in Grade 9, Captain in Grades 10 and 11"],
                "label": "Three seasons. Captain for the last two.",
                "image": {"src": IMG + "volleyball-team.jpg", "kind": "photo",
                          "alt": "The junior varsity volleyball team lined up in uniform before a match"},
                "thumbs": [
                    {"src": IMG + "volleyball-team-bleachers.jpg", "kind": "photo",
                     "alt": "The team together on the bleachers after a match"},
                ],
                "paras": [
                    "The failure in Grade 11 to make varsity was very painful to me. Everybody "
                    "told me to quit &mdash; that continuing junior varsity in Grade 11 was "
                    "meaningless for schoolwork and for college applications. That was not "
                    "important to me.",
                    "<strong>The most valuable thing I have earned from volleyball is not the "
                    "skills but the people.</strong> I still contact the junior captain who "
                    "introduced me to the high school environment when I was a freshman. I want "
                    "to be that same kind of person &mdash; someone my teammates can reach out to "
                    "without any burden. The great people I met over three years are worth the "
                    "time.",
                ],
                "facts": [("2", "Years as captain")],
                "links": [],
            },
            {
                "n": "6.2", "short": "Taekwondo", "title": "Taekwondo", "year": "2022",
                "meta": ["Korea Taekwondo Association &middot; Kukkiwon-registered, June 2022"],
                "label": "Fourth grade, registered with the Kukkiwon in June 2022.",
                "paras": [
                    "Taekwondo is the Korean national martial art, built on kicking, and the "
                    "sport most Korean children try at some point. I trained from when I was "
                    "young and graded through to the fourth level.",
                    "Grades are separated by mandatory waiting periods that lengthen at each "
                    "step, so this is not something that can be reached quickly regardless of "
                    "ability. The years are built into the system.",
                ],
                "facts": [("4th", "Kukkiwon grade")],
                "links": [("Certificate &#8595;", DOC + "taekwondo-4th-dan-certificate.pdf", True)],
            },
            {
                "n": "6.3", "short": "CMAS One Star Diver", "title": "CMAS One Star Diver",
                "year": "2023", "meta": ["Grade 9 &middot; Certification"],
                "label": ("Conf&eacute;d&eacute;ration Mondiale des Activit&eacute;s "
                          "Subaquatiques. One Star &mdash; the entry-level qualification for open "
                          "water diving with a qualified buddy."),
                "paras": [
                    "I certified before the Bali trip in Grade 9, with two other friends who went "
                    "on the same trip.",
                ],
                "links": [("Certificate &#8595;", DOC + "cmas-one-star-certificate.pdf", True)],
            },
        ],
    },
]

HERO_TITLE = "Trying to <em>understand things.</em>"
HERO_INTRO = ("A collection of efforts to understand &mdash; myself, the world, and everything in "
              "between.")

ABOUT = [
    "For me, physics has been my passion for a long time.",
    "From a young age I had an affinity with numbers, and used them as tools to understand the "
    "world around me. It was the simplest yet the most beautiful way to describe everything "
    "around me. That desire to understand and explain the real world has driven me to the "
    "subject, and into many different occasions to study it better. And, of course, I seek a "
    "better understanding in the future.",
    "My obsession with physics does not put me any further from the other parts of myself. I also "
    "enjoy creative work, whether it is music, literature, or movies. I love to express myself in "
    "any form and to immerse myself in different worlds. Every now and then I cry over a movie, "
    "spend hours reading books, make music, and write anything that comes into my mind.",
    "I would not call myself talented, exactly. Although I love music, I have failed a few "
    "auditions, and there have been plenty of times I was not satisfied with myself. The same "
    "goes for volleyball &mdash; passion alone could not make me a starting varsity player. But "
    "that does not change the fact that I feel joy, and feel like myself, when I am doing those "
    "things. I also met a lot of great people doing what I like, which is worth more to me than "
    "any audition or match.",
    "I want to study physics in more depth. I take the initiative to study more of it on my own, "
    "but an individual can only go so far. I would love to be in a community where everybody is "
    "passionate about their studies and I can discuss different problems with them &mdash; "
    "interactive lectures, labs, discussions. That is why I want to continue studying at "
    "university. Also, great physics happens on blackboards, and I don&rsquo;t have a blackboard "
    "at home.",
]


# ─────────────────────────────────────────────── fragments
def head(title, description, css_links, prefix):
    links = "\n".join('  <link rel="stylesheet" href="%s%s">' % (prefix, h) for h in css_links)
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>%s</title>
  <meta name="description" content="%s">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

%s
</head>""" % (title, description, links)


def header(prefix, current):
    cat = ' class="is-current"' if current == "catalogue" else ""
    abt = ' class="is-current"' if current == "about" else ""
    return """  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="shell header-inner">
      <a class="wordmark" href="%sindex.html">Yeonhoo <em>Kim</em></a>

      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>

      <nav class="site-nav label" id="site-nav" aria-label="Main">
        <a href="%sindex.html"%s>Catalogue</a>
        <a href="%sabout.html"%s>About</a>
        <a href="%s%s" download>R&eacute;sum&eacute; &#8595;</a>
      </nav>
    </div>
  </header>""" % (prefix, prefix, cat, prefix, abt, prefix, RESUME)


def footer(prefix, back=False):
    rows = []
    if back:
        rows.append('        <a href="%sindex.html">&#8592; Back to catalogue</a>' % prefix)
    rows.append('        <a href="%s" target="_blank" rel="noopener">Instagram &#8599;</a>' % INSTAGRAM)
    rows.append('        <a href="%s%s" download>R&eacute;sum&eacute;, PDF &#8595;</a>' % (prefix, RESUME))
    return """  <footer class="shell site-footer">
      <div>
        <div class="footer-label label">Write to me</div>
        <a class="footer-email" href="mailto:%s">%s</a>
      </div>
      <div class="footer-links">
%s
      </div>
  </footer>

  <div class="shell footer-colophon">
    <span>&copy; <span data-current-year>2026</span> %s</span>
    <span>Songdo, Korea</span>
  </div>""" % (EMAIL, EMAIL, "<br>\n".join(rows), NAME)


def scripts(prefix, extra):
    out = '  <script src="%sjs/main.js" defer></script>' % prefix
    for src in extra:
        out += '\n  <script src="%s%s" defer></script>' % (prefix, src)
    return out


def stats_block(stats, kind="room"):
    cls = "room-stat" if kind == "room" else "entry-fact"
    wrap = "room-stat" if kind == "room" else "entry-fact-item"
    return "\n".join("""          <div class="%s">
            <div class="%s-figure">%s</div>
            <div class="%s-caption">%s</div>
          </div>""" % (wrap, cls, f, cls, c) for f, c in stats)


def chips(links, prefix):
    if not links:
        return ""
    out = []
    for text, href, primary in links:
        ext = href.startswith("http")
        attrs = ' target="_blank" rel="noopener"' if ext else ' download'
        url = href if ext else prefix + href
        out.append('              <a class="chip%s" href="%s"%s>%s</a>'
                   % (" chip--primary" if primary else "", url, attrs, text))
    return """
            <div class="chips">
%s
            </div>""" % "\n".join(out)


def media_below(block, prefix):
    if not block:
        return ""
    items = []
    for v in block.get("videos", []):
        items.append("""              <figure>
                <video controls preload="none" poster="%s%s">
                  <source src="%s%s" type="video/mp4">
                  Your browser cannot play this video.
                </video>
                <figcaption><strong>%s</strong>%s</figcaption>
              </figure>""" % (prefix, v["poster"], prefix, v["src"], v["title"], v["note"]))
    for l in block.get("links", []):
        items.append("""              <a class="media-link" href="%s" target="_blank" rel="noopener">
                <strong>%s</strong>
                <span>%s</span>
              </a>""" % (l["href"], l["title"], l["note"]))
    return """
            <div class="entry-media-below">
              <h4 class="media-heading">%s</h4>
              <div class="media-grid">
%s
              </div>
            </div>""" % (block["heading"], "\n".join(items))


# ─────────────────────────────────────────────── pages
def build_index():
    tiles, contents = [], []
    for room in ROOMS:
        wide = " room-tile--wide" if room["wide"] else ""
        t = room["tile"]
        if t:
            frame = """<div class="room-tile-frame %s">
            <img class="is-photo" src="%s" alt="%s" loading="lazy">
            <span class="room-tile-enter">Enter &#8594;</span>
          </div>""" % (t["ratio"], t["src"], t["alt"])
        else:
            ratio = "ratio-16-9" if room["wide"] else "ratio-1-1"
            frame = """<div class="room-tile-frame room-tile-frame--type %s">
            <span class="room-tile-numeral">%s</span>
            <span class="room-tile-enter">Enter &#8594;</span>
          </div>""" % (ratio, room["num"])

        tiles.append("""        <a class="room-tile%s" href="rooms/%s.html">
          %s
          <div class="room-tile-label">
            <div class="room-tile-kicker">Room %s &middot; %s</div>
            <h2 class="room-tile-title">%s</h2>
            <p class="room-tile-caption">%s. %s</p>
          </div>
        </a>""" % (wide, room["slug"], frame, room["num"], room["count_word"],
                   room["title"], room["years"], room["tile_caption"]))

        contents.append("""          <a href="rooms/%s.html">
            <span class="contents-num">%s</span>
            <span>%s</span>
            <span class="contents-leader"></span>
            <span class="contents-meta">%s</span>
          </a>""" % (room["slug"], room["num"], room["title"], room["count_short"]))

    html = """%s
<body data-page="home">
%s

  <main id="main">

    <section class="shell hero">
      <div>
        <div class="hero-eyebrow label label--deep">Songdo, Korea &middot; Class of 2027 &middot; Six rooms</div>
        <h1 class="hero-title">%s</h1>
      </div>
      <p class="hero-intro">%s</p>
    </section>

    <section class="shell wall" aria-label="Rooms">
%s
    </section>

    <section class="shell contents contents--ruled">
      <h2 class="contents-heading">Contents</h2>
      <div class="contents-list">
%s
      </div>
    </section>

  </main>

%s

%s
</body>
</html>
""" % (head("%s &mdash; Catalogue" % NAME,
            "Physics research, competitions, writing, service, music and sport — the work of Yeonhoo Kim, Class of 2027.",
            ["css/main.css", "css/index.css"], ""),
       header("", "catalogue"), HERO_TITLE, HERO_INTRO,
       "\n".join(tiles), "\n".join(contents), footer(""), scripts("", ["js/index.js"]))
    write(os.path.join(SITE, "index.html"), html)


def build_about():
    body = ["            <p>%s</p>" % p for p in ABOUT]
    html = """%s
<body data-page="about">
%s

  <main id="main">

    <section class="shell about">
      <figure>
        <img class="about-portrait is-photo" src="%sportrait.jpg"
             alt="Yeonhoo Kim at Cloud Gate in Chicago" loading="lazy">
      </figure>
      <div class="about-body">
        <div class="label label--deep">About</div>
%s
        <a class="chip chip--primary" href="%s" download>R&eacute;sum&eacute;, PDF &#8595;</a>
      </div>
    </section>

  </main>

%s

%s
</body>
</html>
""" % (head("About &mdash; %s" % NAME, "About Yeonhoo Kim, Class of 2027.",
            ["css/main.css", "css/about.css"], ""),
       header("", "about"), IMG, "\n".join(body), RESUME,
       footer(""), scripts("", ["js/about.js"]))
    write(os.path.join(SITE, "about.html"), html)


def build_room(index):
    room = ROOMS[index]
    prev_room = ROOMS[(index - 1) % len(ROOMS)]
    next_room = ROOMS[(index + 1) % len(ROOMS)]
    P = "../"

    contents = "\n".join("""          <a href="#entry-%s" data-entry-link>
            <span class="contents-num">%s</span>
            <span>%s</span>
            <span class="contents-leader"></span>
            <span class="contents-meta">%s</span>
          </a>""" % (e["n"].replace(".", "-"), e["n"], e["short"], e["year"])
                         for e in room["entries"])

    entries = []
    for e in room["entries"]:
        img = e.get("image")
        variant = e.get("variant")

        thumbs = ""
        if e.get("thumbs"):
            cells = "\n".join(
                '              <img class="entry-thumb is-%s" src="%s%s" alt="%s" loading="lazy">'
                % (t["kind"], P, t["src"], t["alt"]) for t in e["thumbs"])
            thumbs = """
            <div class="entry-thumbs">
%s
            </div>""" % cells

        if variant == "wide":
            cls = " entry--wide"
            lead = e.get("lead")
            media = ""
            if lead:
                media = """
          <figure class="entry-lead">
            <img class="is-photo %s" src="%s%s" alt="%s" loading="lazy">
          </figure>""" % (lead["ratio"], P, lead["src"], lead["alt"])
        elif img:
            cls = ""
            cap = ('\n              <figcaption>%s</figcaption>' % img["caption"]) if img.get("caption") else ""
            media = """
          <div class="entry-media">
            <figure>
              <img class="entry-shot is-%s" src="%s%s" alt="%s" loading="lazy">%s
            </figure>%s
          </div>""" % (img["kind"], P, img["src"], img["alt"], cap, thumbs)
        else:
            cls = " entry--text"
            media = ""

        facts = ""
        if e.get("facts"):
            facts = """
            <div class="entry-facts">
%s
            </div>""" % stats_block(e["facts"], "entry")

        paras = "\n".join("            <p>%s</p>" % p for p in e["paras"])
        if paras:
            paras = "\n" + paras

        entries.append("""        <article class="entry%s" id="entry-%s">%s
          <div class="entry-body">
            <div class="entry-number">%s</div>
            <h3 class="entry-title">%s</h3>
            <p class="entry-label">%s</p>%s%s%s%s
          </div>
        </article>""" % (cls, e["n"].replace(".", "-"), media,
                         "Entry %s &middot; %s" % (e["n"], "<br>".join(e["meta"])),
                         e["title"], e["label"], paras, facts,
                         media_below(e.get("media_below"), P), chips(e["links"], P)))

    html = """%s
<body class="room-page" data-page="room" data-room="%s">
%s

  <main id="main">

    <div class="shell crumb label">
      <a href="../index.html">Catalogue</a>
      <span class="crumb-sep">/</span>
      <span class="crumb-current">Room %s</span>
    </div>

    <header class="shell room-header">
      <div>
        <div class="room-kicker label label--deep">Room %s &middot; %s &middot; %s</div>
        <h1 class="room-title">%s</h1>
      </div>
      <div>
        <p class="room-intro">%s</p>
        <div class="room-stats">
%s
        </div>
      </div>
    </header>

    <section class="shell contents">
      <h2 class="contents-heading">In this room</h2>
      <div class="contents-list">
%s
      </div>
    </section>

    <section class="shell entries">
%s
    </section>

    <nav class="room-nav" aria-label="Rooms">
      <a href="%s.html">
        <div class="room-nav-label">&#8592; Previous room</div>
        <div class="room-nav-title">Room %s &middot; %s</div>
      </a>
      <a class="room-nav-next" href="%s.html">
        <div class="room-nav-label">Next room &#8594;</div>
        <div class="room-nav-title">Room %s &middot; %s</div>
      </a>
    </nav>

  </main>

%s

%s
</body>
</html>
""" % (head("%s &mdash; %s" % (room["plain"], NAME),
            "Room %s of the catalogue: %s." % (room["num"], room["plain"]),
            ["css/main.css", "css/room-base.css", "css/rooms/%s.css" % room["slug"]], P),
       room["slug"], header(P, "catalogue"), room["num"],
       room["num"], room["count_word"], room["years"], room["title"],
       room["intro"], stats_block(room["stats"]), contents, "\n".join(entries),
       prev_room["slug"], prev_room["num"], prev_room["title"],
       next_room["slug"], next_room["num"], next_room["title"],
       footer(P, back=True), scripts(P, ["js/room-base.js", "js/rooms/%s.js" % room["slug"]]))

    write(os.path.join(SITE, "rooms", "%s.html" % room["slug"]), html)

    css_path = os.path.join(SITE, "css", "rooms", "%s.css" % room["slug"])
    if not os.path.exists(css_path):
        write(css_path, """/* ==========================================================================
   %s.css — Room %s only
   Layout lives in css/room-base.css. This file loads after it, so anything
   here overrides it. Empty on purpose.
   ========================================================================== */
""" % (room["slug"], room["num"]))

    js_path = os.path.join(SITE, "js", "rooms", "%s.js" % room["slug"])
    if not os.path.exists(js_path):
        write(js_path, """/* ==========================================================================
   %s.js — Room %s only
   Shared room behaviour lives in js/room-base.js.
   ========================================================================== */

(function () {
  'use strict';

  /* no room-specific behaviour yet */
})();
""" % (room["slug"], room["num"]))


def write(path, contents):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(contents)
    print("wrote", os.path.relpath(path, SITE))


if __name__ == "__main__":
    build_index()
    build_about()
    for i in range(len(ROOMS)):
        build_room(i)
    print("\ndone")
