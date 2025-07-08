### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### ArtCNN Upscaling — Very High Performance Required (NVIDIA GPU)

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720           # Integer — downscale input for preprocessing (suggest using your display height)
Lt_Hd = True          # <True|False> — whether to process sources above HD resolution (720p)
Model = 8             # <6|7|8> — model index to use
Gpu = 0               # GPU index; 0 = first detected GPU
Gpu_T = 2             # <1|2|3> — number of GPU threads
St_Eng = False        # <True|False> — use static engine (requires separate preprocessing per resolution); dynamic engine adapts automatically from 64² to DCI 2K
Ws_Size = 0           # Integer (0–1024 MiB) — constrain GPU memory; for static engine min = 128, for dynamic it auto doubles; values below threshold = no limit
H_Max = 1440          # Integer — max output height (recommend your display height)
Lk_Fmt = False        # <True|False> — lock output to yuv420p8 format

ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.ARTCNN_NV(
    clip,
    lt_hd=Lt_Hd,
    model=Model,
    gpu=Gpu,
    gpu_t=Gpu_T,
    st_eng=St_Eng,
    ws_size=Ws_Size
)
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()