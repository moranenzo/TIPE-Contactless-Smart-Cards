<h1>Experiment Report: Measured Amplitude Across the Reader Circuit Capacitor as a Function of Frequency</h1>

<h2>Objective of the Experiment</h2>
<p>
  The objective of this experiment was to determine the optimal frequency for future experiments to observe the greatest physical phenomenon, i.e. the resonance frequency of our circuit. We know that the message will be conveyed in the gap between the high and low values of the voltage amplitude around the capacitor. Thus, the optimal frequency can be found by plotting the measured amplitude across the capacitor as a function of frequency, both with and without resistance in the circuit, and calculating the difference between the two to identify its maximum.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Building the card-reader model</h3>
<p>
    I assembled the card and reader circuits. 
</p>
<p>
<strong>Parameters used:</strong>
</p>
<ul>
    <li>Inductance of coils: L1 = L2 = 9 mH</li>
    <li>Capacity of capacitors: C1 = C2 = 0.22 µF</li>
    <li>Resistance in the card: {0Ω, 1kΩ} (no significant influence when increasing resistance)</li>
    <li>Follower system (OpAmp)</li>
    <li>Low-Frequency Generator: amplitude of 1 V peak-to-peak, frequency not fixed</li>
    <li>Distance between coils: 0 cm (adjusted for optimal reception)</li>
</ul>

<h3>2. Data Collecting</h3>
<p>
    For each frequency value, I measured the amplitude of the voltage with a 0 Ohm resistor in the card ("low value" of voltage) and a 1 kOhm resistor in the card ("high value" of voltage).
</p>

<h3>3. Observations</h3>
<p>
    By plotting all the values I gathered and analyzing the curves, I deduced the following information:
</p>
<ul>
  <li>A maximum difference around 3540 Hz</li>
  <li>Two resonance peaks in the circuit with resistance in the card</li>
  <li>One resonance peak in the circuit with no resistance in the card</li>
</ul>

<h2>Results</h2>
<p>
  The experiment successfully identified the optimal frequency i.e. the resonance frequency, which was approximately 3540 Hz. The presence of multiple resonance peaks suggests complex interactions between the circuit components, particularly the impact of resistance. With resistance, the system exhibited two resonance peaks, likely due to the added damping effects, while without resistance, the card-reader circuit acted like the card was absent and the only peak observed appeared on the resonnance frequency of the reader circuit. These findings will guide future experiments in refining the signal transmission process and optimizing the circuit's performance at resonance.
</p>
