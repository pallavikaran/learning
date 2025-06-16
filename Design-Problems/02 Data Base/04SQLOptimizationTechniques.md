# General SQL Query Optimization (Applies to All Platforms)

| **Technique**                            | **Description**                                                                                       |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| Use EXPLAIN/EXPLAIN PLAN                | Understand how queries are executed, spot full table scans, and find bottlenecks.                    |
| Use SELECT only required columns        | Avoid SELECT *. It loads unnecessary data and can slow down the query.                               |
| Proper indexing                         | Create indexes on frequently filtered, joined, or grouped columns.                                   |
| Avoid functions in WHERE clause         | e.g., WHERE YEAR(date) = 2024 is less efficient than WHERE date BETWEEN '2024-01-01' AND '2024-12-31'.|
| Use JOINs instead of subqueries         | Subqueries can be less efficient and harder to optimize.                                              |
| Filter early                            | Apply filters as early as possible to reduce dataset size.                                           |
| Avoid DISTINCT if not needed            | It adds overhead due to sorting and deduplication.                                                   |
| Use LIMIT/TOP for sampling              | Helps during testing/debugging to avoid full scans.                                                  |
| Use analytic functions wisely           | Especially in Data Warehouses; use ROW_NUMBER(), RANK(), etc. appropriately.                         |

---

# RDBMS-Specific Optimization (e.g., MySQL, PostgreSQL, SQL Server, Oracle)

| **Optimization Technique**              | **Description**                                                                                       |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| Clustered/Composite Indexes             | Optimize for composite search conditions (WHERE col1 AND col2).                                      |
| Partitioning                            | Use table partitioning for large tables to reduce scan size.                                          |
| Materialized Views                      | Precompute and store costly queries (especially aggregates).                                          |
| Stored procedures                       | Encapsulate logic for reuse and better execution planning.                                            |
| Query hints (e.g., FORCE INDEX)         | Used to override optimizer decisions when needed.                                                     |
| Update statistics regularly             | Helps the optimizer make better decisions.                                                            |

---

# Data Lake Optimization (e.g., Hadoop, Spark SQL, Delta Lake, Presto/Trino, Hive)

| **Optimization Technique**              | **Description**                                                                                       |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| Partition pruning                       | Structure tables with partitions and ensure the query uses the partition column in WHERE.            |
| Predicate pushdown                      | Enable pushing filters to data scan layer to reduce I/O.                                              |
| Columnar formats                        | Use Parquet/ORC instead of CSV/JSON for faster scans.                                                 |
| Caching hot datasets                    | Use in-memory caching for iterative or frequently accessed datasets.                                 |
| Avoid small files (file explosion)      | Optimize writes to avoid many small files; consolidate into fewer large files.                       |
| Broadcast joins                         | For small dimension tables, broadcast them to all worker nodes.                                      |
| Optimize & VACUUM                       | Use Delta’s OPTIMIZE and VACUUM to compact files and clean up old versions.                          |
| Z-Ordering / Clustering                 | In Delta Lake, z-order important columns to improve filtering.                                       |

---

# Data Warehouse Optimization (e.g., Snowflake, BigQuery, Redshift, Synapse)

| **Optimization Technique**              | **Description**                                                                                       |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| Clustering & Sorting keys               | Redshift/Snowflake use clustering keys to skip unnecessary data.                                      |
| Materialized Views                      | Speed up repeatable aggregations and joins.                                                           |
| Denormalization                         | Flatten tables to avoid joins; common in analytical systems.                                          |
| Query result caching                    | Use built-in caching (e.g., in Snowflake and BigQuery).                                               |
| Cost-based optimizer awareness          | Use EXPLAIN, but also structure queries to guide the optimizer.                                       |
| Avoid cross joins                       | Can explode result sets unless intentional.                                                           |
| Use stages/temp tables                  | Break complex queries into steps using intermediate results.                                          |
| Concurrency scaling                     | In systems like Redshift, manage slots and workload queues properly.                                  |

---

# Bonus: Performance Monitoring Tools

| **Tool/Feature**                        | **Use**                                                                                               |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------|
| Query Profiler                          | Tools like Snowflake's Query Profiler or Redshift's EXPLAIN analyze execution time per step.         |
| System tables/views                     | Use views like information_schema or pg_stat_statements to detect slow queries.                      |
| Monitoring dashboards                   | Use tools like Datadog, Prometheus, Grafana for metrics on query duration, CPU, I/O.                 |
