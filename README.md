# 🔐 Modular Square Roots
### An Interactive Cryptography & Number Theory Project

An interactive web application built using **Python and Streamlit** to explore modular square roots, quadratic residues and quadratic non-residues through four practical modules.

🌐 **Live Demo:** [Open Modular Square Roots](https://modular-square-roots-vsrzu6ad77gjrvjnjgrptm.streamlit.app/)

---

## 📌 1. Project Overview

Modular arithmetic is one of the fundamental concepts used in number theory and modern cryptography.

One important problem in modular arithmetic is finding the square root of a number under a given modulus.

In ordinary mathematics, finding the square root of a number means finding a value whose square equals that number.

For example:

$$
x^2 = 25
$$

The possible solutions are:

$$
x = \pm 5
$$

In modular arithmetic, the problem becomes:

$$
x^2 \equiv a \pmod{p}
$$

Where:

- **x:** Unknown square root.
- **a:** Given integer.
- **p:** Prime modulus.
- **≡:** Congruence modulo.

The objective is to determine whether a solution exists and, if it does, calculate all possible modular square roots.

This project provides an interactive environment to understand and experiment with four different modules related to modular square roots.

---

## 🎯 2. Problem Statement

Given an integer `a` and a prime number `p`, determine whether there exists an integer `x` satisfying:

$$
x^2 \equiv a \pmod{p}
$$

If a solution exists, calculate the modular square roots.

If no solution exists, identify the number as a Quadratic Non-Residue modulo `p`.

The project demonstrates:

- Finding modular square roots using exhaustive search.
- Identifying quadratic residues using Euler's Criterion.
- Efficient modular square root computation using Tonelli-Shanks.
- Generating prime numbers and verifying quadratic non-residues.

---

## 📚 3. Mathematical Concepts

### 3.1 Modular Arithmetic

Modular arithmetic deals with remainders after division.

Example:

$$
17 \mod 5 = 2
$$

Another example:

$$
7^2 \mod 11 = 49 \mod 11 = 5
$$

Therefore:

$$
7^2 \equiv 5 \pmod{11}
$$

### 3.2 Quadratic Residue

An integer `a` is called a Quadratic Residue modulo an odd prime `p` if there exists an integer `x` such that:

$$
x^2 \equiv a \pmod{p}
$$

Example:

$$
4^2 \mod 11 = 16 \mod 11 = 5
$$

Therefore, 5 is a Quadratic Residue modulo 11.

### 3.3 Quadratic Non-Residue

An integer `a` is a Quadratic Non-Residue modulo `p` if no integer `x` satisfies:

$$
x^2 \equiv a \pmod{p}
$$

Example:

3 is a Quadratic Non-Residue modulo 7 because no integer squared modulo 7 produces 3.

### 3.4 Euler's Criterion

Euler's Criterion is used to determine whether a number is a Quadratic Residue or Quadratic Non-Residue modulo an odd prime.

For a non-zero integer `a`:

$$
a^{\frac{p-1}{2}} \equiv 1 \pmod{p}
$$

If the result is 1, `a` is a Quadratic Residue.

If:

$$
a^{\frac{p-1}{2}} \equiv -1 \pmod{p}
$$

Then `a` is a Quadratic Non-Residue.

In Python, modular exponentiation is performed using:

```python
pow(a, (p-1)//2, p)
```

Special case: If `a mod p = 0`, the modular square root is 0.

---

## ⚙️ 4. Four Interactive Modules

The application provides four separate tasks through its Streamlit interface.

### Module A: Brute Force Algorithm

**Objective:** Find all modular square roots by checking every possible value of `x`.

The algorithm checks all integers from 0 to p-1.

For each value, it evaluates:

$$
x^2 \mod p = a \mod p
$$

If the condition is satisfied, the value of `x` is stored as a valid root.

**Algorithm Workflow:**

1. Initialize an empty list to store roots.
2. Iterate through all possible values of `x`.
3. Calculate the square of `x` modulo `p`.
4. Compare the result with `a mod p`.
5. Store matching values.
6. Return all valid roots.

**Python Implementation:**

```python
def brute_force(a, p):
    roots = []

    for x in range(p):
        if (x*x) % p == a % p:
            roots.append(x)

    return roots
```

**Time Complexity:** O(p) iterations.

**Advantages:**
- Simple implementation.
- Easy to understand.
- Useful for validating results for small prime numbers.

**Limitation:**

The algorithm becomes computationally expensive for large prime numbers because it checks every possible value.

---

### Module B: Euler's Criterion

**Objective:** Determine whether a number is a Quadratic Residue or Quadratic Non-Residue modulo a prime.

It uses the mathematical expression:

$$
a^{\frac{p-1}{2}} \mod p
$$

**Algorithm Workflow:**

1. Reduce `a` modulo `p`.
2. Calculate the exponent `(p-1)//2`.
3. Perform modular exponentiation.
4. Compare the result with 1 and p-1.
5. Classify the number.

**Python Implementation:**

```python
def euler_criterion(a, p):
    a = a % p

    if a == 0:
        return "Zero"

    temp = (p-1)//2
    result = pow(a, temp, p)

    if result == 1:
        return "Quadratic Residue"

    elif result == p-1:
        return "Quadratic Non-Residue"

    else:
        return "Invalid Result"
```

**Advantages:**
- Efficient residue classification.
- Uses modular exponentiation.
- Works efficiently with large prime moduli.

**Important:**

Euler's Criterion only classifies a number. It does not calculate the modular square roots.

---

### Module C: Tonelli-Shanks Algorithm

**Objective:** Calculate modular square roots efficiently for an odd prime modulus.

Tonelli-Shanks is an efficient algorithm for solving:

$$
x^2 \equiv a \pmod{p}
$$

when `p` is an odd prime and `a` is a Quadratic Residue modulo `p`.

#### Mathematical Foundation

First, decompose:

$$
p-1 = q \times 2^s
$$

Where `q` is odd.

Find a Quadratic Non-Residue `z` modulo `p`.

Initialize:

$$
m=s
$$

$$
c=z^q \mod p
$$

$$
t=a^q \mod p
$$

$$
r=a^{\frac{q+1}{2}} \mod p
$$

The algorithm repeatedly updates these values until:

$$
t=1
$$

The resulting value `r` is one square root.

The second root is:

$$
p-r \mod p
$$

Therefore:

$$
x_1=r
$$

$$
x_2=(p-r)\mod p
$$

#### Algorithm Workflow

1. Reduce `a` modulo `p`.
2. Handle the zero case.
3. Check whether `a` is a Quadratic Residue.
4. Decompose `p-1` into `q` and `2^s`.
5. Find a Quadratic Non-Residue.
6. Initialize `m`, `c`, `t` and `r`.
7. Perform Tonelli-Shanks iterations.
8. Calculate both square roots.
9. Return the sorted roots.

#### Interactive Demonstration

This module also demonstrates the reverse verification process:

1. Generate a random 256-bit prime `p`.
2. Generate a random integer `x`.
3. Calculate:

$$
a=x^2 \mod p
$$

4. Apply Tonelli-Shanks to find the square roots of `a`.
5. Verify whether the original `x` appears in the calculated roots.

**Purpose:** Demonstrates how a modular square root can be calculated efficiently without checking every possible integer.

---

### Module D: Quadratic Non-Residue Generation and Verification

**Objective:** Generate a prime number, find a Quadratic Non-Residue and verify its mathematical properties using Euler's Criterion and Tonelli-Shanks.

This module combines prime generation, non-residue discovery and verification.

#### Step 1: Generate a 256-bit Prime

A random 256-bit prime number is generated using SymPy.

```python
from sympy import randprime

def generate_prime():
    start = 2**255
    end = 2**256

    prime = randprime(start, end)

    return prime
```

#### Step 2: Find a Quadratic Non-Residue

Candidate integers are checked until Euler's Criterion gives:

$$
z^{\frac{p-1}{2}} \mod p = p-1
$$

This identifies a Quadratic Non-Residue.

#### Step 3: Verify Using Euler's Criterion

The generated non-residue is passed to Euler's Criterion.

Expected result:

**Quadratic Non-Residue**

#### Step 4: Verify Using Tonelli-Shanks

The same non-residue is passed to the Tonelli-Shanks algorithm.

Since no modular square root exists, the algorithm returns:

```python
None
```

#### Final Verification

The module demonstrates that:

- Euler's Criterion classifies the number as a Quadratic Non-Residue.
- Tonelli-Shanks confirms that no modular square root exists.

**Purpose:** Demonstrates the relationship between quadratic residue classification and modular square root computation.

---

## 🏗️ 5. Project Architecture

The project follows a modular Python architecture.

```text
modular-square-roots/
│
├── app.py
├── main.py
├── prime_generator.py
├── brute_force.py
├── euler_criterion.py
├── tonelli_shanks.py
├── requirements.txt
└── README.md
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `app.py` | Main Streamlit application and user interface |
| `main.py` | Additional Python file retained in the project |
| `prime_generator.py` | Generates random 256-bit prime numbers |
| `brute_force.py` | Implements Brute Force modular square root calculation |
| `euler_criterion.py` | Implements Euler's Criterion |
| `tonelli_shanks.py` | Implements Tonelli-Shanks and non-residue search |
| `requirements.txt` | Stores Python dependencies |
| `README.md` | Project documentation |

### Application Workflow

```text
                  USER
                    |
                    v
              STREAMLIT UI
                    |
              SELECT MODULE
                    |
       +------------+-------------+
       |            |             |
       v            v             v
   MODULE A     MODULE B      MODULE C
   Brute Force  Euler         Tonelli-
                Criterion     Shanks
       |            |             |
       v            v             v
   All Roots    Residue       Square Roots
                Classification
                    |
                    v
                 MODULE D
           Non-Residue Verification
                    |
           +---------+---------+
           |                   |
           v                   v
      Euler Criterion     Tonelli-Shanks
           |                   |
           v                   v
        Non-Residue       No Square Root
           |                   |
           +---------+---------+
                    |
                    v
              DISPLAY RESULTS
```

---

## 🛠️ 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| SymPy | Prime number generation |
| Modular Arithmetic | Mathematical foundation |
| Number Theory | Quadratic residue concepts |
| Git | Version control |
| GitHub | Source code hosting |
| Streamlit Community Cloud | Application deployment |

---

## 📦 7. Installation and Execution

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/arpitpoc/modular-square-roots.git
```

### Step 2: Navigate to Project

```bash
cd modular-square-roots
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📋 8. Requirements

The project uses the following dependencies:

```text
streamlit
sympy
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🌐 9. Live Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live Application:**

[Modular Square Roots – Live Demo](https://modular-square-roots-vsrzu6ad77gjrvjnjgrptm.streamlit.app/)

The application can be accessed directly through a web browser without installing Python locally.

---

## 🔬 10. Applications

Modular square roots have applications in several areas of mathematics and cryptography.

Some important applications include:

- Elliptic Curve Cryptography (ECC).
- Elliptic curve point decompression.
- Finite field arithmetic.
- Cryptographic algorithm research.
- Computational number theory.

For example, elliptic curve point decompression may require calculating a modular square root to recover a missing coordinate.

---

## ⚖️ 11. Algorithm Comparison

| Feature | Brute Force | Euler's Criterion | Tonelli-Shanks | Non-Residue Module |
|---|---|---|---|---|
| Residue classification | Through root search | Yes | Checks before computation | Yes |
| Calculates square roots | Yes | No | Yes | No; verifies non-existence |
| Large prime suitability | No | Yes | Yes | Yes, subject to search cost |
| Main approach | Exhaustive search | Modular exponentiation | Number theory | Generation and verification |
| Main purpose | Root calculation | Residue classification | Efficient root calculation | Non-residue verification |

---

## ⚠️ 12. Limitations

- Brute Force becomes computationally impractical for large prime numbers.
- Tonelli-Shanks is implemented for odd prime moduli.
- Euler's Criterion is applicable to odd prime moduli.
- The non-residue search checks candidate integers sequentially.
- The application is designed for educational and demonstration purposes.
- Prime generation using SymPy does not make the complete application production-ready cryptographic software.

---

## 🚀 13. Future Enhancements

Possible future improvements include:

- Visualization of Tonelli-Shanks iterations.
- Performance benchmarking between algorithms.
- Additional number-theoretic algorithms.
- Downloadable calculation reports.
- Detailed step-by-step mathematical explanations.
- Automated testing for different prime moduli.
- Improved result visualization.

---

## 👨‍💻 14. Author

**Arpit Kumar**

M.Tech – Information Security and Privacy

Sardar Vallabhbhai Patel National Institute of Technology (SVNIT), Surat.

**Project Domain:** Cryptography & Number Theory

---

## 📝 15. Conclusion

This project provides an interactive demonstration of modular square root computation and quadratic residue classification.

It covers four practical modules:

1. Brute Force Algorithm.
2. Euler's Criterion.
3. Tonelli-Shanks Algorithm.
4. Quadratic Non-Residue Generation and Verification.

By combining mathematical theory with Python implementation and an interactive Streamlit interface, the project demonstrates how different number-theoretic approaches can be used to solve and verify modular arithmetic problems.

The application helps bridge the gap between theoretical number theory and practical cryptographic concepts.
