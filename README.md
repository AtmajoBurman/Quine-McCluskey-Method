# 🧮 Quine-McCluskey Boolean Minimizer (with Prime Implicant Chart)

This is a Python implementation of the **Quine-McCluskey method** for minimizing Boolean expressions. The tool helps reduce the number of terms and variables in a logic expression using systematic grouping and chart-based prime implicant selection.

---
▶️ **[Quine McCluskey Implementation Video Demo](https://drive.google.com/file/d/1IoMJO3g2NVDf69poZZKV7o0O5cTA6OeV/view?usp=drive_link)**

This screen recording demonstrates the Quine-McCluskey (QMC) algorithm in action, using the Python program found within this repository. The video walks through an example, showcasing how the code simplifies a Boolean expression step-by-step.

**Example Used in the Video:** `F(A, B, C) = Σ(0, 1, 2, 5,6,7,8,9,10,14)`

**Final Minimized Expression:** `a'bc + a'bd + a'c'd + b'c' + cd'`

---

Note: For certain complex Boolean functions, particularly those with a cyclic prime implicant chart, this solution provides a minimal cover but may not be the absolute most reduced form. A more complex approach, such as Petrick's Method, would be required to solve such cases.

## 🚀 Features

- ✅ Converts decimal minterms to binary
- ✅ Groups terms by number of 1s
- ✅ Combines terms to find prime implicants
- ✅ Builds a Prime Implicant Chart
- ✅ Minimizes the chart using:
  - **Essential Prime Implicants**
  - **Column domination rules**
- ✅ Outputs minimized Boolean expression

---

## 🛠️ How It Works

### 1. Input
- Number of variables
- Variable names (like `A`, `B`, `C`...)
- List of minterms to be minimized

### 2. Process
- Binary conversion of minterms
- Grouping based on number of 1s
- Comparing adjacent groups to combine terms
- Identifying Prime Implicants
- Constructing Prime Implicant Chart
- Applying reduction rules:
  - Select essential prime implicants (Rule 1)
  - Eliminate dominating columns (Rule 2)

### 3. Output
- List of prime implicants
- Boolean expression in minimized form
- Final minimized Prime Implicant Chart

---

## 📷 Sample Output

```
Prime Implicants:
A'B + BC'

Minimized Prime Implicant Chart:
PI      [1]   [3]   [5]
A'B      X     X     
BC'      X           X
```

---

## ▶️ Usage

### Run the script
```bash
python quine.py
```

### Example
```text
Enter number of variables: 4
Enter variable 1: A
Enter variable 2: B
Enter variable 3: C
Enter variable 4: D

Enter minterms:
5
more? 1
7
more? 1
13
more? 0
```

---

## 📂 File Structure

```
.
├── quine.py           # Main script
├── README.md          # This file
```

---

## 📚 Concepts Used

- Quine-McCluskey Algorithm
- Prime Implicants & Essential Prime Implicants
- Boolean Algebra
- Bit Manipulation
- Chart Construction
- Recursive Simplification

---

## 🧠 Inspiration

This project is inspired by how digital logic circuits are optimized in real-world electronics, and explores how logic minimization can be automated using algorithms.

---

## 🤝 Contribution

Feel free to fork the repo and contribute improvements! You can:
- Improve UI / CLI
- Add Karnaugh map visualization
- Support SOP/POS formats
- Add GUI (Tkinter or Web interface)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Atmajo Burman**  
Logic Designer • Coder • Enthusiast
