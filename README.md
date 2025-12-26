# NutriTrack 🥗

NutriTrack is a **chat-based nutrition tracking system** that allows users to log what they eat in natural language (for example, “I ate dal and rice”) and receive calculated nutritional insights such as protein, vitamins, and minerals.

This project is built **step by step for learning purposes**, focusing on fundamentals first and gradually introducing NLP and AI concepts — using **only free tools**.

---

## 🎯 Project Goals

- Convert human food input into structured nutrition data
- Track daily nutrient intake (protein, vitamins, minerals, etc.)
- Store and summarize nutrition data over time
- Learn how backend systems, APIs, NLP, and AI fit together
- Avoid paid APIs and black-box solutions

---

## 🧠 Learning-Oriented Design

NutriTrack is intentionally built in **phases**, each solving a single problem clearly.

### Phase Overview

1. **Phase 1 – Backend Foundations**
   - FastAPI server
   - Chat-style API endpoints
   - Request → response lifecycle

2. **Phase 2 – Nutrition Logic**
   - Food-to-nutrient lookup tables
   - Rule-based nutrient calculation
   - No AI, no storage

3. **Phase 2.5 – Git & Project Hygiene**
   - Meaningful commits
   - Clean repo structure
   - `.gitignore`

4. **Phase 3 – Data Storage**
   - Persist meals and nutrients using Excel
   - Daily meal logging

5. **Phase 4 – Reports**
   - Daily nutrient summaries
   - Historical tracking

6. **Phase 5 – NLP Improvements**
   - Handle natural language variations
   - Synonyms, quantities, normalization

7. **Phase 6 – Lightweight AI **
   - Local NLP models
   - Better food and quantity extraction

8. **Phase 7 – Productization**
   - Optional chat UI
   - UX improvements
   - Scaling ideas

---

## 🛠️ Tech Stack (So Far)

- **Language:** Python
- **Backend:** FastAPI
- **Server:** Uvicorn
- **Data Storage (later):** Excel (pandas)
- **AI/NLP (later):**  local libraries 

---

## 🚀 Current Status

- Phase 1: In progress  
- Backend server setup and basic API endpoints

---

## 🧩 Example Interaction (Future Goal)
I ate dal, rice, and broccoli


**Output**
```json
{
  "protein": 15,
  "iron": 3,
  "vitamin_c": 40
}

**Input**
