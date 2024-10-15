<h1>Experiment Report: Communication Between Two Arduinos</h1>

<h2>Objective of the Experiment</h2>
<p>
  The objective of this experiment was to set up communication between two Arduinos to test our sending and reception scripts. After the first one sent a pulse (message sent: "MP"), the other one could receive the voltage and converted it into a binary list (binary message).
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Launching of the codes at the same time</h3>
<p>
    We first tried to launch the both sending and reception codes simultaneously. However, the initial results showed failure: the first bits were not captured by the system. My hypothesis is that it is due to a latency issue stemming from Python code verification and communication between Arduino and Python.
</p>

<h3>2. Latency Measurement</h3>
<p>
    We attempted to measure this latency to synchronize the start of both systems. Still, the results were inconclusive, with the number of bits not captured varying between trials.
</p>

<h3>3. Detection System Improvement</h3>
<p>
    A method to detect the start of the message was implemented. The binary message was preceded by a '1' that symbolized the beginning of the transmission. This allowed us to initiate the detection process well before launching the message. The system would detect only '0's until it received the signal (i.e., the '1' preceding the binary message).
</p>

<h2>Results</h2>
<p>
  This idea worked, and the code was successfully transmitted. We got enough time to complete the transmission by adding a code to convert the binary back into a readable message. The word 'MP' sent by the first Arduino was successfully received by the second using the system.
</p>
