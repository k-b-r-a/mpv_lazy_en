### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### SVPFlow Frame Interpolation, Moderate Consumption

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440
Cpu = 0
Gpu = 0
Lk_Fmt = False
## Integer, pre-downscale source height (set to your monitor height)
## <0|1> Use CPU only
## <0|11|12|21> GPU index, 0 for the first GPU
## <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.SVP_LQ(clip, fps_in=container_fps, cpu=Cpu, gpu=Gpu)

clip.set_output()
