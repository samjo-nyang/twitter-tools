import json
from datetime import datetime
from os import path

from ttools.settings import STORAGE_PATH
from ttools.utils import get_client, send_email


BNU_FILE_PATH = path.join(STORAGE_PATH, 'bnu.dat')


MSG_BUFFER = []


def get_old_list():
    if not path.exists(BNU_FILE_PATH):
        return '', {}, {}

    with open(BNU_FILE_PATH, 'r') as f:
        data = json.loads(f.read())

    return data['stamp'], data['followers'], data['followings']


def save_list(followers, followings):
    data = {
        'stamp': datetime.now().isoformat(),
        'followers': followers,
        'followings': followings,
    }
    with open(BNU_FILE_PATH, 'w') as f:
        f.write(json.dumps(data))


def get_current_list():
    def transform(user_list):
        return {
            str(k.id): {
                'name': k.name,
            } for k in user_list
        }

    client = get_client()
    followers = transform(client.GetFollowers())
    followings = transform(client.GetFriends())
    return followers, followings


def print_msg(msg):
    MSG_BUFFER.append(msg)
    print(msg)


def print_diff(new, old):
    new_ids = set(new.keys())
    old_ids = set(old.keys())

    added_ids = list(new_ids - old_ids)
    removed_ids = list(old_ids - new_ids)

    if not added_ids and not removed_ids:
        print_msg('  * No Changes')
        return False

    for added_id in added_ids:
        print_msg(f'  + id={added_id}, name={new[added_id]["name"]}')

    for removed_id in removed_ids:
        print_msg(f'  - id={removed_id}, name={old[removed_id]["name"]}')

    return True


def main():
    changes = False
    followers, followings = get_current_list()
    old_stamp, old_followers, old_followings = get_old_list()

    print_msg('Block and Unblock Checking Tool v1')
    print_msg(f'* Use Data on {old_stamp}')
    print_msg('* Printing Diff for Followers')
    changes |= print_diff(followers, old_followers)
    print_msg('* Printing Diff for Followings')
    changes |= print_diff(followings, old_followings)

    if changes:
        send_email('Twitter Tool - BNU', '\n'.join(MSG_BUFFER))

    save_list(followers, followings)
