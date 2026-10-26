import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt

# EMG Signal Processing
# Demonstration using synthetic muscle activity data

SAMPLE_RATE = 1000
DURATION = 10
RANDOM_SEED = 42


def generate_emg():
    rng = np.random.default_rng(RANDOM_SEED)
    time = np.arange(0, DURATION, 1 / SAMPLE_RATE)

    # Simulated muscle contractions
    envelope = np.full(len(time), 0.04)

    for start, end in [(2, 3.5), (5, 6.5), (8, 9)]:
        envelope[(time >= start) & (time < end)] = 0.7

    muscle_signal = envelope * rng.normal(size=len(time))

    # Add power-line interference and baseline noise
    interference = 0.12 * np.sin(2 * np.pi * 60 * time)
    noise = 0.03 * rng.normal(size=len(time))

    return time, muscle_signal + interference + noise


def filter_emg(signal):
    # Bandpass filter: 20-450 Hz
    sos = butter(
        4, [20, 450],
        btype="bandpass",
        fs=SAMPLE_RATE,
        output="sos"
    )
    return sosfiltfilt(sos, signal)


def calculate_rms(signal, window_ms=100):
    window = int(SAMPLE_RATE * window_ms / 1000)
    squared = signal ** 2
    moving_average = np.convolve(
        squared,
        np.ones(window) / window,
        mode="same"
    )
    return np.sqrt(moving_average)


def detect_activation(rms, threshold=0.20):
    return rms > threshold


def main():
    time, raw_emg = generate_emg()

    filtered_emg = filter_emg(raw_emg)
    rms = calculate_rms(filtered_emg)
    activation = detect_activation(rms)

    print("EMG SIGNAL PROCESSING RESULTS")
    print("-----------------------------")
    print(f"Sampling rate: {SAMPLE_RATE} Hz")
    print(f"Duration: {DURATION} seconds")
    print(f"Maximum RMS: {np.max(rms):.4f}")
    print(f"Mean RMS: {np.mean(rms):.4f}")
    print(f"Muscle active: {np.mean(activation)*100:.2f}%")

    fig, axes = plt.subplots(3, 1, figsize=(12, 9),
                            sharex=True)

    axes[0].plot(time, raw_emg, linewidth=0.5)
    axes[0].set_title("Raw Simulated EMG Signal")
    axes[0].set_ylabel("Amplitude")

    axes[1].plot(time, filtered_emg, linewidth=0.5)
    axes[1].set_title("Bandpass Filtered EMG")
    axes[1].set_ylabel("Amplitude")

    axes[2].plot(time, rms, label="RMS Envelope")
    axes[2].axhline(
        0.20, color="red", linestyle="--",
        label="Activation Threshold"
    )
    axes[2].fill_between(
        time, 0, rms, where=activation,
        alpha=0.3, label="Detected Activation"
    )
    axes[2].set_title("Muscle Activation Detection")
    axes[2].set_xlabel("Time (seconds)")
    axes[2].set_ylabel("RMS")
    axes[2].legend()

    plt.tight_layout()
    plt.savefig("emg_results.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
