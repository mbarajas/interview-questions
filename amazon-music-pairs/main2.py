from collections import defaultdict

def get_song_pair_count(song_duration_list):
    dictionary = defaultdict(lambda: 0)
    count = 0

    for i, duration in enumerate(song_duration_list):
        duration %= 60
        target = (60 - duration)%60
        count += dictionary[target]
        dictionary[duration] += 1
    return count

print(get_song_pair_count([37,23,60]))
