def get_song_pair_count(song_duration_list):
    count = 0
    i = 0
    j = i + 1

    list_length = len(song_duration_list)

    for i in range(0, list_length):
        for j in range(i + 1, list_length):
            couple_time = song_duration_list[i] + song_duration_list[j]
            if couple_time % 60 == 0:
                count += 1

    return count


song_duration_list = [37, 23, 60]

print(get_song_pair_count(song_duration_list))
