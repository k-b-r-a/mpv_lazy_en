### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### mvtools frame doubling, moderate overhead

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440
Recal = True
Block = True
Lk_Fmt = False
## Integer, pre-downscale processing source height (fill in your monitor height)
## <True|False> Whether to use second analysis
## <True|False> Whether to use Block mode
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_LQ(clip, fps_in=container_fps, fps_out=container_fps*2, recal=Recal, block=Block)

clip.set_output()
