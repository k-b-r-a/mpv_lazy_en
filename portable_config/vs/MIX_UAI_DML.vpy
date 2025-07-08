### Use Custom AI Upscaling Model (DX12 GPU Required)
### Docs: https://github.com/hooke007/MPV_lazy/discussions/329
### Parameters: https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc#uai_dml

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User Options #
############

H_Pre = 720          # Integer — reduce input resolution for pre-processing
Model = "the_database_AnimeJaNaiV2L1_x2_fp16_op17.onnx"  # Specify model file (located in .../mpv-lazy/vs-plugins/models/)
Fp16_Qnt = True      # <True|False> Use fp16 quantization for fp32 models
Gpu = 0              # GPU index; 0 = first detected GPU
Gpu_T = 2            # <1|2|3> Number of GPU threads
H_Max = 1440         # Integer — limit final output height (e.g. your display height)
Lk_Fmt = False       # <True|False> Lock pixel format to yuv420p8

# Step 1: Initial height check (not output-related)
ret = k7f.FMT_CTRL(clip, h_max=1200, h_ret=True)

# Step 2: Preprocess input format and resolution
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)

# Step 3: Apply AI upscaling with UAI_DML backend
clip = k7f.UAI_DML(
    clip,
    clamp=False,
    model_pth=Model,
    fp16_qnt=Fp16_Qnt,
    gpu=Gpu,
    gpu_t=Gpu_T
)

# Step 4: Final format cleanup and resolution limit
clip = k7f.FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()