import streamlit as st


quiz_data = {


    "surveyor_3": [

    {
        "question": "What was Surveyor 3 designed primarily to demonstrate?",
        "options": [
            "a) A crewed lunar landing",
            "b) A controlled soft landing and surface investigation",
            "c) A sample return from the Moon",
            "d) A long-duration lunar orbit"
        ],
        "answer": "b) A controlled soft landing and surface investigation",
        "explanation": (
            "Surveyor 3 tested a controlled soft landing and "
            "investigated lunar soil through imaging and "
            "surface-sampler experiments."
        )
    },

    {
        "question": "Which instrument capability helped Surveyor 3 investigate the mechanical properties of lunar soil?",
        "options": [
            "a) A deep-space radio telescope",
            "b) A remotely operated surface sampler",
            "c) A seismometer network",
            "d) A high-altitude weather balloon"
        ],
        "answer": "b) A remotely operated surface sampler",
        "explanation": (
            "Surveyor 3's surface sampler dug trenches and performed "
            "tests on the lunar soil, helping characterize its "
            "mechanical behaviour."
        )
    },

    {
        "question": "On which lunar surface feature did NASA's Surveyor 3 successfully land in April 1967?",
        "options": [
            "a) Oceanus Procellarum (Ocean of Storms)",
            "b) Mare Crisium (Sea of Crises)",
            "c) Mare Tranquillitatis (Sea of Tranquility)",
            "d) Mare Imbrium (Sea of Rains)"
        ],
        "answer": "a) Oceanus Procellarum (Ocean of Storms)",
        "explanation": (
            "Surveyor 3 landed in Oceanus Procellarum, "
            "the same broad lunar region later visited by Apollo 12."
        )
    }

],

    


    # ======================================
    # APOLLO 12
    # ======================================

    "apollo_12": [

        {
            "question": "Which Apollo mission visited Surveyor 3?",
            "options": [
                "a) Apollo 11",
                "b) Apollo 12",
                "c) Apollo 14",
                "d) Apollo 15"
            ],
            "answer": "b) Apollo 12",
            "explanation": (
                "Apollo 12 astronauts Pete Conrad and Alan Bean "
                "visited Surveyor 3 in November 1969 and returned "
                "selected parts to Earth."
            )
        },

        {
            "question": "Apollo 12 (1969) achieved a remarkable milestone in lunar exploration. What made its landing particularly significant?",
            "options": [
                "a) It became the first crewed mission to orbit the Moon",
                "b) It brought the first lunar rover to the Moon",
                "c) It performed a precision landing near Surveyor 3",
                "d) It landed on the far side of the Moon"
            ],
            "answer": "c) It performed a precision landing near Surveyor 3",
            "explanation": (
                "Apollo 12 successfully landed close to the "
                "previously landed Surveyor 3 spacecraft."
            )
        },

        {
            "question": "During Apollo 12, astronauts Pete Conrad and Alan Bean visited the Surveyor 3 spacecraft. What did they bring back to Earth from it?",
            "options": [
                "a) Its television camera and other components",
                "b) Its solar panels and landing legs",
                "c) Its complete landing engine",
                "d) Its entire scientific instrument package"
            ],
            "answer": "a) Its television camera and other components",
            "explanation": (
                "The astronauts removed Surveyor 3's television "
                "camera and other parts for examination on Earth."
            )
        }

    ],


    # ======================================
    # LUNAR PROSPECTOR
    # ======================================

    "lunar_prospector": [

        {
            "question": "Why did Lunar Prospector impact near Shoemaker crater?",
            "options": [
                "a) To test a new landing engine",
                "b) To create a seismic event for Apollo astronauts",
                "c) To search for a water-vapour signature in the ejecta",
                "d) To deliver a rover"
            ],
            "answer": "c) To search for a water-vapour signature in the ejecta",
            "explanation": (
                "The deliberate impact was intended to eject material "
                "that Earth-based observatories could examine for "
                "signs of water vapour. The hoped-for signature "
                "was not confirmed."
            )
        },

        {
            "question": "What did Lunar Prospector's neutron measurements detect near the lunar poles?",
            "options": [
                "a) Enhanced hydrogen signatures",
                "b) Active volcanoes",
                "c) Liquid rivers",
                "d) A thick oxygen atmosphere"
            ],
            "answer": "a) Enhanced hydrogen signatures",
            "explanation": (
                "Enhanced hydrogen signatures were consistent with "
                "possible water ice in permanently shadowed polar "
                "regions, but this was indirect evidence."
            )
        },

        {
            "question": "NASA's Lunar Prospector mission detected evidence of hydrogen concentrations near the Moon's polar regions, suggesting the possible presence of water ice.",
            "options": [
                "a) True",
                "b) False"
            ],
            "answer": "a) True",
            "explanation": (
                "Lunar Prospector detected enhanced hydrogen "
                "concentrations near the lunar poles, supporting "
                "the possibility of water ice."
            )
        }

    ],


    # ======================================
    # SPIRIT
    # ======================================

    "spirit": [

        {
            "question": "Why did Spirit stop being able to drive in 2009?",
            "options": [
                "a) Its wheels were removed by astronauts",
                "b) It became embedded in soft soil",
                "c) It ran out of oxygen",
                "d) Its parachute became tangled"
            ],
            "answer": "b) It became embedded in soft soil",
            "explanation": (
                "Spirit became embedded in soft soil. A failed "
                "wheel also dragged through the ground, exposing "
                "material that scientists could study."
            )
        },

        {
            "question": "What were the primary planned surface mission durations for Spirit and Opportunity?",
            "options": [
                "a) 30 sols each",
                "b) 90 sols each",
                "c) One Martian year each",
                "d) Five Earth years each"
            ],
            "answer": "b) 90 sols each",
            "explanation": (
                "The twin rovers were designed for primary missions "
                "of about 90 Martian days, or sols. Both operated "
                "far longer."
            )
        },

        {
            "question": "Which rover was the first of the twin Mars exploration rovers to land?",
            "options": [
                "a) Spirit",
                "b) Opportunity",
                "c) Both landed at the same time",
                "d) Neither; Sojourner landed first"
            ],
            "answer": "a) Spirit",
            "explanation": (
                "Spirit landed on 3 January 2004; Opportunity "
                "followed on 24 January 2004."
            )
        }

    ],


    # ======================================
    # OPPORTUNITY
    # ======================================

    "opportunity": [

        {
            "question": "What environmental event contributed to Opportunity's final loss of communication?",
            "options": [
                "a) A planet-encircling dust storm",
                "b) A global flood",
                "c) A volcanic eruption",
                "d) A solar eclipse lasting months"
            ],
            "answer": "a) A planet-encircling dust storm",
            "explanation": (
                "The 2018 planet-encircling dust storm blocked "
                "sunlight from reaching the rover's solar panels, "
                "preventing it from recharging."
            )
        },

        {
            "question": "Opportunity landed on Mars on which date?",
            "options": [
                "a) 3 January 2004",
                "b) 24 January 2004",
                "c) 25 May 2008",
                "d) 6 August 2012"
            ],
            "answer": "b) 24 January 2004",
            "explanation": (
                "Opportunity landed on 24 January 2004, "
                "three weeks after Spirit."
            )
        },

        {
            "question": "What was the approximate final driving distance of Opportunity?",
            "options": [
                "a) 1.2 km",
                "b) 7.73 km",
                "c) 28 km",
                "d) 45.16 km"
            ],
            "answer": "d) 45.16 km",
            "explanation": (
                "Opportunity's final odometry was 45.16 kilometers, "
                "more than a marathon distance."
            )
        }

    ],


    # ======================================
    # MISCELLANEOUS
    # ======================================

    "miscellaneous": [

        {
            "question": "Which statement about evidence of water and evidence of life is scientifically sound?",
            "options": [
                "a) Any hydrogen detection proves life",
                "b) Past liquid water automatically means life existed",
                "c) Water-related evidence can identify potentially habitable environments but does not prove life",
                "d) A rover can confirm life from a photograph alone"
            ],
            "answer": "c) Water-related evidence can identify potentially habitable environments but does not prove life",
            "explanation": (
                "Water is important for habitability, but evidence "
                "of water alone is not evidence that life actually existed."
            )
        },

        {
            "question": "Which statement best describes the difference between a lander and an orbiter?",
            "options": [
                "a) A lander touches down; an orbiter studies a world from orbit",
                "b) A lander always has wheels; an orbiter has wings",
                "c) An orbiter must return to Earth",
                "d) There is no functional difference"
            ],
            "answer": "a) A lander touches down; an orbiter studies a world from orbit",
            "explanation": (
                "A lander reaches the surface, while an orbiter "
                "remains in orbit and studies the body remotely."
            )
        },

        {
            "question": "What were the primary planned surface mission durations for Spirit and Opportunity?",
            "options": [
                "a) 30 sols each",
                "b) 90 sols each",
                "c) One Martian year each",
                "d) Five Earth years each"
            ],
            "answer": "b) 90 sols each",
            "explanation": (
                "The twin rovers were designed for primary missions "
                "of about 90 Martian days, or sols. Both operated "
                "far longer."
            )
        },

        {
            "question": "What is the primary scientific value of studying rocks on Mars?",
            "options": [
                "a) To identify Earth's continents",
                "b) To reconstruct the planet's geological and environmental history",
                "c) To measure the Moon's orbit",
                "d) To predict Earth's daily weather"
            ],
            "answer": "b) To reconstruct the planet's geological and environmental history",
            "explanation": (
                "Rock textures, minerals and chemistry preserve "
                "evidence of the processes and environments "
                "that shaped Mars."
            )
        },

        {
            "question": "Why are permanently shadowed lunar polar craters scientifically interesting?",
            "options": [
                "a) They contain Earth's atmosphere",
                "b) They may preserve volatile substances such as water ice",
                "c) They are warmer than the equator",
                "d) They receive the most direct sunlight"
            ],
            "answer": "b) They may preserve volatile substances such as water ice",
            "explanation": (
                "Some polar crater floors receive little or no "
                "direct sunlight, allowing volatile materials "
                "to remain extremely cold over long periods."
            )
        }

    ]

}


