class Solution:
    def sumGame(self, num: str) -> bool:
        string_length = len(num)
        first_half = num[:string_length // 2]
        second_half = num[string_length // 2:]
        question_marks_first_half = first_half.count("?")
        question_marks_second_half = second_half.count("?")

        sum_first_half = sum(int(digit) for digit in first_half if digit != "?")
        sum_second_half = sum(int(digit) for digit in second_half if digit != "?")
        total_question_marks = question_marks_first_half + question_marks_second_half
        sum_difference = sum_first_half - sum_second_half
        question_mark_difference = question_marks_second_half - question_marks_first_half
      
        return (total_question_marks % 2 == 1 or 
                sum_difference != 9 * question_mark_difference // 2)