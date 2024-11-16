from censor import censor_audio
import warnings
import torch

# warnings.filterwarnings("ignore", category=FutureWarning)
# warnings.filterwarnings("ignore", category=UserWarning)
# warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")
# warnings.filterwarnings("ignore", category=UserWarning, module="whisper")
# warnings.filterwarnings("ignore", category=FutureWarning, module="torch")

print(torch.cuda.is_available())  # Should return True
if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))  # Prints GPU name


base_audio_path = r"Media\extracted_audio.wav"
# base_audio_path = r"Media\base_audio.wav"
censor_audio_path = r"Media\overlay_audio.wav"
output_audio_path = r"Media\output_audio.wav"
model_name = 'small'
to_censor = ["kill", "killed", "fuck", "fucking", "killing"]
# to_censor=['happier','happy','mourning','mind','thinking']

censor_audio(
    base_audio_path=base_audio_path,
    censor_audio_path=censor_audio_path,
    output_audio_path=output_audio_path,
    model_name=model_name,
    to_censor=to_censor,
    gain_of_censor=0,
    gain_of_base=-100,
    silent=False
)
