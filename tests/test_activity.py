from activity.activity import Solution

def test_case_1():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
    banned = ["hit"]
    expected = "ball"

    s = Solution()
    result = s.mostCommonWord(paragraph, banned)
    assert expected == result

def test_case_2():
    paragraph = "a." 
    banned = []
    expected = "a"

    s = Solution()
    result = s.mostCommonWord(paragraph, banned)
    assert expected == result
