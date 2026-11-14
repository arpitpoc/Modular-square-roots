
import streamlit as st
import random
from sympy import isprime
from prime_generator import generate_prime
from brute_force import brute_force
from euler_criterion import euler_criterion
from tonelli_shanks import tonelli_shanks, find_non_residue

st.set_page_config(
    page_title="Modular Square Roots",
    page_icon="🔐",
    layout="wide"
)



st.markdown("""
<style>


.stApp {
    background:
        radial-gradient(
            ellipse 80% 55% at 5% -10%,
            rgba(139, 92, 246, 0.30),
            transparent 70%
        ),
        radial-gradient(
            ellipse 70% 55% at 100% 0%,
            rgba(6, 182, 212, 0.22),
            transparent 65%
        ),
        radial-gradient(
            ellipse 60% 50% at 50% 110%,
            rgba(79, 70, 229, 0.15),
            transparent 70%
        ),
        #0a0a12;

    background-attachment: fixed;
    color: #ececf4;
}


.block-container {
    max-width: 1150px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}



header[data-testid="stHeader"] {
    background: rgba(10, 10, 18, 0.85);
    border-bottom: 1px solid rgba(255,255,255,0.08);
}



h1, h2, h3 {
    color: #ececf4 !important;
    font-weight: 700 !important;
    text-shadow: none !important;
}

p, label {
    color: #b4b4c7 !important;
}



section[data-testid="stSidebar"] {
    background: rgba(14, 14, 24, 0.92);
    border-right: 1px solid rgba(255,255,255,0.08);
}



[data-testid="stNumberInput"] input,
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.05) !important;
    color: #ececf4 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 10px !important;
}



[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
    color: #ececf4;
}



.stButton > button,
.stButton > button p,
.stButton > button span {
    background: #7c3aed;
    color: #ffffff !important;
    border: none;
    border-radius: 9px;
    font-weight: 600;
}

.stButton > button {
    padding: 9px 18px;
    transition: background 0.2s ease;
}

.stButton > button:hover {
    background: #6d28d9;
    color: #ffffff !important;
}



div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 14px;
}



[data-testid="stCode"] {
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 10px;
}


hr {
    border-color: rgba(255,255,255,0.10) !important;
}



::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.18);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)




st.title("🔐 Modular Square Roots")
st.caption("Cryptography & Number Theory Project")

st.divider()

task= st.sidebar.selectbox(
    "Select Algorithm",
    [
        "Task A - Brute Force",
        "Task B - Euler's Criterion",
        "Task C - Tonelli-Shanks",
        "Task D - Quadratic Non-Residue"  
    ]


)
st.write("Selected",task)


if task == "Task A - Brute Force":

    st.header("Brute Force Algorithm")
    st.write("Find all square roots of a modulo p.")

    p = st.number_input(
        "Enter a small prime Number (p)",
        min_value=2,
        step=1,
        format="%d"
    )

    a = st.number_input(
        "Enter value (a)",
        min_value=0,
        step=1,
        format="%d"
    )

    if st.button("Calculate Roots"):

        if not isprime(p):
            st.error("Please enter a valid prime number.")

        else:
            roots = brute_force(a, p)

            

            if roots:
                st.success(f"Square Roots: {roots}")
            else:
                st.warning("No modular square root exists for this value.")

elif task == "Task B - Euler's Criterion":

    st.header("Euler's Criterion Algorithm")

    st.write(
        "Check whether a is a Quadratic Residue "
        "or Non-Residue modulo p."
    )

    p = st.number_input(
        "Enter a small prime Number (p)",
        min_value=2,
        step=1,
        format="%d",
        key="euler_p"
    )

    a = st.number_input(
        "Enter value (a)",
        min_value=0,
        step=1,
        format="%d",
        key="euler_a"
    )

    if st.button("Check Residue"):

        if not isprime(p):
            st.error("Please enter a valid prime number.")

        else:
            result = euler_criterion(a, p)

            

            if result == "Quadratic Residue":
                st.success(result)

            elif result == "Quadratic Non-Residue":
                st.error(result)

            else:
                st.info(result)

elif task == "Task C - Tonelli-Shanks":

    st.header("Tonelli-Shanks Algorithm")

    # Two equal columns
    col1, col2 = st.columns(2, gap="large")

    # WINDOW 1: Generate Prime
    with col1:

        with st.container( border=True,height=330):

            st.subheader("Generate Prime")

            if st.button("Generate 256-bit Prime", use_container_width=True):

                st.session_state.p = generate_prime()
                st.session_state.x = None
                st.session_state.a = None
                st.session_state.roots = None

            if st.session_state.get("p") is not None:

                st.write("Generated Prime (p):")
                st.code(str(st.session_state.p))


    # WINDOW 2: Calculate a
    with col2:

        with st.container(border=True, height=330):

            st.subheader("Calculate a = x² mod p")

            if st.button("Calculate a", use_container_width=True):

                if st.session_state.get("p") is not None:

                    p = st.session_state.p

                    x = random.randint(1, p - 1)
                    a = pow(x, 2, p)

                    st.session_state.x = x
                    st.session_state.a = a
                    st.session_state.roots = None

                else:
                    st.warning("Generate prime first.")

            if st.session_state.get("a") is not None:

                st.write("Original x:")
                st.code(str(st.session_state.x))

                st.write("Calculated a:")
                st.code(str(st.session_state.a))


    # WINDOW 3: Calculate Square Roots
    with st.container(border=True):

        st.subheader("Calculate Square Root")

        if st.button("Calculate Square Roots", use_container_width=True):

            if st.session_state.get("a") is not None:

                roots = tonelli_shanks(
                    st.session_state.a,
                    st.session_state.p
                )

                st.session_state.roots = roots

            else:
                st.warning("Calculate a first.")

        if st.session_state.get("roots") is not None:

            st.success(f"Square Roots: {st.session_state.roots}")

            st.write(
                "Original x found:",
                st.session_state.x in st.session_state.roots
            )
elif task == "Task D - Quadratic Non-Residue":

    st.header("Quadratic Non-Residue")

    col1, col2 = st.columns(2, gap="large")

    # Window 1: Generate Prime
    with col1:
        with st.container(border=True, height=330):

            st.subheader("Generate Prime")

            if st.button("Generate 256-bit Prime", key="d_prime"):
                st.session_state.dp = generate_prime()
                st.session_state.da = None
                st.session_state.d_result = None
                st.session_state.d_roots = None

            if st.session_state.get("dp") is not None:
                st.write("Generated Prime (p):")
                st.code(str(st.session_state.dp))

    # Window 2: Find Non-Residue
    with col2:
        with st.container(border=True, height=330):

            st.subheader("Find Quadratic Non-Residue")

            if st.button("Generate Non-Residue", key="d_nonresidue"):

                if st.session_state.get("dp") is not None:

                    a = find_non_residue(st.session_state.dp)

                    st.session_state.da = a
                    st.session_state.d_result = None
                    st.session_state.d_roots = None

                else:
                    st.warning("Generate prime first.")

            if st.session_state.get("da") is not None:
                st.write("Non-Residue (a):")
                st.code(str(st.session_state.da))

    # Window 3: Verification
    with st.container(border=True):

        st.subheader("Verify Quadratic Non-Residue")

        if st.button("Verify", key="d_verify"):

            if st.session_state.get("da") is not None:

                a = st.session_state.da
                p = st.session_state.dp

                result = euler_criterion(a, p)
                roots = tonelli_shanks(a, p)

                st.session_state.d_result = result
                st.session_state.d_roots = roots

            else:
                st.warning("Generate non-residue first.")

        if st.session_state.get("d_result") is not None:

            st.write("Euler Criterion:")
            st.error(st.session_state.d_result)

            st.write("Tonelli-Shanks Result:")
            st.error(f"Square Roots: {st.session_state.d_roots}")