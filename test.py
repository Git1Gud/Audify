from censor import censor_audio
import warnings


warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")
print('\n')
# base_audio_path = "extracted_audio.wav"
base_audio_path = "base_audio.wav"
censor_audio_path = "overlay_audio.wav"
output_audio_path = "output_audio.wav"
model_name = 'small'
# to_censor = ["kill", "killed", "fuck", "fucking", "killing"]
to_censor=['happier','happy','mourning','mind','thinking']

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
