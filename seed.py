from project import db, User

# s1 = User(first_name='Tyrion', last_name='Lannister', username='debtpayer6000', email='tyrionlannister1@hotmail.com', location='Westeros', bio='Still going strong', password='lannister')
s2 = User(first_name='Jamie', last_name='Lannister', username='SirCognitiveDissonance36', email='goldhand36@hotmail.com', location='Westeros', bio='What am I even doing anymore', password='lannister2')


# db.session.add(s1)
db.session.add(s2)

db.session.commit()