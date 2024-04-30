### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Using custom AI upscaling model, NVIDIA GPU only

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720
Model = "Sirosky_AniScale2S_Compact_x2_fp16_op17.onnx"
Gpu = 0
Gpu_T = 2
Res_Opt = [1280, 720]
Res_Max = [1920, 1200]
Ws_Size = 0
H_Max = 1440
Lk_Fmt = False
## Integer, pre-downscale processing source height
## Model to use
## GPU index, 0 for the first GPU
## <1|2|3> Number of GPU threads to use
## Optimized source resolution (height not greater than H_Pre)
## Maximum supported source resolution
## <0~1024> Integer, constraint VRAM (MiB), minimum value is 128, set to a value lower than this to remove the limit
## Integer, output height limit (fill in your monitor height)
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.UAI_NV_TRT(clip, clamp=False, model_pth=Model, opt_lv=3, cuda_opt=[0, 0, 0], fp16=True, gpu=Gpu, gpu_t=Gpu_T, st_eng=False, res_opt=Res_Opt, res_max=Res_Max, ws_size=Ws_Size)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
