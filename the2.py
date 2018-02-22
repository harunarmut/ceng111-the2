
def minority_shape_intersect(first,second):


    return lenght_check(first,second);

listo = []
main = []

def m_finder2(p1,p2,p3,p4):
    x1 = p2[0] - p1[0]
    x2 = p4[0] - p3[0]
    y1 = p2[1] - p1[1]
    y2 = p4[1] - p3[1]
  #  print  x1,x2,y1,y2
    if x1 == 0 and x2 ==0:
        m1 = 999999999999.
        m2 = 999999999999.
        return m1, m2

    elif x1 == 0:
        if y2 == 0:
            m1 = 999999999999.
            m2 = 0.000000000001
            return m1, m2
        else:
            m1 = 999999999999.
            m2 = float(y2)/x2
            return m1,m2
    elif x2 == 0:
        if y1 == 0:
            m2 = 999999999999.
            m1 = 0.000000000001
            return m1, m2
        else:
            m2 = 9999999999.
            m1 = float(y1) / x1
            return m1, m2

    else :
        if y1 == 0 and y2 ==0:
            m1 = 0.000000000001
            m2 = 0.000000000001
            return m1, m2

        elif y2 ==0:
            m2 = 0.000000000001
            m1 = float(y1) / x1
            return m1, m2
        elif y1 == 0:
            m1 = 0.0000000001
            m2 = float(y2) / x2
            return m1, m2
        else:
            m1 = float(y1) / x1
            m2 = float(y2) / x2
            return m1, m2

def m_finder(p1,p2):
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    if x1 == 0:
        m = 9999999999.
        return m;
    elif y1 ==0:
        m = 0.0000000001
        return m
    else:
        m = float(y1)/x1
        return m;

def intersec_finder(a1,a2,b1,b2):

    m = m_finder2(a1, a2, b1, b2);

    if abs(m[0] - m[1]) < 0.000000001 :
        return
    else:
      #  print m
        sec1 = float(b1[1] - a1[1] + (m[0]*a1[0]) - (m[1]*b1[0])) / (m[0]-m[1])
        sec2 = (float(m[0]*m[1]) / (m[1]-m[0])) * (b1[0] - a1[0] -float((b1[1])/m[1]) + float(a1[1])/m[0])
        return sec1, sec2;

def check(a,b,x,y,q):

    f_x = [a[0], b[0]]
    f_y = [a[1], b[1]]
    s_x = [x[0], y[0]]
    s_y = [x[1], y[1]]
    k = round(q[0],6)
    l = round(q[1],6)

    if min(s_x) <= k <= max(s_x) and min(f_x) <= k <= max(f_x) and min(f_y) <= l <= max(f_y) and min(s_y) <= l <= max(s_y):
        return True
    else:
        return False
def distance(a,b):
    a =  ((abs(a[0] - b[0]) ** 2 )+ (abs(a[1] - b[1]) ** 2 )) ** 0.5
    return a


def between(a,b,x):
    xs = [a[0],b[0]]
    ys = [a[1],b[1]]
    if min(xs) <= x[0] <= max(xs) and min(ys) <= x[1] <= max(ys):
        return True
    else:
        return False

def appender(q,w,e,r):
    if intersec_finder(q, w, e, r) and check(q, w, e, r,intersec_finder(q, w, e, r)) :
        listo.append(intersec_finder(q, w, e, r))




def appender_between(q,w,e,r,x):
    if intersec_finder(q,w,e,r)  and check(q, w, e, r,intersec_finder(q, w, e, r)) and (between(e, r, intersec_finder(q, w, e, r)) or between(x, r,intersec_finder(q, w, e,r))):
        listo.append(intersec_finder(q, w, e, r))

def inside1(po1_1,po1_2,po1_3,po21,po22,x):



    if inside_area(po1_1,po1_2,po1_3,x):
        listo.append(x)

        appender(po1_1, po1_2, po21, po22)
        appender(po1_3, po1_2, po21, po22)
        appender(po1_1, po1_3, po21, po22)

        appender_between(po1_1, po1_2, po22, x, po21)
        appender_between(po1_3, po1_2, po22, x, po21)
        appender_between(po1_1, po1_3, po22, x, po21)

        appender_between(po1_1, po1_3, po21, x, po22)
        appender_between(po1_1, po1_2, po21, x, po22)
        appender_between(po1_3, po1_2, po21, x, po22)
