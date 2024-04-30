### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### waifu2x upscaling or denoising, extremely high performance requirements, only supports DX12 GPUs

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
## Integer, pre-reduce processing source height
## <True|False> Whether to process sources exceeding HD resolution (720P)
## <3|5|6> Model used
## <-1|0|1|2|3> Denoising level, -1 for no denoising
## GPU number used, 0 is sorted as number one
## <1|2|3> Number of GPU threads used
## Integer, output height limit (fill in your monitor height)
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.WAIFU_DML(clip, lt_hd=Lt_Hd, model=Model, nr_lv=Nr_Lv, gpu=Gpu, gpu_t=Gpu_T)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
