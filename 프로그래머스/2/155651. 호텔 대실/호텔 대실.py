import heapq

def time_to_min(time) :
    hh, mm = map(int,time.split(':'))
    return hh * 60 + mm


def solution(book_time):
    answer = 0
    book_time = list(sorted(book_time,key=lambda x : (x[0],x[1])))
    heap = []
    
    for i in range(len(book_time)) :
        start_time = time_to_min(book_time[i][0])
        end_time = time_to_min(book_time[i][1]) + 10
        
        if heap and heap[0] <= start_time :
            heapq.heappop(heap)
        else :
            answer += 1
        heapq.heappush(heap,end_time)
    return answer