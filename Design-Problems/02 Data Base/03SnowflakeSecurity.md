# Snowflake Security and HIPAA Compliance Guide

## 📌 Overview

Snowflake provides robust features that help organizations comply with HIPAA and manage access to PII/PHI data. This guide outlines best practices, security configurations, and access control mechanisms.

---

## 🔒 Snowflake Business-Critical and VPS Features for HIPAA

1. **Dedicated Metadata Store and Compute Resources**  
   Isolates workloads to reduce risk of unauthorized PHI access.

2. **Private Connectivity Options**  
   Secure channels via AWS PrivateLink, Azure Private Link, and Google Cloud Private Service Connect.

3. **Customer-Managed Encryption Keys (Tri-Secret Secure)**  
   Enforces strict access control by requiring customer-provided encryption keys.

4. **Complete Infrastructure Isolation (VPS only)**  
   Prevents unauthorized access with total environment separation.

5. **Access Controls**  
   Use RBAC to limit PHI access based on user roles.

6. **Audit Logging and Monitoring**  
   Enables detection and response to unauthorized access attempts.

7. **Data Encryption**  
   Ensures PHI is encrypted both at rest and in transit.

---

## 🧩 PHI/PII Segregation Strategies in Snowflake

### 1. **Dynamic Data Masking (DDM)**  
Mask data based on user roles.  
*Example:* Show full SSN only to Admins.

### 2. **Row Access Policies**  
Control visibility of specific rows based on user conditions.  
*Example:* Restrict patient records to users in the same department.

### 3. **Role-Based Access Control (RBAC)**  
Define granular role access.
*Example:*  
- Admins: Full access  
- Engineers: Limited access  
- Analysts: Processed data only

### 4. **Secure Views**  
Encapsulate logic and prevent access to underlying tables.

### 5. **External Tokenization**  
Store tokens instead of raw data. Original values retrievable only via external services.

---

## 🛠️ Key Design Principles

- **Table-Level Access Control**  
  Separate PHI/PII into dedicated tables with RBAC.

- **Ensure Data Encryption**  
  Use Snowflake's built-in features.

- **Anonymization**  
  Generate synthetic data for test environments.

- **Data Lineage & Auditing**  
  Track data changes and access history.

- **Domain Restrictions**  
  Limit access to domains (e.g., clinical, financial).

---

## 🧾 Assumptions

1. Data is limited to what's purchased or sourced via Snowflake products.
2. No employee HR/legal data is included.
3. Development is limited to lower environments—no access concerns.
4. Define Data Domains & Sensitive Data Types:
   - **Domains:** Clinical, Financials, Claims, Eligibility, Marketing, Surveys
   - **Sensitive Types:** PII, PHI, Financial Info

---

## 👥 Roles and Permissions Matrix

| Role               | Access Level                                       |
|--------------------|----------------------------------------------------|
| Admin              | Full access to raw data                            |
| DataOps / DevOps   | Full access to raw data                            |
| Data Engineer      | No access                                          |
| Analyst / Scientist| Read access to processed data only                 |

---

## 🔐 Implementing Row-Level Security
```
-- Define Row Access Policy
CREATE OR REPLACE ROW ACCESS POLICY company_data_policy
  AS (company_id VARCHAR)
  RETURNS BOOLEAN ->
    CASE
      WHEN CURRENT_ROLE() = 'ADMIN_ROLE' THEN TRUE
      WHEN CURRENT_ROLE() IN ('DATA_ENGINEER_ROLE', 'DATA_OPS_ROLE', 'DEV_OPS_ROLE', 'BUSS_ANYLS_ROLE', 'DS_ML_ROLE', 'REPORTNG_BI_ROLE') AND company_id != 'ORGANIZATION NAME' THEN TRUE
      ELSE FALSE
    END;

-- Apply Policy
ALTER TABLE prsn_prfl
  ADD ROW ACCESS POLICY company_data_policy
  USING ('ORGANIZATION NAME');
```