def inside2(po2_1,po2_2,po2_3,po11,po12,x):
    if inside_area(po2_1,po2_2,po2_3,x):
        listo.append(x)
#(po2_1, po2_2, po2_3, po1_3, po1_1, po1_2)
        appender(po2_1, po2_2, po11, po12)
        appender(po2_3, po2_2, po11, po12)
        appender(po2_1, po2_3, po11, po12)

        appender_between(po2_1, po2_2, po12, x, po11)
        appender_between(po2_3, po2_2, po12, x, po11)
        appender_between(po2_1, po2_3, po12, x, po11)

        appender_between(po2_1, po2_3, po11, x, po12)
        appender_between(po2_1, po2_2, po11, x, po12)
        appender_between(po2_3, po2_2, po11, x, po12)

def inside_4_1(po1_1,po1_2,po1_3,po2_1,po2_2,po2_3,x):
    if inside_area(po2_1,po2_2,po2_3,x):
        listo.append(x)

        appender(po2_1, po2_2, po1_1, po1_3)
        appender(po2_3, po2_2, po1_1, po1_3)
        appender(po2_1, po2_3, po1_1, po1_3)

        appender(po2_1, po2_2, po1_2, po1_3)
        appender(po2_3, po2_2, po1_2, po1_3)
        appender(po2_1, po2_3, po1_2, po1_3)

        appender_between(po2_1, po2_2, po1_2, x, po1_1)
        appender_between(po2_3, po2_2, po1_2, x, po1_1)
        appender_between(po2_1, po2_3, po1_2, x, po1_1)

        appender_between(po2_1, po2_3, po1_1, x, po1_2)
        appender_between(po2_1, po2_2, po1_1, x, po1_2)
        appender_between(po2_3, po2_2, po1_1, x, po1_2)

def inside_4_2(po1_1,po1_2,po1_3,po1_4,po2_1,po2_2,x):
    if inside_area_4(po1_1,po1_2,po1_3,po1_4,x):
        listo.append(x)

    appender(po1_1, po1_2, po2_1, po2_2)
    appender(po1_1, po1_4, po2_1, po2_2)
    appender(po1_2, po1_3, po2_1, po2_2)
    appender(po1_3, po1_4, po2_1, po2_2)

    appender_between(po1_1, po1_2, po2_1, x, po2_2)
    appender_between(po1_1, po1_4, po2_1, x, po2_2)
    appender_between(po1_2, po1_3, po2_1, x, po2_2)
    appender_between(po1_3, po1_4, po2_1, x, po2_2)

    appender_between(po1_1, po1_2, po2_2, x, po2_1)
    appender_between(po1_1, po1_4, po2_2, x, po2_1)
    appender_between(po1_2, po1_3, po2_2, x, po2_1)
    appender_between(po1_3, po1_4, po2_2, x, po2_1)



def intersects(po1_1,po1_2,po1_3,po2_1,po2_2,po2_3):

    inside1(po1_1,po1_2,po1_3,po2_2,po2_3,po2_1)
    inside1(po1_1,po1_2,po1_3,po2_1,po2_3,po2_2)
    inside1(po1_1,po1_2,po1_3,po2_2,po2_1,po2_3)

    inside2(po2_1, po2_2, po2_3, po1_2, po1_1, po1_3)
    inside2(po2_1, po2_2, po2_3, po1_3, po1_1, po1_2)
    inside2(po2_1, po2_2, po2_3, po1_2, po1_3, po1_1)

    appender(po1_1, po1_2, po2_1, po2_2)
    appender(po1_3, po1_2, po2_1, po2_2)
    appender(po1_1, po1_3, po2_1, po2_2)

    appender(po1_1, po1_2, po2_3, po2_1)
    appender(po1_1, po1_3, po2_3, po2_1)
    appender(po1_3, po1_2, po2_3, po2_1)

    appender(po1_1, po1_2, po2_2, po2_3)
    appender(po1_3, po1_2, po2_2, po2_3)
    appender(po1_1, po1_3, po2_2, po2_3)
    return listo

