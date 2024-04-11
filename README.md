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
7. Alternatives:
   7a. Alternative 2: A U-Net Based System for Environmental Sound Generation and Enhancement : Study ongoing
   7b. Alternative 1: Wave Unet: accurate phase , temporal features : Open source on music: reproduced 
8. Implement MFCC (DCT, spectogram), UNET, and inverse MFCC: Open source and MFCC completed but need to combine
9. Dataset study : Generate samples with added white gaussian noise : 10 done
10. Additions for denoising that can be made lightweight:
   10a. Compressed sensing loss
   10b.  Shuffle Attention mechanism https://www.mdpi.com/2076-3417/12/9/4161
   10c. Robust Principal Component Analysis (RPCA) 
11. Evaluation metric understanding and implementation
12. Evaluation

# Proposal 1: DO we need to reduce the dimensionality of Log Mel Bands using DCT? DCT is used to reduce the dimensionality 
# Proposal 1a: If necessary evaluate DCT vs RPCA to reduce dimensionality - partial work done in paper
# Proposal 2: How important is phase of the input sound, will the noise in the application cause a phasal distortion? MFCC not prefered for preserving or predicting phase
# Proposal 3: 
