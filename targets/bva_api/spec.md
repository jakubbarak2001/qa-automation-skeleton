## Username length specification

### Partitions
- **Valid partition (5–30 characters):** expect **200 OK**
- **Invalid partition (<5 characters):** expect **422 error** (too short)
- **Invalid partition (>30 characters):** expect **422 error** (too long)

### Boundary values for 3BVA
- 4 -> 422 (too short)
- 5 -> 200 OK
- 6 -> 200 OK
- 11 -> 200 OK
- 29 -> 200 OK
- 30 -> 200 OK
- 31 -> 422 (too long)