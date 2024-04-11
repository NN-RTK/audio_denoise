# audio_denoise
Input MFCC spectogram to UNET to denoise the audio 
# Tasks:
1. Understand sound signal and differences between image and sound input: COmpleted 
2. Audio processing basics: Sampling, Quantization, Fourier Transform, STFT, MFCC : Complete
3. STFT vs MFCC : Complete:
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
12. Evaluation metric understanding and implementation
13. Evaluation
