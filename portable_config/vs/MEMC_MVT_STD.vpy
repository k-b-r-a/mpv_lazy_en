### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### mvtools conservative frame interpolation strategy, moderate consumption.

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440
Fps_Out = 60.0
Lk_Fmt = False
## Integer, pre-downscale processing source height (fill in your monitor height)
## Float, target frame rate, for example, about 60fps. Special values like display_fps/2 mean the target is half the display refresh rate; fill container_fps*2 for frame doubling (higher frame rates increase energy consumption and produce more artifacts, usually unnecessary. For example, for a 144Hz display, at most 72fps interpolation is needed, and the rest can be handled by --interpolation frame mixing compensation)
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_STD(clip, fps_in=container_fps, fps_out=Fps_Out)

clip.set_output()
