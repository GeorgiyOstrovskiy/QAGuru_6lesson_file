import zipfile
import os

resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
archive_dir = os.path.join(resources_dir, 'testzip.zip')


def create_archive():
    with zipfile.ZipFile(archive_dir, 'w', compression=zipfile.ZIP_DEFLATED) as zippfile:
        for file in os.listdir(resources_dir):
            if file.endswith('.zip'):
                continue
            zippfile.write(os.path.join(resources_dir, file))
