def min_max_scaling(data: list) -> list:
    rows=len(data)
    cols=len(data[0])

    newdata = [[0.0] * cols for _ in range(rows)]
    for col in range(cols):
        col_values = [data[row][col] for row in range(rows)]
        minimum=min(col_values)
        maximum=max(col_values)
        span= maximum-minimum
        for row in range(rows):
            if span==0:
                newdata[row][col]=0
            else:
                newdata[row][col] = (data[row][col] - minimum) / span
    return newdata;
    
    
    
    
    
    