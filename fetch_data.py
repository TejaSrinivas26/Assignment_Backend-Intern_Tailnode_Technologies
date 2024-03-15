import requests
import mysql.connector
from datetime import datetime


APP_ID = "6514fd46392a65cf6191a4fe"
BASE_URL = "https://dummyapi.io/data/v1"

# MySQL Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Tej@12345"
DB_NAME = "mytestdb"

# Function to create users table if it doesn't exist
def create_users_table():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id VARCHAR(255) PRIMARY KEY,
            title VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            picture VARCHAR(255)
        )
    """)

    connection.commit()
    connection.close()

# Function to fetch users from API and store in database
def fetch_and_store_users():
    url = f"{BASE_URL}/user"
    headers = {"app-id": APP_ID}

    response = requests.get(url, headers=headers)
    users_data = response.json().get("data", [])

    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = connection.cursor()

    for user in users_data:
        user_id = user["id"]
        title = user["title"]
        first_name = user["firstName"]
        last_name = user["lastName"]
        picture = user["picture"]
        cursor.execute(
            "INSERT INTO users (user_id, title, first_name, last_name, picture) VALUES (%s, %s, %s, %s, %s)",
            (user_id, title, first_name, last_name, picture),
        )

    connection.commit()
    connection.close()

def create_posts_table():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            post_id VARCHAR(255) PRIMARY KEY,
            image VARCHAR(255),
            likes INT,
            tags TEXT,
            text TEXT,
            publishDate DATETIME,
            owner_id VARCHAR(255),
            owner_title VARCHAR(255),
            owner_firstName VARCHAR(255),
            owner_lastName VARCHAR(255),
            owner_picture VARCHAR(255),
            FOREIGN KEY (owner_id) REFERENCES users(user_id)
        )
    """)

    connection.commit()
    connection.close()

def convert_to_mysql_datetime(datetime_str):
    # Parse the datetime string
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    # Convert to MySQL-compatible format
    mysql_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return mysql_datetime

def fetch_and_store_posts():
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    cursor = connection.cursor()

    cursor.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    for user_id in user_ids:
        url = f"{BASE_URL}/user/{user_id}/post"
        headers = {"app-id": APP_ID}

        response = requests.get(url, headers=headers)
        posts_data = response.json().get("data", [])

        for post in posts_data:
            post_id = post["id"]
            image = post["image"]
            likes = post["likes"]
            tags = ','.join(post["tags"])
            text = post["text"]
            publish_date = convert_to_mysql_datetime(post["publishDate"])
            owner = post["owner"]
            owner_id = owner["id"]
            owner_title = owner["title"]
            owner_first_name = owner["firstName"]
            owner_last_name = owner["lastName"]
            owner_picture = owner["picture"]
            
            cursor.execute(
                "INSERT INTO posts (post_id, image, likes, tags, text, publishDate, owner_id, owner_title, owner_firstName, owner_lastName, owner_picture) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (post_id, image, likes, tags, text, publish_date, owner_id, owner_title, owner_first_name, owner_last_name, owner_picture),
            )

    connection.commit()
    connection.close()


def main():
    create_users_table()
    fetch_and_store_users()
    create_posts_table()
    fetch_and_store_posts()

if __name__ == "__main__":
    main()
