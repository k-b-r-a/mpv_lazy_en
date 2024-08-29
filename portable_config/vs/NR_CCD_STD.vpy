### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Reduce Color Noise, Moderate Consumption

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Nr_Lv = 30.0
## Float, color noise threshold; higher values increase denoising effect (more smearing)

clip = k7f.CCD_STD(clip, nr_lv=Nr_Lv)

clip.set_output()
