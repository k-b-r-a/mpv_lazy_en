### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Super deinterlace / anti-interlace

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Deint_Lv = 4
Src_Type = 0
Tff = 0
Cpu = True
Gpu = -1
## <1|2|3|4|5|6|7|8|9|10|11> Quality level
## <0|1|2|3> Source type (when 0 is used for frame doubling), corresponding to interlaced(0) general-progressive(1) badly-deinterlaced(2/3)
## <0|1|2> Field order, corresponding to auto-detection(0) top-field-first(1) bottom-field-first(2)
## <True|False> Whether to use CPU only
## <-1|0|1|2> GPU number used, -1 for automatic, 0 for sorted number one

clip = k7f.DEINT_EX(clip, fps_in=container_fps, obs=True, deint_lv=Deint_Lv, src_type=Src_Type, deint_den=1, tff=Tff, cpu=Cpu, gpu=Gpu)
clip.set_output()
