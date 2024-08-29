### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE (v4+) Frame Interpolation, High Performance Requirements, NVIDIA Card Only

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440
Lt_D2k = False
Model = 46
Ext_Proc = False
T_Tta = False
Fps_Num = 2
Fps_Den = 1
Sc_Mode = 1
Gpu = 0
Gpu_T = 2
St_Eng = False
Ws_Size = 0
Lk_Fmt = False
## Integer, pre-downscale source height (set to your monitor height)
## <True|False> Frame interpolation for sources above DCI2K resolution
## <46|422|4221> Model to use
## <True|False> Use external padding and cropping processing
## <True|False> Use ensemble version of the model
## Integer, Fps_Num/Fps_Den determines the frame rate multiplier
## Integer
## <0|1|2> Scene change detection mode, 0 to disable
## GPU Index, 0 for the first GPU
## <1|2|3> Number of GPU threads
## <True|False> Use static engine (requires preprocessing for each source resolution); dynamic engine adapts to different resolutions (QVGA→DCI4K)
## Integer, constrain VRAM (MiB), minimum for static engine is 128 (dynamic engine automatically doubles), setting a lower value maximizes utilization
## <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.RIFE_NV(clip, lt_d2k=Lt_D2k, model=Model, ext_proc=Ext_Proc, t_tta=T_Tta, fps_in=container_fps, fps_num=Fps_Num, fps_den=Fps_Den, sc_mode=Sc_Mode, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)

clip.set_output()
