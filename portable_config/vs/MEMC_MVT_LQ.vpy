### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### mvtools-based frame doubling with moderate resource usage

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440          # Integer — pre-scaled source height (e.g. your display’s vertical resolution)
Recal = True          # <True|False> — whether to use second-pass motion estimation (re-analysis)
Block = True          # <True|False> — whether to use block-based estimation
Lk_Fmt = False        # <True|False> — lock pixel format to yuv420p8

# Determine source framerate (returns container_fps)
ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)

# Preprocessing: scale clip and optionally change pixel format
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Apply low-complexity motion interpolation (double framerate)
clip = k7f.MVT_LQ(clip, fps_in=container_fps, fps_out=container_fps*2, recal=Recal, block=Block)

clip.set_output()