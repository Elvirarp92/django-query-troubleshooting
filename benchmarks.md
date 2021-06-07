# Benchmarks for 1300 files

## Iteration 1 - Commit b94ff9f60c3fd9638b859c527b73cb720a619c3b
> Base state
> 
> Reproducing as closely as possible the OG state of the legalq app as a baseline for benchmarking

http://127.0.0.1:8000/api/v1/legalfiles/

| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |   3900   |    0     |   3900   |     1      |
|------|-----------|----------|----------|----------|------------|
Total queries: 3900 in 6.1581s 


http://127.0.0.1:8000/api/v1/legalfile_contactroles/

| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |   2601   |    0     |   2601   |     1      |
|------|-----------|----------|----------|----------|------------|
Total queries: 2601 in 3.4846s 


http://127.0.0.1:8000/api/v1/contacts/

| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |    3     |    0     |    3     |     1      |
|------|-----------|----------|----------|----------|------------|
Total queries: 3 in 0.2587s 


http://127.0.0.1:8000/api/v1/contact_subtypes/

| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |    3     |    0     |    3     |     1      |
|------|-----------|----------|----------|----------|------------|
Total queries: 3 in 0.1295s 

Observe how the n+1 problem comes with relationships.

## Iteration 2 - Commit ecdaf332504248f0a8c8693384b2832df35acb33

> Attempt 1: implementing EagerLoadingMixin naively

http://127.0.0.1:8000/api/v1/legalfile_contactroles/

| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |    3     |    0     |    3     |     1      |
|------|-----------|----------|----------|----------|------------|
Total queries: 3 in 0.5721s 

http://127.0.0.1:8000/api/v1/legalfiles/

| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |   2602   |    0     |   2602   |     1      |
|------|-----------|----------|----------|----------|------------|
Total queries: 2602 in 5.3187s 

N+1 problem persists in deeper relationships