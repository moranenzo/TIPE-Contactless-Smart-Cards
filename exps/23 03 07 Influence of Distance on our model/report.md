<h1>Experiment Report: Influence of Distance on Our Model</h1>

<h2>Objective of the Experiment</h2>
<p>
  In a previous experiment, I highlighted the significant effect of distance between the two coils on the induction effect. This experiment aims to further investigate the influence of distance on our model and determine the maximum effective distance for reliable operation. Since no message is transmitted when the card is not directly in front of the reader, the distance between the two coils is expected to greatly affect message transmission quality. Defining a maximum operational distance is therefore essential.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the Card-Reader Model</h3>
<p>
    I assembled the card and reader circuits.
</p>
<p>
<strong>Parameters Used:</strong>
</p>
<ul>
    <li>Inductance of coils: L1 = L2 = 9 mH</li>
    <li>Capacitance of capacitors: C1 = C2 = 0.22 µF</li>
    <li>Resistance in the card: {0 Ω, 1 kΩ} (no significant effect observed with higher resistance)</li>
    <li>Follower system (OpAmp)</li>
    <li>Low-Frequency Generator: 5 V peak-to-peak amplitude, frequency not fixed</li>
    <li>Distance between coils: 0 cm (initially set for optimal reception)</li>
</ul>

<h3>2. Data Collection</h3>
<p>
    To examine the impact of distance between the coils, I measured the amplitude of the voltage across the capacitor in the reader circuit at various distances. I then plotted the voltage amplitude as a function of the distance between the coils.
</p>

<h3>3. Observations</h3>
<p>
    By analyzing the plotted data, I deduced the following information:
</p>
<ul>
  <li>Distance significantly affects the voltage amplitude, as expected.</li>
  <li>At distances of 2 to 3 cm, the amplitude becomes insufficient to transmit complex signals, defining this as our effective distance limit.</li>
</ul>

<h2>Results</h2>
<p>
  The experiment demonstrated a clear relationship between distance and voltage amplitude. As anticipated, increasing the distance between the coils caused a decrease in the amplitude of the voltage measured in the capacitor. Results confirmed that at distances of 2 to 3 cm, the voltage amplitude is inadequate for transmitting complex signals, establishing this range as the effective operational limit for our model. This finding is crucial for future experiments, as it provides a guideline for optimizing the card-reader system’s design and functionality.
</p>
