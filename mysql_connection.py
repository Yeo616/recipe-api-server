import mysql.connector 

def get_connection():
    connection = mysql.connector.connect(
        host = 'yh-db.c6isfff1nnnu.ap-northeast-2.rds.amazonaws.com',
        # host 를 써야, 접속할수가 있다. mysql참고 혹은 aws 참고
        database = 'recipe_db1',
        # mysql의 스키마 이름
        user = 'recipe_user2',
        password = 'recipe1234'
    )
    return connection
# 파이썬에서 mysql로 접속하는 코드

# 내가 mysql로 작성했던 내용과 같은 정보가 들어가야한다. (아래 참고)
# Host는 내가 mysql정보에서 확인 가능하다. 혹은 AWS에 들어가서 확인이 가능하다. 

# use mysql;
# create user 'recipe_user2'@'%' identified by 'recipe1234';
# grant all on recipe_db1.* to 'recipe_user2'@'%';




