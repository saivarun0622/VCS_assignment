"""Basic student management functions."""

def list_students(students):
    """Return a readable list of student names."""
    return [student.strip() for student in students if student.strip()]
