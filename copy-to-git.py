"""
これは　わたし用のプログラムだぜ☆つ（＾～＾）！
"""
import os
import shutil
import subprocess

source = 'C:/Users/むずでょ/source/repos/tororo-go-js'
destination = 'C:/Users/むずでょ/Documents/GitHub/tororo-go-js'


def go():
    print('Trace   | Remove.')
    remove_destination_dir('/meta')
    remove_destination_dir('/src')
    remove_destination_dir('/tool')
    remove_destination_file('/copy-to-git.py')
    remove_destination_file('/LICENSE')
    remove_destination_file('/README.md')

    print('Trace   | Copy.')
    copy_dir('/meta')
    copy_dir('/src')
    copy_dir('/tool', ignore=shutil.ignore_patterns('__pycache__'))
    copy_file('/copy-to-git.py')
    copy_file('/LICENSE')
    copy_file('/README.md')

    print('Trace   | Git hub.')
    subprocess.run(
        r"C:\Users\むずでょ\AppData\Local\GitHubDesktop\GitHubDesktop.exe")

    print('Trace   | Finished.')


def remove_destination_dir(child_path: str):
    path = f'{destination}{child_path}'
    if os.path.isdir(path):
        shutil.rmtree(path)


def remove_destination_file(child_path: str):
    path = f'{destination}{child_path}'
    if os.path.isfile(path):
        os.remove(path)


def copy_dir(child_path: str, ignore=None):
    shutil.copytree(f'{source}{child_path}',
                    f'{destination}{child_path}', ignore=ignore)


def copy_file(child_path: str):
    shutil.copy2(f'{source}{child_path}', f'{destination}{child_path}')


go()
