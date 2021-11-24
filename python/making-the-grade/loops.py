def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    new_list = []

    for grade in student_scores:
        new_list.append(round(grade))

    return new_list


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    counter = 0

    for grade in student_scores:
        if grade <= 40:
            counter += 1

    return counter


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    new_list = []

    for grade in student_scores:
        if grade >= threshold:
            new_list.append(grade)

    return new_list


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    lower_thresh_list = []
    increment = round((highest - 40) / 4)

    d_grade = 41
    c_grade = d_grade + increment
    b_grade = c_grade + increment
    a_grade = b_grade + increment

    lower_thresh_list.append(d_grade)
    lower_thresh_list.append(c_grade)
    lower_thresh_list.append(b_grade)
    lower_thresh_list.append(a_grade)

    return lower_thresh_list


def student_ranking(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """

    ranked_list = []
    counter = 0

    for name in student_names:
        student_rank_str = str(counter + 1)
        student_score_str = str(student_scores[counter])
        ranked_list.append(f"{student_rank_str}. {name}: {student_score_str}")
        counter += 1

    return ranked_list


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    first_perfect_score = []

    for bundle in student_info:
        if bundle[1] == 100:
            first_perfect_score.append(bundle[0])
            first_perfect_score.append(bundle[1])
            return first_perfect_score

    return first_perfect_score
