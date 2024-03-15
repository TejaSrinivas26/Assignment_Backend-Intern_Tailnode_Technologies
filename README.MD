# Python Intern Assignment-Tailnode Technologies

## PART - A 

Fetch Users and Posts from API and Store in Database

### Objective
The objective of this project is to fetch users and their corresponding posts data from an external API and store it in a database.

#### Functional Requirements
- Login to the website and obtain an app_id.
- Utilize the obtained app_id to access the required APIs.
- Fetch Users data from https://dummyapi.io/data/v1/user and store it in the users table in the database.
- Fetch users list from the Database and fetch their corresponding posts data from https://dummyapi.io/data/v1/user/{{user_id}}/post.
- Store the posts data in the database

## Setup
Clone Repository:

```
git clone <repository_url>
```

## Install Dependencies:
```
pip install mysql-connector-python requests
```

## Database Setup:

- Set up a MySQL database of your choice.
- Create tables users and posts with appropriate columns as mentioned in the script.
## Obtain app_id:

* Login to the website and create an app_id.

## Configure Script:

* Open the script and update the APP_ID, DB_HOST, DB_USER, DB_PASSWORD, and DB_NAME variables with your credentials.

#### Usage
- Run the Python script "fetch_data.py" to fetch users and posts data from the API and store it in the database.
```
python fetch_data.py
```

## Dependencies
- mysql-connector-python: MySQL driver for Python.

- requests: HTTP library for making API requests.

## Database Schema

#### Users Table
| Column Name | Type     | 
| :-------- | :----- |
| `user_id` | `VARCHAR` |
| `title`   | `VARCHAR` |
| `first_name` | `VARCHAR` |
| `last_name` | `VARCHAR` |
| `picture` | `VARCHAR` |


#### Posts Table

| Column Name     | Data Type |
| :-------------- | :-------- |
| `post_id`       | `VARCHAR` |
| `image`         | `VARCHAR` |
| `likes`         | `INT`     |
| `tags`          | `TEXT`    |
| `text`          | `TEXT`    |
| `publishDate`   | `DATETIME`|
| `owner_id`      | `VARCHAR` |
| `owner_title`   | `VARCHAR` |
| `owner_firstName` | `VARCHAR` |
| `owner_lastName` | `VARCHAR` |
| `owner_picture` | `VARCHAR` |


### Obtain app_id:

#### 1. Login to the website: 
* Visit the website where the API is hosted.`https://dummyapi.io/`
#### 2. Create an app_id: 
* Navigate to the appropriate section of the website for developers or API access. There should be an option to create an application or obtain an API key (app_id). Follow the instructions to create a new application or obtain your API key.
### Configure Script:

- Open the script and update the `APP_ID`, `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` variables with your credentials.

#### 1. Open the script: 
- Locate the Python script file `fetch_data.py` in your project directory.
#### 2. Update credentials:
* `APP_ID`: Replace the placeholder value with the app_id obtained from the website.
* `DB_HOST`: Provide the hostname or IP address of your MySQL database server.
* `DB_USER`: Enter the username for accessing the MySQL database.
* `DB_PASSWORD`: Enter the password associated with the provided username.
* `DB_NAME`: Specify the name of the database where you want to store the fetched data.

#### Example:

```
# MySQL Database credentials
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database_name"

# Obtain app_id from the website
APP_ID = "your_app_id"
```

Replace `your_username`, `your_password`, `your_database_name`, and `your_app_id` with your actual credentials obtained from your MySQL database and the app_id obtained from the website, respectively.

By updating these variables with your actual credentials, the script will be able to authenticate with the API using your app_id and connect to your MySQL database for storing the fetched data.

# Usage

Run the Python script fetch_data.py to fetch users and posts data from the API and store it in the database.

```
python fetch_data.py
```

# Dependencies

- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/): MySQL driver for Python. This library provides a Python interface for connecting to MySQL databases, allowing you to interact with your MySQL database from your Python script.
- [requests](https://pypi.org/project/requests/): HTTP library for making API requests. This library allows you to easily make HTTP requests to web servers, making it ideal for fetching data from external APIs in your Python script.

# API Usage

To fetch users and posts data from the provided API endpoints, follow these steps:

1. **Fetch Users Data**: Utilize the API endpoint [User API](https://dummyapi.io/data/v1/user) to fetch users data. You'll need to include your obtained `app_id` in the request headers for authentication.

2. **Fetch Posts Data**: After storing users data in your database, fetch the list of user IDs from the `users` table. Then, for each user ID, utilize the API endpoint [User Post API](https://dummyapi.io/data/v1/user/{{user_id}}/post) to fetch their corresponding posts data. Again, include your `app_id` in the request headers for authentication.

3. **Store Data in Database**: Once you've fetched the users and posts data, store it in your MySQL database tables (`users` and `posts`) using the appropriate SQL queries and the MySQL connector library.

By following these steps and utilizing the provided API endpoints with your `app_id`, you'll be able to fetch users and posts data from the API and store it in your MySQL database.


# PART - B



Scrape Books Data from [books.toscrape.com](http://books.toscrape.com) and Store it in Database

### Objective

The objective of this project is to scrape books data from the website [books.toscrape.com](http://books.toscrape.com) and store it in a MySQL database.

### Functional Requirements

- Scrape all book attributes such as name, price, availability, and ratings from all 50 pages of the website.
- Store the scraped data in a MySQL database.

### Setup

1. **Clone Repository**: 
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies**: 
   ```bash
   pip install requests beautifulsoup4 pymysql
   ```

3. **Database Setup**: 
   - Set up a MySQL database of your choice.
   - Create a table named `books` with the following schema:

```sql
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price FLOAT,
    star_rating VARCHAR(10),
    availability VARCHAR(20)
);
```

4. **Configure Script**: 
   - Open the script (`scrape_books.py`) and update the `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` variables with your MySQL database credentials.

### Usage

Run the Python script `scrape_books.py` to scrape books data from the website and store it in the database.

```bash
python scrape_books.py
```

### Dependencies

- [requests](https://pypi.org/project/requests/): HTTP library for making requests to web servers.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): Python library for pulling data out of HTML and XML files.
- [pymysql](https://pypi.org/project/PyMySQL/): Python client library for MySQL database.

### Contributing

Contributions are welcome! Please submit any issues or pull requests.

