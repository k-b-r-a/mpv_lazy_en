### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE v4+ frame interpolation — very high performance demand

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440         # Integer — pre-scaled input height (e.g. your display resolution)
Model = 23           # <23|70|72|73> — RIFE model version
T_Tta = False        # <True|False> — whether to use the ensemble (multi-view) model variant
Fps_Num = 2          # Integer — numerator of output framerate (frame multiplier)
Fps_Den = 1          # Integer — denominator of output framerate
Sc_Mode = 1          # <0|1|2> — scene change detection mode; 0 = disabled
Skip = True          # <True|False> — skip interpolation for static frames
Stat_Th = 60.0       # Float — threshold value to classify frames as static
Gpu = 0              # Integer — GPU index; 0 = first in list
Gpu_T = 2            # <1|2|3> — number of GPU threads
Lk_Fmt = False       # <True|False> — lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.RIFE_STD(
    clip,
    model=Model,
    t_tta=T_Tta,
    fps_num=Fps_Num,
    fps_den=Fps_Den,
    sc_mode=Sc_Mode,
    skip=Skip,
    stat_th=Stat_Th,
    gpu=Gpu,
    gpu_t=Gpu_T
)

clip.set_output()