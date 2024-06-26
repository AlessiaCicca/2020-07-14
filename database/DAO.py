from database.DB_connect import DBConnect
from model.squadra import Squadra


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select t.*, tot
from 
(select t1.s1 as s1, (parH*1+ vinH*3+vinA*3+parA) as tot
from 
	(select m.TeamHomeID as s1,count(*) as parH
	from matches m 
	where m.ResultOfTeamHome=0
	group by m.TeamHomeID ) as t1,
(select m.TeamHomeID as s2 ,count(*) as vinH
from matches m 
where m.ResultOfTeamHome=1
group by m.TeamHomeID ) as t2,
	(select m.TeamAwayID as s3 ,count(*) as vinA
	from matches m 
	where m.ResultOfTeamHome=-1
	group by m.TeamAwayID) as t3,
	(select m.TeamAwayID as s4 ,count(*) as parA
	from matches m 
	where m.ResultOfTeamHome=0
	group by m.TeamAwayID) as t4
where t1.s1=t2.s2 and t1.s1=t3.s3 and t1.s1=t4.s4) as cla, teams t
where cla.s1=t.TeamID 

"""

        cursor.execute(query)

        for row in cursor:
            result.append(Squadra(**row))

        cursor.close()
        conn.close()
        return result
