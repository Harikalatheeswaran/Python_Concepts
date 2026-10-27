# INFORMATION_SCHEMA Explained Using the Feynman Technique

## Step 1: Imagine a Library

Suppose a database is a huge library.

- A **database** = the library building
- A **table** = a bookshelf
- A **row** = a book
- A **column** = a property of every book

Example:

Table: `songs`

| song_id | title | artist | duration |
|----------|--------|---------|----------|
| 1 | Hello | Adele | 295 |
| 2 | Shape of You | Ed Sheeran | 234 |

Here:

- `song_id`, `title`, `artist`, `duration` are columns
- The actual song records are rows

---

# The Big Question

How does the database itself remember:

- What tables exist?
- What columns exist?
- Which column is a primary key?
- Which columns allow NULL values?
- What data type each column uses?

The database needs somewhere to store this information.

That "information about the database" is called:

## Metadata

Think:

> Data = the actual song records

> Metadata = information about the song table itself

Example:

Data:

```text
Song Name = Hello
Artist = Adele
```

Metadata:

```text
Table Name = songs
Column Name = artist
Data Type = VARCHAR(100)
Nullable = NO
```

---

# What is INFORMATION_SCHEMA?

`INFORMATION_SCHEMA` is a collection of special system views that expose metadata.

You can think of it as:

```text
Database about the database
```

Or

```text
A catalog describing everything inside the database
```

It does NOT store your business data.

It stores information like:

```text
Tables
Columns
Views
Constraints
Indexes
Privileges
Relationships
```

---

# Why It Exists

Imagine having 500 tables.

Would you manually check each one?

Of course not.

Instead you ask the system:

```sql
SELECT *
FROM INFORMATION_SCHEMA.TABLES;
```

The database replies:

```text
songs
albums
artists
users
playlists
```

---

# INFORMATION_SCHEMA.COLUMNS

Think of this as:

```text
A table that describes every column
inside every table.
```

Let's say:

```sql
CREATE TABLE songs
(
    song_id INT,
    title VARCHAR(100),
    artist VARCHAR(100),
    duration INT
);
```

Now:

```sql
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS;
```

might contain rows like:

```text
TABLE_NAME  COLUMN_NAME DATA_TYPE
----------- ----------- ---------
songs       song_id     int
songs       title       varchar
songs       artist      varchar
songs       duration    int
```

Notice something interesting:

The columns of `songs` become rows inside
`INFORMATION_SCHEMA.COLUMNS`.

---

# Why This Query Works

When you run:

```sql
SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'songs';
```

you're basically asking:

```text
Dear database,

Look inside your metadata storage.

Find all rows describing the table "songs".

Return their column names.
```

Result:

```text
song_id
title
artist
duration
```

---

# Can We Query Other INFORMATION_SCHEMA Objects?

Absolutely.

This is where things become powerful.

Think of INFORMATION_SCHEMA as a package.

```text
INFORMATION_SCHEMA
│
├── TABLES
├── COLUMNS
├── VIEWS
├── TABLE_CONSTRAINTS
├── KEY_COLUMN_USAGE
├── REFERENTIAL_CONSTRAINTS
├── ROUTINES
├── PARAMETERS
└── ...
```

---

# INFORMATION_SCHEMA.TABLES

Shows all tables.

```sql
SELECT *
FROM INFORMATION_SCHEMA.TABLES;
```

Example output:

```text
songs
albums
artists
users
```

Useful when you don't know what tables exist.

---

# INFORMATION_SCHEMA.COLUMNS

Shows all columns of all tables.

```sql
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS;
```

Example:

```text
songs.song_id
songs.title
songs.artist

albums.album_id
albums.name
```

---

# INFORMATION_SCHEMA.VIEWS

Lists database views.

```sql
SELECT *
FROM INFORMATION_SCHEMA.VIEWS;
```

Example:

```text
active_users
monthly_sales
top_songs
```

---

# INFORMATION_SCHEMA.TABLE_CONSTRAINTS

Shows constraints.

```sql
SELECT *
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS;
```

Example:

```text
PRIMARY KEY
FOREIGN KEY
UNIQUE
CHECK
```

For example:

```text
PK_songs
FK_song_artist
```

---

# INFORMATION_SCHEMA.KEY_COLUMN_USAGE

Shows which columns participate in keys.

```sql
SELECT *
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE;
```

Example:

```text
songs.song_id
artists.artist_id
albums.album_id
```

Useful for discovering:

- Primary keys
- Foreign keys

---

# INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS

Shows table relationships.

Example:

```text
songs.artist_id
   ->
artists.artist_id
```

This is how the database knows tables are related.

---

# INFORMATION_SCHEMA.ROUTINES

Shows stored procedures and functions.

```sql
SELECT *
FROM INFORMATION_SCHEMA.ROUTINES;
```

Example:

```text
GetSongById
CalculateRevenue
UpdatePlaylist
```

---

# Real-World Superpower

Suppose you're joining a new project.

You know nothing.

First thing many experienced developers do:

```sql
SELECT *
FROM INFORMATION_SCHEMA.TABLES;
```

Find all tables.

Then:

```sql
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS;
```

Find all columns.

Then:

```sql
SELECT *
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE;
```

Find keys.

Then:

```sql
SELECT *
FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS;
```

Find relationships.

Within minutes they understand the database structure.

---

# What Is Actually Stored Inside INFORMATION_SCHEMA?

Important concept:

Many beginners think:

```text
INFORMATION_SCHEMA is a normal table.
```

Not exactly.

It is usually a set of:

```text
System Views
```

built on top of internal system catalogs maintained by the database engine.

Think:

```text
Actual Metadata Storage
        ↓
System Catalogs
        ↓
INFORMATION_SCHEMA Views
        ↓
Your SQL Queries
```

So when you query:

```sql
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS;
```

you're really reading a friendly view over the database's internal metadata.

---

# Mental Model to Remember Forever

Think of a company:

```text
Employees Table
```

contains employee data.

And:

```text
HR Records
```

contain information about the employees.

Now replace that idea with databases:

```text
songs table
albums table
artists table
```

contain business data.

while

```text
INFORMATION_SCHEMA.TABLES
INFORMATION_SCHEMA.COLUMNS
INFORMATION_SCHEMA.KEY_COLUMN_USAGE
```

contain information ABOUT those tables.

So:

```text
Data              → songs
Metadata          → INFORMATION_SCHEMA
```

or even simpler:

```text
songs             = "the book"

INFORMATION_SCHEMA = "the library catalog"
```

You don't read the book to know where it is located.

You read the catalog.

That's exactly what `INFORMATION_SCHEMA` does for a database.