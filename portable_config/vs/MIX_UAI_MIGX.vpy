### Use Custom AI Upscaling Model — RDNA GPU Required
### Docs: https://github.com/hooke007/MPV_lazy/discussions/329
### Parameters: https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc#uai_migx

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720           # Integer — reduce source resolution prior to processing
Model = "the_database_AnimeJaNaiV2L1_x2_fp32_op17.onnx"  # Model filename (located in .../mpv-lazy/vs-plugins/models/)
Fp16_Qnt = True       # <True|False> — apply fp16 quantization to fp32 model
Exh_Tune = False      # <True|False> — enable exhaustive tuning (trial optimization)
Gpu = 0               # GPU index; 0 = first detected
Gpu_T = 2             # <1|2|3> — number of GPU execution threads
H_Max = 1440          # Integer — clamp output height to this maximum (e.g., display height)
Lk_Fmt = False        # <True|False> — lock pixel format to yuv420p8

# Step 1: Resolution check (intermediate)
ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)

# Step 2: Pre-scaling and format conversion
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Step 3: Apply AI Upscaling using MIGX backend
clip = k7f.UAI_MIGX(
    clip,
    clamp=False,
    model_pth=Model,
    fp16_qnt=Fp16_Qnt,
    exh_tune=Exh_Tune,
    gpu=Gpu,
    gpu_t=Gpu_T
)

# Step 4: Post-scaling and format validation
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()