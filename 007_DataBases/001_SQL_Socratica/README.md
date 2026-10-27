# SQL Concepts from Socratica

Study notes and examples based on [Socratica's SQL tutorial series](https://www.youtube.com/playlist?list=PLi01XoE8jYojRqM4qGBF1U90Ee1Ecb5tt). The material introduces relational databases and SQL, with PostgreSQL installation guidance and practical query examples.

## Folder Structure

```text
001_SQL_Socratica/
│
├── README.md
├── SQL_Socratica.md
├── image.png
└── image-1.png
```

## Contents

| Resource | Description |
| --- | --- |
| [SQL_Socratica.md](./SQL_Socratica.md) | Main study notes, tutorial summaries, SQL examples, tables, and ASCII diagrams. |
| [image.png](./image.png) and [image-1.png](./image-1.png) | Supporting images accompanying the notes. |

## Topics Covered

- Relational database concepts, table structures, schemas, and primary keys.
- Choosing a relational database and getting started with PostgreSQL.
- Defining and modifying database structures with commands such as `CREATE`, `ALTER`, and `DROP`.
- Retrieving and filtering data with `SELECT`, `ORDER BY`, `LIMIT`, `DISTINCT`, `BETWEEN`, and `LIKE`.
- Aggregate functions, including `COUNT`, `MIN`, `MAX`, `AVG`, and `SUM`.
- Adding, updating, and deleting records with `INSERT INTO`, `UPDATE`, and `DELETE`.
- Grouping results with `GROUP BY`.

## Using the Notes

1. Open the [main SQL notes](./SQL_Socratica.md) and use their contents list to select a topic.
2. Refer to the linked tutorial series for the original lessons and context.
3. To execute examples, prepare a database environment and create the tables and sample data required by the relevant section.

This folder is a documentation resource; it does not include a database dump, automated setup script, or runnable application. SQL syntax and setup steps may vary between database systems. The SQLite database in the separate [Socratica Python folder](../../005_Socratica_Python/) is not a PostgreSQL setup for these notes.

**Use a disposable practice database.** Statements such as `UPDATE`, `DELETE`, and `DROP` can change or permanently remove data. Review each statement and its target before executing it.

## Related Resources

- [Socratica SQL tutorial series](https://www.youtube.com/playlist?list=PLi01XoE8jYojRqM4qGBF1U90Ee1Ecb5tt)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [Repository overview](../../README.md)