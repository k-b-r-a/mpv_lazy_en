### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Real-ESRGAN 放大或降噪，性能要求极高，N卡专用
### RIFE (v4.6) 补帧，性能要求较高，N卡专用

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# RIFE #
############

H_Prer = 1080
Lt_D2kr = False
Modelr = 46
Ext_Procr = True
T_Ttar = False
Fps_Numr = 2
Fps_Denr = 1
Sc_Moder = 1
Gpur = 0
Gpu_Tr = 2
St_Engr = False
Ws_Sizer = 0
Lk_Fmtr = False

############
# MVT #
############

Fps_In = 48
Fps_Out = 149

## Integer, pre-downscale processing source height (fill in your monitor height)
## <True|False> Whether to interpolate sources above DCI2K resolution
## <46|422|4221> Model used
## <True|False> Whether to use external padding and cropping processing
## <True|False> Whether to use the ensemble version of the model
## Integer, the value of Fps_Num/Fps_Den is the frame rate multiplier
## Integer
## <0|1|2> Scene change detection mode, 0 is disabled
## Sequence number of the graphics card used, 0 is the first number in the sequence
## <1|2|3> Number of graphics card threads used
## <True|False> Whether to use static engine (requires preprocessing of sources of different resolutions); dynamic engine adapts to different resolutions (QVGA→DCI4K)
## Integer, constraint video memory (MiB), minimum value for static engine is 128 (dynamic engine automatically doubles), setting a value lower than this maximizes utilization
## <True|False> Lock pixel format to yuv420p8

## Integer, pre-downscale processing source height (fill in your monitor height)
## Float, target frame rate, for example approximately 60fps. Special values such as display_fps/2 means target frame rate is half of the display refresh rate; fill container_fps*2 for double frame rate (higher frame rates consume more resources, produce more artifacts, and are generally unnecessary. For example, for a 144Hz monitor, you only need to interpolate up to 72fps, and leave the rest for frame blending compensation)
## <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Prer, fmt_pix=1 if Lk_Fmtr else 0)
clip = k7f.RIFE_NV_MVT(clip, lt_d2k=Lt_D2kr, model=Modelr, sc_mode=Sc_Moder, fps_num=Fps_Numr,fps_den=Fps_Denr, t_tta=T_Ttar, ext_proc=Ext_Procr, gpu=Gpur, gpu_t=Gpu_Tr, st_eng=St_Engr, ws_size=Ws_Sizer,fps_in = Fps_In, fps_out=Fps_Out)

clip.set_output()