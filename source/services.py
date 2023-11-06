def get_path_to_upload(instance, file) -> str:
    model_name = instance.__class__.__name__
    if model_name == 'Video':
        author = instance.author
    else:
        author = instance.source_video.author
    return f'{author}/{model_name}/{file}'