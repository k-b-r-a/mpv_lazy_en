### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Conservative Frame Interpolation Strategy with mvtools, Moderate Resource Consumption

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
## Integer, pre-downscale source height (set to your monitor height)
## Float, target frame rate, the example is approximately 60fps. Special values like display_fps/2 mean the target is half the monitor's refresh rate; setting container_fps*2 means frame doubling (higher frame rates increase energy consumption and produce more artifacts, which is often unnecessary. For example, with a 144Hz monitor, up to 72fps is usually sufficient, and the rest can be compensated with --interpolation frame blending)
## <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_STD(clip, fps_in=container_fps, fps_out=Fps_Out)

clip.set_output()
