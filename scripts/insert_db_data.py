import os
import sys
import string
import psycopg2

# os.environ.get returns None if the variable doesn't exist
DATABASE = os.environ.get('MIGHTY_PROJECT_DB_NAME')
HOST = os.environ.get('MIGHTY_PROJECT_DB_HOST')
PORT = os.environ.get('MIGHTY_PROJECT_DB_PORT')
PASSWORD = os.environ.get('MIGHTY_PROJECT_AD_PW')
USER = os.environ.get('MIGHTY_PROJECT_USER')

# throw error if the variables do not exist in the environment variables
if not (DATABASE and HOST and PORT and PASSWORD and USER):
    sys.exit("""You have not set all environment variables. Check for:
      * MIGHTY_PROJECT_DB_NAME
        * MIGHTY_PROJECT_DB_HOST
        * MIGHTY_PROJECT_DB_PORT
        * MIGHTY_PROJECT_AD_PW
        * MIGHTY_PROJECT_USER """
    )

# set environment variables for db info   
conn = psycopg2.connect(
    database=DATABASE,
    host=HOST,
    port=PORT,
    password=PASSWORD,
    user=USER
)

# Connects to db 
cur = conn.cursor()

# Initialize all variables for Queries
firstName_1 = "Vivian"
firstName_2 = "Mighty"
firstName_3 = "Ken"
firstName_4 = "Jason"
firstName_5 = "Lemon"
firstName_6 = "Bob"
firstName_7 = "Rex"
firstName_8 = "Le"
firstName_9 = "Vivian"
firstName_10 = "Vivian"

last_name_1 = "Lee"
last_name_2 = "Bradley"
last_name_3 = "Smith"
last_name_4 = "Nguyen"
last_name_5 = "Le"
last_name_6 = "Tran"
last_name_7 = "Pham"
last_name_8 = "Vivian"
last_name_9 = "Le"
last_name_10 = "Lee"

userRole1 = "Webmaster"
userRole2 = "Teacher"
userRole3 = "Student"
userRole4 = "Student"
userRole5 = "Student"
userRole6 = "Webmaster"
userRole7 = "Student"
userRole8 = "Student"
userRole9 = "Student"
userRole10 = "Student"

hobby1 = "adipiscing at in tellus integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit amet porttitor eget dolor morbi non arcu risus quis varius"
hobby2 = "duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu non odio"
hobby3 = "viverra mauris in aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id aliquet"
hobby4 = "etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet massa vitae"
hobby5 = "leo duis ut diam quam nulla porttitor massa id neque aliquam vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet nulla malesuada pellentesque elit"
hobby6 = "orci dapibus ultrices in iaculis nunc sed augue lacus viverra vitae congue eu consequat ac felis donec et odio pellentesque diam volutpat commodo sed egestas"
hobby7 = "tellus elementum sagittis vitae et leo duis ut diam quam nulla porttitor massa id neque aliquam vestibulum morbi blandit cursus risus at ultrices mi tempus"
hobby8 = "maecenas sed enim ut sem viverra aliquet eget sit amet tellus cras adipiscing enim eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum lectus"
hobby9 = "fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum"
hobby10 = "aliquam ut porttitor leo a diam sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet risus nullam eget felis"

bio1 = "dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer eget aliquet nibh praesent tristique magna sit amet purus gravida quis blandit turpis cursus in hac habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus mauris a diam maecenas sed enim ut sem viverra aliquet eget sit amet tellus cras adipiscing enim eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum lectus mauris ultrices eros in cursus turpis massa tincidunt dui ut ornare lectus sit amet est placerat in egestas erat"
bio2 = "sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel pretium"
bio3 = "id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris augue neque gravida in fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus quam id leo in vitae turpis massa sed elementum tempus egestas sed sed risus pretium quam vulputate dignissim suspendisse in est ante in nibh mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus"
bio4 = "nulla facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis eu volutpat odio facilisis mauris sit amet massa vitae tortor condimentum lacinia quis vel eros donec ac odio tempor orci dapibus ultrices in iaculis nunc sed augue lacus viverra vitae congue eu consequat ac felis donec et odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed velit dignissim sodales ut eu sem integer vitae justo eget magna fermentum iaculis eu non diam"
bio5 = "cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu non odio euismod lacinia at quis risus sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in"
bio6 = "in fermentum et sollicitudin ac orci phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus quam id leo in vitae turpis massa sed elementum tempus egestas sed sed risus pretium quam vulputate dignissim suspendisse in est ante in nibh mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim convallis aenean et tortor at risus viverra adipiscing at in"
bio7 = "eu mi bibendum neque egestas congue quisque egestas diam in arcu cursus euismod quis viverra nibh cras pulvinar mattis nunc sed blandit libero volutpat sed cras ornare arcu dui vivamus arcu felis bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque dignissim enim sit amet venenatis urna cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu non"
bio8 = "fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper a lacus vestibulum sed arcu non odio euismod lacinia at quis risus sed vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida"
bio9 = "quam quisque id diam vel quam elementum pulvinar etiam non quam lacus suspendisse faucibus interdum posuere lorem ipsum dolor sit amet consectetur adipiscing elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula ipsum a arcu cursus vitae congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas maecenas pharetra convallis posuere morbi leo urna molestie at elementum eu facilisis sed odio morbi quis commodo odio aenean sed adipiscing diam donec adipiscing tristique risus nec feugiat in fermentum posuere urna nec tincidunt praesent semper feugiat"
bio10 = "vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies leo integer malesuada nunc vel risus commodo viverra maecenas accumsan lacus vel facilisis volutpat est velit egestas dui id ornare arcu odio ut sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum est ultricies integer quis auctor elit sed vulputate mi sit amet mauris commodo quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat interdum varius sit amet mattis vulputate enim nulla"

favNum1 = 95
favNum2 = 9
favNum3 = 58
favNum4 = 3
favNum5 = 61
favNum6 = 47
favNum7 = 57
favNum8 = 23
favNum9 = 50
favNum10 = 99

# Insert data into IDTable

# Create Query to insert into Database
insert_data_IDTable = ("""
    INSERT INTO IDTable (firstName, lastName, userRole, hobby, bio, favNum)
    VALUES (%s, %s, %s, %s, %s, %s)
""")

# Run the query with filler data 

#userID_1 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_1, last_name_1, userRole1, hobby1, bio1, favNum1)
)

#userID_2 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_2, last_name_2, userRole2, hobby2, bio2, favNum2)
)

#userID_3 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_3, last_name_3, userRole3, hobby3, bio3, favNum3)
)

#userID_4 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_4, last_name_4, userRole4, hobby4, bio4, favNum4)
)

#userID_5 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_5, last_name_5, userRole5, hobby5, bio5, favNum5)
)

#userID_6 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_6, last_name_6, userRole6, hobby6, bio6, favNum6)
)

#userID_7 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_7, last_name_7, userRole7, hobby7, bio7, favNum7)
)

#userID_8 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_8, last_name_8, userRole8, hobby8, bio8, favNum8)
)

#userID_9 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_9, last_name_9, userRole9, hobby9, bio9, favNum9)
)

#userID_10 = cur.fetchone()[0]
cur.execute(
    insert_data_IDTable,
    (firstName_10, last_name_10, userRole10, hobby10, bio10, favNum10)
)

# Commit changes to Database
conn.commit()

# Close the connection to Database
cur.close()