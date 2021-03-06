import random

def histogram(l):
    uniq = list(set(l))
    reps = []
    for i in uniq:
        n = l.count(i)
        reps.append(n)
    freqDist = list(zip(uniq, reps))
    random.shuffle(freqDist)
    sortFunc(freqDist, 0, len(freqDist))
    return freqDist

def sortFunc(seq, l, r):
    if r-l <= 1:
        return
    
    if r-l > 1:
        yellow = l + 1
        for green in range(l+1, r):
            if seq[green][1] < seq[l][1]:
                seq[green], seq[yellow] = seq[yellow], seq[green]
                yellow += 1

            elif seq[green][1] == seq[l][1]:
                if seq[green][0] < seq[l][0]:
                    seq[green], seq[yellow] = seq[yellow], seq[green]
                    yellow += 1

        seq[l], seq[yellow-1] = seq[yellow-1], seq[l]
        sortFunc(seq, l, yellow-1)
        sortFunc(seq, yellow, r)

ans = histogram([123 ,123 ,123 ,123 ,123 ,9 ,9 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,32 ,32 ,32 ,32 ,32 ,32 ,447 ,447 ,447 ,447 ,447 ,447 ,447 ,583 ,583 ,583 ,583 ,583 ,583 ,829 ,829 ,407 ,407 ,407 ,407 ,407 ,407 ,407 ,407 ,53 ,53 ,53 ,53 ,53 ,962 ,962 ,962 ,962 ,962 ,962 ,962 ,694 ,694 ,694 ,694 ,694 ,694 ,694 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,168 ,168 ,168 ,354 ,354 ,354 ,354 ,354 ,354 ,354 ,354 ,354 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,221 ,221 ,221 ,221 ,440 ,440 ,440 ,440 ,440 ,739 ,739 ,378 ,378 ,378 ,458 ,458 ,458 ,458 ,458 ,458 ,412 ,412 ,412 ,412 ,412 ,412 ,412 ,412 ,814 ,814 ,814 ,297 ,297 ,297 ,297 ,297 ,297 ,297 ,297 ,297 ,295 ,295 ,295 ,295 ,295 ,295 ,701 ,701 ,701 ,701 ,701 ,701 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,397 ,786 ,786 ,786 ,786 ,108 ,108 ,108 ,108 ,108 ,108 ,262 ,262 ,262 ,33 ,33 ,33 ,33 ,33 ,33 ,905 ,905 ,393 ,393 ,393 ,393 ,393 ,206 ,206 ,206 ,407 ,407 ,407 ,407 ,407 ,407 ,407 ,407 ,407 ,407 ,861 ,861 ,861 ,861 ,861 ,861 ,861 ,564 ,564 ,564 ,564 ,564 ,564 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,634 ,634 ,634 ,634 ,634 ,663 ,663 ,663 ,663 ,663 ,663 ,663 ,663 ,492 ,492 ,492 ,492 ,802 ,802 ,802 ,850 ,850 ,850 ,850 ,850 ,850 ,850 ,850 ,850 ,850 ,112 ,112 ,112 ,112 ,112 ,112 ,112 ,112 ,112 ,887 ,887 ,887 ,887 ,887 ,887 ,887 ,887 ,887 ,887 ,814 ,814 ,814 ,814 ,814 ,814 ,814 ,814 ,814 ,910 ,910 ,910 ,910 ,910 ,910 ,910 ,910 ,910 ,213 ,213 ,90 ,90 ,90 ,90 ,90 ,90 ,90 ,32 ,32 ,32 ,32 ,32 ,32 ,32 ,32 ,32 ,32 ,525 ,525 ,525 ,525 ,525 ,525 ,726 ,726 ,726 ,726 ,726 ,726 ,168 ,168 ,168 ,168 ,168 ,168 ,831 ,831 ,831 ,831 ,831 ,831 ,831 ,831 ,549 ,549 ,549 ,549 ,549 ,549 ,298 ,298 ,298 ,298 ,298 ,298 ,298 ,811 ,811 ,811 ,811 ,811 ,811 ,811 ,811 ,811 ,508 ,508 ,508 ,508 ,508 ,508 ,555 ,555 ,555 ,555 ,555 ,555 ,555 ,555 ,555 ,641 ,641 ,903 ,903 ,903 ,903 ,903 ,903 ,86 ,86 ,86 ,86 ,86 ,590 ,590 ,590 ,590 ,590 ,590 ,590 ,590 ,538 ,538 ,538 ,538 ,538 ,538 ,538 ,538 ,538 ,331 ,331 ,331 ,331 ,331 ,331 ,331 ,331 ,331 ,331 ,943 ,943 ,943 ,943 ,943 ,943 ,943 ,943 ,670 ,670 ,670 ,670 ,670 ,670 ,670 ,670 ,670 ,34 ,34 ,34 ,34 ,34 ,34 ,34 ,735 ,735 ,735 ,735 ,735 ,735 ,735 ,630 ,630 ,630 ,630 ,630 ,630 ,352 ,352 ,298 ,298 ,298 ,298 ,298 ,298 ,59 ,59 ,59 ,59 ,59 ,59 ,59 ,117 ,117 ,117 ,117 ,895 ,895 ,895 ,895 ,895 ,895 ,895 ,895 ,895 ,895 ,446 ,446 ,446 ,446 ,446 ,446 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,623 ,709 ,709 ,709 ,709 ,709 ,709 ,709 ,709 ,709 ,31 ,31 ,31 ,31 ,31 ,31 ,728 ,728 ,728 ,728 ,728 ,728 ,728 ,728 ,728 ,728 ,137 ,137 ,137 ,137 ,137 ,137 ,137 ,641 ,641 ,641 ,641 ,329 ,329 ,329 ,329 ,329 ,329 ,574 ,574 ,535 ,535 ,535 ,535 ,535 ,535 ,535 ,535 ,535 ,918 ,918 ,918 ,918 ,918 ,918 ,918 ,351 ,351 ,351 ,351 ,351 ,351 ,157 ,157 ,157 ,747 ,747 ,747 ,747 ,747 ,360 ,360 ,360 ,468 ,468 ,468 ,468 ,468 ,468 ,468 ,468 ,985 ,985 ,985 ,985 ,985 ,985 ,])
anskey = [(9, 2), (213, 2), (352, 2), (574, 2), (739, 2), (829, 2), (905, 2), (157, 3), (206, 3), (262, 3), (360, 3), (378, 3), (802, 3), (117, 4), (221, 4), (492, 4), (786, 4), (53, 5), (86, 5), (123, 5), (393, 5), (440, 5), (634, 5), (747, 5), (31, 6), (33, 6), (108, 6), (295, 6), (329, 6), (351, 6), (446, 6), (458, 6), (508, 6), (525, 6), (549, 6), (564, 6), (583, 6), (630, 6), (641, 6), (701, 6), (726, 6), (903, 6), (985, 6), (34, 7), (59, 7), (90, 7), (137, 7), (447, 7), (694, 7), (735, 7), (861, 7), (918, 7), (962, 7), (412, 8), (468, 8), (590, 8), (663, 8), (831, 8), (943, 8), (112, 9), (168, 9), (297, 9), (354, 9), (535, 9), (538, 9), (555, 9), (670, 9), (709, 9), (811, 9), (910, 9), (10, 10), (331, 10), (728, 10), (850, 10), (887, 10), (895, 10), (814, 12), (298, 13), (32, 16), (623, 17), (407, 18), (397, 27)]
print(ans==anskey)


def transcript(coursedetails, studentdetails, grades):
    ans = list()
    studentdetails.sort()
    coursedetails.sort()
    grades.sort()
    for studentdet in studentdetails:
        tuple = studentdet
        inlist = []
        for grade in grades:
            if studentdet[0] == grade[0]:
                for cdetail in coursedetails:
                    if grade[1] == cdetail[0]:
                        intuple = cdetail
                        intuple = intuple + (grade[2],)
                        inlist.append(intuple)
        tuple = tuple + (inlist,)
        ans.append(tuple)
    return ans

courseDet = coursDet = [("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")]
studDet = [("UGM2021001","Rohit Grewal"),("UGP2021132","Neha Talwar")]
grades = [("UGM2021001","MA101","AB"),("UGP2021132","PH101","B"),("UGM2021001","PH101","B")]

ans1 = transcript(courseDet, studDet, grades)
anskey1 = [('UGM2021001', 'Rohit Grewal', [('MA101', 'Calculus', 'AB'), ('PH101', 'Mechanics', 'B')]), 
            ('UGP2021132', 'Neha Talwar', [('PH101', 'Mechanics', 'B')])]
print(ans1==anskey1)