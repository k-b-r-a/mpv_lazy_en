### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### svpflow frame doubling, moderate resource consumption

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
## Integer, pre-downscale processing source height (fill in your monitor height)
## <0|1> Whether to use only CPU
## <0|11|12|21> The index of the GPU in use, 0 is the first one
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.SVP_LQ(clip, fps_in=container_fps, cpu=Cpu, gpu=Gpu)

clip.set_output()
