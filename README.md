<h1 align="center">TIPE: Communication of Contactless Smart Cards - Principles and Applications</h1>

<p align="center">
  <strong>Author:</strong> Enzo Moran and Mathis Rezaï <br> 
  <strong>GitHub:</strong> <a href="https://github.com/moranenzo">moranenzo</a>, <a href="https://github.com/mathisrezai">mathisrezai</a>
</p>

<p>This repository showcases our TIPE (Travail d'Initiative Personnelle Encadré) project, which earned us a score of 17/20 from the jury. This project is all about <strong>contactless smart card communication</strong> using <strong>RFID technology</strong>. The objective was to explore how data can be transmitted and received from transport cards using RFID, and also to create a model for the card-reader interaction and experimenting by sending our own message.</p>

<h2>Project Overview</h2>

<h3>1. RFID Technology</h3>
<p>Radio Frequency Identification (RFID) is used for contactless communication in various applications, such as transport cards and contactless payments. The first part of the project explains how RFID works, focusing on:</p>
<ul>
  <li>The principles of electromagnetic induction.</li>
  <li>The effect of frequency on induction.</li>
  <li>Different frequency ranges and their use cases (Low, High, and Ultra-High Frequency).</li>
</ul>

<h3>2. Card-Reader Interaction Model</h3>
<p>This section involves the modeling of the interaction between a transport card and its reader. Key aspects include:</p>
<ul>
  <li>Calculation of resonance frequencies based on the characteristics of the card and the reader.</li>
  <li>Experimental setup to determine optimal frequency for the communication link.</li>
  <li>Analysis of the coupling between the card and the reader, by focusing on the voltage and the frequency variations.</li>
</ul>

<h3>3. Custom Message Transmission</h3>
<p>In the final part, we conducted an experiment to transmit a custom message using the card-reader setup. The key steps included:</p>
<ul>
  <li>Sending a message via the RFID link.</li>
  <li>Receiving it by demodulating of the carrier signal to retrieve the transmitted data via Arduino.</li>
  <li>Using Python to retrieve the message by processing the received data and to compare it with the transmitted message via Python.</li>
</ul>

<h2>Contents</h2>
<ul>
  <li><strong>/docs</strong>: The MCOT and presentation slides detailing the project methodology, experiments, and conclusions.</li>
  <li><strong>/exps</strong>: All our experiments with reports, pics and the data used.</li>
  <li><strong>/refs</strong>: Resources used to discover the double induction and its application to RFID.</li>
  <li><strong>/src</strong>: Contains the Python and C++ code for the message transmission and signal processing.</li>
</ul>

<h2>Key Results</h2>
<ul>
  <li>Modeling and optimizing the interaction between the smart card and reader.</li>
  <li>Transmission and reception of custom messages using an Arduino for signal transmission and Python for signal processing.</li>
  <li>Successful demonstration of contactless communication using RFID.</li>
</ul>

<h2>How to Use</h2>
<ol>
  <li>Clone the repository:  
    <pre><code>git clone https://github.com/moranenzo/TIPE-Contactless-Smart-Cards.git</code></pre>
  </li>
  <li>Explore the code in the <strong>/src</strong> directory for signal processing and transmission.</li>
  <li>Refer to the <strong>/docs</strong> folder for detailed explanations of the project.</li>
</ol>
