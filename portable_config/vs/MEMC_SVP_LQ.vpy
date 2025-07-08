### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### SVPflow frame interpolation — medium resource usage

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440       # Integer — pre-scale input height (set to your monitor’s vertical resolution)
Cpu = 0            # <0|1> — whether to use CPU only
Gpu = 0            # <0|11|12|21> — GPU index (0 = first GPU)
Lk_Fmt = False     # <True|False> — lock pixel format to yuv420p8

# Detect input framerate
ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)

# Preprocess scaling and pixel format
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Apply low-complexity SVPflow-based frame interpolation
clip = k7f.SVP_LQ(clip, fps_in=container_fps, cpu=Cpu, gpu=Gpu)

clip.set_output()