### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE (v4+) Frame Interpolation — high performance requirements, DX12 GPU only

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440         # Integer — pre-scaled processing height (e.g. your display’s vertical resolution)
Model = 46           # <46|4251|426|4262> RIFE model index to use
Fps_Num = 2          # Integer — numerator of target frame rate (Fps_Num / Fps_Den)
Fps_Den = 1          # Integer — denominator of target frame rate
Sc_Mode = 1          # <0|1|2> Scene change detection mode; 0 = disabled
Gpu = 0              # Index of GPU to use; 0 = first detected device
Gpu_T = 2            # <1|2|3> Number of threads for GPU backend
Lk_Fmt = False       # <True|False> Lock pixel format to yuv420p8

# Detect framerate
ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)

# Preprocessing: scaling + format handling
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Apply RIFE-based frame interpolation
clip = k7f.RIFE_DML(
    clip,
    model=Model,
    turbo=True,
    fps_in=container_fps,
    fps_num=Fps_Num,
    fps_den=Fps_Den,
    sc_mode=Sc_Mode,
    gpu=Gpu,
    gpu_t=Gpu_T
)

clip.set_output()