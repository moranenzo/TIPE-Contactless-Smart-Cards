<h1>Experiment Report: Measured Amplitude Across the Reader Circuit Capacitor as a Function of Frequency</h1>

<h2>Objective of the Experiment</h2>
<p>
  This experiment aimed to determine the optimal frequency for future experiments to observe the strongest physical effect, specifically the resonance frequency of our circuit. Since the message will be transmitted within the variation range of the voltage amplitude across the capacitor, identifying the optimal frequency involves plotting the amplitude as a function of frequency, both with and without resistance in the circuit, and calculating the difference between these amplitudes to locate the maximum.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the Card-Reader Model</h3>
<p>
    We assembled the card and reader circuits.
</p>
<p>
<strong>Parameters Used:</strong>
</p>
<ul>
    <li>Inductance of coils: L1 = L2 = 9 mH</li>
    <li>Capacitance of capacitors: C1 = C2 = 0.22 µF</li>
    <li>Resistance in the card: {0 Ω, 1 kΩ} (no significant effect with higher resistance)</li>
    <li>Follower system (OpAmp)</li>
    <li>Low-Frequency Generator: 1 V peak-to-peak amplitude, variable frequency</li>
    <li>Distance between coils: 0 cm (adjusted for optimal reception)</li>
</ul>

<h3>2. Data Collection</h3>
<p>
    For each frequency, we measured the voltage amplitude across the capacitor with a 0 Ω resistor in the card ("low value" of voltage) and with a 1 kΩ resistor ("high value" of voltage).
</p>

<h3>3. Observations</h3>
<p>
    After plotting and analyzing the data, we noted the following:
</p>
<ul>
  <li>A maximum difference at approximately 3540 Hz</li>
  <li>Two resonance peaks when resistance is added to the card circuit</li>
  <li>A single resonance peak in the circuit without card resistance</li>
</ul>

<h2>Results</h2>
<p>
  The experiment successfully identified the optimal resonance frequency at approximately 3540 Hz. The presence of multiple resonance peaks suggests complex interactions between the circuit components, particularly due to resistance. With added resistance, the system exhibited two resonance peaks, likely caused by damping effects, while without resistance, the circuit behaved as though the card was absent, with only one resonance peak appearing at the reader circuit’s resonance frequency. These findings will guide future experiments by refining signal transmission and optimizing the circuit’s performance at resonance.
</p>
