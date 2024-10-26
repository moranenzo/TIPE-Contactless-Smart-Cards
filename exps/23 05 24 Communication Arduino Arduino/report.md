<h1>Experiment Report: Communication Between Two Arduinos</h1>

<h2>Objective of the Experiment</h2>
<p>
  The objective of this experiment was to establish communication between two Arduinos in order to test our transmission and reception scripts. The first Arduino would send a pulse (message: "MP"), and the second would receive the voltage signal, converting it into a binary list (binary message).
</p>

<h2>Steps of the Experiment</h2>

<h3>1. Simultaneous Code Launch</h3>
<p>
    We initially attempted to run both the transmission and reception codes at the same time. However, the first trials were unsuccessful: the system did not capture the initial bits. We hypothesized that this issue stemmed from latency due to Python code verification and communication delays between Arduino and Python.
</p>

<h3>2. Latency Measurement</h3>
<p>
    To address the timing issues, we attempted to measure the latency to synchronize both systems at launch. Unfortunately, results were inconsistent, as the number of bits missed varied across different trials.
</p>

<h3>3. Detection System Enhancement</h3>
<p>
    To improve detection, we added a method to identify the start of the message. A ‘1’ bit was added at the beginning of the binary message to signify the start of transmission. This allowed us to initiate detection before launching the main message, with the system ignoring any preceding ‘0’s until the ‘1’ was received, signaling the start of the message.
</p>

<h2>Results</h2>
<p>
  This approach proved effective, and the binary message was successfully transmitted. The reception process had ample time to capture the entire message, and we implemented a code to decode the binary sequence back into a readable message. As a result, the word "MP" sent by the first Arduino was accurately received by the second, confirming successful communication between the devices.
</p>
