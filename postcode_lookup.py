import psycopg2

#connect to PostgreSQL database - replace with details of your own local version (see readme for more information)
def postcode_lookup(postcode):
    conn = psycopg2.connect(database="postcodes_mps",
                            host="localhost",
                            user="postgres",
                            password="postgres",
                            port="5432")

    cursor = conn.cursor()
    #query database to return constituency and MP information matching input postcode
    cursor.execute(f"""
                SELECT constituency_name, mps.name, parties.name, mps.phone, mps.email
                FROM postcodes
                JOIN constituencies ON postcodes.constituency_id = constituencies.id
                JOIN mps ON constituencies.mp_id = mps.id
                JOIN parties on mps.party_id = parties.id
                WHERE postcode = '{postcode}'
                """)
    
    mp_info = cursor.fetchall()

    return mp_info