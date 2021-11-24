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

    D_Grade = 41
    C_Grade = D_Grade + increment
    B_Grade = C_Grade + increment
    A_Grade = B_Grade + increment

    lower_thresh_list.append(D_Grade)
    lower_thresh_list.append(C_Grade)
    lower_thresh_list.append(B_Grade)
    lower_thresh_list.append(A_Grade)

    return lower_thresh_list


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    pass


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    pass
