# Connection to Senior Design Project
This project was developed as an exploratory software component related to my Senior Design project, Adaptive Wearable Electrode and Sensor Interface for Post-Stroke Rehabilitation, at Marian University.
Our Senior Design project focuses on developing a wearable interface that supports adaptable electrode placement for muscle monitoring and electrical stimulation applications. As we work toward developing and testing a physical prototype, I wanted to explore how EMG signals could be processed and analyzed using Python.
Since we are still in the early stages of prototype development, this program uses synthetic EMG signals with simulated muscle contractions, electrical interference, and noise. These generated values allow me to experiment with different signal-processing techniques, including bandpass filtering, RMS calculations, and muscle activation detection.

The purpose of this initial implementation is to:
- Explore different approaches to processing EMG signals before collecting physical measurements.
- Understand how noise and filtering affect signal interpretation.
- Experiment with muscle activation thresholds using simulated data.
- Develop a preliminary software workflow that could later be adapted to process measurements collected from our wearable prototype.
- Identify potential software requirements and limitations before integrating physical sensors.

# Future Prototype Integration
Once the physical prototype is developed and appropriate EMG measurement hardware is available, I hope to adapt this code to analyze actual muscle activity measurements.
Future testing could involve comparing signals collected under different electrode placements, evaluating signal quality during movement, and determining whether the processing pipeline can reliably identify muscle activation.

Current Status: Preliminary software exploration using synthetic data. No human EMG measurements or physical prototype validation have been performed through this program.

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
