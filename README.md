# audio_denoise
Input MFCC spectogram to UNET to denoise the audio 
# Tasks:
1. Understand sound signal and differences between image and sound input: COmpleted 
2. Audio processing basics: Sampling, Quantization, Fourier Transform, STFT, MFCC : Complete
3. STFT vs MFCC : Complete
   PCM -> Window -> STFT -> Power spectrum -> Mel bands -> Log -> DCT -> MFCC
   
   3a spectograms are NOT spatially invariant: check use with UNET
4. Kinds of noise : COmplete
5. Denoising approaches : WIP 80 % 
6. UNET architecture: Completed
   6a. Spectogram/COmplex number input for UNET : study ongoing 
   6b. Phase infprmation from audio : needed or not important for required application

7. Open source project has similar approach to our proposed approach: Spectrogram – UNET – Inverse Spectrogram
   a.	Differences : music dataset 
   b.	Differences: they use STFT as input 
   c.	Differences: Three layer UNET
8.	Reproduced open source results for stft as input
9.	Created dataset of 10 audio samples by adding white noise & “car passing by” noise. Used a few samples  from Audio Set as saved on the server.
10.	Implement MFCC (DCT, spectogram), UNET, and inverse MFCC: Open source and MFCC completed, Generated dataset and results with MFCC and Mel spectrogram
11.	Analyse UNET architecture from Verisilicon : Added to the ongoing setup with original UNET
12.	Retrain using new dataset : ongoing
13.	Alternatives:
    13a. Alternative 3: A U-Net Based System for Environmental Sound Generation and Enhancement : Study ongoing
    13b. Alternative 1: Wave Unet: accurate phase , temporal features : Open source on music: Reproduced, setup complete
    13c. Alternative 2: Phase aware speech enhancement : Implementation ongoing https://github.com/pheepa/DCUnet
14. Get open source noise samples with different spectral makeup : 
   a.	Noisy speech database for training speech enhancement algorithmshttps://datashare.ed.ac.uk/handle/10283/2791
15. Additions for denoising that can be made lightweight:
   10a. Compressed sensing loss
   10b.  Shuffle Attention mechanism https://www.mdpi.com/2076-3417/12/9/4161
   10c. Robust Principal Component Analysis (RPCA) 
16. Evaluation metric understanding and implementation
17. Evaluation

# Observations
1.	Results from using STFT are the better than others but performance drops for low SNR. MFCC show promise in noise removal but not in recovery of the signal. Melspectogram results show promise in recovery of the signal. 
2.	MFCC is not invertible like the STFT. There is loss of information while generating the MFCCs. Tasks such as audio feature extraction, classification, recognition don’t require us to regenerate the waveform from the spectrogram. However, denoising needs recovery of the signal. 
3.	White noise contains energy across all frequencies while MFCCs are designed to capture spectral envelope of speech signals and may not capture the features that facilitates denoising. Especially if SNR is low
4.	Audio data is not spatially invariant, but convolution networks are designed for images which are spatially invariant (a face would be a face anywhere in the image space but a shape has different implications when shifted along frequency axis)
5.	MFCC doesn’t capture phase. May affect the results. Studied Phase aware denoising : https://openreview.net/pdf?id=SkeRTsAcYm

# Plan and proposals
Here are some tasks planned based on the above observations:
1.	Decide input features: Mel spectrogram/MFCC/STFT combined with others. Literature study references:
   •	Study modifications to MFCC in literature for other audio tasks: Ongoing 
   •	Study Ref: https://link.springer.com/article/10.1007/s43926-023-00049-y
   •	Study Ref: https://www.mdpi.com/2076-3417/12/23/12151#:~:text=Mel%2DScale%20Frequency%20Cepstral%20Coefficients%20(MFCC),responds%20differently%20at%20different%20frequencies. 
   •	Study Ref: https://github.com/eloimoliner/denoising-historical-recordings/blob/master/README.md
   •	Study Ref: https://github.com/pheepa/DCUnet/blob/master/README.md
2. Decide network: Use simpler/modifiable 2 layer UNET (as provided by verisilicon) to generate results and compare them.
•	Network for spatially variant audio input: Use vertical filter kernels covering the frequency axis, Use dilated kernels capturing wider input image space.
3.	Decide dataset/ type of noise and signal: Gather and study more datasets or add real-life audio sounds as noise.
•	Noisy speech database for training speech enhancement algorithmshttps://datashare.ed.ac.uk/handle/10283/2791
•	Check if the resulting model shows difference in performance for singular audio events with different spectral makeup or a persistent background noise (like AWGN)
4.	Alternative / Modified approach: Phase-aware features or network modification
5.	Alternative approach : Wave UNET: takes time series input: 
•	Completed: reproduced official results, 
•	TODO: check on white noise added signals and Real Life noise audio 

>> Proposal 1: DO we need to reduce the dimensionality of Log Mel Bands using DCT? DCT is used to reduce the dimensionality 
>> Proposal 1a: If necessary evaluate DCT vs RPCA to reduce dimensionality - partial work done in paper
>> Proposal 2: How important is phase of the input sound, will the noise in the application cause a phasal distortion? MFCC not prefered for preserving or predicting phase
>> Proposal 3: 
