### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### BM3D Denoising, NVIDIA GPU Only

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Nr_Lv = [5,0,0]
Bs_Ref = 8
Bs_Out = 7
Gpu = 0
## Integer array, denoising strength for each plane
## <1|2|3|4|5|6|7|8> block_step
## <1|2|3|4|5|6|7|8> Must be less than or equal to Bs_Ref
## GPU index, 0 for the first GPU

clip = k7f.BM3D_NV(clip, nr_lv=Nr_Lv, bs_ref=Bs_Ref, bs_out=Bs_Out, gpu=Gpu)

clip.set_output()
