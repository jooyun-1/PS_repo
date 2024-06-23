def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'B#' in music:
        music = music.replace('B#', 'b')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')
    return music

def solution(m, musicinfos):
    answer = []
    index = 0
    m = change(m)
    for mi in musicinfos :
        index += 1
        info = mi.split(',')
        
        # 시작 시간 start[0],start[1]
        start = info[0].split(':')
        # 끝 시간 end[0],end[1]
        end = info[1].split(':')
        # 재생 시간
        play_time = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))
        # 바뀐 멜로디
        changed_music = change(info[3])
        # 멜로디 길이
        music_length = len(changed_music)
        
        play_music = changed_music * (play_time // music_length) + changed_music[:play_time % music_length]
        print(play_music, m)
        if m in play_music :
            answer.append((play_time,index,info[2]))
    if len(answer) == 0 :
        return "(None)"
    elif len(answer) == 1 :
        return answer[0][2]
    else :
        answer = list(sorted(answer, key = lambda x : (-x[0],x[1])))
        return answer[0][2]
