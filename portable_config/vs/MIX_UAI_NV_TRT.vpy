### Use Custom AI Upscaling Model — RTX/NVIDIA GPU with TensorRT Required
### Docs: https://github.com/hooke007/MPV_lazy/discussions/329
### Parameters: https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc#uai_nv_trt

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720           # Integer — downscale input resolution before processing
Model = "the_database_AnimeJaNaiV2L1_x2_fp16_op17.onnx"  # Model filename (must be in .../mpv-lazy/vs-plugins/models/)
Fp16_Qnt = True        # <True|False> — Use FP16 quantization for FP32 models
Gpu = 0                # Integer — GPU index; 0 = first GPU
Gpu_T = 2              # <1|2|3> — Number of GPU threads used
St_Eng = False         # <True|False> — Use static engine; otherwise use dynamic engine
Res_Opt = [1280, 720]  # Resolution used to optimize dynamic engine (height must not exceed H_Pre)
Res_Max = [1920, 1200] # Maximum supported resolution for dynamic engine
Ws_Size = 0            # Integer 0–1024 — VRAM constraint (in MiB); minimum 128. Values below 128 disable limits
H_Max = 1440           # Integer — limit output resolution (e.g. your display height)
Lk_Fmt = False         # <True|False> — Lock pixel format to yuv420p8

# Step 1: Resolution pre-check
ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)

# Step 2: Pre-processing scale and pixel format
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Step 3: Apply AI upscaling with UAI_NV_TRT (TensorRT backend)
clip = k7f.UAI_NV_TRT(
    clip,
    clamp=False,
    model_pth=Model,
    opt_lv=3,
    cuda_opt=[0, 0, 0],
    int8_qnt=False,
    fp16_qnt=Fp16_Qnt,
    gpu=Gpu,
    gpu_t=Gpu_T,
    st_eng=St_Eng,
    res_opt=Res_Opt,
    res_max=Res_Max,
    ws_size=Ws_Size
)

# Step 4: Final formatting and resolution cap
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()