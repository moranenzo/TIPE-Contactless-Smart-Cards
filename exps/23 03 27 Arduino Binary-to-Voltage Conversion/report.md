<h1>Experiment Report: Basic Code and Arduino Binary-to-Voltage Conversion</h1>

<h2>Objective of the Experiment</h2>
<p>
  This experiment aimed to develop a script to transmit a message by converting a binary sequence into voltage variations. The focus was on troubleshooting challenges with the C++ code and Arduino hardware integration.
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Initial Coding Challenges</h3>
<p>
    We encountered initial issues with the code, as we could not test it without an Arduino on hand. After debugging multiple errors, we managed to get the code functioning correctly. Upon successful testing, the LED responded as expected, turning on and off based on the binary sequence.
</p>
<p>
  <strong>Note:</strong> The LED briefly lights up when the code is uploaded to the board.
</p>

<h3>2. Arduino Code for Binary-to-Voltage Conversion</h3>
<h4>2.1 Code Execution and Testing</h4>
<ul>
  <li>We sent the binary message from the Arduino Serial Monitor</li>
  <li>We connected an oscilloscope to verify voltage output from the Arduino</li>
  <li>Successful test example observed: see result (1)</li>
</ul>
<p>
  <strong>Note:</strong> Voltage spikes were noticed when the code was uploaded to the board.
</p>

<h4>2.2 Issue Identification</h4>
<p>
  We observed two distinct sets of voltage spikes: one during the initial reception of the uploaded code on the Arduino board and another set when the upload was completed.
</p>
<p>
  This behavior is illustrated in results (2) and (3).
</p>

<h3>3. Message Transmission Test from Python</h3>
<p>
    Our attempt to send the message via Python was unsuccessful. Due to time constraints, we opted to continue with message transmission through the Arduino Console, as it did not significantly impact the experiment.
</p>

<h3>Observation Details</h3>
<p>
  Below are notes to interpret the oscilloscope results:
</p>
<ul>
  <li><strong>(1)</strong> Outcome of the command 11001100001111</li>
  <li><strong>(2)</strong> Spike packets observed before the actual signal</li>
  <li><strong>(3)</strong> Close-up of the spike packets</li>
</ul>

<h2>Results</h2>
<p>
  The experiment confirmed that binary messages could be converted into voltage variations via Arduino. Oscilloscope tests validated the expected voltage spikes during message transmission. Although our Python-based transmission attempt did not succeed, using the Arduino Serial Monitor produced the desired outcomes. The LED’s behavior validated the accuracy of the binary-to-voltage conversion, overcoming the initial coding and hardware synchronization challenges. Overall, the experiment achieved its goal successfully.
</p>
