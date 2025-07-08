### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### BM3D Denoising (NVIDIA GPU only)

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Nr_Lv = [5,0,0]     # Integer list — denoising strength per plane (Y, U, V)
Bs_Ref = 8          # <1–8> — block size for reference patches
Bs_Out = 7          # <1–8> — block size for filtered output (must be ≤ Bs_Ref)
Gpu = 0             # Integer — GPU index (0 = first device)

clip = k7f.BM3D_NV(
    clip,
    nr_lv=Nr_Lv,
    bs_ref=Bs_Ref,
    bs_out=Bs_Out,
    gpu=Gpu
)

clip.set_output()