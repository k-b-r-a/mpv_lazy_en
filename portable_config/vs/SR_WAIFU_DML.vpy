### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### waifu2x Upscaling or Denoising, Extremely High Performance Requirement, DX12 GPUs Only

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720
Lt_Hd = False
Model = 3
Nr_Lv = 2
Gpu = 0
Gpu_T = 2
H_Max = 1440
Lk_Fmt = False
## Integer, pre-scale processing source height
## <True|False> Whether to process sources exceeding HD resolution (720P)
## <3|5|6> Model to use
## <-1|0|1|2|3> Denoising level, -1 for no denoising
## GPU index, 0 for the first GPU
## <1|2|3> Number of GPU threads to use
## Integer, output height limit (fill in your display height)
## <True|False> Whether to lock pixel format to yuv420p8

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.WAIFU_DML(clip, lt_hd=Lt_Hd, model=Model, nr_lv=Nr_Lv, gpu=Gpu, gpu_t=Gpu_T)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
