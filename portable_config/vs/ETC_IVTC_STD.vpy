### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Convert pseudo 25 or 30 fps source to 24 fps

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Ivtc_M = 1
## <1|2> ivtc mode

clip = k7f.IVTC_STD(clip, fps_in=container_fps, ivtc_m=Ivtc_M)

clip.set_output()