def intersects_4_3(po1_1,po1_2,po1_3,po1_4,po2_1,po2_2,po2_3):
    inside_4_2(po1_1, po1_2, po1_3, po1_4, po2_1, po2_2, po2_3)
    inside_4_2(po1_1, po1_2, po1_3, po1_4, po2_2, po2_3, po2_1)
    inside_4_2(po1_1, po1_2, po1_3, po1_4, po2_3, po2_1, po2_2)

    inside_4_1(po1_4, po1_2, po1_3, po2_2, po2_3, po2_1, po1_1)
    inside_4_1(po1_1, po1_3, po1_4, po2_2, po2_3, po2_1, po1_2)
    inside_4_1(po1_2, po1_4, po1_1, po2_2, po2_3, po2_1, po1_3)
    inside_4_1(po1_3, po1_1, po1_2, po2_2, po2_3, po2_1, po1_4)

    appender(po1_1, po1_2, po2_1, po2_2)
    appender(po1_1, po1_4, po2_1, po2_2)
    appender(po1_2, po1_3, po2_1, po2_2)
    appender(po1_3, po1_4, po2_1, po2_2)

    appender(po1_1, po1_2, po2_1, po2_3)
    appender(po1_1, po1_4, po2_1, po2_3)
    appender(po1_2, po1_3, po2_1, po2_3)
    appender(po1_3, po1_4, po2_1, po2_3)

    appender(po1_1, po1_2, po2_3, po2_2)
    appender(po1_1, po1_4, po2_3, po2_2)
    appender(po1_2, po1_3, po2_3, po2_2)
    appender(po1_3, po1_4, po2_3, po2_2)
    return listo

def inside_4_4(po1_1,po1_2,po1_3,po1_4,po2_1,po2_2,po2_3,x):
    if inside_area_4(po1_1, po1_2, po1_3, po1_4, x):
        listo.append(x)

    appender(po1_1, po1_2, po2_1, po2_2)
    appender(po1_1, po1_4, po2_1, po2_2)
    appender(po1_2, po1_3, po2_1, po2_2)
    appender(po1_3, po1_4, po2_1, po2_2)

    appender(po1_1, po1_2, po2_3, po2_2)
    appender(po1_1, po1_4, po2_3, po2_2)
    appender(po1_2, po1_3, po2_3, po2_2)
    appender(po1_3, po1_4, po2_3, po2_2)

    appender_between(po1_1, po1_2, po2_3, x, po2_1)
    appender_between(po1_1, po1_4, po2_3, x, po2_1)
    appender_between(po1_2, po1_3, po2_3, x, po2_1)
    appender_between(po1_3, po1_4, po2_3, x, po2_1)

    appender_between(po1_1, po1_2, po2_1, x, po2_3)
    appender_between(po1_1, po1_4, po2_1, x, po2_3)
    appender_between(po1_2, po1_3, po2_1, x, po2_3)
    appender_between(po1_3, po1_4, po2_1, x, po2_3)


def intersects_4_4(po1_1,po1_2,po1_3,po1_4,po2_1,po2_2,po2_3,po2_4):

    inside_4_4(po1_1, po1_2, po1_3, po1_4, po2_1, po2_2, po2_3,po2_4)
    inside_4_4(po1_1, po1_2, po1_3, po1_4, po2_2, po2_3, po2_4,po2_1)
    inside_4_4(po1_1, po1_2, po1_3, po1_4, po2_3, po2_4, po2_1,po2_2)
    inside_4_4(po1_1, po1_2, po1_3, po1_4, po2_2, po2_1, po2_4,po2_3)

    inside_4_4(po2_1, po2_2, po2_3, po2_4, po1_1, po1_2, po1_3, po1_4)
    inside_4_4(po2_1, po2_2, po2_3, po2_4, po1_2, po1_1, po1_4, po1_3)
    inside_4_4(po2_1, po2_2, po2_3, po2_4, po1_1, po1_4, po1_3, po1_2)
    inside_4_4(po2_1, po2_2, po2_3, po2_4, po1_2, po1_3, po1_4, po1_1)

    appender(po1_1, po1_2, po2_1, po2_2)
    appender(po1_1, po1_4, po2_1, po2_2)
    appender(po1_2, po1_3, po2_1, po2_2)
    appender(po1_3, po1_4, po2_1, po2_2)

    appender(po1_1, po1_2, po2_2, po2_3)
    appender(po1_1, po1_4, po2_2, po2_3)
    appender(po1_2, po1_3, po2_2, po2_3)
    appender(po1_3, po1_4, po2_2, po2_3)

    appender(po1_1, po1_2, po2_3, po2_4)
    appender(po1_1, po1_4, po2_3, po2_4)
    appender(po1_2, po1_3, po2_3, po2_4)
    appender(po1_3, po1_4, po2_3, po2_4)

    appender(po1_1, po1_2, po2_1, po2_4)
    appender(po1_1, po1_4, po2_1, po2_4)
    appender(po1_2, po1_3, po2_1, po2_4)
    appender(po1_3, po1_4, po2_1, po2_4)
    return listo

