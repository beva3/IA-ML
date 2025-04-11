
**Linear Regression**

---

### ✅ What is Linear Regression?

**Linear regression** is a method to **predict a number** using other numbers.  
It draws a **straight line** to show the **relation between variables**.

Example:  
You want to predict your **weight** from your **height**. Linear regression can help.

---

### ✅ Why use this?

- To **predict values** (price, age, score, etc.).
- To **see trends** in your data.
- To **understand** how one thing affects another.

---

### ✅ How does it work?

- It finds the **best straight line** between points (data).
- This line shows the **relation** between input (X) and output (Y).

---

### ✅ The formula (if linear regression):  
```
y = a1 * x + a0
```

| Element | Name                  | Meaning                                |
|---------|-----------------------|----------------------------------------|
| `y`     | **Output / Target**   | What we want to predict                |
| `x`     | **Input / Feature**   | The known value (like height, size…)  |
| `a1`    | **Slope / Coefficient** | Shows how much y changes when x changes |
| `a0`    | **Intercept**         | Where the line starts (when x = 0)    |

---

### ✅ Steps to do linear regression:

1. **Collect data**  
   (X = input, Y = output)

2. **Split data** into:
   - **Train set** (to learn)
   - **Test set** (to check the model)

3. **Scale (normalize)** data (make values similar)

4. **Train the model**  
   Use the train set to find the best line

5. **Predict**  
   Use the line to find Y from new X

6. **Evaluate**  
   Check if the model is good (with error calculation)

---

Let's make it super easy.

---

### ✅ Step 2: What does **"Split data"** mean?

It means:  
👉 We **divide our data** into **two parts**:

- **Training set**: To **teach** the model  
- **Test set**: To **check** if the model works well

Why?  
We want to see if the model can **predict new values** (not just memorize old ones).

---

### ✅ 3 Easy Examples (with numbers):

#### 📊 Example 1: Predict weight from height
You have this data:

| Height (x) | Weight (y) |
|------------|------------|
| 150 cm     | 45 kg      |
| 155 cm     | 48 kg      |
| 160 cm     | 52 kg      |
| 165 cm     | 55 kg      |
| 170 cm     | 58 kg      |

**Split:**

- Train: 150, 155, 160 → (to learn)
- Test: 165, 170 → (to test the model)

---

#### 📊 Example 2: Predict marks from study hours

| Hours (x) | Marks (y) |
|-----------|-----------|
| 1         | 40        |
| 2         | 50        |
| 3         | 60        |
| 4         | 65        |
| 5         | 70        |

**Split:**

- Train: (1, 2, 3)
- Test: (4, 5)

---

#### 📊 Example 3: Predict salary from experience

| Experience (x) | Salary (y) |
|----------------|------------|
| 0              | 30K        |
| 1              | 35K        |
| 2              | 40K        |
| 3              | 50K        |
| 4              | 55K        |

**Split:**

- Train: (0, 1, 2)
- Test: (3, 4)

---

So the idea is:  
✅ Use some data to **learn**  
✅ Use the rest to **test** (check prediction)


**régression logistique** :

---

### 🔷 What is **logistic regression**?

It is a **linear model** like linear regression,  
👉 but it is used for **classification**, not prediction of a number.

---

### 🔷 When to use it?

Use logistic regression when:
- Your result (**y**) is **yes or no**,  
- Example: "Will the person open the email?" → Yes (1) or No (0)

This is called a **binary variable**: only two values (1 or 0)

---

### 🔷 How does it work?

1. You have data → example:  
   - `x1 = average shopping cart`  
   - `x2 = number of emails opened`

2. You want to know if the person will **open** the next email (yes = 1, no = 0)

3. Like linear regression, it creates a **line**:  
   `y = a1x1 + a2x2 + a0`  
   But here, `y` must be **between 0 and 1**

4. So we use a **special function**:  
   ✅ It’s called the **sigmoid function**

   This function **converts** any number into a value **between 0 and 1**

   - If output is close to **1** → class is **yes (1)**  
   - If output is close to **0** → class is **no (0)**

---

### 🔷 Formula (don’t worry, just look):

#### Sigmoid:
```
      1
-------------
  1 + e^(-z)
```
where `z = a1x1 + a2x2 + a0`

This gives us a **probability** (how likely something is to happen)

---

### 🔷 What is the goal?

We want the model to:
- **Give correct class** (1 or 0)
- **Minimize error** (called **cost**)

But here, we use a **new cost function** called **log loss**  
(looks complicated, but same idea: punish wrong answers, reward good ones)

---

### 🔷 Summary (Easy Words):

| Concept                   | Linear Regression     | Logistic Regression     |
|--------------------------|------------------------|--------------------------|
| Goal                     | Predict a number       | Predict a class (yes/no) |
| Example                  | Predict salary         | Predict if email opened  |
| Output                   | Any number             | Between 0 and 1          |
| Special function         | None                   | Sigmoid                  |
| Cost function            | MSE (squared error)    | Log Loss                 |

---
