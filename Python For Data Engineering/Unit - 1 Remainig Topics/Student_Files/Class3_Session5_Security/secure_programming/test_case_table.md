# Test-case table

| Test case      | Example input | Expected result          | Actual | Pass? |
|----------------|---------------|--------------------------|--------|-------|
| Normal case    | Quantity 3    | Accepted                 |        |       |
| Boundary case  | Quantity 1    | Accepted                 |        |       |
| Invalid type   | abc           | Clear validation message |        |       |
| Zero value     | Quantity 0    | Rejected                 |        |       |
| Negative value | Quantity -2   | Rejected                 |        |       |
