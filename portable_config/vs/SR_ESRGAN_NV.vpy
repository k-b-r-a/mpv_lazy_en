### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Real-ESRGAN Upscaling or Denoising, extremely high performance requirements, Nvidia card exclusive

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720
Lt_Hd = False
Model = 5005
Gpu = 0
Gpu_T = 2
St_Eng = False
Ws_Size = 0
H_Max = 1440
Lk_Fmt = False
## Integer, pre-downscale processing source height
## <True|False> Whether to process sources above HD resolution (720P)
## <0|2|5005|5006|5007> Model used
## Sequence number of the graphics card used, 0 is the first number in the sequence
## <1|2|3> Number of graphics card threads used
## <True|False> Whether to use static engine (requires preprocessing of sources of different resolutions); dynamic engine adapts to different resolutions (64²→DCI2K)
## <0~1024> Constraint video memory (MiB), minimum value for static engine is 128 (dynamic engine automatically doubles), setting a value lower than this means no restriction
## Integer, output height limit (fill in your monitor height)
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.ESRGAN_NV(clip, lt_hd=Lt_Hd, model=Model, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
