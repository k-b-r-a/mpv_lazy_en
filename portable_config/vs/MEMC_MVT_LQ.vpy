### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### mvtools Frame Doubling, General Usage

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
## Integer, pre-downscale source height (set to your monitor height)
## <True|False> Use Recalculation (second analysis)
## <True|False> Use Block Mode
## <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_LQ(clip, fps_in=container_fps, fps_out=container_fps*2, recal=Recal, block=Block)

clip.set_output()
