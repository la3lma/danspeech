from danspeech.deepspeech.model import DeepSpeech
from danspeech.utils.data_utils import get_model


# ToDo: Add model package link for release
MODEL_PACKAGE = "toDo"


def Baseline(cache_dir=None):
    """
    Baseline DanSpeech model.

    2 Conv layers

    5 RNN Layers with 800 hidden units

    :param str cache_dir: If you wish to use custom directory to stash/cache your models. This is generally not
        recommended, and if left out, the DanSpeech models will be stored in the ``~/.danspeech/models/`` folder.

    :return: Pretrained DeepSpeech (Baseline) model.
    :rtype: ``danspeech.deepspeech.model.DeepSpeech``
    """
    model_path = get_model(model_name="Baseline.pth", origin=MODEL_PACKAGE,
                           file_hash="e2c0c16d518fc57cd61c86cbb0170660", cache_dir=cache_dir)
    model = DeepSpeech.load_model(model_path)
    return model

