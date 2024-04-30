### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Reduce chroma noise, moderate cost

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

Nr_Lv = 30.0
## Float, chroma noise threshold, higher values result in more pronounced denoising (heavier smearing)

clip = k7f.CCD_STD(clip, nr_lv=Nr_Lv)

clip.set_output()
