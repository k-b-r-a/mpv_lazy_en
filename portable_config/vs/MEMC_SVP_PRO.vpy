### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Simplified Variant Based on the "Blackmagic" Method

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1440         # Integer — pre-scale processing height (e.g., your display resolution)
Fps_Num = 60000      # Integer — numerator for output framerate or multiplier
Fps_Den = 1001       # Integer — denominator for output framerate or multiplier
Abs = True           # <True|False> — True = specify absolute FPS, False = specify multiplier
Nvof = False         # <True|False> — enable NVIDIA Optical Flow
Gpu = 0              # <0|11|12|21> — GPU device index; 0 = first detected
Lk_Fmt = False       # <True|False> — lock pixel format to yuv420p8

# Step 1: Read FPS
ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)

# Step 2: Format and resolution preprocessing
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Step 3: Apply SVP_PRO interpolation
clip = k7f.SVP_PRO(
    clip,
    fps_in=container_fps,
    fps_num=Fps_Num,
    fps_den=Fps_Den,
    abs=Abs,
    nvof=Nvof,
    gpu=Gpu
)

clip.set_output()