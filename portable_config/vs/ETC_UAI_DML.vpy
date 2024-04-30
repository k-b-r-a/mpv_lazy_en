### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Using custom AI upscaling model, DX12 GPU only

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720
Model = "Sirosky_AniScale2S_Compact_x2_fp32_op17.onnx"
Gpu = 0
Gpu_T = 2
H_Max = 1440
Lk_Fmt = False
## Integer, pre-downscale processing source height
## Model to use (limited to fp32 models)
## GPU index, 0 for the first GPU
## <1|2|3> Number of GPU threads to use
## Integer, output height limit (fill in your monitor height)
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.UAI_DML(clip, clamp=False, model_pth=Model, gpu=Gpu, gpu_t=Gpu_T)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
