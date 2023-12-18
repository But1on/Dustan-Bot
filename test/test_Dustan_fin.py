import pytest
from Dustan_fin import correct_rait
from Dustan_fin import super_sorted
from Dustan_fin import super_join

def test_correct_rait():
    for rait in range(1,5):
        for count  in range(1,5):
            a = [0,1,2]
            a.append(rait)
            a.append(count)
            assert correct_rait(a) == int((rait/count)*100+(rait/count)*1000%10//5)/100
    assert correct_rait([0,1,2,0,1]) == 0
    assert correct_rait([0,1,2,1,0]) == 0

def test_super_sorted():
    assert super_sorted('warlock','warlock') == 'warlock'
    assert super_sorted('warlock,hunter','warlock') == 'hunter,warlock'
    assert super_sorted('warlock','hunter') == 'hunter,warlock'
    assert super_sorted('warlock,titan','warlock') == 'titan,warlock'
    for i in range(10,50,10):
        for j in range(50,100,10):
            m = [str(i),str(j)]
            assert super_sorted(','.join(m),str(i)) == f'{i},{j}'

def test_super_join():
    assert super_join(['0','1','2','3','4','5','6']) == '1 - 5 - 6'
    assert super_join(['nasa','asa','dasa','oppo','yt','er','fdf']) == 'asa - er - fdf'
    assert super_join(['a','b','c','d','e','f','t']) == 'b - f - t'


