# emg-signal-processing
# EMG Signal Processing & Muscle Activation Detection

A Python-based signal processing project exploring
electromyography (EMG) signals for wearable rehabilitation
and human-machine interface applications.

## Project Overview

Electromyography measures the electrical activity produced
by skeletal muscles. EMG signal analysis can support
applications including rehabilitation, prosthetics,
and wearable sensor systems.

This project demonstrates a signal processing pipeline
using synthetic EMG data.

## Features

- Synthetic EMG signal generation
- Simulated muscle contractions
- Power-line interference and noise simulation
- Butterworth bandpass filtering (20-450 Hz)
- Root Mean Square (RMS) signal analysis
- Muscle activation detection using thresholds
- Signal visualization using Matplotlib

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib
- Digital Signal Processing

## Signal Processing Pipeline

1. Generate synthetic EMG data at 1000 Hz.
2. Simulate muscle contractions at different intervals.
3. Add electrical interference and random noise.
4. Apply a Butterworth bandpass filter.
5. Calculate a moving RMS envelope.
6. Detect activation using an amplitude threshold.
7. Visualize raw, filtered, and processed signals.

## Running the Project

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python main.py
```

The program generates three plots and saves them as
`emg_results.png`.

## Applications

This project explores concepts relevant to:

- Wearable biosignal monitoring
- Post-stroke rehabilitation research
- Muscle activation detection
- Biomedical signal processing
- Human-machine interfaces

## Limitations

This project uses simulated signals rather than
measurements collected from human participants.

The activation threshold is illustrative and would
require calibration and validation for real-world use.

## Future Improvements

- Integrate real EMG sensor data
- Compare different filtering techniques
- Evaluate activation detection accuracy
- Explore real-time signal processing
- Investigate electrode placement effects
