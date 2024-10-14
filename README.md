#TIPE: Communication of Contactless Smart Cards - Principles and Applications
**Author:** Enzo Moran
**GitHub:** moranenzo

This repository contains the work for my TIPE (Travail d'Initiative Personnelle Encadré) project, focused on contactless smart card communication using RFID technology. The objective was to explore how data can be transmitted and received from transport cards using RFID, alongside creating a model for the card-reader interaction and experimenting with sending custom messages.

##Project Overview

###1. RFID Technology
Radio Frequency Identification (RFID) is used for contactless communication in various applications, such as transport cards and contactless payments. The first part of the project explains how RFID works, focusing on:
- The principles of electromagnetic induction.
- The effect of frequency on induction.
- Different frequency ranges and their use cases (Low, High, and Ultra-High Frequency).

###2. Card-Reader Interaction Model
This section involves the modeling of the interaction between a transport card and its reader. Key aspects include:
- Modeling the resonance frequencies of the card and the reader.
- Experimental setup to determine optimal frequency for the communication link.
- Analysis of the coupling between the card and the reader, including voltage and frequency variations.

###3. Custom Message Transmission
In the final part, I conducted an experiment to transmit a custom message using the card-reader setup. The key steps included:
- Sending and receiving a message via the RFID link.
- Demodulation of the carrier signal to retrieve the transmitted data.
- Comparison and analysis of the transmitted and received signals using an Arduino setup.

##Contents
- /src: Ressources used to discover the double induction and its application to RFID.
- /code: Contains the Python and Arduino code for the message transmission and signal processing.
- /experiment: All our experiments with a report, pics and the data used.
- /docs: The full report and presentation slides detailing the project methodology, experiments, and conclusions.

##Key Results
- Modeling and optimizing the interaction between the smart card and reader.
- Transmission and reception of custom messages using an Arduino for signal transmission and Python for signal processing.
- Successful demonstration of contactless communication using RFID.

##How to Use
1. Clone the repository: git clone https://github.com/moranenzo/TIPE-Contactless-Smart-Cards.git
2. Explore the code in the /code directory for signal processing and transmission.
3. Refer to the /docs folder for detailed explanations of the project.
