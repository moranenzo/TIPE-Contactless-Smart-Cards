<h1 align="center"> References - Contactless Smart Card Communication</h1>

<p align="center">
  <strong>TIPE Project - Bibliographic Resources</strong>  
</p>

This folder contains all the key references we used to guide our research and experiments during the TIPE project. Each resource here played a specific role in helping us understand, model, and implement the transmission of custom messages through electromagnetic coupling.

---

##  Reference Overview

### `encode_hamming.py` & `decode_hamming.py`

These Python scripts implement **Hamming Error-Correcting Codes**. They allowed us to detect and correct specific transmission errors. This was essential to ensure the **integrity of the messages** transmitted over the RFID link, especially during our custom message experiments. This approach helped us understand the fundamentals of **error correction** in digital communication.

---

### `Systèmes et techniques RFID - Claude TETELIN.pdf`

This in-depth technical document introduced us to the **core physical principles of RFID**. It was key to understanding:
- How electromagnetic induction enables contactless communication,
- The distinction between low, high, and ultra-high frequency RFID systems,
- The physics behind **resonant circuits** and the **energy coupling** between card and reader.

It provided the **scientific foundation** we needed to define our experimental scope and replicate key phenomena at our scale.

---

### `Site G-Goessel.url`

This is a link to an older **TIPE project** by another student that was extremely useful for practical insights. It showed how to:
- Transmit a message via RFID by amplitude modulation,
- Use **operational amplifiers** to **modulate and demodulate signals**,
- Design electronic circuits for message transmission.

This resource helped us **design our own electrical setup** for modulating and receiving messages.

---

### `PT-2015-Info-RFID-Sujet.pdf` and `PT-2015-Info-RFID-Corrigé.pdf`

These documents, published by **Banque PT**, are among the first we found on the topic of RFID. They offered:
- A clear introduction to how RFID systems work,
- Most of the **core equations** we used to model our experiments,
- Practical examples and **data tables** we compared against our results.

They served as a **technical reference and learning base** throughout the project and helped us link theory with our experimental observations.

---

We are thankful for the authors of these resources. Their contributions helped us shape our project.

