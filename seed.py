import os
from app import db, Regulation, Semester, Subject

# Seed data for regulations, semesters, and subjects

def seed_database():
    # Clear existing data
    # db.session.query(Review).delete()  # Removed
    db.session.query(Subject).delete()
    db.session.query(Semester).delete()
    db.session.query(Regulation).delete()
    db.session.commit()
    reg_2025 = Regulation(code='2025', title='Regulation 2025')
    db.session.add(reg_2025)
    db.session.commit()

    semesters_2025 = [
        Semester(regulation_id=reg_2025.id, name='Sem I', sequence=1),
        Semester(regulation_id=reg_2025.id, name='Sem II', sequence=2),
        Semester(regulation_id=reg_2025.id, name='Sem III', sequence=3),
        Semester(regulation_id=reg_2025.id, name='Sem IV', sequence=4),
        Semester(regulation_id=reg_2025.id, name='Sem V', sequence=5),
        Semester(regulation_id=reg_2025.id, name='Sem VI', sequence=6),
        Semester(regulation_id=reg_2025.id, name='Sem VII', sequence=7),
        Semester(regulation_id=reg_2025.id, name='Sem VIII', sequence=8),
    ]
    db.session.add_all(semesters_2025)
    db.session.commit()

    # Subjects for 2025
    subjects_data_2025 = [
        {'semester': 'Sem I', 'code': 'MA25C01', 'name': 'Applied Calculus', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'cat': 'BS', 'prac': '—'},
        {'semester': 'Sem I', 'code': 'EN25C01', 'name': 'English Essentials – I', 'type': 'T', 'ltp': '2-0-0', 'credits': 2, 'cat': 'HUM', 'prac': '—'},
        {'semester': 'Sem I', 'code': 'UC25H01', 'name': 'தமிழர் மரபு / Heritage of Tamils', 'type': 'T', 'ltp': '1-0-0', 'credits': 1, 'cat': 'HUM', 'prac': '—'},
        {'semester': 'Sem I', 'code': 'PH25C01', 'name': 'Applied Physics – I', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'BS', 'prac': 'PH25C01 Applied Physics – I Lab'},
        {'semester': 'Sem I', 'code': 'CY25C01', 'name': 'Applied Chemistry – I', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'BS', 'prac': 'CY25C01 Applied Chemistry – I Lab'},
        {'semester': 'Sem I', 'code': 'CS25C01', 'name': 'Computer Programming: C', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'ES (PC)', 'prac': 'CS25C01 C Programming Lab'},
        {'semester': 'Sem I', 'code': 'CS25C03', 'name': 'Essentials of Computing', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'ES (PC)-DIC', 'prac': 'CS25C03 Essentials of Computing Lab'},
        {'semester': 'Sem I', 'code': 'ME25C04', 'name': 'Makerspace', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'cat': 'SD', 'prac': 'ME25C04 Makerspace Lab'},
        {'semester': 'Sem I', 'code': 'UC25A01', 'name': 'Life Skills for Engineers – I*', 'type': '-', 'ltp': '1-0-2', 'credits': 0, 'cat': 'HUM', 'prac': 'UC25A01 Life Skills Lab (Audit)'},
        {'semester': 'Sem I', 'code': 'UC25A02', 'name': 'Physical Education – I*', 'type': '-', 'ltp': '0-0-4', 'credits': 1, 'cat': 'HUM', 'prac': 'UC25A02 Physical Education (Audit)'},
        {'semester': 'Sem II', 'code': 'MA25C02', 'name': 'Linear Algebra', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'cat': 'BS', 'prac': '—'},
        {'semester': 'Sem II', 'code': 'EE25C01', 'name': 'Basic Electrical and Electronics Engineering', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (G)', 'prac': '—'},
        {'semester': 'Sem II', 'code': 'CS25C06', 'name': 'Digital Principles and Computer Organization', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem II', 'code': 'UC25H02', 'name': 'தமிழர்களும் தொழில்நுட்பமும் / Tamils and Technology', 'type': 'T', 'ltp': '1-0-0', 'credits': 1, 'cat': 'HUM', 'prac': '—'},
        {'semester': 'Sem II', 'code': 'PH25C03', 'name': 'Applied Physics (CSIE) – II', 'type': 'T', 'ltp': '2-1-0', 'credits': 3, 'cat': 'BS', 'prac': '—'},
        {'semester': 'Sem II', 'code': 'AD25201', 'name': 'Python for Data Science', 'type': 'LIT', 'ltp': '3-0-2', 'credits': 4, 'cat': 'ES (PC)', 'prac': 'AD25201 Python for Data Science Lab'},
        {'semester': 'Sem II', 'code': 'EN25C02', 'name': 'English Essentials – II', 'type': 'LIT', 'ltp': '1-0-2', 'credits': 2, 'cat': 'HUM', 'prac': 'EN25C02 English Essentials Lab'},
        {'semester': 'Sem II', 'code': 'ME25C05', 'name': 'Re-Engineering for Innovation', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'cat': 'SD', 'prac': 'ME25C05 Re-Engineering Lab'},
        {'semester': 'Sem II', 'code': 'UC25A03', 'name': 'Life Skills for Engineers – II*', 'type': '-', 'ltp': '1-0-2', 'credits': 0, 'cat': 'HUM', 'prac': 'UC25A03 Life Skills Lab (Audit)'},
        {'semester': 'Sem II', 'code': 'UC25A04', 'name': 'Physical Education – II*', 'type': '-', 'ltp': '0-0-4', 'credits': 1, 'cat': 'HUM', 'prac': 'UC25A04 Physical Education (Audit)'},
        {'semester': 'Sem III', 'code': 'MA25C03', 'name': 'Discrete Mathematics', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'cat': 'BS', 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS25C02', 'name': 'Data Structures', 'type': 'LIT', 'ltp': '3-0-4', 'credits': 5, 'cat': 'ES (PC)', 'prac': 'Data Structures Lab'},
        {'semester': 'Sem III', 'code': 'CS25C04', 'name': 'Java Programming', 'type': 'LIT', 'ltp': '3-0-4', 'credits': 5, 'cat': 'ES (PC)', 'prac': 'Java Programming Lab'},
        {'semester': 'Sem III', 'code': 'CS25C05', 'name': 'Exploratory Data Analysis', 'type': 'LIT', 'ltp': '3-0-2', 'credits': 4, 'cat': 'ES (PC)', 'prac': 'Exploratory Data Analysis Lab'},
        {'semester': 'Sem III', 'code': 'CS25C07', 'name': 'Operating Systems', 'type': 'LIT', 'ltp': '3-0-2', 'credits': 4, 'cat': 'ES (PC)', 'prac': 'Operating Systems Lab'},
        {'semester': 'Sem III', 'code': 'CS25C08', 'name': 'Skill Development Course – I', 'type': 'LIT', 'ltp': '1-0-2', 'credits': 2, 'cat': 'SD', 'prac': 'Skill Development Course – I Lab'},
        {'semester': 'Sem III', 'code': 'EN25C03', 'name': 'English Communication Skills Laboratory – II', 'type': 'LIT', 'ltp': '0-0-2', 'credits': 1, 'cat': 'HUM', 'prac': 'English Communication Skills Lab – II'},
        {'semester': 'Sem IV', 'code': 'MA25C04', 'name': 'Probability and Statistics', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'BS', 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS25C09', 'name': 'Algorithms', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS25C10', 'name': 'Artificial Intelligence Essentials', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS25C11', 'name': 'Data Privacy and Security', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS25C12', 'name': 'Standards in Artificial Intelligence', 'type': 'T', 'ltp': '1-0-0', 'credits': 1, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS25C13', 'name': 'Database Management Systems', 'type': 'LIT', 'ltp': '3-0-4', 'credits': 5, 'cat': 'ES (PC)', 'prac': 'Database Management Systems Lab'},
        {'semester': 'Sem IV', 'code': 'CS25C14', 'name': 'Skill Development Course – II', 'type': 'LIT', 'ltp': '1-0-2', 'credits': 2, 'cat': 'SD', 'prac': 'Skill Development Course – II Lab'},
        {'semester': 'Sem IV', 'code': 'EN25C04', 'name': 'English Communication Skills Laboratory – III', 'type': 'LIT', 'ltp': '0-0-2', 'credits': 1, 'cat': 'HUM', 'prac': 'English Communication Skills Lab – III'},
        {'semester': 'Sem V', 'code': 'MA25C05', 'name': 'Optimisation Techniques', 'type': 'T', 'ltp': '2-0-0', 'credits': 2, 'cat': 'BS', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS25C15', 'name': 'Natural Language Processing', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS25C16', 'name': 'Programme Elective – I', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PE)', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS25C17', 'name': 'Programme Elective – II', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PE)', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS25C18', 'name': 'Machine Learning', 'type': 'LIT', 'ltp': '3-0-2', 'credits': 4, 'cat': 'ES (PC)', 'prac': 'Machine Learning Lab'},
        {'semester': 'Sem V', 'code': 'CS25C19', 'name': 'Computer Networks', 'type': 'LIT', 'ltp': '3-0-2', 'credits': 4, 'cat': 'ES (PC)', 'prac': 'Computer Networks Lab'},
        {'semester': 'Sem V', 'code': 'CS25C20', 'name': 'Internet of Things', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'ES (PC)', 'prac': 'Internet of Things Lab'},
        {'semester': 'Sem V', 'code': 'CS25C21', 'name': 'Skill Development Course – III', 'type': 'LIT', 'ltp': '1-0-2', 'credits': 2, 'cat': 'SD', 'prac': 'Skill Development Course – III Lab'},
        {'semester': 'Sem V', 'code': 'CS25C22', 'name': 'Industry Oriented Course – I', 'type': 'LIT', 'ltp': '1-0-2', 'credits': 1, 'cat': 'SD', 'prac': 'Industry Oriented Course – I Lab'},
        {'semester': 'Sem V', 'code': 'CS25C23', 'name': 'Capstone Design Project - Level I (Honours)', 'type': 'CDP', 'ltp': '0-0-12', 'credits': 6, 'cat': 'SD', 'prac': 'Capstone Design Project - Level I'},
        {'semester': 'Sem V', 'code': 'CS25C24', 'name': 'Honours Elective – I', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS25C25', 'name': 'Honours Elective – II', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'GE25C01', 'name': 'Minor Elective – I', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem V', 'code': 'GE25C02', 'name': 'Minor Elective – II', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS25C26', 'name': 'Compiler Design', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS25C27', 'name': 'Programme Elective – III', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PE)', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'GE25C03', 'name': 'Open Elective', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS25C28', 'name': 'Deep Learning', 'type': 'LIT', 'ltp': '3-0-2', 'credits': 4, 'cat': 'ES (PC)', 'prac': 'Deep Learning Lab'},
        {'semester': 'Sem VI', 'code': 'CS25C29', 'name': 'Image Processing', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'ES (PC)', 'prac': 'Image Processing Lab'},
        {'semester': 'Sem VI', 'code': 'CS25C30', 'name': 'UI/UX Design and Human Centered Design', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'ES (PC)', 'prac': 'UI/UX Design Lab'},
        {'semester': 'Sem VI', 'code': 'CS25C31', 'name': 'Industry Oriented Course - II', 'type': 'LIT', 'ltp': '1-0-2', 'credits': 1, 'cat': 'SD', 'prac': 'Industry Oriented Course - II Lab'},
        {'semester': 'Sem VI', 'code': 'CS25C32', 'name': 'Full Stack Development Laboratory', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'cat': 'ES (PC)', 'prac': 'Full Stack Development Lab'},
        {'semester': 'Sem VI', 'code': 'CS25C33', 'name': 'Self-Learning Course', 'type': '-', 'ltp': '0-0-0', 'credits': 1, 'cat': 'SL', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS25C34', 'name': 'Capstone Design Project - Level II (Honours)', 'type': 'CDP', 'ltp': '0-0-12', 'credits': 6, 'cat': 'SD', 'prac': 'Capstone Design Project - Level II'},
        {'semester': 'Sem VI', 'code': 'CS25C35', 'name': 'Honours Elective – III', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS25C36', 'name': 'Honours Elective – IV', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'GE25C04', 'name': 'Minor Elective – III', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'GE25C05', 'name': 'Minor Elective – IV', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS25C37', 'name': 'Programme Elective – IV', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PE)', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS25C38', 'name': 'Programme Elective – V', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PE)', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'GE25C06', 'name': 'Climate Change and Sustainability', 'type': 'T', 'ltp': '2-0-0', 'credits': 2, 'cat': 'HUM', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS25C39', 'name': 'Ethical Hacking and Penetration Testing', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'ES (PC)', 'prac': 'Ethical Hacking and Penetration Testing Lab'},
        {'semester': 'Sem VII', 'code': 'ME25C06', 'name': 'Engineering Entrepreneurship Development', 'type': 'LIT', 'ltp': '2-0-2', 'credits': 3, 'cat': 'HUM', 'prac': 'Engineering Entrepreneurship Lab'},
        {'semester': 'Sem VII', 'code': 'CS25C40', 'name': 'Summer Internship', 'type': '-', 'ltp': '—', 'credits': 1, 'cat': 'SD', 'prac': 'Summer Internship'},
        {'semester': 'Sem VII', 'code': 'CS25C41', 'name': 'Capstone Design Project – Level III (Honours)', 'type': 'CDP', 'ltp': '0-0-12', 'credits': 6, 'cat': 'SD', 'prac': 'Capstone Design Project – Level III'},
        {'semester': 'Sem VII', 'code': 'CS25C42', 'name': 'Honours Elective – V', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS25C43', 'name': 'Honours Elective – VI', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'ES (PC)', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'GE25C07', 'name': 'Minor Elective – V', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'GE25C08', 'name': 'Minor Elective – VI', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'cat': 'OE', 'prac': '—'},
        {'semester': 'Sem VIII', 'code': 'CS25C44', 'name': 'Project Work / Internship cum Project Work', 'type': 'PW/IPW', 'ltp': '0-0-16', 'credits': 8, 'cat': 'SD', 'prac': 'Project Work / Internship cum Project Work'},
    ]

    for data in subjects_data_2025:
        sem = Semester.query.filter_by(name=data['semester'], regulation_id=reg_2025.id).first()
        if sem:
            subj = Subject(
                semester_id=sem.id,
                course_code=data['code'],
                course_name=data['name'],
                course_type=data['type'],
                ltp=data['ltp'],
                credits=data['credits'],
                category=data['cat'],
                practical=data.get('prac')
            )
            db.session.add(subj)

    # Regulation 2021
    reg_2021 = Regulation(code='2021', title='Regulation 2021')
    db.session.add(reg_2021)
    db.session.commit()

    semesters_2021 = [
        Semester(regulation_id=reg_2021.id, name='Sem I', sequence=1),
        Semester(regulation_id=reg_2021.id, name='Sem II', sequence=2),
        Semester(regulation_id=reg_2021.id, name='Sem III', sequence=3),
        Semester(regulation_id=reg_2021.id, name='Sem IV', sequence=4),
        Semester(regulation_id=reg_2021.id, name='Sem V', sequence=5),
        Semester(regulation_id=reg_2021.id, name='Sem VI', sequence=6),
        Semester(regulation_id=reg_2021.id, name='Sem VII', sequence=7),
        Semester(regulation_id=reg_2021.id, name='Sem VIII', sequence=8),
    ]
    db.session.add_all(semesters_2021)
    db.session.commit()

    # Subjects for 2021 
    subjects_data_2021 = [
        {'semester': 'Sem I', 'code': 'IP3151', 'name': 'Induction Programme', 'cat': '-', 'type': '-', 'ltp': '-', 'credits': 0, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'HS3152', 'name': 'Professional English - I', 'cat': 'HSMC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'MA3151', 'name': 'Matrices and Calculus', 'cat': 'BSC', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'PH3151', 'name': 'Engineering Physics', 'cat': 'BSC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'CY3151', 'name': 'Engineering Chemistry', 'cat': 'BSC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'GE3151', 'name': 'Problem Solving and Python Programming', 'cat': 'ESC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'GE3152', 'name': 'தமிழர் மரபு / Heritage of Tamils', 'cat': 'HSMC', 'type': 'T', 'ltp': '1-0-0', 'credits': 1, 'prac': '—'},
        {'semester': 'Sem I', 'code': 'GE3171', 'name': 'Problem Solving and Python Programming Laboratory', 'cat': 'ESC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'GE3171 Python Programming Lab'},
        {'semester': 'Sem I', 'code': 'BS3171', 'name': 'Physics and Chemistry Laboratory', 'cat': 'BSC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'BS3171 Physics & Chemistry Lab'},
        {'semester': 'Sem I', 'code': 'GE3172', 'name': 'English Laboratory', 'cat': 'EEC', 'type': 'L', 'ltp': '0-0-2', 'credits': 1, 'prac': 'GE3172 English Lab'},
        {'semester': 'Sem II', 'code': 'HS3252', 'name': 'Professional English - II', 'cat': 'HSMC', 'type': 'T', 'ltp': '2-0-0', 'credits': 2, 'prac': '—'},
        {'semester': 'Sem II', 'code': 'MA3251', 'name': 'Statistics and Numerical Methods', 'cat': 'BSC', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'prac': '—'},
        {'semester': 'Sem II', 'code': 'PH3256', 'name': 'Physics for Information Science', 'cat': 'BSC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem II', 'code': 'BE3251', 'name': 'Basic Electrical and Electronics Engineering', 'cat': 'ESC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem II', 'code': 'GE3251', 'name': 'Engineering Graphics', 'cat': 'ESC', 'type': 'T', 'ltp': '2-0-4', 'credits': 4, 'prac': 'GE3251 Engineering Graphics Lab'},
        {'semester': 'Sem II', 'code': 'AD3251', 'name': 'Data Structures Design', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem II', 'code': 'GE3252', 'name': 'தமிழரும் தொழில்நுட்பமும் / Tamils and Technology', 'cat': 'HSMC', 'type': 'T', 'ltp': '1-0-0', 'credits': 1, 'prac': '—'},
        {'semester': 'Sem II', 'code': 'GE3271', 'name': 'Engineering Practices Laboratory', 'cat': 'ESC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'GE3271 Engineering Practices Lab'},
        {'semester': 'Sem II', 'code': 'AD3271', 'name': 'Data Structures Design Laboratory', 'cat': 'PCC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'AD3271 Data Structures Lab'},
        {'semester': 'Sem II', 'code': 'GE3272', 'name': 'Communication Laboratory / Foreign Language', 'cat': 'EEC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'GE3272 Communication / Foreign Language Lab'},
        {'semester': 'Sem III', 'code': 'MA3252', 'name': 'Discrete Mathematics', 'cat': 'BSC', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS3151', 'name': 'Digital Principles and Computer Organization', 'cat': 'ESC', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS3152', 'name': 'Database Design and Management', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS3153', 'name': 'Design and Analysis of Algorithms', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS3154', 'name': 'Data Exploration and Visualization', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS3155', 'name': 'Artificial Intelligence', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem III', 'code': 'CS3171', 'name': 'Database Design and Management Laboratory', 'cat': 'PCC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'Database Management Lab'},
        {'semester': 'Sem III', 'code': 'CS3172', 'name': 'Artificial Intelligence Laboratory', 'cat': 'PCC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'AI Lab'},
        {'semester': 'Sem IV', 'code': 'MA3253', 'name': 'Probability and Statistics', 'cat': 'BSC', 'type': 'T', 'ltp': '3-1-0', 'credits': 4, 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS3156', 'name': 'Operating Systems', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS3157', 'name': 'Machine Learning', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS3158', 'name': 'Fundamentals of Data Science and Analytics', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS3159', 'name': 'Computer Networks', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'GE3153', 'name': 'Environmental Sciences and Sustainability', 'cat': 'HSMC', 'type': 'T', 'ltp': '2-0-0', 'credits': 2, 'prac': '—'},
        {'semester': 'Sem IV', 'code': 'CS3173', 'name': 'Data Science and Analytics Laboratory', 'cat': 'PCC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'Data Science & Analytics Lab'},
        {'semester': 'Sem IV', 'code': 'CS3174', 'name': 'Machine Learning Laboratory', 'cat': 'PCC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'Machine Learning Lab'},
        {'semester': 'Sem V', 'code': 'CS3160', 'name': 'Deep Learning', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS3161', 'name': 'Data and Information Security', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS3162', 'name': 'Distributed Computing', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS3163', 'name': 'Big Data Analytics', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem V', 'code': 'CS3175', 'name': 'Deep Learning Laboratory', 'cat': 'PCC', 'type': 'L', 'ltp': '0-0-4', 'credits': 2, 'prac': 'Deep Learning Lab'},
        {'semester': 'Sem VI', 'code': 'CS3164', 'name': 'Embedded Systems and IoT', 'cat': 'PCC', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS3165', 'name': 'Programme Elective – I', 'cat': 'PE', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS3166', 'name': 'Programme Elective – II', 'cat': 'PE', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'GE3161', 'name': 'Open Elective', 'cat': 'OE', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VI', 'code': 'CS3181', 'name': 'Project Work Phase I', 'cat': 'PW', 'type': '-', 'ltp': '0-0-12', 'credits': 6, 'prac': 'Project Work Phase I'},
        {'semester': 'Sem VII', 'code': 'GE3154', 'name': 'Human Values and Ethics', 'cat': 'HSMC', 'type': 'T', 'ltp': '2-0-0', 'credits': 2, 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS3167', 'name': 'Programme Elective – III', 'cat': 'PE', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS3168', 'name': 'Programme Elective – IV', 'cat': 'PE', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VII', 'code': 'CS3169', 'name': 'Programme Elective – V', 'cat': 'PE', 'type': 'T', 'ltp': '3-0-0', 'credits': 3, 'prac': '—'},
        {'semester': 'Sem VIII', 'code': 'CS3182', 'name': 'Project Work / Internship', 'cat': 'PW/IPW', 'type': 'L', 'ltp': '0-0-20', 'credits': 10, 'prac': 'Project Work / Internship'},
    ]

    for data in subjects_data_2021:
        sem = Semester.query.filter_by(name=data['semester'], regulation_id=reg_2021.id).first()
        if sem:
            subj = Subject(
                semester_id=sem.id,
                course_code=data['code'],
                course_name=data['name'],
                course_type=data['type'],
                ltp=data['ltp'],
                credits=data['credits'],
                category=data['cat'],
                practical=data.get('prac')
            )
            db.session.add(subj)

    db.session.commit()
    print("Database seeded successfully.")

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()
        seed_database()
