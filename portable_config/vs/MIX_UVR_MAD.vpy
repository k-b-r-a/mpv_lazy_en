### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### NGU Test

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Ngu = 4             # <0|1|2|3|4> Disable / AA / Soft / Standard / Sharp
Ngu_Q = 2           # <1|2|3|4> NGU quality level: low, medium, high, very high
Rca_Lv = 0          # <0–14> RCA enhancement strength level
Rca_Q = 2           # <1|2|3|4> RCA quality: low, medium, high, very high

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.UVR_MAD(clip, ngu=Ngu, ngu_q=Ngu_Q, rca_lv=Rca_Lv, rca_q=Rca_Q)

clip.set_output()