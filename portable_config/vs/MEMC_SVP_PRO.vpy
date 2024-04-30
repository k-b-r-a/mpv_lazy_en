### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Modification based on the Black Mickey scheme

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1080
Fps_Num = 60000
Fps_Den = 1001
Abs = True
Nvof = True
Gpu = 0
Lk_Fmt = False
## Integer, pre-downscale processing source height (fill in your monitor height)
## Integer, the result of Fps_Num/Fps_Den calculation, which is the final frame rate or multiple
## Integer
## <True|False> Output frame rate (True) or multiple (False)
## <True|False> Whether to enable Optical Flow (Nvidia only)
## <0|11|12|21> The sequence number of the graphics card used, 0 is the first number in the sequence
## <True|False> Whether to lock the pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.SVP_PRO(clip, fps_in=container_fps, fps_num=Fps_Num, fps_den=Fps_Den, abs=Abs, nvof=Nvof, gpu=0)

clip.set_output()
