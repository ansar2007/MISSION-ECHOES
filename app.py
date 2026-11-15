import streamlit as st
import html
import textwrap
import base64
from pathlib import Path
import mimetypes
from components.quiz import main_quiz
# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="MISSION: ECHOES",
    page_icon="🚀",
    layout="wide"
)
# Load external CSS
def load_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path, "r", encoding="utf-8") as file:
        css = file.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )

# Apply CSS styling
load_css()
# ---------------- CUSTOM STYLING ----------------

st.markdown("""
<style>

/* Remove default top whitespace */
.block-container {
    padding-top: 2rem;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 4px;
    margin-bottom: 5px;
}

.tagline {
    text-align: center;
    font-size: 13px;
    letter-spacing: 3px;
    opacity: 0.7;
    margin-bottom: 25px;
}

/* Navigation buttons */
div.stButton > button {
    background: transparent;
    border: none;
    border-radius: 0;
    font-size: 14px;
    font-weight: 600;
    padding: 8px 4px;
    color: inherit;
}

div.stButton > button:hover {
    color: #55B8E8;
    border-bottom: 2px solid #55B8E8;
    background: transparent;
}

/* Mission card */
.mission-card {
    display: block;
    position: relative;
    overflow: hidden;
    border: 1px solid #454545;
    border-radius: 12px;
    margin-bottom: 22px;
    color: inherit !important;
    text-decoration: none !important;
    transition: border-color 0.3s ease, transform 0.3s ease;
}

.mission-card:hover {
    border-color: #69BDEB;
    transform: translateY(-4px);
}

/* Image placeholder */
.mission-card-image {
    height: 190px;
    background: linear-gradient(135deg, #202A38, #394653);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
}

.mission-card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.mission-card:hover .mission-card-image img {
    transform: scale(1.07);
}

.mission-card-overlay {
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.mission-card:hover .mission-card-overlay {
    opacity: 1;
}

.mission-card-overlay span {
    color: white;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: 2px;
}

.mission-card-content {
    padding: 18px;
}

.mission-card-content h3 {
    margin: 0 0 10px 0;
    font-size: 23px;
}

.mission-card-content p {
    margin: 0;
    color: #A5A5A5;
    font-size: 14px;
}

.mission-card-image {
    height: 190px;
    overflow: hidden;
    position: relative;
}

.mission-card-image img {
    width: 100%;
    height: 190px;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.mission-card:hover .mission-card-image img {
    transform: scale(1.07);
}

.image-placeholder {
    height: 190px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #B8C5D3;
    letter-spacing: 3px;
}


/* MISSION DETAIL PAGES */

.mission-detail-title {
    text-align: center;
    font-size: 42px;
    font-weight: 850;
    letter-spacing: 3px;
    margin: 35px 0 35px 0;
}

.mission-section-title {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: 2px;
    margin: 45px 0 22px 0;
}

.video-placeholder {
    min-height: 300px;
    height: 100%;
    background: linear-gradient(135deg, #101923, #293847);
    border: 1px solid #526171;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #d5e0eb;
    padding: 25px;
}

.video-placeholder .play-icon {
    font-size: 48px;
    margin-bottom: 12px;
}

.mission-overview {
    background: rgba(100, 120, 140, 0.10);
    border: 1px solid rgba(160, 180, 200, 0.25);
    border-radius: 12px;
    padding: 25px;
    min-height: 300px;
    height: 100%;
}

.timeline-image {
    min-height: 180px;
    background: linear-gradient(135deg, #182432, #354454);
    border: 1px solid #526171;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #c7d2df;
    padding: 15px;
}

.timeline-entry {
    padding: 18px 0;
}

.mission-action {
    border: 1px solid rgba(150, 180, 210, 0.4);
    border-radius: 10px;
    padding: 15px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# ---------------- WEBSITE TITLE ----------------

st.markdown(
    '<div class="main-title">MISSION: ECHOES</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tagline">THE FORGOTTEN MACHINES OF THE MOON AND MARS</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- NAVIGATION ----------------

if "current_page" not in st.session_state:
    st.session_state.current_page = "HOME"

# Handle navigation from clickable mission cards
if "page" in st.query_params:
    requested_page = st.query_params["page"]

    allowed_pages = [
        "HOME", "MOON", "MARS", "QUIZ", "SOURCE",
        "SURVEYOR 3", "APOLLO 12", "LUNAR PROSPECTOR",
        "SPIRIT", "OPPORTUNITY"
    ]

    if requested_page in allowed_pages:
        st.session_state.current_page = requested_page

# Logo + navigation layout
columns = st.columns([1.3, 1, 1, 1, 1, 1])

with columns[0]:
    logo_path = Path(__file__).parent / "assets" / "images" / "logo.py.jpeg"
    logo_data = base64.b64encode(logo_path.read_bytes()).decode()

st.markdown(
    f'<img src="data:image/png;base64,{logo_data}" class="nav-logo">',
    unsafe_allow_html=True
)
navigation = ["HOME", "MOON", "MARS", "QUIZ", "SOURCE"]

for i, section in enumerate(navigation, start=1):
    with columns[i]:
        if st.button(section, key=f"nav_{section}", use_container_width=True):
            st.query_params.clear()
            st.session_state.current_page = section
            st.rerun()


st.divider()






def mission_card(title, caption, target_page, image_path):

    safe_title = html.escape(title)
    safe_caption = html.escape(caption)
    safe_page = html.escape(target_page, quote=True)

    # Resolve image path from the project folder
    image_file = Path(__file__).parent / image_path

    if image_file.is_file():

        image_data = base64.b64encode(
            image_file.read_bytes()
        ).decode("utf-8")

        # Automatically detect JPG or PNG
        mime_type = mimetypes.guess_type(
            image_file.name
        )[0] or "image/jpeg"

        image_html = f"""
        <img src="data:{mime_type};base64,{image_data}"
             alt="{safe_title}">
        """

    else:
        image_html = f"""
        <div class="image-placeholder">
            IMAGE NOT FOUND
            <br>
            {html.escape(str(image_path))}
        </div>
        """

    card_html = textwrap.dedent(f"""
    <a class="mission-card" href="?page={safe_page}">
        <div class="mission-card-image">
            {image_html}

            <div class="mission-card-overlay">
                <span>EXPLORE MISSION →</span>
            </div>
        </div>

        <div class="mission-card-content">
            <h3>{safe_title}</h3>
            <p>{safe_caption}</p>
        </div>
    </a>
    """)

    st.html(card_html)




def render_mission_page(title, subtitle, overview, chapters):

    # Mission title
    st.markdown(
        f'<div class="mission-detail-title">{html.escape(title)}</div>',
        unsafe_allow_html=True
    )

    # Mission overview
    st.markdown(
        '<div class="mission-section-title">MISSION OVERVIEW</div>',
        unsafe_allow_html=True
    )

    video_col, info_col = st.columns([1.25, 1], gap="large")

    # VIDEO SECTION
    with video_col:

        video_files = {
            "SURVEYOR 3": "surveyor3.mp4",
            "APOLLO 12": "apollo12.mp4",
            "LUNAR PROSPECTOR": "lunarprospector.mp4",
            "SPIRIT": "rovers.mp4",
            "OPPORTUNITY": "rovers.mp4"
        }

        video_path = (
            Path(__file__).parent
            / "assets"
            / "videos"
            / video_files[title]
        )

        if video_path.is_file():
            st.video(str(video_path))
        else:
            st.warning(f"Video not found: {video_path.name}")

    # VIDEO DESCRIPTION
    with info_col:
        st.markdown(
            f'<div class="mission-overview">'
            f'<h3>{html.escape(subtitle)}</h3>'
            f'<p>{html.escape(overview)}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

    # TIMELINE SECTION
    st.markdown(
        '<div class="mission-section-title">LIVE THROUGH THE MISSION</div>',
        unsafe_allow_html=True
    )

    for index, chapter in enumerate(chapters, start=1):

        story_col, image_col = st.columns([1.5, 1], gap="large")

        with story_col:
            st.markdown(
                f"### CHAPTER {index:02d} — {chapter['heading']}"
            )
            st.write(chapter["story"])

        with image_col:

            mission_folder = title.replace(" ", "_")

            image_path = (
                Path(__file__).parent
                / "assets"
                / "images"
                / mission_folder
                / f"chapter{index}.jpg"
            )

            if image_path.is_file():
                st.image(
                    str(image_path),
                    use_container_width=True
                )
            else:
                st.warning(
                    f"Image not found: {image_path.name}"
                )

        st.divider()

    # BOTTOM BUTTONS
    quiz_col, source_col = st.columns(2, gap="large")

    with quiz_col:
        st.button(
            "MISSION QUIZ →",
            key=f"quiz_{title}",
            use_container_width=True,
            disabled=True
        )

    with source_col:
        st.button(
            "KNOW MORE ↗",
            key=f"source_{title}",
            use_container_width=True,
            disabled=True
        )



# ---------------- MISSION STORY CONTENT ----------------

MISSION_DATA = {

    "SURVEYOR 3": {
        "subtitle": "THE ROBOT THAT PREPARED THE WAY FOR HUMANS",
        "overview": (
            "Launched in April 1967, Surveyor 3 was sent to investigate "
            "the lunar surface and demonstrate that a spacecraft could "
            "land safely on the Moon. Its cameras and robotic sampler "
            "helped scientists understand the nature of lunar soil."
        ),
        "chapters": [
            {
                "heading": "A JOURNEY TO THE UNKNOWN",
                "story": (
                    "Surveyor 3 launched on 17 April 1967. Its mission "
                    "was to achieve a soft landing on the Moon and study "
                    "the surface before human explorers arrived."
                )
            },
            {
                "heading": "THREE BOUNCES ON THE MOON",
                "story": (
                    "On 20 April 1967, Surveyor 3 landed in the Oceanus "
                    "Procellarum region. Its descent engine failed to "
                    "shut off at the expected moment, causing the "
                    "spacecraft to bounce twice before finally settling. "
                    "It transmitted 6,326 television images and used "
                    "its sampler to investigate lunar soil."
                )
            },
            {
                "heading": "AN UNEXPECTED VISITOR",
                "story": (
                    "In November 1969, Apollo 12 astronauts landed near "
                    "Surveyor 3. Charles Conrad and Alan Bean visited "
                    "the silent spacecraft and recovered parts of its "
                    "camera and soil sampler. A machine that had once "
                    "explored alone became part of human lunar history."
                )
            }
        ]
    },

    "APOLLO 12": {
        "subtitle": "THE HUMAN MISSION THAT REVISITED A ROBOTIC PIONEER",
        "overview": (
            "Apollo 12 was NASA's second crewed lunar landing mission. "
            "It demonstrated precision landing, expanded lunar science "
            "and connected human exploration with the earlier robotic "
            "Surveyor missions."
        ),
        "chapters": [
            {
                "heading": "A LIGHTNING-STRUCK LAUNCH",
                "story": (
                    "Apollo 12 launched on 14 November 1969 with "
                    "Charles Conrad, Richard Gordon and Alan Bean. "
                    "Lightning struck the Saturn V shortly after "
                    "liftoff, disrupting spacecraft instrumentation. "
                    "The crew and mission control recovered the systems "
                    "and continued toward the Moon."
                )
            },
            {
                "heading": "THE PINPOINT LANDING",
                "story": (
                    "On 19 November 1969, Conrad and Bean landed the "
                    "Intrepid lunar module near Surveyor 3 in the "
                    "Ocean of Storms. The mission deployed scientific "
                    "experiments, collected lunar samples and explored "
                    "the surrounding terrain."
                )
            },
            {
                "heading": "THE ROBOTIC ENCOUNTER",
                "story": (
                    "The astronauts visited Surveyor 3 and recovered "
                    "parts of the old spacecraft for examination on "
                    "Earth. Apollo 12 returned safely on 24 November "
                    "1969, leaving behind a remarkable connection "
                    "between robotic and human exploration."
                )
            }
        ]
    },

    "LUNAR PROSPECTOR": {
        "subtitle": "SEARCHING THE MOON FOR ITS HIDDEN SECRETS",
        "overview": (
            "Lunar Prospector was a NASA robotic orbiter launched in "
            "1998. It mapped the Moon's composition, investigated "
            "magnetic and gravitational fields, and searched for "
            "evidence of water ice near the lunar poles."
        ),
        "chapters": [
            {
                "heading": "A NEW LUNAR INVESTIGATION",
                "story": (
                    "Lunar Prospector launched in January 1998 and "
                    "entered lunar orbit on 12 January. Its instruments "
                    "were designed to investigate the Moon's chemical "
                    "composition and search for signs of polar ice."
                )
            },
            {
                "heading": "SECRETS BENEATH THE SURFACE",
                "story": (
                    "The spacecraft mapped major elements across the "
                    "Moon and detected hydrogen concentrations near "
                    "both poles. These observations provided evidence "
                    "suggesting that water ice could exist in "
                    "permanently shadowed regions."
                )
            },
            {
                "heading": "A FINAL EXPERIMENT",
                "story": (
                    "After an extended mission, Lunar Prospector was "
                    "deliberately directed into Shoemaker crater on "
                    "31 July 1999. Scientists hoped to observe signs "
                    "of water in the resulting dust cloud, but no "
                    "clear water-vapour signature was detected. "
                    "Its mission nevertheless transformed lunar science."
                )
            }
        ]
    },

    "SPIRIT": {
        "subtitle": "THE ROVER THAT REFUSED TO GIVE UP",
        "overview": (
            "Spirit was one of NASA's twin Mars Exploration Rovers. "
            "Designed for a much shorter mission, it spent years "
            "exploring the Martian surface and uncovering evidence "
            "that ancient Mars was once much wetter."
        ),
        "chapters": [
            {
                "heading": "THE BEGINNING OF AN ADVENTURE",
                "story": (
                    "Spirit launched on 10 June 2003 and landed in "
                    "Gusev Crater on 3 January 2004. Its mission was "
                    "to investigate rocks and soil for clues about "
                    "the history of water on Mars."
                )
            },
            {
                "heading": "A WORLD OF DISCOVERIES",
                "story": (
                    "Spirit explored the Martian plains and the "
                    "Columbia Hills. Its observations revealed "
                    "strong evidence of past water activity and "
                    "showed that Mars had experienced environments "
                    "very different from today's dry surface."
                )
            },
            {
                "heading": "SILENCE IN THE MARTIAN DUST",
                "story": (
                    "Spirit became trapped in soft soil in 2009 "
                    "and could no longer move into a favourable "
                    "position for winter. Its last communication "
                    "came in March 2010. NASA ended contact efforts "
                    "on 25 May 2011. It had operated for over six years."
                )
            }
        ]
    },

    "OPPORTUNITY": {
        "subtitle": "THE ROVER WHOSE JOURNEY BECAME LEGENDARY",
        "overview": (
            "Opportunity was Spirit's twin rover, sent to the opposite "
            "side of Mars. Its discoveries provided evidence that "
            "liquid water had once altered Martian rocks, while its "
            "extraordinary lifetime far exceeded the original plan."
        ),
        "chapters": [
            {
                "heading": "A SECOND EXPLORER ARRIVES",
                "story": (
                    "Opportunity launched on 7 July 2003 and landed "
                    "in Meridiani Planum on 24 January 2004. Its "
                    "scientific mission was to investigate rocks "
                    "and minerals for evidence of ancient water."
                )
            },
            {
                "heading": "A JOURNEY BEYOND EXPECTATIONS",
                "story": (
                    "Opportunity discovered geological evidence "
                    "that liquid water had once interacted with "
                    "Martian rocks. It travelled more than 45 "
                    "kilometres, far exceeding its planned "
                    "90-sol primary mission."
                )
            },
            {
                "heading": "THE LAST MESSAGE",
                "story": (
                    "A planet-wide dust storm in 2018 covered the "
                    "rover's solar panels and interrupted communication. "
                    "Its last communication reached Earth on "
                    "10 June 2018. NASA declared the mission over "
                    "on 13 February 2019, after nearly fifteen years "
                    "of exploration."
                )
            }
        ]
    }
}


# ---------------- PAGE CONTENT ----------------

page = st.session_state.current_page

if page == "HOME":
    # HOMEPAGE LOGO

    st.markdown("""
    <style>
    .home-heading {

    

    .mission-card {
        position: relative;
        overflow: hidden;
        border-radius: 14px;
        height: 300px;
        background-size: cover;
        background-position: center;
        cursor: pointer;
        transition: transform 0.3s ease;
    }

    .mission-card:hover {
        transform: scale(1.025);
    }

    .mission-overlay {
        position: absolute;
        inset: 0;
        background: rgba(0, 0, 0, 0.12);
        display: flex;
        justify-content: center;
        align-items: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .mission-card:hover .mission-overlay {
        opacity: 1;
        background: rgba(0, 0, 0, 0.58);
    }

    .mission-overlay span {
        color: white;
        font-size: 22px;
        font-weight: 700;
        letter-spacing: 3px;
    }

    .mission-caption {
        text-align: center;
        font-size: 15px;
        opacity: 0.75;
        margin-top: 12px;
        margin-bottom: 25px;
    }

    div.stButton > button[kind="secondary"] {
        border: 1px solid rgba(255,255,255,0.35);
        border-radius: 8px;
        padding: 12px 25px;
        font-weight: 700;
    }

    </style>
    """, unsafe_allow_html=True)

    # Main heading
    st.markdown(
        '<div class="home-heading">THEY WERE NEVER MEANT TO RETURN</div>',
        unsafe_allow_html=True
    )

    # Moon and Mars cards
    moon_col, mars_col = st.columns(2, gap="large")

    with moon_col:
        st.image("assets/images/mission Echoes/moon.png",
         use_container_width=True)

        st.markdown(
            '<div class="mission-caption">'
            '<b>THE MOON</b><br>'
            'Where humanity left its first robotic explorers.'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button("EXPLORE THE MOON", key="moon_home",
                     use_container_width=True):
            st.session_state.current_page = "MOON"
            st.rerun()

    with mars_col:
        st.image("assets/images/mission Echoes/mars.png",
         use_container_width=True)

        st.markdown(
            '<div class="mission-caption">'
            '<b>MARS</b><br>'
            'Where robotic explorers became unexpected survivors.'
            '</div>',
            unsafe_allow_html=True
        )

        if st.button("EXPLORE MARS", key="mars_home",
                     use_container_width=True):
            st.session_state.current_page = "MARS"
            st.rerun()

    # Quiz section
    st.divider()

    st.markdown(
        "<h3 style='text-align:center;'>"
        "HOW MUCH DO YOU KNOW ABOUT THEIR JOURNEYS?"
        "</h3>",
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1, 1.5, 1])

    with center:
        if st.button(
            "TEST YOUR KNOWLEDGE  →",
            key="home_quiz",
            use_container_width=True
        ):
            st.session_state.current_page = "QUIZ"
            st.rerun()



elif page == "MOON":

    st.markdown("""
    <h1 style="text-align:center;">THE MOON</h1>
    <p style="text-align:center; letter-spacing:3px; opacity:0.7;">
        A LEGACY WRITTEN IN LUNAR DUST
    </p>
    """, unsafe_allow_html=True)

    left_col, right_col = st.columns(2, gap="large")

    with left_col:
        st.subheader("THE LUNAR REUNION")

        mission_card(
    "SURVEYOR 3",
    "The spacecraft that received an unexpected human visitor.",
    "SURVEYOR 3",
    "assets/images/Title_cards/surveyor3.jpg"
)

        mission_card(
            "APOLLO 12",
            "The human mission that revisited Surveyor 3.",
            "APOLLO 12",
            "assets/images/Title_cards/apollo12.jpg"
        )

    with right_col:
        st.subheader("THE FINAL EXPERIMENT")

        mission_card(
            "LUNAR PROSPECTOR",
            "A spacecraft that ended its journey in a final lunar experiment.",
            "LUNAR PROSPECTOR",
            "assets/images/Title_cards/lunarpros.jpg"
        )


elif page == "MARS":

    st.markdown("""
    <h1 style="text-align:center;">THE RED PLANET</h1>
    <p style="text-align:center; letter-spacing:3px; opacity:0.7;">
        TWO EXPLORERS. TWO EXTRAORDINARY JOURNEYS.
    </p>
    """, unsafe_allow_html=True)

    spirit_col, opportunity_col = st.columns(2, gap="large")

    with spirit_col:
        mission_card(
            "SPIRIT",
            "The unexpected survivor that outlived its planned mission.",
            "SPIRIT",
            "assets/images/Title_cards/spirit.jpg"
        )

    with opportunity_col:
        mission_card(
            "OPPORTUNITY",
            "The rover whose journey lasted nearly fifteen years.",
            "OPPORTUNITY",
            "assets/images/Title_cards/opportunity.jpg"
        )
# INDIVIDUAL MISSION DESTINATIONS


# ---------------- INDIVIDUAL MISSION DESTINATIONS ----------------

elif page in MISSION_DATA:

    mission = MISSION_DATA[page]

    render_mission_page(
        title=page,
        subtitle=mission["subtitle"],
        overview=mission["overview"],
        chapters=mission["chapters"]
    )

    st.info("Opportunity's mission archive will be built next.")

elif page == "QUIZ":
    main_quiz()


elif page == "SOURCE":

    st.markdown("""
    <h1 style="text-align:center; letter-spacing:3px;">
        MISSION ARCHIVE & REFERENCES
    </h1>
    <p style="text-align:center; opacity:0.7; letter-spacing:2px;">
        EVERY DISCOVERY HAS A STORY. EVERY STORY HAS A SOURCE.
    </p>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("## THE LUNAR ARCHIVE")
    st.caption("Historical missions and robotic exploration of the Moon.")

    with st.expander("01 — SURVEYOR 3", expanded=True):
        st.write(
            "NASA's robotic lunar lander, its surface experiments "
            "and its historic encounter with Apollo 12."
        )
        st.markdown(
            "[NASA — Surveyor 3](https://science.nasa.gov/mission/surveyor-3/)"
        )
        st.markdown(
            "[NASA JPL — Surveyor 3](https://www.jpl.nasa.gov/missions/surveyor-3/)"
        )

    with st.expander("02 — APOLLO 12"):
        st.write(
            "NASA's second crewed lunar landing and the mission "
            "that revisited Surveyor 3."
        )
        st.markdown(
            "[NASA — Apollo 12](https://www.nasa.gov/mission/apollo-12/)"
        )
        st.markdown(
            "[NASA — Apollo 12 and Surveyor 3 photograph]"
            "(https://science.nasa.gov/resource/apollo-12-and-surveyor-3/)"
        )

    with st.expander("03 — LUNAR PROSPECTOR"):
        st.write(
            "The lunar orbiter that mapped the Moon's composition "
            "and investigated evidence of polar ice."
        )
        st.markdown(
            "[NASA — Lunar Prospector](https://science.nasa.gov/mission/lunar-prospector/)"
        )

    st.divider()

    st.markdown("## THE MARTIAN ARCHIVE")
    st.caption("Two robotic explorers. Two extraordinary journeys.")

    with st.expander("04 — SPIRIT"):
        st.write(
            "The Mars Exploration Rover that investigated Gusev Crater "
            "and uncovered evidence of ancient water."
        )
        st.markdown(
            "[NASA — Spirit](https://science.nasa.gov/mission/mer-spirit/)"
        )

    with st.expander("05 — OPPORTUNITY"):
        st.write(
            "The long-lived Mars rover that explored Meridiani Planum "
            "for nearly fifteen years."
        )
        st.markdown(
            "[NASA — Opportunity](https://science.nasa.gov/mission/mer-opportunity/)"
        )

    st.markdown(
        "[NASA — Mars Exploration Rovers: Spirit and Opportunity]"
        "(https://science.nasa.gov/mission/mars-exploration-rovers-spirit-and-opportunity/)"
    )

    st.divider()

    st.markdown("## MEDIA & ATTRIBUTION")

    st.write(
        "Mission photographs, videos, scientific visualisations and "
        "illustrations are included for educational and storytelling "
        "purposes. Individual media credits and original source links "
        "will be listed here."
    )

    st.info(
        "Media attribution is being finalised. Please refer to the "
        "original NASA or JPL media page for the exact creator, "
        "image identification and usage information."
    )

    st.divider()

    st.markdown(
        "<p style='text-align:center; opacity:0.65;'>"
        "RESEARCHED WITH NASA MISSION ARCHIVES"
        "</p>",
        unsafe_allow_html=True
    )



st.divider()