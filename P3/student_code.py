import heapq
from math import sqrt

def calc_distance(p1, p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    return sqrt((x1-x2)**2+(y1-y2)**2)
    
def reconstruct_path(came_from, current):
    total_path=[current]
    while current in came_from:
        current=came_from[current]
        total_path=[current]+total_path
    return total_path


def shortest_path(M,start,goal):
    came_from={} # For backtracking the path i.e. reconstructing the path
    g_score=[1e9]*len(M.intersections) # gScores of all intersections initialized to inf
    g_score[start]=0 # gScore of starting intersection is zero
    f_score=[1e9]*len(M.intersections) # fScores of all intersections initialized to inf (fScore(current)=gScore(current)+h(current))
    f_score[start]=calc_distance(M.intersections[start], M.intersections[goal]) # fScore of starting intersection is h(start) (h is heuristic function)
    
    open_set=[] # Stores the frontier values
    heapq.heappush(open_set, (f_score[start], start)) # min-heap used with comparision of first element in the tuple (here-> f_score[start])
    visited=[False]*len(M.intersections) # for the reference whether it is in open-set or not
    
    while (len(open_set)>0):
        visited[open_set[0][1]]=True 
        cur_score, current=heapq.heappop(open_set)
        if (current==goal):
            return reconstruct_path(came_from, current)
    
        for neighbor in M.roads[current]:
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore=g_score[current]+calc_distance(M.intersections[current], M.intersections[neighbor])
            if (tentative_gScore<g_score[neighbor]):
                # This path to neighbor is better than any previous one.
                came_from[neighbor]=current
                g_score[neighbor]=tentative_gScore
                f_score[neighbor]=g_score[neighbor]+calc_distance(M.intersections[neighbor], M.intersections[goal])
                if (visited[neighbor]==False):
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    
    # Open set is empty but goal was never reached
    return -1