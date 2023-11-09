def get_path_to_upload(instance, file) -> str:
    model_name = instance.__class__.__name__
    if model_name == 'Video':
        author = instance.author
    else:
        author = instance.source_video.author
    return f'{author}/{model_name}/{file}'



def set_auth_for_camera(data: dict) -> str:
    url = f'rtsp://{data['username']}:{data['password']}@' + data['url'].split('@')[1]
    return url