## 🧑‍💻 Role Assignment & Testing
```
GRANT ROLE DATA_ENGINEER_ROLE TO USER data_engineer_user;
GRANT ROLE ADMIN_ROLE TO USER admin_user;

-- Admin
USE ROLE ADMIN_ROLE;
SELECT * FROM your_table_name;

-- Data Engineer
USE ROLE DATA_ENGINEER_ROLE;
SELECT * FROM your_table_name;
```
# 🕵️ Data Masking & Column-Level Security
## Masking Examples

| Column                | Admin | DataOps | Engineer | Analyst | Scientist |
|-----------------------|--------|---------|----------|---------|-----------|
| Full Name             | ✓      | ✓       | ✗        | Masked  | Masked    |
| SSN                   | ✓      | ✓       | ✗        | Masked  | Masked    |
| DOB, Address, Gender  | ✓      | ✓       | ✗        | Masked  | ✓         |
| Email, Phone          | ✓      | ✓       | ✗        | Masked  | Masked    |
| Financial Info        | ✓      | ✓       | ✗        | Masked  | Masked    |

### SQL: Masking Policy
```
-- Email Masking Policy
CREATE MASKING POLICY email_masking_policy
  AS (val STRING)
  RETURNS STRING ->
    CASE
      WHEN CURRENT_ROLE() IN ('admin', 'data_scientist') THEN val
      ELSE 'XXX@XXX.com'
    END;

-- Apply Policy
ALTER TABLE prsn_prfl
  MODIFY COLUMN email SET MASKING POLICY email_masking_policy;
```

### 🏷️ ABAC: Attribute-Based Access Control
Hierarchy: Region > Department > Domain

Example Regions
```
CREATE OR REPLACE TABLE region_access_mapping (
  role_name VARCHAR,
  region VARCHAR
);

INSERT INTO region_access_mapping VALUES
  ('REGION_NA_MANAGER', 'NA'),
  ('REGION_EU_MANAGER', 'EU'),
  ('REGION_US_MANAGER', 'US');
Region Access Policy
```
```
CREATE OR REPLACE ROW ACCESS POLICY region_access_policy
  AS (region_column VARCHAR) RETURNS BOOLEAN ->
    EXISTS (
      SELECT 1
      FROM region_access_mapping
      WHERE region = 'US'
        AND role_name IN (
          SELECT value FROM TABLE(flatten(input => CURRENT_AVAILABLE_ROLES()))
        )
    );
Combined Department + Region Policy
```
```
CREATE OR REPLACE ROW ACCESS POLICY combined_access_policy
  AS (department STRING, region_column VARCHAR)
  RETURNS BOOLEAN ->
    CASE
      WHEN CURRENT_ROLE() = 'ADMIN_ROLE' THEN TRUE
      WHEN CURRENT_ROLE() = 'DATA_ENGINEER_ROLE' AND region_column = 'US' AND department = 'data_platform' THEN TRUE
      ELSE FALSE
    END;

ALTER TABLE your_table_name
  ADD ROW ACCESS POLICY combined_access_policy
  USING (department, region_column);
```

### 📊 Monitor and Audit Access
```
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY
WHERE EVENT_TIMESTAMP > CURRENT_DATE() - INTERVAL '30 days';
```
### 🌍 Data Residency Considerations
1. **Choose Snowflake Region Carefully**
  Maintain accounts in specific regions for legal compliance.

2. **Use Data Privacy Vaults**
  Store sensitive data externally and only use de-identified/tokenized data in Snowflake.

3. **Secure Data Sharing**
  Share data without physically moving it between accounts.

4. **Use Dynamic Data Masking**
  Limit sensitive data exposure by role.

5. **Leverage Compliance Certifications**
  E.g., FedRAMP, StateRAMP, TX-RAMP.

6. **Third-Party Residency Tools**
  Tools like InCountry can enforce strict data localization rules.

## 🏗️ Compliance-Oriented Architecture Best Practices
  1. **Data Localization**
  Store/process data in required jurisdictions.

  2. **Access Controls**
  Limit who can view/access sensitive data.

  3. **Data Minimization**
  Only collect what's absolutely necessary.

  4. **Auditing**
  Monitor data access and activity regularly.
