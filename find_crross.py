import math
import numpy as np
from numpy import linalg

def find_cross(pos_1, pos_2, pos_3, pos_4):
    """
    ２直線の交点を求める　※２次元、３次元に対応
    """
    u1 = np.array(pos_2) - np.array(pos_1) # u1
    u1 = u1 / np.linalg.norm(u1)
    u2 = -(np.array(pos_4) - np.array(pos_3)) # -u2 # - がついていることに注意!
    u2 = u2 / np.linalg.norm(u2)
    print(u1, u2)
    dot = np.inner(u1, u2)
    if dot * dot == 1:
        print("same line !")
        return
        
    U = np.array([u1.tolist(),u2.tolist()]).T # u2.T -u1.T
    print(U)
    
    a1 = np.array(pos_1)
    a2 = np.array(pos_3)
    print(a1, a2)
    A = a2 - a1
    print(A)

    UU = U.T @ U 
    
    try:
        t1, t2 = np.linalg.inv(UU) @ U.T @ A # ２直線の媒介変数
        print(t1, t2)
    except:
        print("No cross point")
        return

    p1 = a1 + u1 * t1 # 直線１の座標
    p2 = a2 - u2 * t2 # 直線２の座標
    print(p1, p2)
    if (p1 == p2).all():
        print("p1 = p2")
        return p1
    else:
        print("p1 != p2")
    
    

if __name__ == "__main__":
    pos_1 = [1/2, 0, 0]
    pos_2 = [1/2, 1, 0]
    pos_3 = [0, 1/2, 0]
    pos_4 = [1, 1/2, 0]
    find_cross(pos_1, pos_2, pos_3, pos_4)

