### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE (v4+) Frame Interpolation — NVIDIA GPU required, high performance demand

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 1080          # Integer — pre-scaled input height (set to your display’s height)
Model = 46            # <46|4251|426|4262> — model ID used by RIFE
Fps_Num = 2           # Integer — numerator of output FPS (frame multiplier)
Fps_Den = 1           # Integer — denominator of output FPS
Sc_Mode = 1           # <0|1|2> — scene change detection mode; 0 = off
Gpu = 0               # Integer — GPU index; 0 = first listed device
Gpu_T = 2             # <1|2|3> — number of GPU threads
Ws_Size = 0           # Integer — manually constrain GPU memory during engine build (MiB); minimum 128; use 0 or below to maximize usage
Lk_Fmt = False        # <True|False> — lock pixel format to yuv420p8

############
# MVT #
############

Fps_In = 48
Fps_Out = 149       # Float — target output frame rate. Example: ~60fps. 
                     # Special cases: display_fps/2 = half of your monitor refresh rate;
                     # container_fps*2 = double the source rate.
                     # Higher FPS = more artifacts and CPU/GPU usage — often unnecessary.
                     # For a 144Hz monitor, 72fps is sufficient; remaining frames can be handled via --interpolation blending

# Determine input framerate
ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)

# Optionally resize and constrain pixel format
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Apply NVIDIA-tuned RIFE frame interpolation
clip = k7f.RIFE_NV(
    clip,
    model=Model,
    int8_qnt=False,
    turbo=True,
    fps_in=container_fps,
    fps_num=Fps_Num,
    fps_den=Fps_Den,
    sc_mode=Sc_Mode,
    gpu=Gpu,
    gpu_t=Gpu_T,
    ws_size=Ws_Size,
)
clip = k7f.MVT_STD(clip, fps_in=Fps_In, fps_out=Fps_Out)

clip.set_output()

