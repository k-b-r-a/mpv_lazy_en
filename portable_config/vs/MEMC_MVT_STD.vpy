### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Conservative mvtools-based frame interpolation — medium performance impact

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440         # Integer — pre-scale height for processing (e.g. your display height)
Fps_Out = 60.0       # Float — target output frame rate. Example: ~60fps. 
                     # Special cases: display_fps/2 = half of your monitor refresh rate;
                     # container_fps*2 = double the source rate.
                     # Higher FPS = more artifacts and CPU/GPU usage — often unnecessary.
                     # For a 144Hz monitor, 72fps is sufficient; remaining frames can be handled via --interpolation blending
Lk_Fmt = False       # <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_STD(clip, fps_in=container_fps, fps_out=Fps_Out)

clip.set_output()