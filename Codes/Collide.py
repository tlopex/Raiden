from math import sqrt

def distance(A, B):
    return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

def collide(Es, My):
    for each in Es:
        A = each.position
        B = My.position
        # print(distance(A, B))
        if distance(A, B) <= (each.rect.width + My.rect.width) // 2:
            Es.remove(each)
            # print("Get ", each.position)
            return True
        
def collide_check(Es, x):
    for each in Es:
        A = each.position
        B = x.position

        if distance(A, B) <= (each.rect.width + x.rect.width) // 2:
            return True

    return False