def lenght_check(list1,list2):

    if len(list1) == 4 and len(list2) == 4 :
        p1_1 = list1[0]
        p1_2 = list1[1]
        p1_3 = list1[2]
        p1_4 = list1[3]

        p2_1 = list2[0]
        p2_2 = list2[1]
        p2_3 = list2[2]
        p2_4 = list2[3]
        return cleaner(intersects_4_4(p1_1, p1_2, p1_3,p1_4, p2_1, p2_2, p2_3, p2_4))
    elif len(list1) == 4 and len(list2) == 3 :
        p1_1 = list1[0]
        p1_2 = list1[1]
        p1_3 = list1[2]
        p1_4 = list1[3]

        p2_1 = list2[0]
        p2_2 = list2[1]
        p2_3 = list2[2]

        return cleaner(intersects_4_3(p1_1, p1_2, p1_3, p1_4, p2_1, p2_2, p2_3))

    elif len(list1) == 3 and len(list2) == 4 :
        p1_1 = list2[0]
        p1_2 = list2[1]
        p1_3 = list2[2]
        p1_4 = list2[3]

        p2_1 = list1[0]
        p2_2 = list1[1]
        p2_3 = list1[2]

        return cleaner(intersects_4_3(p1_1, p1_2, p1_3, p1_4, p2_1, p2_2, p2_3))
    else:
        p1_1 = list1[0]
        p1_2 = list1[1]
        p1_3 = list1[2]

        p2_1 = list2[0]
        p2_2 = list2[1]
        p2_3 = list2[2]

        return cleaner(intersects(p1_1,p1_2,p1_3,p2_1,p2_2,p2_3))

def area_finder(a,b,c):

    val = abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1])  + c[0] * (a[1] - b[1])) / 2.0)
    return val

def inside_area(a,b,c,x):

    a1 = area_finder(a,b,x)
    a2 = area_finder(c,b,x)
    a3 = area_finder(a,c,x)

    ma = area_finder(a,b,c)
    if abs(ma - (a1+a2+a3)) < 0.0001:
        return True
    else:
        return False
def inside_area_4(a,b,c,d,x):
    if inside_area(a,b,c,d):
        if inside_area(b,d,c,x) or inside_area(b,d,a,x)  or is_on(b,d,x) :
            return True,'a'
        else:
            return False
    elif inside_area(a,b,d,c):
        if inside_area(a,b,c,x) or inside_area(c,d,a,x)  or is_on(c,a,x) :
            return True
        else:
            return False
    elif inside_area(a,c,d,b):
        if inside_area(a,b,d,x) or inside_area(c,d,b,x)  or is_on(b,d,x) :
            return True
        else:
            return False
    elif inside_area(b,c,d,a):
        if inside_area(a,b,c,x) or inside_area(c,d,a,x)  or is_on(a,c,x) :
            return True
        else:
            return False
    else:

        if inside_area(a,b,c,x) or inside_area(c,d,a,x)  or is_on(b,d,x) :
            return True
        else:
            return False

def is_on(a,b,x):
    ax = m_finder(a, x)
    bx = m_finder(b, x)

    if ax == bx and between(a,b,x):
        return True
    else:
        return False
def cleaner(list_d):
    list_c = []
    list_n = []
    list_n = list_d[:]

    del list_d[:]

    for x in range(len(list_n)):
        list_c.append((round(list_n[x][0], 6), round(list_n[x][1], 6)))

    return list(set(list_c))
