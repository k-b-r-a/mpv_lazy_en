### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### waifu2x upscaling or denoising, extremely high performance requirements, N-card only

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
St_Eng = False
Ws_Size = 0
H_Max = 1440
Lk_Fmt = False
## Integer, pre-reduce processing source height
## <True|False> Whether to process sources exceeding HD resolution (720P)
## <3|5|6> Model used
## <-1|0|1|2|3> Denoising level, -1 for no denoising
## GPU number used, 0 is sorted as number one
## <1|2|3> Number of GPU threads used
## <True|False> Whether to use static engine (requires pre-processing of sources of different resolutions); dynamic engine adapts to different resolutions (64²→DCI2K)
## <0~1024> Integer, restrict VRAM (MiB), minimum value for static engine is 128 (dynamic engine automatically doubles), set to a value lower than this to be unlimited
## Integer, output height limit (fill in your monitor height)
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.WAIFU_NV(clip, lt_hd=Lt_Hd, model=Model, nr_lv=Nr_Lv, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
