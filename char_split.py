def char_split(df, column, n):
    '''
    df - DataFrame  
    Column - column name you wish to split (str)
    n - Number of interval
        for ex - a = '123456'
                n = 2
                then split will be - ['12','34','56']
    -------------------------------------------------
    Returns - nested list
    '''
    main=[]
    for j in df[column]:
        main.append([str(j)[i:i+n] for i in range(0, len(str(j)), n)])
        
    return main