# ==========================================
# MAIN QUIZ PAGE
# ==========================================

def main_quiz():

    current_page = st.session_state.get("quiz_page", "main")

    if current_page == "main":

        st.title("SPACE EXPLORATION QUIZ")

        st.write(
            "Test your knowledge about the forgotten machines "
            "of the Moon and Mars!"
        )

        st.write("Choose a quiz category to begin.")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Surveyor 3", use_container_width=True):
                open_machine_quiz("surveyor_3")

            if st.button("Apollo 12", use_container_width=True):
                open_machine_quiz("apollo_12")

            if st.button("Lunar Prospector", use_container_width=True):
                open_machine_quiz("lunar_prospector")

        with col2:

            if st.button("Spirit", use_container_width=True):
                open_machine_quiz("spirit")

            if st.button("Opportunity", use_container_width=True):
                open_machine_quiz("opportunity")

            if st.button("Miscellaneous", use_container_width=True):
                open_machine_quiz("miscellaneous")

    else:

        quiz_pages = {
            "surveyor_3": surveyor_3_quiz,
            "apollo_12": apollo_12_quiz,
            "lunar_prospector": lunar_prospector_quiz,
            "spirit": spirit_quiz,
            "opportunity": opportunity_quiz,
            "miscellaneous": miscellaneous_quiz
        }

        selected_quiz = quiz_pages.get(current_page)

        if selected_quiz:
            selected_quiz()

        else:
            st.error("Quiz page not found.")

        if st.button("← Back to Quiz Categories"):

            st.session_state.quiz_page = "main"

            st.rerun()


