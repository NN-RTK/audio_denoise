import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
FIG_SIZE = (8,6)

file = "/home/ruchi/work/models/Audio-Denoiser-CNN/Final_Output/Noisy_Audio_Sample_Roshan.wav"
# load audio file with Librosa
signal, sample_rate = librosa.load(file, sr=22050)

# FFT -> power spectrum
# perform Fourier transform
fft = np.fft.fft(signal)

# calculate abs values on complex numbers to get magnitude
spectrum = np.abs(fft)

# create frequency variable
f = np.linspace(0, sample_rate, len(spectrum))

# take half of the spectrum and frequency
left_spectrum = spectrum[:int(len(spectrum)/2)]
left_f = f[:int(len(spectrum)/2)]

# STFT -> spectrogram
hop_length = 512 # in num. of samples
n_fft = 2048 # window in num. of samples

# calculate duration hop length and window in seconds
hop_length_duration = float(hop_length)/sample_rate
n_fft_duration = float(n_fft)/sample_rate

print("STFT hop length duration is: {}s".format(hop_length_duration))
print("STFT window duration is: {}s".format(n_fft_duration))

# perform stft
stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)
print("STFT performed")
# calculate abs values on complex numbers to get magnitude
spectrogram = np.abs(stft)

# apply logarithm to cast amplitude to Decibels
log_spectrogram = librosa.amplitude_to_db(spectrogram)
print("Log STFT")

# MFCCs
# extract 13 MFCCs
MFCCs = librosa.feature.mfcc(y=signal, sr=sample_rate, n_fft=n_fft, hop_length=hop_length, n_mfcc=256)
print("MFCC calculated")
# inverse MFCC
y_output = librosa.feature.inverse.mfcc_to_audio(MFCCs, sr=sample_rate, n_fft=n_fft, hop_length=hop_length)
print("inverse MFCC")
# perform stft
stft_output = librosa.stft(y_output, n_fft=n_fft, hop_length=hop_length)
spectrogram_output = np.abs(stft_output)
log_spectrogram_output = librosa.amplitude_to_db(spectrogram_output)

# input WAVEFORM
# display waveform
plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(y=signal, sr=sample_rate, alpha=0.4, color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Input Waveform")
#plt.show()
plt.savefig("Input_Waveform.jpg")

# plot spectrum
plt.figure(figsize=FIG_SIZE)
plt.plot(left_f, left_spectrum, alpha=0.4)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
#plt.show()
plt.savefig("Power_spec.jpg")

# display spectrogram
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(spectrogram, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
plt.title("Spectrogram")
#plt.show()
plt.savefig("STFTSpectrogram.jpg")

plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(log_spectrogram, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram (dB)")
#plt.show()
plt.savefig("LogSpectrogramdB.jpg")


# display MFCCs
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(MFCCs, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC coefficients")
plt.colorbar()
plt.title("MFCCs")
#plt.show()
plt.savefig("MFCC13.jpg")

# output WAVEFORM
plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(y=y_output, sr=sample_rate, alpha=0.4, color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Out Waveform")
#plt.show()
plt.savefig("Output_Waveform.jpg")

# display spectrogram
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(spectrogram_output, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
plt.title("Spectrogram output")
#plt.show()
plt.savefig("STFTSpectrogram_output.jpg")

plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(log_spectrogram_output, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram_output (dB)")
#plt.show()
plt.savefig("LogSpectrogramdB_output.jpg")