# ==========================================
# NAVIGATION FUNCTION
# ==========================================

def open_machine_quiz(machine_name):

    st.session_state.quiz_page = machine_name

    st.session_state.quiz_state = {
        "index": 0,
        "score": 0,
        "submitted": False,
        "finished": False
    }

    st.rerun()


# ==========================================
# COMMON QUIZ INTERFACE
# ==========================================

def quiz_interface(title, category):

    questions = quiz_data[category]

    if not questions:

        st.title(title)
        st.info("Questions will be added soon.")

        return

    if "quiz_state" not in st.session_state:

        st.session_state.quiz_state = {
            "index": 0,
            "score": 0,
            "submitted": False,
            "finished": False
        }

    state = st.session_state.quiz_state

    total_questions = len(questions)

    # ======================================
    # FINAL RESULT
    # ======================================

    if state["finished"]:

        st.title("QUIZ COMPLETED!")

        st.metric(
            "Final Score",
            f"{state['score']} / {total_questions}"
        )

        percentage = (state["score"] / total_questions) * 100

        st.progress(int(percentage))

        st.subheader(f"Your Result: {percentage:.1f}%")

        if st.button("Retake Quiz"):

            st.session_state.quiz_state = {
                "index": 0,
                "score": 0,
                "submitted": False,
                "finished": False
            }

            st.rerun()

        return

    # ======================================
    # CURRENT QUESTION
    # ======================================

    index = state["index"]

    question = questions[index]

    radio_key = f"{category}_answer_{index}"

    st.title(title)

    st.progress(index / total_questions)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Question",
            f"{index + 1} / {total_questions}"
        )

    with col2:

        st.metric(
            "Score",
            state["score"]
        )

    st.divider()

    # ======================================
    # QUESTION SECTION
    # ======================================

    with st.container(border=True):

        st.subheader(f"Question {index + 1}")

        st.write(question["question"])

        st.write("Select your answer:")

        selected_answer = st.radio(
            "Choose one option",
            question["options"],
            index=None,
            key=radio_key,
            disabled=state["submitted"]
        )

    # ======================================
    # SUBMIT ANSWER
    # ======================================

    if not state["submitted"]:

        if st.button(
            "Submit Answer",
            disabled=selected_answer is None,
            use_container_width=True
        ):

            state["submitted"] = True

            if selected_answer == question["answer"]:

                state["score"] += 1

            st.rerun()

    # ======================================
    # FEEDBACK
    # ======================================

    if state["submitted"]:

        if selected_answer == question["answer"]:

            st.success("Correct! Well done.")

        else:

            st.error("Incorrect answer.")

            st.write(
                "**Correct Answer:** " + question["answer"]
            )

        # ==================================
        # NEXT QUESTION BUTTON
        # ==================================

        if index == total_questions - 1:

            button_text = "Finish Quiz"

        else:

            button_text = "Next Question"

        if st.button(
            button_text,
            use_container_width=True
        ):

            if index == total_questions - 1:

                state["finished"] = True

            else:

                state["index"] += 1

            state["submitted"] = False

            st.rerun()

        # ==================================
        # MISSION INSIGHT
        # ==================================

        st.divider()

        with st.container(border=True):

            st.subheader("💡 MISSION INSIGHT")

            st.info(question["explanation"])


# ==========================================
# INDIVIDUAL QUIZ PAGES
# ==========================================

def surveyor_3_quiz():

    quiz_interface("SURVEYOR 3 QUIZ", "surveyor_3")


def apollo_12_quiz():

    quiz_interface("APOLLO 12 QUIZ", "apollo_12")


def lunar_prospector_quiz():

    quiz_interface("LUNAR PROSPECTOR QUIZ", "lunar_prospector")


def spirit_quiz():

    quiz_interface("SPIRIT QUIZ", "spirit")


def opportunity_quiz():

    quiz_interface("OPPORTUNITY QUIZ", "opportunity")


def miscellaneous_quiz():

    quiz_interface("MISCELLANEOUS QUIZ", "miscellaneous")